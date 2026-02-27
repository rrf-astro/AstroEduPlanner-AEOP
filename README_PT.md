# 🔭 AstroEduPlanner (AEOP): Planejador de Observações Astronômicas Educacional de Código Aberto

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Astropy-Enabled](https://img.shields.io/badge/Astropy-Enabled-blueviolet)](https://www.astropy.org/)
[![Interface: Streamlit](https://img.shields.io/badge/Interface-Streamlit-red)](https://streamlit.io/)

**AstroEduPlanner (AEOP)** é uma ferramenta educacional de código aberto em Python para planejamento de observações astronômicas. Utilizando uma arquitetura modular construída sobre as bibliotecas [Astropy](https://www.astropy.org/) e [Astroplan](https://astroplan.readthedocs.io/), a ferramenta permite que professores, estudantes e astrônomos amadores analisem a visibilidade de corpos celestes a partir de qualquer localização na Terra.

> 🇧🇷 Desenvolvido especialmente para escolas públicas e instituições de ensino superior brasileiras.  
> A versão em inglês deste documento está disponível em [README.md](README.md).

---

## ✨ Funcionalidades Principais

- **🌙 Análise Noturna Detalhada** — Gere gráficos de altitude vs. tempo para múltiplos alvos em uma noite específica, incluindo regiões de crepúsculo civil, náutico e astronômico.
- **📅 Calendário de Visibilidade Anual** — Crie mapas de calor interativos para identificar as melhores noites para observar um alvo ao longo do ano.
- **📍 Localização Flexível** — Defina seu local de observação pelo nome da cidade (ex: `"Porto, Portugal"`) ou por coordenadas geográficas.
- **🎯 Seleção Abrangente de Alvos** — Use listas pré-definidas, adicione objetos do sistema solar ou insira qualquer objeto manualmente (ex: `"NGC 1300"`).
- **🌡️ Restrições Atmosféricas** — Configure a elevação mínima do alvo acima do horizonte para otimizar a qualidade da observação.
- **🌕 Análise de Impacto da Lua** — Calcule a iluminação lunar e a separação angular dos alvos selecionados.
- **☁️ Previsão Meteorológica** — Previsões de cobertura de nuvens em tempo real via API [Open-Meteo](https://open-meteo.com/).

---

## 📁 Estrutura do Projeto

```
AstroEduPlanner-AEOP/
├── README.md                    # Versão em inglês
├── README_PT.md                 # Este arquivo (Português)
├── LICENSE                      # Licença MIT
├── requirements.txt             # Dependências Python
├── pyproject.toml               # Configuração de build
├── app.py                       # Aplicação web Streamlit
├── analise_astronomica.ipynb    # Jupyter Notebook interativo (PT)
├── analise_astronomica_EN.ipynb # Jupyter Notebook interativo (EN)
├── create_notebook.py           # Script de geração do notebook
├── src/                         # Código-fonte modular
│   ├── config.py               # Configurações centralizadas
│   ├── location.py             # Utilitários de geolocalização
│   ├── targets.py              # Gerenciamento de alvos
│   ├── analysis.py             # Cálculos astronômicos
│   └── plotting.py             # Rotinas de visualização
└── tests/                       # Suite de testes pytest
    ├── test_analysis.py
    ├── test_location.py
    └── test_targets.py
```

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/rrf-astro/AstroEduPlanner-AEOP.git
   cd AstroEduPlanner-AEOP
   ```

2. **Crie um ambiente virtual** (recomendado):

   ```bash
   python3 -m venv venv
   source venv/bin/activate       # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

### Instalação Alternativa

```bash
pip install -e .
```

---

## 💻 Opções de Uso

### Opção 1 — Aplicação Web (Streamlit) 🌐

Ideal para uma experiência visual e interativa sem necessidade de programação.

```bash
streamlit run app.py
```

A aplicação abrirá automaticamente no navegador em `http://localhost:8501`.

**Fluxo de uso:**
1. Configure sua localização na barra lateral
2. Selecione a data e a elevação mínima
3. Escolha entre análise noturna ou calendário anual
4. Explore os gráficos interativos

### Opção 2 — Jupyter Notebook 📓

Ideal para personalização, análise de dados e integração com outros scripts Python.

```bash
jupyter notebook
```

Abra `analise_astronomica.ipynb` no navegador. O notebook contém instruções detalhadas em células Markdown.

---

## 📖 Tutorial Rápido

### Análise Noturna (Streamlit)

1. **Defina sua Localização** — Digite o nome da cidade (ex: `São Paulo, Brazil`) e clique em **Definir Localização**
2. **Ajuste Parâmetros** — Selecione a data e a elevação mínima
3. **Selecione Alvos** — Use listas pré-definidas, objetos do sistema solar ou adicione manualmente
4. **Gere a Análise** — Clique em **Gerar Análise da Noite**
5. **Visualize Resultados** — Veja gráficos de altitude vs. tempo para cada alvo selecionado

### Calendário Anual (Streamlit)

1. **Configure a Localização** (como acima)
2. **Escolha um Alvo** — Digite o nome do objeto (ex: `M31`)
3. **Selecione o Ano** — Use o campo numérico
4. **Gere o Calendário** — Clique em **Gerar Calendário Anual**
5. **Leia o Heatmap** — Cores mais claras indicam maior altitude do alvo (melhor visibilidade)

---

## 🧪 Executando os Testes

```bash
pytest tests/
```

Para verificar a cobertura de código:

```bash
pytest --cov=src tests/
```

---

## 🎓 Casos de Uso Educacional

Este software foi desenvolvido pensando nos seguintes contextos:

**Ensino Médio (alinhado à BNCC)**  
Sem escrever código, os estudantes usam a interface Streamlit para investigar a visibilidade sazonal dos alvos, entender a interferência lunar e explorar como a massa de ar afeta a qualidade das observações.

**Graduação em Astronomia Observacional**  
Antes de uma sessão com o telescópio, os alunos elaboram uma proposta de observação usando o AEOP: selecionando alvos dentro de um limite de massa de ar de 2,0, evitando alta proximidade lunar e justificando a janela escolhida com base nas previsões meteorológicas.

**Introdução ao Python Científico**  
Os alunos usam o Jupyter Notebook para aprender o ecossistema Astropy, modificando o código fornecido para adicionar restrições de observação personalizadas específicas ao perfil de horizonte do observatório local.

**Divulgação e Extensão Universitária**  
Organizadores de eventos de astronomia pública usam a integração meteorológica e os gráficos de altitude do AEOP para programar eventos e selecionar alvos que estarão otimamente posicionados para telescópios de pequena abertura.

---

## 🤝 Como Contribuir

Contribuições são muito bem-vindas! Este é um projeto educacional e comunitário.

1. Faça um fork do repositório
2. Crie seu branch: `git checkout -b feature/MinhaFeature`
3. Faça o commit: `git commit -m 'Adiciona MinhaFeature'`
4. Envie o branch: `git push origin feature/MinhaFeature`
5. Abra um Pull Request

Leia o guia completo em [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 🌟 Agradecimentos

- [Astropy](https://www.astropy.org/) — Biblioteca central de astronomia em Python
- [Astroplan](https://astroplan.readthedocs.io/) — Planejamento de observações baseado no Astropy
- [Streamlit](https://streamlit.io/) — Framework de aplicação web interativa
- [Open-Meteo](https://open-meteo.com/) — API de previsão meteorológica de código aberto
- A comunidade brasileira de educação em astronomia

---

## 📝 Licença

Este projeto está licenciado sob a Licença MIT — veja [LICENSE](LICENSE) para detalhes.

---

## 📧 Contato e Suporte

- **Issues** — Reporte bugs ou sugira funcionalidades via [GitHub Issues](https://github.com/rrf-astro/AstroEduPlanner-AEOP/issues)
- **Discussões** — Participe das [GitHub Discussions](https://github.com/rrf-astro/AstroEduPlanner-AEOP/discussions)

---

*Boas observações! 🔭✨*
