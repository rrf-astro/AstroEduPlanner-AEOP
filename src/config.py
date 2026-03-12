# src/config.py

"""
Configuration Module.

This file centralises the import of commonly used libraries and the
configuration of global parameters for the tool. Dependencies
specific to each module (such as geopy or astroquery) should be imported
directly in the modules that use them.
"""

# --- Standard Library ---
import warnings
from datetime import datetime, timedelta, date

# --- Data Analysis Libraries ---
import numpy as np
import pandas as pd

# --- Astronomical Libraries ---
import astropy.units as u
from astropy.coordinates import EarthLocation, SkyCoord, AltAz, get_body
from astropy.coordinates.funcs import get_sun
from astropy.time import Time
from astroplan import Observer
from astroplan.moon import moon_illumination
from astropy.utils.exceptions import AstropyWarning
import erfa

# --- Visualisation Libraries ---
import matplotlib.pyplot as plt

# --- Other ---
import requests
from tqdm.auto import tqdm

# --- Global Configuration ---
warnings.filterwarnings('ignore', category=AstropyWarning)
warnings.filterwarnings('ignore', category=erfa.ErfaWarning)

# Constants and Parameters
MIN_ALTITUDE_DEFAULT = 30 * u.deg

print("Configuration module (src/config.py) loaded successfully.")
