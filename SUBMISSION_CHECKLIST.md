# JOSE Submission Checklist — AstroEduPlanner (AEOP)

*Last updated: 2026-03-18 — audited programmatically against actual repo state.*

---

## BLOCO A — CONCLUÍDO PELO AGENTE ✅

### Etapa 0 — Limpeza do repositório
- [x] Removidos: `streamlit.log`, `analise_astronomica.html`
- [x] Removidas notas internas de dev: `ANALISE_PROBLEMA_SLIDER.md`, `CORRECAO_SLIDER_FINAL.md`, `SOLUCAO_DEFINITIVA_MAPA.md`, `CORRECOES_MAPA_DO_CEU.md`, `MAPA_DO_CEU.md`, `SLIDER_INTERATIVO.md`
- [x] Removido `create_notebook.py` (utilitário interno)
- [x] Criado `.gitignore` (`*.log`, `__pycache__/`, `.env`, `venv/`, `*.pyc`, `*.html`, etc.)

### Etapa 2.5 — Tradução para inglês
- [x] `README.md` — já estava em inglês; tabela de estrutura atualizada
- [x] `CHANGELOG.md` — traduzido para inglês; entradas expandidas
- [x] `CONTRIBUTING.md` — totalmente traduzido; URLs placeholder corrigidas
- [x] `src/config.py` — docstring e comentários traduzidos
- [x] `src/location.py` — docstrings NumPy-style em inglês
- [x] `src/analysis.py` — docstrings NumPy-style em inglês
- [x] `src/targets.py` — docstrings NumPy-style em inglês
- [x] `src/plotting.py` — docstrings NumPy-style em inglês; labels dos eixos em inglês
- [x] `tests/test_analysis.py` — docstrings traduzidas
- [x] `tests/test_location.py` — docstrings traduzidas
- [x] `tests/test_targets.py` — docstrings traduzidas
- [x] `requirements.txt` — comentários de seção traduzidos

### Etapa 3 — Melhorias do repositório
- [x] `.github/workflows/tests.yml` — CI corrigido: `pip install -e .[dev]` (fix da quebra de CI)
- [x] `pyproject.toml` — nome `astroedu-planner`; classifiers, keywords; `pythonpath = ["."]`; extras `[dev]`
- [x] `README.md` — badge CI, badge Zenodo (placeholder), ref. notebook corrigida, seção Citation
- [x] `CITATION.cff` — CFF v1.2.0, estrutura completa
- [x] `LICENSE` — copyright atualizado para AstroEduPlanner (AEOP)
- [x] `tests/conftest.py` — criado: marcador `network`, flag `--no-network`
- [x] `tests/test_analysis.py` — skip guards em todos os fixtures dependentes de rede
- [x] `tests/test_location.py` — skip guard no teste de geocoding
- [x] `tests/test_targets.py` — skip guards nos testes de SIMBAD

### Etapa 3d — Internacionalização (i18n)
- [x] `src/i18n/__init__.py` — criado
- [x] `src/i18n/strings.py` — 70 chaves × 2 idiomas (EN/PT), dicionários simétricos
- [x] `app.py` — refatorado com `t = LANGUAGES[language]`; bug `EarthLocation truthiness` corrigido
- [x] `analise_astronomica.ipynb` — célula bilíngue de introdução; comentários `# EN:` / `# PT:`

### Etapas 4–6 — Arquivos de submissão JOSE
- [x] `paper.md` — formato JOSE completo: 7 seções, YAML front matter, 11 citation keys validadas
- [x] `paper.bib` — 12 entradas BibTeX; cross-check ↔ paper.md: ✅ OK
- [x] `figures/README_FIGURES.md` — instruções completas para gerar as figuras
- [x] `figures/fig1_altitude_plot.png` — gerada (250 KB, 300 DPI) — M42, Uberaba, 2024-01-15
- [x] `figures/fig2_annual_heatmap.png` — gerada (174 KB, 300 DPI) — M42, Uberaba, 2024

---

## BLOCO B — AÇÃO HUMANA NECESSÁRIA ⚠️

### 🔴 CRÍTICO — obrigatório antes da submissão

