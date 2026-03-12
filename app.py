# app.py
# AstroEduPlanner (AEOP) — Streamlit web application
# Supports English and Portuguese via src/i18n/strings.py

import streamlit as st
from datetime import date, timedelta
import pytz

from src.config import *
from src.location import get_location_from_city, set_timezone_for_sao_paulo
from src.targets import get_target_skycoords, registrar_alvos_sistema_solar, DEEP_SKY_TARGETS_PRESET
from src.analysis import calculate_nightly_events, analyze_target_visibility_for_night, analyze_year_visibility
from src.plotting import plot_target_visibility, plot_yearly_visibility, plot_sky_map
from src.i18n.strings import LANGUAGES

# ── Page configuration (must be the first Streamlit call) ──────────────────
st.set_page_config(
    page_title="AstroEduPlanner",
    page_icon="🔭",
    layout="wide"
)

# ── Language selector (top of sidebar, before any t[] reference) ────────────
language = st.sidebar.selectbox(
    "🌐 Language / Idioma",
    list(LANGUAGES.keys()),
    index=0
)
t = LANGUAGES[language]

# ── App title ───────────────────────────────────────────────────────────────
st.title(t["app_title"])

# ── Sidebar: Analysis settings header ──────────────────────────────────────
st.sidebar.header(t["sidebar_header"])

# ── Sidebar: Observer Location ──────────────────────────────────────────────
st.sidebar.subheader(t["location_subheader"])
location_method = st.sidebar.radio(
    t["location_method_label"],
    (t["location_method_city"], t["location_method_coords"])
)
observer_location = None

if location_method == t["location_method_city"]:
    city_name = st.sidebar.text_input(t["city_input_label"], t["city_input_default"])
    if st.sidebar.button(t["city_button"]):
        with st.spinner(t["city_spinner"].format(city=city_name)):
            observer_location = get_location_from_city(city_name)
else:
    lat_lon_str = st.sidebar.text_input(
        t["coords_input_label"],
        t["coords_input_placeholder"]
    )
    if st.sidebar.button(t["coords_button"]):
        try:
            lat, lon = map(float, lat_lon_str.split(','))
            observer_location = EarthLocation(lat=lat * u.deg, lon=lon * u.deg)
        except ValueError:
            st.sidebar.error(t["coords_invalid_error"])

# Persist location in session state
if observer_location is not None:
    st.session_state['observer_location'] = observer_location
    st.sidebar.success(
        t["location_set_success"].format(
            lat=observer_location.lat.deg,
            lon=observer_location.lon.deg
        )
    )
elif 'observer_location' in st.session_state:
    observer_location = st.session_state['observer_location']
    st.sidebar.info(
        t["location_cached_info"].format(
            lat=observer_location.lat.deg,
            lon=observer_location.lon.deg
        )
    )
else:
    st.sidebar.warning(t["location_missing_warning"])

# ── Sidebar: Observation parameters ─────────────────────────────────────────
analysis_date = st.sidebar.date_input(t["date_input_label"], date.today())
min_altitude_deg = st.sidebar.slider(t["min_alt_label"], 10, 90, 30)
min_altitude = min_altitude_deg * u.deg

# ── Tabs ─────────────────────────────────────────────────────────────────────
tab1, tab2 = st.tabs([t["tab_nightly"], t["tab_annual"]])

