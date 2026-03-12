---
title: 'AstroEduPlanner (AEOP): An Open-Source Python Tool for Astronomical Observation Planning in Educational Contexts'
tags:
  - Python
  - astronomy
  - education
  - observation planning
  - astropy
  - streamlit
  - jupyter
  - open-source
authors:
  - name: PLACEHOLDER Full Name of Author 1
    orcid: 0000-0000-0000-0000
    affiliation: 1
  - name: PLACEHOLDER Full Name of Author 2
    orcid: 0000-0000-0000-0000
    affiliation: PLACEHOLDER
affiliations:
  - name: PLACEHOLDER Institution Name, City, Country
    index: 1
date: 12 March 2026
bibliography: paper.bib
---

# Summary

AstroEduPlanner (AEOP) is an open-source, Python-based tool designed to lower the technical barriers to astronomical observation planning in educational settings. Built on the Astropy [@astropy2013; @astropy2018; @astropy2022] and Astroplan [@Morris2018] libraries, AEOP enables teachers, students, and amateur astronomers to determine when and where celestial objects are observable from any location on Earth, without requiring prior knowledge of observational astronomy software or professional ephemeris systems.

The tool exposes two complementary interfaces targeting different user profiles. The first is an interactive web application built with Streamlit [@Streamlit2024], which requires no programming skills: users select their observing site, date, and targets through a graphical sidebar and obtain publication-quality altitude-versus-time plots and annual visibility calendars immediately. The second is a fully documented Jupyter Notebook that exposes the same modular Python backend, allowing students and instructors to inspect, modify, and extend the underlying calculations as part of coursework in observational astronomy or scientific computing.

AEOP resolves target names through the SIMBAD database via Astroquery, computes Solar System body positions for ten objects, estimates lunar interference (illumination fraction and angular separation), and integrates real-time cloud cover forecasts from the Open-Meteo API [@Zippenfenig2023]. The software has been developed with Brazilian public schools and higher education institutions in mind, where access to commercial observatory planning platforms is typically unavailable.

# Statement of Need

Observation planning is a foundational skill in practical astronomy education. Before a telescope session — whether at a secondary school, a university observatory, or a public outreach event — students must determine which objects will be above the horizon, assess the interference from the Moon, check atmospheric conditions, and justify their target selection within a limited observing window. This process requires knowledge of coordinate systems, astronomical twilight, airmass, and ephemeris computation that are rarely covered in introductory courses before hands-on observing sessions begin [@Bretones2016].

Several established tools address observation planning for professional or advanced amateur use. Stellarium [@Stellarium2024] and Cartes du Ciel provide rich sky visualisation but offer no programmatic API and cannot be scripted for classroom assignments. Skyfield provides precise ephemerides as a Python library but has no built-in educational interface and presupposes substantial programming experience. Astroplan [@Morris2018] targets professional observatory scheduling and, while powerful, lacks a user-friendly interface accessible to students with no programming background.

A gap therefore exists for a tool that simultaneously serves two distinct educational audiences: students who benefit from a visual, interactive interface requiring zero programming knowledge, and students learning scientific Python who need a structured, well-documented codebase they can explore and modify. This dual-interface design philosophy is the primary innovation of AEOP relative to existing solutions, and mirrors pedagogical strategies increasingly adopted in astronomy education research [@Caballero2020].

The need is particularly acute in Brazil and analogous middle-income countries, where public secondary schools and regional universities face severe resource constraints. Commercial observation planning platforms are expensive or inaccessible from institutional networks with restricted outbound connectivity. AEOP is entirely free, open-source under the MIT Licence, operates without authentication, and connects only to free APIs (Nominatim for geocoding, SIMBAD for target resolution, Open-Meteo for weather). The preset target list has been curated to include southern-hemisphere showpieces — Omega Centauri, 47 Tucanae, Eta Carinae Nebula — that are prominent from Brazilian latitudes and rarely foregrounded in northern-hemisphere-centric textbooks [@Bretones2016].

Several papers in the Journal of Open Source Education and the Journal of Open Source Software have demonstrated the value of purpose-built, open-source tools for narrowing access gaps in astronomy education [@Villano2023; @Fitzgerald2021]. AEOP follows this tradition by targeting the specific bottleneck of pre-observation planning, a step that is consistently identified by instructors as the stage where students require the most scaffolded support.

# Instructional Design

AEOP's architecture reflects two evidence-based instructional principles. The first is the separation of conceptual understanding from technical complexity: students who are learning *what* astronomical visibility means should not be simultaneously required to learn *how* to write Python. The Streamlit interface eliminates programming as a barrier, allowing the instructor to focus discussion on the underlying astronomy — why does Orion disappear from Brazilian skies in May? how does a 70% illuminated Moon affect observation of a faint galaxy? — rather than on software operation.

The second principle is progressive disclosure. The Jupyter Notebook is structured so that all parameters are configurable in a single cell at the top of the document before any calculations run. Students in an introductory scientific Python course can therefore begin by simply changing values (`NOME_DA_CIDADE`, `DATA_ANALISE`, `ELEVACAO_MINIMA_GRAUS`) and re-running cells, observing how outputs change before they are expected to read or modify the underlying functions in `src/`. Advanced students can then inspect `src/analysis.py` and `src/plotting.py` to understand how Astropy's `AltAz` frame transformation pipeline works, providing a direct pedagogical pathway into the Astropy ecosystem [@astropy2022].