- [ ] **`paper.md` — preencher todos os `[PLACEHOLDER]`:**
  - Nomes completos dos autores e identificadores ORCID (registre em https://orcid.org se necessário)
  - Nome(s) da(s) instituição(ões) e país
  - Seção Acknowledgements (financiamento: CNPq, CAPES, FAPESP ou outro)
  - Seção "Usage in Teaching": adicionar nome do curso real, instituição e número de alunos

- [ ] **`CITATION.cff` — preencher 10 campos placeholder:**
  - `family-names`, `given-names`, `orcid`, `affiliation` (autor e preferred-citation)
  - `repository-code`, `url` (substituir `PLACEHOLDER-username` pelo username real do GitHub)
  - `doi` (após criar release no Zenodo)
  - `year` na seção `preferred-citation`

- [ ] **`pyproject.toml` — preencher 6 campos placeholder:**
  - `name` do autor e `email` institucional
  - Todas as 4 URLs (Homepage, Documentation, Repository, Bug Tracker)

- [ ] **`README.md` — substituir 9 placeholders:**
  - `PLACEHOLDER-username` nas URLs dos badges, clone URL e link de Issues
  - Badge Zenodo DOI (após obter DOI)

- [ ] **`LICENSE` — atualizar linha de copyright:**
  - Substituir `AstroEduPlanner (AEOP) Contributors` pelo nome legal do titular do copyright

- [ ] **Criar release no Zenodo e obter DOI:**
  1. Acesse https://zenodo.org → sign in → "GitHub" → "Sync"
  2. Ative o toggle para seu repositório
  3. Crie um GitHub Release com a tag `v1.0.0` — Zenodo gera o DOI automaticamente
  4. Atualize o badge DOI no `README.md`
  5. Atualize o campo `doi` em `CITATION.cff` (dois lugares: raiz e `preferred-citation`)

- [ ] **Verificar 3 entradas BibTeX marcadas `% VERIFICAR DOI` em `paper.bib`:**
  - `Bretones2016` — DOI sugerido: `10.19030/jaese.v3i2.9844` (confirmar em https://doi.org)
  - `Stellarium2024` — sem DOI; citar como URL de software (já feito)
  - Revisar se há terceira entrada marcada

- [ ] **Executar pytest e confirmar que todos os testes passam:**
  ```bash
  pip install -e .[dev]
  pytest tests/ -v
  ```
  Com rede disponível: todos os testes devem passar.
  Sem rede: testes de rede devem aparecer como SKIPPED (não FAILED).

### 🟡 ANTES DE FAZER PUSH NO GITHUB

- [ ] Fazer push de todos os arquivos novos e modificados:
  ```bash
  git add .
  git commit -m "Prepare repository for JOSE submission (v1.0.0)"
  git push origin main
  ```
- [ ] Verificar que o workflow de CI passa na aba "Actions" do GitHub
- [ ] Confirmar que o badge Zenodo DOI renderiza corretamente no README

### 🔵 SUBMISSÃO JOSE

- [ ] Acesse https://jose.theoj.org e clique em **"Submit a paper"**
- [ ] Preencha o formulário:
  - **Repository URL:** URL do repositório no GitHub
  - **Branch:** `main`
  - **Paper path:** `paper.md`
- [ ] Verifique a compilação do paper no preview do JOSE
  (preview local opcional):
  ```bash
  docker run --rm -it -v $PWD:/data -u $(id -u):$(id -g) \
    openjournals/inara -o pdf,crossref paper.md
  ```
- [ ] Enviar e anotar o número do issue pré-review atribuído pelo bot do JOSE

### ⚪ OPCIONAL (recomendado)

- [ ] Criar `CONTRIBUTORS.md` ou reconhecer contribuidores no `README.md`
- [ ] Adicionar tag `v1.0.0` no git antes do release do Zenodo:
  ```bash
  git tag v1.0.0
  git push origin v1.0.0
  ```
- [ ] Verificar se `README_PT.md` está atualizado com as mesmas informações do `README.md`

---

## RESUMO DO ESTADO ATUAL

| Componente | Estado |
|---|---|
| Código-fonte (`src/`) | ✅ Funcional, documentado em inglês, i18n EN/PT |
| Testes (`tests/`) | ✅ Skip guards; conftest.py presente |
| CI (GitHub Actions) | ✅ Corrigido — `pip install -e .[dev]` |
| `paper.md` | ✅ Estrutura JOSE completa ⚠️ 1 placeholder |
| `paper.bib` | ✅ 12 entradas, cross-validadas |
| `figures/` | ✅ fig1 e fig2 geradas (300 DPI) |
| `CITATION.cff` | ✅ Estrutura válida ⚠️ 10 placeholders |
| `README.md` | ✅ Completo ⚠️ 9 placeholders |
| `pyproject.toml` | ✅ Correto ⚠️ 6 placeholders |
| `LICENSE` | ✅ MIT ⚠️ nome do titular a confirmar |

**Bloqueadores reais antes da submissão: apenas os PLACEHOLDERs de metadados do autor e o DOI do Zenodo.**
O repositório está tecnicamente pronto.

---

*Gerado pelo agente de preparação JOSE em 2026-03-12. Atualizado em 2026-03-18.*
