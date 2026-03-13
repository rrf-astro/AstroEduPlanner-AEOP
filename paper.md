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

AEOP resolves target names through the SIMBAD database via Astroquery, computes Solar System body positions for ten objects, estimates lunar interference (illumination fraction and angular separation), and integrates real-time cloud cover forecasts from the Open-Meteo API [@Zippenfenig2023]. The software has been developed with Brazilian public schools and higher education institutions in mind, where access to commercial observatory planning platforms is typically unavailable. Both the Streamlit interface and the Jupyter Notebook are available in English and Brazilian Portuguese, selected via a single sidebar control, reflecting the tool's dual audience of international educators and Brazilian teachers and students for whom operating a scientific tool in a foreign language would constitute an additional and unnecessary barrier.

# Statement of Need

Observation planning is a foundational skill in practical astronomy education. Before a telescope session — whether at a secondary school, a university observatory, or a public outreach event — students must determine which objects will be above the horizon, assess the interference from the Moon, check atmospheric conditions, and justify their target selection within a limited observing window. This process requires knowledge of coordinate systems, astronomical twilight, airmass, and ephemeris computation that are rarely covered in introductory courses before hands-on observing sessions begin [@Bretones2016].

Several established tools address observation planning for professional or advanced amateur use. Stellarium [@Stellarium2024] and Cartes du Ciel provide rich sky visualisation but offer no programmatic API and cannot be scripted for classroom assignments. Skyfield provides precise ephemerides as a Python library but has no built-in educational interface and presupposes substantial programming experience. Astroplan [@Morris2018] targets professional observatory scheduling and, while powerful, lacks a user-friendly interface accessible to students with no programming background.

A gap therefore exists for a tool that simultaneously serves two distinct educational audiences: students who benefit from a visual, interactive interface requiring zero programming knowledge, and students learning scientific Python who need a structured, well-documented codebase they can explore and modify. This dual-interface design philosophy is the primary innovation of AEOP relative to existing solutions, and mirrors pedagogical strategies increasingly adopted in astronomy education research [@Caballero2020].

The need is particularly acute in Brazil and analogous middle-income countries, where public secondary schools and regional universities face severe resource constraints. Commercial observation planning platforms are expensive or inaccessible from institutional networks with restricted outbound connectivity. AEOP is entirely free, open-source under the MIT Licence, operates without authentication, and connects only to free APIs (Nominatim for geocoding, SIMBAD for target resolution, Open-Meteo for weather). The preset target list has been curated to include southern-hemisphere showpieces — Omega Centauri, 47 Tucanae, Eta Carinae Nebula — that are prominent from Brazilian latitudes and rarely foregrounded in northern-hemisphere-centric textbooks [@Bretones2016].

Several papers in the Journal of Open Source Education and the Journal of Open Source Software have demonstrated the value of purpose-built, open-source tools for narrowing access gaps in astronomy education [@Villano2023; @Fitzgerald2021]. AEOP follows this tradition by targeting the specific bottleneck of pre-observation planning, a step that is consistently identified by instructors as the stage where students require the most scaffolded support.

# Instructional Design

AEOP's architecture reflects two evidence-based instructional principles. The first is the separation of conceptual understanding from technical complexity: students who are learning *what* astronomical visibility means should not be simultaneously required to learn *how* to write Python. The Streamlit interface eliminates programming as a barrier, allowing the instructor to focus discussion on the underlying astronomy — why does Orion disappear from Brazilian skies in May? how does a 70% illuminated Moon affect observation of a faint galaxy? — rather than on software operation.

The second principle is progressive disclosure. The Jupyter Notebook is structured so that all parameters are configurable in a single cell at the top of the document before any calculations run. Students in an introductory scientific Python course can therefore begin by simply changing values (`NOME_DA_CIDADE`, `DATA_ANALISE`, `ELEVACAO_MINIMA_GRAUS`) and re-running cells, observing how outputs change before they are expected to read or modify the underlying functions in `src/`. Advanced students can then inspect `src/analysis.py` and `src/plotting.py` to understand how Astropy's `AltAz` frame transformation pipeline works, providing a direct pedagogical pathway into the Astropy ecosystem [@astropy2022].

