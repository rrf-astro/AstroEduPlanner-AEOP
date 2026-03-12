# tests/test_analysis.py

import pytest
from astropy.coordinates import EarthLocation, SkyCoord
from astropy.time import Time
from astropy import units as u
import pytz
import pandas as pd
from datetime import date

from src.location import get_location_from_city, set_timezone_for_sao_paulo
from src.analysis import (
    calculate_nightly_events,
    analyze_target_visibility_for_night,
    check_hemisphere_visibility,
    analyze_moon_impact,
    analyze_year_visibility
)

@pytest.fixture(scope="module")
def observer_location():
    """Fixture providing an observer location (São Paulo, Brazil)."""
    return get_location_from_city("São Paulo, Brazil")

@pytest.fixture(scope="module")
def observer_timezone(observer_location):
    """Fixture providing the observer's timezone."""
    return set_timezone_for_sao_paulo(observer_location)

@pytest.fixture(scope="module")
def southern_target():
    """Fixture for a target in the southern celestial hemisphere (Sirius)."""
    return SkyCoord.from_name('Sirius')

@pytest.fixture(scope="module")
def northern_target():
    """Fixture for a target in the northern celestial hemisphere (Polaris)."""
    return SkyCoord.from_name('Polaris')

def test_calculate_nightly_events(observer_location, observer_timezone):
    """
    Tests that nightly events are computed correctly and contain expected keys.
    """
    test_date = date(2023, 1, 15)
    events = calculate_nightly_events(test_date, observer_location, observer_timezone)

    assert isinstance(events, dict)
    keys = ['inicio_noite', 'fim_noite', 'meia_noite_real']
    for key in keys:
        assert key in events
        assert isinstance(events[key], Time)
    assert events['inicio_noite'] < events['fim_noite']

def test_analyze_target_visibility_for_night_visible(observer_location, observer_timezone, southern_target):
    """
    Tests visibility analysis for a target that should be observable.
    """
    # Use January, when Sirius is visible from the southern hemisphere.
    test_date = date(2023, 1, 15)
    events = calculate_nightly_events(test_date, observer_location, observer_timezone)
    df = analyze_target_visibility_for_night(
        events['inicio_noite'], events['fim_noite'], observer_location, southern_target, 30*u.deg
    )

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert 'altitude' in df.columns
    assert df['altitude'].max() > 30

def test_analyze_target_visibility_for_night_not_visible(observer_location, observer_timezone, northern_target):
    """
    Tests that a target unobservable from the southern hemisphere returns an empty DataFrame.
    """
    test_date = date(2023, 6, 15)
    events = calculate_nightly_events(test_date, observer_location, observer_timezone)
    df = analyze_target_visibility_for_night(
        events['inicio_noite'], events['fim_noite'], observer_location, northern_target, 30*u.deg
    )
    assert df.empty

def test_check_hemisphere_visibility(observer_location, southern_target, northern_target):
    """
    Tests the hemisphere visibility pre-filter logic.
    """
    assert check_hemisphere_visibility(observer_location, southern_target) == True
    assert check_hemisphere_visibility(observer_location, northern_target) == False

def test_analyze_moon_impact(observer_location, southern_target):
    """
    Tests that lunar impact analysis returns illumination and separation values.
    """
    time = Time('2023-01-15T23:00:00')
    moon_analysis = analyze_moon_impact(time, observer_location, southern_target)

    assert isinstance(moon_analysis, dict)
    assert 'moon_illumination' in moon_analysis
    assert 'moon_separation' in moon_analysis
    assert 0.0 <= moon_analysis['moon_illumination'] <= 100.0
    assert isinstance(moon_analysis['moon_separation'], u.Quantity)

def test_analyze_year_visibility(observer_location, observer_timezone, southern_target):
    """
    Tests that the annual visibility function returns a correctly structured DataFrame.
    """
    year = 2023
    min_altitude = 30 * u.deg
    df_year = analyze_year_visibility(year, observer_location, observer_timezone, southern_target, min_altitude)

    assert isinstance(df_year, pd.DataFrame)
    if not df_year.empty:
        expected_columns = ['date', 'start_time', 'end_time', 'duration_hours']
        for col in expected_columns:
            assert col in df_year.columns
