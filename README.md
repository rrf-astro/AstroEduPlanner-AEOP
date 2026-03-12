# 🔭 AstroEduPlanner (AEOP): An Open-Source Educational Astronomical Observation Planner

[![Tests](https://github.com/PLACEHOLDER-username/AstroEduPlanner-AEOP/actions/workflows/tests.yml/badge.svg)](https://github.com/PLACEHOLDER-username/AstroEduPlanner-AEOP/actions/workflows/tests.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Astropy-Enabled](https://img.shields.io/badge/Astropy-Enabled-blueviolet)](https://www.astropy.org/)
[![Interface: Streamlit](https://img.shields.io/badge/Interface-Streamlit-red)](https://streamlit.io/)

**AstroEduPlanner (AEOP)** is an open-source, Python-based educational tool for planning astronomical observations. Using a modular architecture built on the [Astropy](https://www.astropy.org/) and [Astroplan](https://astroplan.readthedocs.io/) libraries, the tool enables teachers, students, and amateur astronomers to analyse the visibility of celestial objects from any location on Earth.

> 🇧🇷 Originally developed for Brazilian public schools and higher education institutions.  
> A Portuguese version of this document is available in [README_PT.md](README_PT.md).

---

## ✨ Key Features

- **🌙 Detailed Nightly Analysis** — Generate altitude vs. time plots for multiple targets on a given night, including civil, nautical, and astronomical twilight regions.
- **📅 Annual Visibility Calendar** — Create interactive heatmaps to identify the best nights to observe a target throughout the year.
- **📍 Flexible Location Input** — Define your observing site by city name (e.g., `"Porto, Portugal"`) or by geographic coordinates.
- **🎯 Comprehensive Target Selection** — Use pre-defined target lists, add Solar System objects, or enter any object manually (e.g., `"NGC 1300"`).
- **🌡️ Atmospheric Constraints** — Set a minimum target elevation above the horizon to optimise observation quality.
- **🌕 Lunar Impact Analysis** — Calculate lunar illumination and angular separation from selected targets.
- **☁️ Weather Forecast Integration** — Real-time cloud cover and seeing forecasts via the [Open-Meteo](https://open-meteo.com/) API.

---

## 📁 Project Structure

```
AstroEduPlanner-AEOP/
├── README.md                    # This file (English)
├── README_PT.md                 # Portuguese version
├── LICENSE                      # MIT Licence
├── CITATION.cff                 # Machine-readable citation metadata
├── requirements.txt             # Python dependencies
├── pyproject.toml               # Build configuration
├── paper.md                     # JOSE submission paper
├── paper.bib                    # BibTeX references
├── figures/                     # Figures for the paper
├── app.py                       # Streamlit web application
├── analise_astronomica.ipynb    # Interactive Jupyter Notebook
├── src/                         # Modular source code
│   ├── config.py               # Centralised configuration
│   ├── location.py             # Geolocation utilities
│   ├── targets.py              # Target management
│   ├── analysis.py             # Astronomical calculations
│   └── plotting.py             # Visualisation routines
├── tests/                       # pytest test suite
│   ├── test_analysis.py
│   ├── test_location.py
│   └── test_targets.py
└── .github/workflows/
    └── tests.yml                # Continuous integration (GitHub Actions)
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/rrf-astro/AstroEduPlanner-AEOP.git
   cd AstroEduPlanner-AEOP
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate       # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Alternative Installation

```bash
pip install -e .
```

---

## 💻 Usage

### Option 1 — Web Application (Streamlit) 🌐

Ideal for an interactive visual experience with no programming required.

```bash
streamlit run app.py
```

The application will open automatically in your browser at `http://localhost:8501`.

**Workflow:**
1. Set your observing location in the sidebar
2. Select the date and minimum elevation constraint
3. Choose between a nightly analysis or annual visibility calendar
4. Explore the interactive plots

### Option 2 — Jupyter Notebook 📓

Ideal for customisation, data analysis, and integration with other Python scripts.

```bash
jupyter notebook
```

Open `analise_astronomica_EN.ipynb` from the browser interface. The notebook includes step-by-step instructions in Markdown cells.

---

## 📖 Quick Tutorial

### Nightly Analysis (Streamlit)

1. **Set Location** — Type your city (e.g., `São Paulo, Brazil`) and click **Set Location**
2. **Set Parameters** — Choose the observation date and minimum elevation
3. **Select Targets** — Use pre-defined lists, Solar System objects, or enter objects manually
4. **Run Analysis** — Click **Generate Nightly Analysis**
5. **Explore Results** — View altitude vs. time plots for each selected target

### Annual Visibility Calendar (Streamlit)

1. **Configure Location** (as above)
2. **Choose a Target** — Enter an object name (e.g., `M31`)
3. **Select the Year** — Use the numeric input field
4. **Generate Calendar** — Click **Generate Annual Calendar**
5. **Read the Heatmap** — Lighter colours indicate higher target altitude (better visibility)

---

## 🧪 Running Tests

```bash
pytest tests/
```

To check code coverage:

```bash
pytest --cov=src tests/
```

---

## 🎓 Educational Use Cases

This software was designed with the following contexts in mind:

**Secondary Schools (aligned with the Brazilian BNCC curriculum)**  
Without writing any code, students use the Streamlit interface to investigate seasonal target visibility, understand lunar interference, and explore how airmass affects observation quality.

**Undergraduate Observational Astronomy**  
Prior to a telescope session, students draft an observation proposal using AEOP: selecting targets within an airmass limit of 2.0, avoiding high lunar proximity, and justifying their chosen window using integrated weather forecasts.

**Introduction to Scientific Python**  
Students use the Jupyter Notebook to learn the Astropy ecosystem, modifying the provided code to add custom observing constraints specific to their local observatory's horizon profile.

**Public Outreach and Extension Programmes**  
Organisers of public stargazing events use AEOP's weather integration and altitude plots to schedule events and select targets that will be optimally positioned for small-aperture telescopes.

---

## 🤝 Contributing

Contributions are very welcome! This is an educational and community-driven project.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/MyFeature`
3. Commit your changes: `git commit -m 'Add MyFeature'`
4. Push to the branch: `git push origin feature/MyFeature`
5. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for full contribution guidelines.

---

## 🌟 Acknowledgements

- [Astropy](https://www.astropy.org/) — Core astronomy library for Python
- [Astroplan](https://astroplan.readthedocs.io/) — Observation planning built on Astropy
- [Streamlit](https://streamlit.io/) — Interactive web application framework
- [Open-Meteo](https://open-meteo.com/) — Open-source weather forecast API
- The Brazilian astronomy education community

---

## 📝 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

## 📧 Contact and Support

- **Issues** — Report bugs or suggest features via [GitHub Issues](https://github.com/rrf-astro/AstroEduPlanner-AEOP/issues)
- **Discussions** — Join the conversation on [GitHub Discussions](https://github.com/rrf-astro/AstroEduPlanner-AEOP/discussions)

---

## 🔗 Related Software

AEOP occupies a distinct niche among existing tools:

| Tool | Type | Target Audience | Key Limitation for Education |
|---|---|---|---|
| [Stellarium](https://stellarium.org/) | Desktop/Web GUI | General public | No programmatic API; cannot be scripted for classroom exercises |
| [Cartes du Ciel](https://www.ap-i.net/skychart/) | Desktop GUI | Amateur astronomers | Windows-centric; no Python integration |
| [Skyfield](https://rhodesmill.org/skyfield/) | Python library | Developers | No educational interface; requires programming expertise |
| [astroplan](https://astroplan.readthedocs.io/) | Python library | Research astronomers | Designed for observatory scheduling, not pedagogy |
| **AEOP** | Python app (dual interface) | **Students & teachers** | — |

AEOP uniquely combines a **no-code web interface** (Streamlit) with a **programmable Jupyter Notebook**, both built on the same modular scientific backend, making it appropriate for a continuum of users from secondary school students to undergraduate researchers.

---

## 📖 Citation

If you use AstroEduPlanner (AEOP) in your research or teaching, please cite:

```bibtex
@article{PLACEHOLDER_JOSE_2025,
  author  = {PLACEHOLDER: Author Names},
  title   = {AstroEduPlanner (AEOP): An Open-Source Python Tool for
             Astronomical Observation Planning in Educational Contexts},
  journal = {Journal of Open Source Education},
  year    = {PLACEHOLDER},
  volume  = {PLACEHOLDER},
  number  = {PLACEHOLDER},
  pages   = {PLACEHOLDER},
  doi     = {PLACEHOLDER}
}
```

A machine-readable citation file is available at [`CITATION.cff`](CITATION.cff).

---

*Good skies! 🔭✨*
