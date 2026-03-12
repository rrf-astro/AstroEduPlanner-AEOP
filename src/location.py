# src/location.py

"""
Location Module.
Provides utilities for resolving city names to geographic coordinates
and for determining the observer's timezone.
"""

# Fix: Import dependencies directly, not via config.
try:
    from geopy.geocoders import Nominatim
    from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
    GEOPY_USABLE = True
except ImportError:
    # If geopy is not installed, set a flag to disable the functionality
    Nominatim = None
    GeocoderTimedOut = None
    GeocoderUnavailable = None
    GEOPY_USABLE = False

import pytz
from astropy import units as u
from astropy.coordinates import EarthLocation

def get_location_from_city(city_name_input, altitude_meters=None):
    """
    Attempts to convert a city name into geographic coordinates using an online service.

    Args:
        city_name_input (str): City name (e.g. "São Paulo, Brazil").
        altitude_meters (float, optional): Observer altitude in metres above sea level.
            Defaults to 0 if not provided.

    Returns:
        astropy.coordinates.EarthLocation or None: Location object if successful,
            None if the city was not found or the service is unavailable.
    """
    if not GEOPY_USABLE:
        print("WARNING: The 'geopy' library is not available. Cannot resolve city name to coordinates.")
        return None

    print(f"Searching geographic coordinates for: '{city_name_input}'...")
    try:
        geolocator = Nominatim(user_agent="astro_planner_modular/1.0")
        location_data = geolocator.geocode(city_name_input, timeout=10)

        if location_data:
            latitude = location_data.latitude
            longitude = location_data.longitude
            altitude = altitude_meters if altitude_meters is not None else 0

            print(f"  Location found: Latitude {latitude:.4f}°, Longitude {longitude:.4f}°")
            print(f"  Altitude set to: {altitude}m")

            return EarthLocation(lat=latitude*u.deg, lon=longitude*u.deg, height=altitude*u.m)
        else:
            print(f"  Could not find coordinates for '{city_name_input}'. Please check the name.")
            return None

    except (GeocoderTimedOut, GeocoderUnavailable) as e:
        print(f"  Geocoding service unavailable or timed out: {e}")
        return None
    except Exception as e:
        print(f"  An unexpected error occurred while fetching city coordinates: {e}")
        return None

def set_location_for_uberaba():
    """
    Convenience function to quickly set the observer location to Uberaba, MG, Brazil.

    Returns:
        astropy.coordinates.EarthLocation: Hardcoded coordinates for Uberaba.
    """
    print("Setting test location to Uberaba, MG, Brazil.")
    uberaba_lat = -19.7485
    uberaba_lon = -47.9318
    uberaba_alt = 823
    return EarthLocation(lat=uberaba_lat*u.deg, lon=uberaba_lon*u.deg, height=uberaba_alt*u.m)

def set_timezone_for_sao_paulo(location):
    """
    Returns the 'America/Sao_Paulo' timezone if the location falls within the Brazilian region.

    Args:
        location (astropy.coordinates.EarthLocation): Observer location.

    Returns:
        pytz.timezone or None: Timezone object if inside the Brazilian bounding box,
            None otherwise.
    """
    # Simple bounding box check for the Brazilian longitude/latitude range
    if -53 < location.lon.deg < -34 and -34 < location.lat.deg < 5:
        return pytz.timezone('America/Sao_Paulo')
    return None  # Returns None if outside the area


print("Location module (src/location.py) loaded.")
