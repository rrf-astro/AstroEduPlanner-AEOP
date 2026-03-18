# tests/test_targets.py

import pytest
from astropy.coordinates import SkyCoord
from astropy import units as u

from src.targets import get_target_skycoords, registrar_alvos_sistema_solar

def test_get_target_skycoords_single_target():
    """
    Tests that the function returns correct coordinates for a single well-known target.

    Skipped if the SIMBAD/Astroquery name-resolution service is unavailable.
    """
    targets = get_target_skycoords(['Sirius'])
    if not targets:
        pytest.skip("SIMBAD/Astroquery unavailable — skipping network-dependent test.")
    assert 'Sirius' in targets
    assert isinstance(targets['Sirius'], SkyCoord)
    # Approximate coordinates of Sirius
    assert u.isclose(targets['Sirius'].ra, 101.28 * u.deg, atol=1 * u.deg)
    assert u.isclose(targets['Sirius'].dec, -16.71 * u.deg, atol=1 * u.deg)

def test_get_target_skycoords_multiple_targets():
    """
    Tests processing of a list of multiple targets.

    Skipped if the SIMBAD/Astroquery name-resolution service is unavailable.
    """
    target_names = ['Sirius', 'Betelgeuse']
    targets = get_target_skycoords(target_names)
    if not targets:
        pytest.skip("SIMBAD/Astroquery unavailable — skipping network-dependent test.")
    assert len(targets) == 2
    assert 'Sirius' in targets
    assert 'Betelgeuse' in targets

def test_get_target_skycoords_invalid_target():
    """
    Tests that invalid targets are silently skipped and not present in the result.

    Skipped if the SIMBAD/Astroquery service is unavailable (returns empty dict for any input).
    """
    target_names = ['Sirius', 'InvalidTarget123']
    targets = get_target_skycoords(target_names)
    if not targets:
        pytest.skip("SIMBAD/Astroquery unavailable — skipping network-dependent test.")
    assert len(targets) == 1
    assert 'Sirius' in targets
    assert 'InvalidTarget123' not in targets

def test_registrar_alvos_sistema_solar():
    """
    Tests that the Solar System function returns a dictionary of SkyCoord objects.
    """
    from astropy.time import Time

    # An observation time is required to compute Solar System body positions
    observation_time = Time('2023-01-01T00:00:00')

    ss_targets = registrar_alvos_sistema_solar(observation_time)

    assert isinstance(ss_targets, dict)
    assert 'Mars' in ss_targets  # Verify that a known planet is present
    assert 'Moon' in ss_targets
    assert isinstance(ss_targets['Mars'], SkyCoord)
