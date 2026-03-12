# src/plotting.py

"""
Plotting Module.
Contains functions for generating all astronomical data visualisations:
altitude-vs-time plots, polar sky maps, and annual visibility heatmaps.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy import units as u
from matplotlib.dates import DateFormatter
import seaborn as sns
from astropy.coordinates import SkyCoord, AltAz

def plot_target_visibility(df_visible, target_name, analysis_date, min_altitude_deg):
    """
    Generates an altitude-vs-time plot for a target over a single night.

    Args:
        df_visible (pandas.DataFrame): DataFrame with 'time' and 'altitude' columns,
            filtered to rows where altitude >= min_altitude_deg.
        target_name (str): Name of the target object.
        analysis_date (datetime.date): Date of the observation.
        min_altitude_deg (float): Minimum elevation threshold in degrees.

    Returns:
        matplotlib.figure.Figure: The generated figure.
    """
    fig, ax = plt.subplots(figsize=(12, 6))

    if not df_visible.empty:
        ax.plot(df_visible['time'], df_visible['altitude'], label=f'Altitude of {target_name}', color='royalblue')
        ax.fill_between(df_visible['time'], min_altitude_deg, df_visible['altitude'],
                        where=(df_visible['altitude'] >= min_altitude_deg),
                        color='green', alpha=0.3, label=f'Observation Window (>{min_altitude_deg}°)')

    ax.axhline(min_altitude_deg, color='red', linestyle='--', label=f'Minimum Elevation ({min_altitude_deg}°)')
    ax.set_ylim(0, 90)
    ax.set_xlabel(f'Time (UTC) on {analysis_date.strftime("%Y-%m-%d")}')
    ax.set_ylabel('Altitude (degrees)')
    ax.set_title(f'Visibility of {target_name}')
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.7)

    # Time axis formatting
    ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
    fig.autofmt_xdate()

    return fig

def plot_sky_map(targets_coords, observer_location, time):
    """
    Generates a polar sky map showing target positions above the horizon at a specific time.

    The map uses a North-up, East-left azimuthal projection. Only objects
    currently above the horizon (altitude > 0°) are plotted.

    Args:
        targets_coords (dict): Mapping from target name to astropy SkyCoord.
        observer_location (astropy.coordinates.EarthLocation): Observer's location.
        time (astropy.time.Time): Time for which to compute positions.

    Returns:
        matplotlib.figure.Figure: The generated polar figure.
    """
    frame = AltAz(obstime=time, location=observer_location)

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})

    for name, coord in targets_coords.items():
        altaz = coord.transform_to(frame)
        if altaz.alt > 0:  # Only plot objects above the horizon
            ax.plot(altaz.az.radian, 90 - altaz.alt.deg, 'o', label=name, markersize=10)

    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_rlim(0, 90)
    ax.set_yticks([0, 30, 60, 90])  # Set tick positions
    ax.set_yticklabels(['90° (Zenith)', '60°', '30°', '0° (Horizon)'])
    ax.set_title(f'Sky Map at {time.to_datetime():%Y-%m-%d %H:%M} UTC')
    ax.legend(bbox_to_anchor=(1.1, 1.1))
    ax.grid(True)

    return fig

def plot_yearly_visibility(df_year, target_name, year):
    """
    Generates a calendar heatmap of a target's visibility throughout a year.

    Each cell represents one night; colour intensity encodes the number of
    hours the target was above the minimum elevation.

    Args:
        df_year (pandas.DataFrame): Output of analyze_year_visibility(), with
            columns 'date', 'start_time', 'end_time', 'duration_hours'.
        target_name (str): Name of the target object.
        year (int): The year being displayed.

    Returns:
        matplotlib.figure.Figure or None: The generated figure, or None if
            df_year is empty.
    """
    if df_year.empty:
        print(f"No visibility data to plot for {target_name} in {year}.")
        return None  # Return None if there is no data

    # Prepare data for the heatmap
    df_year['month'] = pd.to_datetime(df_year['date']).dt.month
    df_year['day'] = pd.to_datetime(df_year['date']).dt.day

    heatmap_data = df_year.pivot_table(index='month', columns='day', values='duration_hours')

    fig, ax = plt.subplots(figsize=(18, 7))
    sns.heatmap(heatmap_data, cmap='viridis', robust=True, ax=ax, cbar_kws={'label': 'Hours of Visibility'})

    ax.set_title(f'Visibility Calendar for {target_name} in {year} (hours > {df_year.get("min_alt", 30)}°)')
    ax.set_xlabel('Day of Month')
    ax.set_ylabel('Month')
    ax.set_yticks(ticks=np.arange(12) + 0.5, labels=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ], rotation=0)

    return fig

print("Plotting module (src/plotting.py) loaded.")
