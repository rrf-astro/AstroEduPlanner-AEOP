# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-24

### Added
- Interactive web interface with Streamlit (no programming required)
- Jupyter Notebook for customisable analyses and scientific Python education
- Nightly visibility analysis for multiple targets (altitude vs. time plots with twilight regions)
- Annual visibility calendar with heatmap (colour-coded by hours of visibility)
- **Sky map (polar projection)** — Interactive sky chart showing target positions above the horizon at any selected time, available in both Streamlit (via `st.slider`) and Jupyter Notebook (via `ipywidgets.IntSlider`)
- Deep-sky target support via SIMBAD (Astroquery) with fallback to SkyCoord name resolver
- Solar System body positions for 10 objects (Sun, Moon, planets, Pluto) at any epoch
- Hemisphere visibility pre-filter to skip observationally inaccessible targets
- Lunar impact analysis: illumination percentage and angular separation from target
- Weather forecast integration via Open-Meteo API (cloud cover for next observing night)
- Automatic geolocation from city name (Nominatim/geopy)
- Minimum elevation constraint (configurable, default 30°)
- Complete pytest test suite covering analysis, location, and target modules
- Comprehensive documentation (README, CONTRIBUTING, CODE_OF_CONDUCT)
- MIT Licence for free educational use

### Modules
- `src/config.py` — Centralised imports and global configuration
- `src/location.py` — City-name geocoding and timezone utilities
- `src/targets.py` — Deep-sky and Solar System target management
- `src/analysis.py` — Visibility calculations, lunar impact, and weather forecast
- `src/plotting.py` — Altitude plots, sky maps, and annual heatmaps

### Tests
- `tests/test_analysis.py` — Tests for the analysis module
- `tests/test_location.py` — Tests for geolocation
- `tests/test_targets.py` — Tests for target management

---

## [Unreleased]

### Planned
- Support for custom target catalogues (CSV/FITS)
- PDF export of observation reports
- Offline mode (cached ephemerides)
- Spanish localisation
- Integration with automated telescope mounts

---

[1.0.0]: https://github.com/seu-usuario/Skyler-Testes/releases/tag/v1.0.0
