# src/targets.py

"""
Target Management Module.
Provides functions for resolving deep-sky object names to sky coordinates
via SIMBAD/Astroquery, and for computing Solar System body positions.
"""
import warnings

from astroquery.simbad import Simbad
# Fix: The correct exception name is TimeoutError, not AstroqueryTimeoutError.
from astroquery.exceptions import RemoteServiceError, TimeoutError

from astropy.coordinates import SkyCoord, get_body
from astropy.time import Time
from astropy import units as u
import pandas as pd
from tqdm.auto import tqdm

DEEP_SKY_TARGETS_PRESET = [
    'M31', 'M42', 'M45', 'M13', 'M51', 'M8', 'M20',
    'Eta Carinae Nebula', '47 Tucanae', 'Omega Centauri',
    'Sirius', 'Canopus', 'Betelgeuse', 'Rigel', 'Vega'
]
SOLAR_SYSTEM_TARGETS_PRESET = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

def get_target_skycoords(target_names_list):
    """
    Resolves celestial coordinates (RA/Dec) for a list of target names.

    Queries SIMBAD via Astroquery as the primary resolver, falling back
    to SkyCoord.from_name() if SIMBAD is unavailable.

    Args:
        target_names_list (list of str): List of object names (e.g. ['M31', 'Sirius']).

    Returns:
        dict: Mapping from target name to astropy SkyCoord object.
            Targets that could not be resolved are omitted from the dictionary.
    """
    print(f"Resolving coordinates for {len(target_names_list)} targets...")
    targets_coords = {}

    simbad = Simbad()
    simbad.add_votable_fields('ra', 'dec')

    for name in tqdm(target_names_list, desc="Fetching Targets"):
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                result_table = simbad.query_object(name)

            if result_table:
                ra = result_table['RA'][0]
                dec = result_table['DEC'][0]
                targets_coords[name] = SkyCoord(ra=ra*u.deg, dec=dec*u.deg, frame='icrs')
            else:
                targets_coords[name] = SkyCoord.from_name(name)
        except (RemoteServiceError, TimeoutError, Exception) as e:
            print(f"  WARNING: Could not resolve target '{name}'. Trying fallback. Error: {e}")
            try:
                # If SIMBAD fails, try the default SkyCoord name resolver
                targets_coords[name] = SkyCoord.from_name(name)
            except Exception as fallback_e:
                print(f"  WARNING: Fallback also failed for '{name}'. Error: {fallback_e}")
                continue

    return targets_coords

def registrar_alvos_sistema_solar(observation_time):
    """
    Retrieves the coordinates of major Solar System bodies for a given epoch.

    Args:
        observation_time (astropy.time.Time): Time of observation.

    Returns:
        dict: Mapping from body name to astropy SkyCoord (or SkyCoordInfo object
            from get_body). Bodies that could not be computed are omitted.
    """
    print("Fetching Solar System body positions...")
    ss_targets = {}
    for name in tqdm(SOLAR_SYSTEM_TARGETS_PRESET, desc="Computing Positions"):
        try:
            ss_targets[name] = get_body(name.lower(), observation_time)
        except Exception as e:
            print(f"  WARNING: Could not obtain coordinates for '{name}'. Error: {e}")
    return ss_targets

print("Target management module (src/targets.py) loaded.")