# ═══════════════════════════════════════════════════════════════════════════ #
#  TAB 1 — Nightly Analysis                                                   #
# ═══════════════════════════════════════════════════════════════════════════ #
with tab1:
    st.header(t["nightly_header"])
    col1, col2 = st.columns(2)
    with col1:
        use_deep_sky     = st.checkbox(t["checkbox_deep_sky"],     value=True)
        use_solar_system = st.checkbox(t["checkbox_solar_system"], value=True)
    with col2:
        manual_targets_input = st.text_area(
            t["manual_targets_label"],
            t["manual_targets_default"]
        )

    if st.button(t["run_nightly_button"], type="primary"):
        if 'observer_location' not in st.session_state:
            st.error(t["no_location_error"])
        else:
            observer_location  = st.session_state['observer_location']
            observer_timezone  = set_timezone_for_sao_paulo(observer_location) or pytz.UTC

            # Compute nightly events
            with st.spinner(t["nightly_spinner"]):
                night_events = calculate_nightly_events(
                    analysis_date, observer_location, observer_timezone
                )

            if not night_events:
                st.error(t["nightly_events_error"])
            else:
                start_night = night_events['inicio_noite']
                end_night   = night_events['fim_noite']

                # Night info summary
                st.info(f"""
**{t["night_info_title"].format(date=analysis_date.strftime('%d/%m/%Y'))}**
- {t["night_sunset"]}: {night_events['por_do_sol'].to_datetime():%H:%M} {t["time_utc_suffix"]}
- {t["night_start"]}: {start_night.to_datetime():%H:%M} {t["time_utc_suffix"]}
- {t["night_end"]}: {end_night.to_datetime():%H:%M} {t["time_utc_suffix"]}
- {t["night_sunrise"]}: {night_events['nascer_do_sol'].to_datetime():%H:%M} {t["time_utc_suffix"]}
""")

                # Collect target names
                target_names = []
                if use_deep_sky:
                    target_names.extend(DEEP_SKY_TARGETS_PRESET)
                if manual_targets_input.strip():
                    target_names.extend(
                        [ln.strip() for ln in manual_targets_input.split('\n') if ln.strip()]
                    )

                # Resolve deep-sky coordinates
                all_targets = {}
                if target_names:
                    with st.spinner(t["fetching_coords_spinner"].format(n=len(target_names))):
                        all_targets.update(get_target_skycoords(target_names))

                # Add Solar System bodies
                if use_solar_system:
                    with st.spinner(t["solar_system_spinner"]):
                        all_targets.update(registrar_alvos_sistema_solar(start_night))

                if not all_targets:
                    st.warning(t["no_targets_warning"])
                else:
                    st.success(t["analysing_targets"].format(n=len(all_targets)))

                    # Visibility plot for each target
                    for target_name, target_coord in all_targets.items():
                        if target_coord is not None:
                            df_visible = analyze_target_visibility_for_night(
                                start_night, end_night,
                                observer_location, target_coord, min_altitude
                            )
                            if not df_visible.empty:
                                st.subheader(f"✅ {target_name}")
                                fig = plot_target_visibility(
                                    df_visible, target_name, analysis_date, min_altitude_deg
                                )
                                st.pyplot(fig)
                                plt.close(fig)

                                duration = (
                                    df_visible['time'].iloc[-1] - df_visible['time'].iloc[0]
                                ).total_seconds() / 3600.0
                                max_alt = df_visible['altitude'].max()
                                st.write(t["obs_window_label"].format(dur=duration))
                                st.write(t["max_alt_label"].format(alt=max_alt))
                            else:
                                st.warning(
                                    t["target_not_visible"].format(
                                        name=target_name, min=min_altitude_deg
                                    )
                                )

                    # ── Sky Map ──────────────────────────────────────────
                    st.markdown("---")
                    st.subheader(t["sky_map_subheader"])
                    st.write(t["sky_map_description"])

                    midnight_hour = night_events['meia_noite_real'].to_datetime().hour
                    col_sl, col_btn = st.columns([4, 1])
                    with col_sl:
                        selected_hour = st.slider(
                            t["sky_map_slider"],
                            min_value=0, max_value=23,
                            value=midnight_hour, step=1,
                            format="%d:00",
                            help=t["sky_map_slider"]
                        )
                    with col_btn:
                        st.write("")
                        st.write("")
                        if st.button(t["sky_map_button"], key="sky_map_button", type="primary"):
                            try:
                                hour = selected_hour
                                map_datetime = (
                                    analysis_date.replace(hour=hour, minute=0)
                                    if hour >= 12
                                    else (analysis_date + timedelta(days=1)).replace(
                                        hour=hour, minute=0
                                    )
                                )
                                map_time = Time(map_datetime)

                                # Filter targets visible at the selected hour
                                visible_at_time = {}
                                frame = AltAz(obstime=map_time, location=observer_location)
                                for name, coord in all_targets.items():
                                    if coord is not None:
                                        altaz = coord.transform_to(frame)
                                        if altaz.alt.deg >= min_altitude_deg:
                                            visible_at_time[name] = coord

                                if visible_at_time:
                                    st.success(
                                        t["sky_map_success"].format(
                                            n=len(visible_at_time), h=hour
                                        )
                                    )
                                    fig = plot_sky_map(
                                        visible_at_time, observer_location, map_time
                                    )
                                    st.pyplot(fig)
                                    plt.close(fig)
                                    st.info(t["sky_map_how_to_read"])
                                else:
                                    st.warning(
                                        t["sky_map_no_targets"].format(
                                            min=min_altitude_deg, h=hour
                                        )
                                    )
                            except Exception as e:
                                st.error(t["sky_map_error"].format(err=e))

