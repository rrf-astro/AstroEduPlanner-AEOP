# tests/test_location.py

import pytest
from astropy.coordinates import EarthLocation
from astropy import units as u
import pytz

from src.location import get_location_from_city, set_timezone_for_sao_paulo

def test_get_location_from_city_success():
    """
    Tests that the function returns a valid EarthLocation object for a known city.
    """
    city = "São Paulo, Brazil"
    location = get_location_from_city(city)

    assert isinstance(location, EarthLocation)
    assert u.isclose(location.lat, -23.55 * u.deg, atol=1 * u.deg)
    assert u.isclose(location.lon, -46.63 * u.deg, atol=1 * u.deg)

def test_get_location_from_city_not_found():
    """
    Tests that the function returns None for a non-existent city name.
    """
    # Fix: The function returns None rather than raising an exception.
    location = get_location_from_city("NonExistentCity12345")
    assert location is None

def test_set_timezone_for_sao_paulo_inside():
    """
    Tests that the correct timezone is returned for a location inside the Brazilian bounding box.
    """
    location_sp = EarthLocation(lat=-23.55 * u.deg, lon=-46.63 * u.deg)
    tz = set_timezone_for_sao_paulo(location_sp)

    assert tz is not None
    assert tz == pytz.timezone('America/Sao_Paulo')

def test_set_timezone_for_sao_paulo_outside():
    """
    Tests that None is returned for a location outside the Brazilian bounding box.
    """
    location_lisbon = EarthLocation(lat=38.72 * u.deg, lon=-9.13 * u.deg)
    tz = set_timezone_for_sao_paulo(location_lisbon)

    assert tz is None
