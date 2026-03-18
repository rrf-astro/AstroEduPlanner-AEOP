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

## [1.5] - 2026-03-18

### Added
- **Bilingual interface (EN/PT)** — full internationalisation via `src/i18n/strings.py` with 70 UI string keys per language; language selector in the Streamlit sidebar (`st.sidebar.selectbox`); parallel `# EN:` / `# PT:` comments throughout the Jupyter Notebook configuration cell
- **GitHub Actions CI** — automated test workflow (`.github/workflows/tests.yml`) with matrix across Python 3.10 and 3.11; coverage report via `pytest-cov`
- **CITATION.cff** — machine-readable software citation in Citation File Format v1.2.0 with full author metadata, ORCID, affiliation, and Zenodo DOI
- **JOSE submission files** — `paper.md` (all 7 required sections), `paper.bib` (12 BibTeX entries), `figures/fig1_altitude_plot.png` and `figures/fig2_annual_heatmap.png` (both at 300 DPI)
- **Zenodo DOI** — software archived at [https://doi.org/10.5281/zenodo.19102549](https://doi.org/10.5281/zenodo.19102549)
- **Network-resilient test suite** — `tests/conftest.py` with `--no-network` CLI flag and `pytest.skip()` guards in all three test modules for Nominatim and SIMBAD dependencies

### Fixed
- `ValueError: EarthLocation truthiness is ambiguous` in `app.py` — replaced `if observer_location:` with `if observer_location is not None:`

### Changed
- `pyproject.toml` — corrected project name to `astroedu-planner`; added `[project.optional-dependencies] dev`; added `pythonpath = ["."]` to pytest options; updated all URLs to `github.com/rrf-astro/AstroEduPlanner-AEOP`
- `README.md` — added CI badge, Zenodo DOI badge, Related Software comparison table, and Citation section
- All source files (`src/`, `tests/`) — docstrings and inline comments fully translated to English (NumPy-style)
- CI install step changed from `pip install -r requirements.txt` to `pip install -e .[dev]` to ensure the package is installed in editable mode before tests run

### Planned
- Support for custom target catalogues (CSV/FITS)
- PDF export of observation reports
- Offline mode (cached ephemerides)
- Spanish localisation
- Integration with automated telescope mounts

---

[1.5]: https://github.com/rrf-astro/AstroEduPlanner-AEOP/releases/tag/v1.5
[1.0.0]: https://github.com/rrf-astro/AstroEduPlanner-AEOP/releases/tag/v1.0.0
