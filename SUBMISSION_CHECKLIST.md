# JOSE Submission Checklist — AstroEduPlanner (AEOP)

---

## BLOCO A — O QUE O AGENTE JÁ FEZ (nesta sessão)

### Repository Cleanup (Etapa 0)
- [x] Removed `streamlit.log`, `analise_astronomica.html`
- [x] Removed internal dev notes: `ANALISE_PROBLEMA_SLIDER.md`, `CORRECAO_SLIDER_FINAL.md`, `SOLUCAO_DEFINITIVA_MAPA.md`, `CORRECOES_MAPA_DO_CEU.md`
- [x] Migrated sky map and interactive slider feature documentation to `CHANGELOG.md`, then removed `MAPA_DO_CEU.md` and `SLIDER_INTERATIVO.md`
- [x] Removed `create_notebook.py` (internal development utility)
- [x] Created `.gitignore` (covers `*.log`, `__pycache__/`, `.env`, `venv/`, `*.pyc`, `*.html`, etc.)

### Configuration Files
- [x] `pyproject.toml` — corrected project name (`astroedu-planner`), added classifiers, keywords, URLs; replaced placeholder author; translated all Portuguese comments

### Translation (Etapa 2.5)
- [x] `README.md` — already in English; project structure table updated
- [x] `CHANGELOG.md` — translated to English; entries expanded with feature detail
- [x] `CONTRIBUTING.md` — fully translated to English; placeholder GitHub URLs corrected
- [x] `src/config.py` — docstring and all inline comments translated to English
- [x] `src/location.py` — docstrings and inline comments translated to English
- [x] `src/analysis.py` — full NumPy-style docstrings written in English
- [x] `src/targets.py` — full NumPy-style docstrings written in English
- [x] `src/plotting.py` — full NumPy-style docstrings written in English
- [x] `tests/test_analysis.py` — all docstrings translated
- [x] `tests/test_location.py` — all docstrings translated; Portuguese city name in test kept (it is test data, not a comment)
- [x] `tests/test_targets.py` — all docstrings translated
- [x] `requirements.txt` — inline comments translated

### Repository Improvements (Etapa 3)
- [x] `.github/workflows/tests.yml` — GitHub Actions CI workflow (Python 3.10 + 3.11, pytest, coverage)
- [x] `README.md` — added CI badge, Zenodo DOI badge (placeholder), project structure updated, "Related Software" comparison table, "Citation" section with BibTeX placeholder
- [x] `CITATION.cff` — Citation File Format v1.2, full metadata with ORCID and DOI placeholders

### JOSE Submission Files (Etapas 4–6)
- [x] `paper.md` — complete JOSE-format paper (~1230 words), YAML front matter, all 6 sections
- [x] `paper.bib` — 12 BibTeX entries; 2 entries marked `% VERIFICAR DOI`
- [x] `figures/README_FIGURES.md` — complete instructions for generating both paper figures

---

## BLOCO B — O QUE O AUTOR HUMANO AINDA PRECISA FAZER

### Critical — must be done before submission

- [ ] **Fill in all `[PLACEHOLDER]` fields in `paper.md`:**
  - Author full names and ORCID identifiers (register at https://orcid.org if needed)
  - Institution name(s) and country
  - Acknowledgements section (funding: CNPq, CAPES, FAPESP, or other)
  - `Usage in Teaching` section: add real course name, institution, number of students

- [ ] **Fill in all `PLACEHOLDER` fields in `CITATION.cff`** (author name, ORCID, institution)

- [ ] **Fill in all `PLACEHOLDER-username` GitHub URLs** in:
  - `README.md` (badge URLs, clone URL, Issues link)
  - `CONTRIBUTING.md` (clone URL)
  - `pyproject.toml` (project URLs)
  - `CITATION.cff` (repository-code URL)

- [ ] **Generate the two paper figures** following `figures/README_FIGURES.md`:
  - `figures/fig1_altitude_plot.png` (300 DPI minimum)
  - `figures/fig2_annual_heatmap.png` (300 DPI minimum)

- [ ] **Create a Zenodo release and link it to GitHub:**
  1. Go to https://zenodo.org, sign in, click "GitHub" → "Sync"
  2. Flip the toggle for your repository
  3. Create a GitHub Release (tag `v1.0.0`) — Zenodo auto-deposits and assigns a DOI
  4. Update the DOI badge in `README.md`
  5. Update `doi` field in `CITATION.cff`
  6. Update `doi` field in the `preferred-citation` block of `CITATION.cff`

- [ ] **Verify the two BibTeX entries marked `% VERIFICAR DOI`** in `paper.bib`:
  - `Bretones2016` — DOI: 10.19030/jaese.v3i2.9844
  - `Stellarium2024` — no DOI exists; cite as software URL (already done)

- [ ] **Run pytest and confirm all tests pass:**
  ```bash
  pip install -r requirements.txt
  pytest tests/ -v
  ```
  Fix any failing tests before pushing.

- [ ] **Update the project structure in `README.md`** if `README_PT.md` is to be kept or removed.

### Before pushing to GitHub

- [ ] Push all new and modified files to the main branch:
  ```bash
  git add .
  git commit -m "Prepare repository for JOSE submission"
  git push origin main
  ```
- [ ] Verify that the GitHub Actions CI workflow passes (check the Actions tab)
- [ ] Confirm that Zenodo DOI badge renders correctly in the README

### JOSE Submission

- [ ] Go to https://jose.theoj.org and click **"Submit a paper"**
- [ ] Fill in the submission form:
  - **Repository URL:** your GitHub repository URL
  - **Branch:** `main`
  - **Paper path:** `paper.md`
- [ ] Verify the paper compiles correctly in the JOSE preview
  (local preview: `docker run --rm -it -v $PWD:/data -u $(id -u):$(id -g) openjournals/inara -o pdf,crossref paper.md`)
- [ ] Submit and note the pre-review issue number assigned by the JOSE editor bot

### Optional but recommended

- [ ] Add a second language version of the Jupyter Notebook in English
  (`analise_astronomica_EN.ipynb`) — currently referenced in the old README but the file does not exist; either create it or remove the reference (already removed from the updated README)
- [ ] Add a `CONTRIBUTORS.md` or acknowledge contributors in `README.md`
- [ ] Tag version `v1.0.0` in git before the Zenodo release

---

*Generated by JOSE preparation agent on 2026-03-12.*