The modular architecture — five independent Python modules in `src/` covering configuration, geolocation, target resolution, visibility analysis, and plotting — was deliberately designed to align with software engineering concepts typically introduced in second-year undergraduate curricula: separation of concerns, unit testing with pytest, and dependency management via `requirements.txt` and `pyproject.toml`.

# Features and Functionality

AEOP implements the following core features, all verified against the source code in `src/`:

**Nightly visibility analysis.** The function `analyze_target_visibility_for_night()` samples a target's altitude above the observer's horizon at 5-minute intervals throughout the astronomical night (from evening to morning astronomical twilight, computed via Astroplan's `Observer` class). Results are filtered to intervals above a user-defined minimum elevation (default 30°) and returned as a pandas DataFrame. The companion function `plot_target_visibility()` renders an altitude-versus-time plot with the observation window highlighted in green and the minimum elevation threshold marked as a horizontal dashed line (Figure 1).

**Annual visibility calendar.** The function `analyze_year_visibility()` iterates over all 365 nights of a selected year, computing the total hours of visibility above the threshold for each night. Results are visualised as a month-by-day heatmap using seaborn, where colour intensity encodes hours of visibility (Figure 2). This calendar allows students to identify seasonal patterns and identify the optimal observing window for a given target.

**Polar sky map.** The function `plot_sky_map()` renders a North-up azimuthal projection of all selected targets above the horizon at a user-selected time. In the Streamlit interface, the time is controlled by an interactive slider over the observing night; in the Jupyter Notebook, the same slider is implemented via `ipywidgets`.

**Lunar impact analysis.** The function `analyze_moon_impact()` computes the Moon's illumination fraction (as a percentage) and its angular separation from any selected target using Astropy's `moon_illumination` and `SkyCoord.separation()`.

**Flexible target selection.** Deep-sky objects are resolved by name through the SIMBAD database via Astroquery, with automatic fallback to `SkyCoord.from_name()`. Solar System bodies (Sun, Moon, eight planets, and Pluto) are computed via Astropy's `get_body()` at the epoch of observation. A hemisphere pre-filter (`check_hemisphere_visibility()`) silently excludes targets that are geometrically inaccessible from the observer's latitude.

**Weather forecast integration.** Cloud cover forecasts for the coming observing night are retrieved from the Open-Meteo API [@Zippenfenig2023] and displayed in the Streamlit sidebar alongside the observing parameters.

![Altitude-versus-time plot generated by `plot_target_visibility()` for the Orion Nebula (M42) observed from Uberaba, Brazil (lat. −19.7°) on a representative winter night. The green shaded area marks the observation window above the 30° elevation threshold; the red dashed line marks the threshold itself.](figures/fig1_altitude_plot.png)

![Annual visibility calendar heatmap generated by `plot_yearly_visibility()` for M42 (Orion Nebula) as seen from Uberaba, Brazil in 2024. Each cell encodes the number of hours the target was above 30° on that night; darker cells indicate longer visibility windows. The gap in June–July reflects the southern winter when Orion is a daytime object.](figures/fig2_annual_heatmap.png)

# Usage in Teaching

**Secondary school — BNCC-aligned inquiry activity.** The Brazilian National Curriculum (BNCC) includes competencies related to Earth's position in the Solar System and seasonal sky changes. An instructor can direct students to the Streamlit interface, set the location to their school's city, and ask: "In which month can we best observe the Southern Cross from here? What would change if we were in Manaus instead of Porto Alegre?" Students adjust parameters, compare altitude plots across dates and locations, and record observations, with no code involved. The activity takes approximately 50 minutes and requires only a browser.

**Undergraduate observational astronomy — pre-observation proposal.** Before a scheduled telescope session, students use AEOP to draft a two-page observation proposal: they select three targets with peak altitude above 45° during the allocated window, verify that lunar separation exceeds 30° for each, and confirm that cloud cover forecast is below 20%. They justify their choices by exporting and annotating the altitude plots generated by AEOP. This structured workflow mirrors professional observing proposal formats (e.g., those used by Brazilian telescope facilities) while remaining accessible to third-semester students.

**Introduction to Scientific Python — notebook exploration.** Students clone the repository, install dependencies, and open `analise_astronomica.ipynb`. They first run all cells with default parameters to verify that the environment works, then complete a series of guided exercises: changing the observation date, adding a custom target from a CSV file, modifying `ELEVACAO_MINIMA_GRAUS`, and finally reading the source of `analyze_year_visibility()` to explain in their own words how the annual calendar is constructed. [PLACEHOLDER: add specific course name, institution, and number of students if real deployment data are available.]

# Acknowledgements

[PLACEHOLDER: Acknowledge funding sources (CNPq, CAPES, FAPESP, or other) and any colleagues who contributed to testing or course deployment. Example: "The authors thank the students of [course name] at [institution] for feedback during development."]

# References
