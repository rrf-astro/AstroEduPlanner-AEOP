# 🔭 AstroEduPlanner (AEOP): An Open-Source Educational Astronomical Observation Planner

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Este repositório contém uma ferramenta educacional de código aberto para planejamento de observações astronômicas. Utilizando uma arquitetura modular em Python, a ferramenta permite que professores, estudantes e astrônomos amadores analisem a visibilidade de corpos celestes a partir de qualquer localização na Terra.

**Desenvolvido especialmente para escolas públicas e instituições de ensino superior brasileiras.**

A ferramenta oferece duas interfaces principais para atender a diferentes necessidades:
1. **Aplicação Web com Streamlit**: Uma interface gráfica interativa, ideal para uso rápido e visual.
2. **Jupyter Notebook**: Para usuários que desejam explorar a análise de forma mais profunda, personalizar o código ou integrá-lo em seus próprios scripts.

![Python](https://img.shields.io/badge/Astropy-Enabled-blueviolet)
![Streamlit](https://img.shields.io/badge/Interface-Streamlit-red)

---

## ✨ Funcionalidades Principais

-   **🌙 Análise Noturna Detalhada**: Gere gráficos de altitude vs. tempo para múltiplos alvos em uma noite específica.
-   **📅 Calendário de Visibilidade Anual**: Crie um mapa de calor para identificar as melhores noites para observar um alvo ao longo de um ano.
-   **📍 Localização Flexível**: Defina sua localização pelo nome da cidade (ex: "Porto, Portugal") ou coordenadas geográficas.
-   **🎯 Seleção de Alvos Abrangente**: Use listas pré-selecionadas, adicione alvos do sistema solar ou insira manualmente qualquer objeto (ex: "NGC 1300").
-   **🌡️ Considerações Atmosféricas**: Configure a elevação mínima do alvo acima do horizonte para otimizar a qualidade da observação.
-   **🌕 Análise de Impacto da Lua**: Calcule a iluminação lunar e separação angular dos alvos.
-   **☁️ Previsão Meteorológica**: Integração com API Open-Meteo para previsão do tempo.

---

## 📁 Estrutura do Projeto

```
├── README.md                    # Este arquivo
├── LICENSE                      # Licença MIT
├── requirements.txt             # Dependências do projeto
├── app.py                       # Aplicação web Streamlit
├── analise_astronomica.ipynb    # Jupyter Notebook interativo
├── create_notebook.py           # Script para gerar o notebook
├── src/                         # Código-fonte modular
│   ├── config.py               # Configurações centralizadas
│   ├── location.py             # Funções de geolocalização
│   ├── targets.py              # Gerenciamento de alvos
│   ├── analysis.py             # Cálculos astronômicos
│   └── plotting.py             # Visualizações
└── tests/                       # Suite de testes (pytest)
    ├── test_analysis.py
    ├── test_location.py
    └── test_targets.py
```

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação via pip

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/Skyler-Testes.git
   cd Skyler-Testes
   ```

2. **Crie um ambiente virtual** (recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

### Instalação Alternativa (setup.py)

```bash
pip install -e .
```

---

## 💻 Opções de Uso

Você pode escolher a interface que melhor se adapta ao seu fluxo de trabalho.

### Opção 1: Aplicação Web (Streamlit) 🌐

Ideal para uma experiência visual e interativa sem necessidade de programação.

1. **Inicie o servidor**:
   ```bash
   streamlit run app.py
   ```

2. **Acesse no navegador**: A aplicação abrirá automaticamente em `http://localhost:8501`

3. **Use a interface**:
   - Configure sua localização na barra lateral
   - Selecione a data e elevação mínima
   - Escolha entre análise noturna ou calendário anual
   - Visualize os gráficos interativos

### Opção 2: Jupyter Notebook 📓

Ideal para personalização, análise de dados e integração com outros scripts Python.

1. **Inicie o Jupyter**:
   ```bash
   jupyter notebook
   ```

2. **Abra o notebook**: No navegador, abra `analise_astronomica.ipynb`

3. **Siga o guia**: O notebook contém instruções detalhadas em células Markdown

---

## 📖 Tutorial Rápido

### Análise Noturna (Streamlit)

1. **Defina sua Localização**: Digite o nome da sua cidade (ex: `São Paulo, Brazil`) e clique em **Definir Localização**
2. **Ajuste Parâmetros**: Selecione a data e a elevação mínima
3. **Selecione Alvos**: Escolha alvos pré-definidos, sistema solar ou adicione manualmente
4. **Gere a Análise**: Clique em **Gerar Análise da Noite**
5. **Visualize Resultados**: Veja gráficos de altitude vs. tempo para cada alvo

### Calendário Anual (Streamlit)

1. **Configure a Localização** (como acima)
2. **Escolha um Alvo**: Digite o nome (ex: `M31`)
3. **Selecione o Ano**: Use o campo numérico
4. **Gere o Calendário**: Clique em **Gerar Calendário Anual**
5. **Analise o Heatmap**: Cores mais claras indicam melhor visibilidade

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

## 🤝 Como Contribuir

Contribuições são muito bem-vindas! Este é um projeto educacional e comunitário.

1. **Fork o projeto**
2. **Crie um branch** para sua feature (`git checkout -b feature/MinhaFeature`)
3. **Commit suas mudanças** (`git commit -m 'Adiciona MinhaFeature'`)
4. **Push para o branch** (`git push origin feature/MinhaFeature`)
5. **Abra um Pull Request**

Leia o guia completo em [CONTRIBUTING.md](CONTRIBUTING.md) para mais detalhes.

---

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 🌟 Agradecimentos

- [Astropy](https://www.astropy.org/) - Biblioteca fundamental para astronomia em Python
- [Astroplan](https://astroplan.readthedocs.io/) - Planejamento de observações
- [Streamlit](https://streamlit.io/) - Interface web interativa
- Comunidade de astronomia educacional brasileira

---

## 📧 Contato e Suporte

- **Issues**: Reporte bugs ou sugira features através das [GitHub Issues](../../issues)
- **Discussões**: Participe das [GitHub Discussions](../../discussions)

---

## 🎓 Uso Educacional

Este software foi desenvolvido pensando em:
- **Escolas Públicas**: Ferramenta gratuita para ensino de astronomia
- **Graduação**: Material didático para cursos de física e astronomia
- **Pós-Graduação**: Base para pesquisas em planejamento observacional
- **Astrônomos Amadores**: Planejamento de sessões de observação

**Boas observações! 🔭✨**