A third design principle is **linguistic accessibility**. Language barriers constitute a genuine form of exclusion in science education: Brazilian public school teachers and students with limited English proficiency have historically been unable to use English-only scientific tools without additional support. AEOP addresses this directly with a built-in bilingual interface (English and Brazilian Portuguese) controlled by a single `selectbox` in the Streamlit sidebar and by parallel `# EN:` / `# PT:` comments throughout the Jupyter Notebook configuration cell. The Portuguese interface allows Brazilian instructors to focus classroom time on the astronomy rather than on navigating a foreign-language tool; the English interface ensures the software is fully accessible to and citable by the international astronomy education community. The 62 string pairs are managed in a single `src/i18n/strings.py` module, designed to make the addition of further languages (e.g. Spanish, for broader Latin American reach) a localised and non-invasive change.

The modular architecture — five independent Python modules in `src/` covering configuration, geolocation, target resolution, visibility analysis, and plotting — was deliberately designed to align with software engineering concepts typically introduced in second-year undergraduate curricula: separation of concerns, unit testing with pytest, and dependency management via `requirements.txt` and `pyproject.toml`.

# Features and Functionality

AEOP's core capabilities, verified against the source code in `src/`, include: (1) **nightly visibility analysis** — altitude-versus-time plots sampled at 5-minute intervals across the astronomical night (Figure 1); (2) **annual visibility calendar** — a month-by-day heatmap of observing hours for any target over a full year (Figure 2); (3) **polar sky map** — a North-up azimuthal chart of all targets above the horizon at a user-selected time, controlled by an interactive slider in both interfaces; (4) **lunar impact** — Moon illumination fraction and angular separation from any target; (5) **weather forecast** — cloud cover for the coming night via the Open-Meteo API [@Zippenfenig2023]; (6) **flexible target selection** — deep-sky objects resolved via SIMBAD/Astroquery with `SkyCoord.from_name()` fallback, plus Solar System body positions for ten objects via `get_body()`; and (7) **bilingual interface (EN/PT)** — a single sidebar selector switches all 62 visible strings between English and Brazilian Portuguese, with further languages addable via `src/i18n/strings.py`.

![Altitude-versus-time plot generated by `plot_target_visibility()` for the Orion Nebula (M42) observed from Uberaba, Brazil (lat. −19.7°) on a representative winter night. The green shaded area marks the observation window above the 30° elevation threshold; the red dashed line marks the threshold itself.](figures/fig1_altitude_plot.png)

![Annual visibility calendar heatmap generated by `plot_yearly_visibility()` for M42 (Orion Nebula) as seen from Uberaba, Brazil in 2024. Each cell encodes the number of hours the target was above 30° on that night; darker cells indicate longer visibility windows. The gap in June–July reflects the southern winter when Orion is a daytime object.](figures/fig2_annual_heatmap.png)

# Usage in Teaching

**Scenario 1 — International university course (English interface).** In an undergraduate observational astronomy course, students use the English Streamlit interface to draft a pre-observation proposal before a scheduled telescope session: selecting three targets with peak altitude above 45°, verifying lunar separation exceeds 30° for each, and confirming cloud cover forecast is below 20%. They justify target choices by annotating the altitude plots generated by AEOP. This workflow mirrors professional proposal formats while remaining accessible to second-year students with no prior planning-software experience.

**Scenario 2 — Brazilian public school (Portuguese interface, no coding required).** A secondary school teacher switches the interface to Português and directs students to the Streamlit application, requiring only a browser. Aligned with the Brazilian National Curriculum (BNCC) competencies on Earth's position in the Solar System, the activity asks: "In which month can we best observe the Southern Cross from here? What would change if we were in Manaus instead of Porto Alegre?" Students adjust parameters and compare altitude plots with no code involved. The fully Portuguese interface eliminates the foreign-language barrier that would otherwise prevent independent use in this context.

**Scenario 3 — Scientific Python course (bilingual Jupyter Notebook).** Students open `analise_astronomica.ipynb`, where the configuration cell contains parallel `# EN:` / `# PT:` comments on every line. They begin by modifying only the configuration variables, then read the English-documented source in `src/analysis.py` to understand how Astropy's `AltAz` frame transformation works, and finally write a short function that extends the existing pipeline. The bilingual structure allows native Portuguese speakers to start in their first language and transition to English documentation as their confidence grows. [PLACEHOLDER: add course name, institution, and enrolment if deployment data are available.]

# Acknowledgements

[PLACEHOLDER: Acknowledge funding sources (CNPq, CAPES, FAPESP, or other) and any colleagues who contributed to testing or course deployment. Example: "The authors thank the students of [course name] at [institution] for feedback during development."]

# References