# ═══════════════════════════════════════════════════════════════════════════ #
#  TAB 2 — Annual Calendar                                                    #
# ═══════════════════════════════════════════════════════════════════════════ #
with tab2:
    st.header(t["annual_header"])
    yearly_target_name = st.text_input(
        t["annual_target_label"], t["annual_target_default"], key="yearly_target"
    )
    year = st.number_input(
        t["annual_year_label"],
        value=date.today().year, min_value=1900, max_value=2100, key="yearly_year"
    )

    if st.button(t["annual_button"], type="primary", key="yearly_button"):
        if 'observer_location' not in st.session_state:
            st.error(t["no_location_error"])
        else:
            observer_location = st.session_state['observer_location']
            observer_timezone = set_timezone_for_sao_paulo(observer_location) or pytz.UTC

            with st.spinner(t["annual_target_spinner"].format(name=yearly_target_name)):
                target_coords = get_target_skycoords([yearly_target_name])

            if (yearly_target_name not in target_coords
                    or target_coords[yearly_target_name] is None):
                st.error(t["annual_target_error"].format(name=yearly_target_name))
            else:
                target_coord = target_coords[yearly_target_name]

                with st.spinner(
                    t["annual_analysis_spinner"].format(name=yearly_target_name, year=year)
                ):
                    df_year = analyze_year_visibility(
                        year, observer_location, observer_timezone,
                        target_coord, min_altitude
                    )

                if df_year.empty:
                    st.warning(
                        t["annual_no_data"].format(
                            name=yearly_target_name, min=min_altitude_deg, year=year
                        )
                    )
                else:
                    st.success(
                        t["annual_success"].format(
                            name=yearly_target_name, n=len(df_year), year=year
                        )
                    )

                    fig = plot_yearly_visibility(df_year, yearly_target_name, year)
                    if fig:
                        st.pyplot(fig)
                        plt.close(fig)

                    st.subheader(t["stats_subheader"])
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric(t["stat_visible_nights"], len(df_year))
                    with col2:
                        avg_dur = df_year['duration_hours'].mean()
                        st.metric(t["stat_avg_duration"], f"{avg_dur:.2f}h")
                    with col3:
                        max_dur = df_year['duration_hours'].max()
                        st.metric(t["stat_max_duration"], f"{max_dur:.2f}h")

                    # Best month
                    best_month_idx = (
                        df_year
                        .groupby(pd.to_datetime(df_year['date']).dt.month)['duration_hours']
                        .mean()
                        .idxmax()
                    )
                    month_name = t["month_names"][best_month_idx - 1]
                    st.info(t["best_period"].format(month=month_name, year=year))
