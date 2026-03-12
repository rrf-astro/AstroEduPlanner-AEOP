# src/analysis.py

"""
Astronomical Analysis Module.
Contains functions for computing nightly events, target visibility,
lunar impact, weather forecast integration, and annual visibility calendars.
"""
from astroplan import Observer
from .config import (
    np, pd, u, AltAz, Time, requests, get_sun, get_body,
    datetime, timedelta, date, moon_illumination, tqdm, erfa
)

def calculate_nightly_events(analysis_date, observer_location, observer_timezone):
    """
    Calculates sunset, astronomical twilight, and sunrise times for a given date.

    Args:
        analysis_date (datetime.date): The date to analyse.
        observer_location (astropy.coordinates.EarthLocation): Observer's location.
        observer_timezone (pytz.timezone): Observer's local timezone.

    Returns:
        dict: Dictionary with keys 'inicio_noite', 'fim_noite', 'por_do_sol',
              'nascer_do_sol', 'meia_noite_real' as astropy Time objects.
              Returns an empty dict on failure.
    """
    try:
        observer = Observer(location=observer_location, timezone=observer_timezone)
        time_midday = Time(f"{analysis_date.strftime('%Y-%m-%d')} 12:00:00")

        # Fix: Remove .astimezone() call. Observer already returns time in the correct timezone.
        sunset_time = observer.sun_set_time(time_midday, which='next')
        sunrise_time = observer.sun_rise_time(time_midday, which='next')
        evening_astro_twilight = observer.twilight_evening_astronomical(time_midday, which='next')
        morning_astro_twilight = observer.twilight_morning_astronomical(time_midday, which='next')
        midnight_time = observer.midnight(time_midday, which='next')

        return {
            "inicio_noite": evening_astro_twilight,
            "fim_noite": morning_astro_twilight,
            "por_do_sol": sunset_time,
            "nascer_do_sol": sunrise_time,
            "meia_noite_real": midnight_time
        }
    except Exception as e:
        print(f"Warning: Could not calculate nightly events for {analysis_date}. Error: {e}")
        return {}

def analyze_target_visibility_for_night(start_time, end_time, observer_location, target_coord, min_altitude):
    """
    Computes the altitude of a target throughout a single night at 5-minute intervals.

    Args:
        start_time (astropy.time.Time): Start of the observing window (evening twilight).
        end_time (astropy.time.Time): End of the observing window (morning twilight).
        observer_location (astropy.coordinates.EarthLocation): Observer's location.
        target_coord (astropy.coordinates.SkyCoord): Target sky coordinates.
        min_altitude (astropy.units.Quantity): Minimum observable altitude.

    Returns:
        pandas.DataFrame: Rows where the target is above min_altitude,
            with columns 'time' and 'altitude'. Empty if never above threshold.
    """
    time_range = pd.date_range(start=start_time.to_datetime(), end=end_time.to_datetime(), freq='5min')
    if time_range.empty:
        return pd.DataFrame()

    times_astro = Time(time_range)
    frame = AltAz(obstime=times_astro, location=observer_location)
    target_altaz = target_coord.transform_to(frame)

    df = pd.DataFrame({'time': time_range, 'altitude': target_altaz.alt.deg})
    df_visible = df[df['altitude'] >= min_altitude.value].copy()
    return df_visible

def check_hemisphere_visibility(observer_location, target_coord):
    """
    Checks whether a target is potentially observable from the observer's hemisphere.

    Applies a simple declination filter: targets more than 30° into the opposite
    hemisphere are considered unobservable.

    Args:
        observer_location (astropy.coordinates.EarthLocation): Observer's location.
        target_coord (astropy.coordinates.SkyCoord): Target sky coordinates.

    Returns:
        bool: True if the target may be observable, False otherwise.
    """
    observer_lat = observer_location.lat.deg
    target_dec = target_coord.dec.deg
    if (observer_lat > 0 and target_dec < -30) or (observer_lat < 0 and target_dec > 30):
        return False
    return True

def analyze_moon_impact(time, observer_location, target_coord):
    """
    Calculates the Moon's illumination fraction and its angular separation from a target.

    Args:
        time (astropy.time.Time): Time of observation.
        observer_location (astropy.coordinates.EarthLocation): Observer's location.
        target_coord (astropy.coordinates.SkyCoord): Target sky coordinates.

    Returns:
        dict: Dictionary with keys 'moon_illumination' (float, 0–100 %)
              and 'moon_separation' (astropy Quantity in degrees).
    """
    moon = get_body("moon", time, location=observer_location)
    frame = AltAz(obstime=time, location=observer_location)

    illum = moon_illumination(time) * 100
    separation = moon.separation(target_coord)

    return {
        "moon_illumination": illum,
        "moon_separation": separation
    }

def get_weather_forecast(lat, lon):
    """
    Retrieves average cloud cover for the coming night using the Open-Meteo API.

    Args:
        lat (float): Observer latitude in decimal degrees.
        lon (float): Observer longitude in decimal degrees.

    Returns:
        str: Average cloud cover as a percentage string (e.g. "23.4%"),
             or "N/A" if the request fails or no data is available.
    """
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=cloudcover&forecast_days=2"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        hourly_data = pd.DataFrame(data['hourly'])
        hourly_data['time'] = pd.to_datetime(hourly_data['time'])

        now = datetime.now()
        start_night = datetime(now.year, now.month, now.day, 18)
        if now.hour > 18: start_night += timedelta(days=1)
        end_night = start_night + timedelta(hours=12)

        night_forecast = hourly_data[(hourly_data['time'] >= start_night) & (hourly_data['time'] <= end_night)]

        if not night_forecast.empty:
            avg_cloud_cover = night_forecast['cloudcover'].mean()
            return f"{avg_cloud_cover:.1f}%"
    except Exception:
        return "N/A"
    return "N/A"

def analyze_year_visibility(year, observer_location, observer_timezone, target_coord, min_altitude):
    """
    Analyses the visibility of a target for every night of a full year.

    Args:
        year (int): The year to analyse.
        observer_location (astropy.coordinates.EarthLocation): Observer's location.
        observer_timezone (pytz.timezone): Observer's local timezone.
        target_coord (astropy.coordinates.SkyCoord): Target sky coordinates.
        min_altitude (astropy.units.Quantity): Minimum observable altitude.

    Returns:
        pandas.DataFrame: One row per visible night, with columns
            'date', 'start_time', 'end_time', 'duration_hours'.
            Empty DataFrame if the target is never visible.
    """
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    results = []

    for day_offset in tqdm(range((end_date - start_date).days + 1), desc=f"Analysing {year}", unit="night"):
        current_date = start_date + timedelta(days=day_offset)
        with np.errstate(all='ignore'):
            night_events = calculate_nightly_events(current_date, observer_location, observer_timezone)

        if not night_events or not night_events.get("inicio_noite") or not night_events.get("fim_noite"): continue
        start_night, end_night = night_events["inicio_noite"], night_events["fim_noite"]
        if start_night >= end_night: continue

        df_visible = analyze_target_visibility_for_night(start_night, end_night, observer_location, target_coord, min_altitude)

        if not df_visible.empty:
            duration = (df_visible['time'].iloc[-1] - df_visible['time'].iloc[0]).total_seconds() / 3600.0
            results.append({
                'date': pd.to_datetime(current_date),
                'start_time': df_visible['time'].iloc[0],
                'end_time': df_visible['time'].iloc[-1],
                'duration_hours': duration
            })
    return pd.DataFrame(results)

print("Analysis module (src/analysis.py) loaded.")
