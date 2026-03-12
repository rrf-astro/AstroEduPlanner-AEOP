# Contributing to AstroEduPlanner (AEOP)

Thank you for your interest in contributing to **AstroEduPlanner (AEOP)**! This project is aimed at the educational community and contributions of all kinds are warmly welcome.

## 🚀 Getting Started

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/PLACEHOLDER-username/AstroEduPlanner-AEOP.git
   cd AstroEduPlanner-AEOP
   ```
3. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🔧 Development

### Project Structure

- `src/` — Modular source code
  - `config.py` — Centralised configuration and imports
  - `location.py` — Geolocation utilities
  - `targets.py` — Astronomical target management
  - `analysis.py` — Visibility calculations
  - `plotting.py` — Visualisation routines
- `tests/` — Unit tests with pytest
- `app.py` — Streamlit web application
- `analise_astronomica.ipynb` — Jupyter Notebook interface

### Running the Tests

```bash
pytest tests/
```

With coverage report:
```bash
pytest --cov=src tests/
```

### Running the Application

**Streamlit:**
```bash
streamlit run app.py
```

**Jupyter Notebook:**
```bash
jupyter notebook analise_astronomica.ipynb
```

## 📝 Contribution Guidelines

### Types of Contributions

- 🐛 **Bug fixes** — Report or fix bugs via GitHub Issues
- ✨ **New features** — Add useful functionality
- 📚 **Documentation** — Improve README, docstrings, or examples
- 🧪 **Tests** — Increase test coverage
- 🌐 **Translation** — Help internationalise the project

### Contribution Workflow

1. **Open an issue** describing what you intend to do
2. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/my-feature
   ```
3. **Make your changes** following the code style guidelines below
4. **Write or update tests** for your changes
5. **Run the tests** to ensure everything passes
6. **Commit your changes** with descriptive messages:
   ```bash
   git commit -m "Add moon phase calculation to nightly analysis"
   ```
7. **Push to your fork**:
   ```bash
   git push origin feature/my-feature
   ```
8. **Open a Pull Request** with a clear description of your changes

### Code Style

- Follow [PEP 8](https://pep8.org/) for Python code
- Use clear, descriptive variable and function names in English
- Add docstrings to all public functions (NumPy or Google style)
- Keep lines to a maximum of 100 characters
- Use type hints where appropriate

### Commit Messages

Use clear, descriptive commit messages:
- ✅ `Add moon phase calculation to nightly analysis`
- ✅ `Fix altitude plot x-axis formatting for short nights`
- ❌ `Update`
- ❌ `Fix`

## 🧪 Writing Tests

All new features must include tests. Use pytest and follow the existing patterns:

```python
def test_my_function():
    """Test that my_function returns the expected value."""
    result = my_function(parameter)
    assert result == expected_value
```

## 📚 Documentation

Add docstrings to new functions following this style:

```python
def my_function(parameter):
    """
    Brief description of the function.

    Args:
        parameter: Description of the parameter.

    Returns:
        Description of the return value.
    """
```

Update `README.md` if you add significant new features, and include usage examples where relevant.

## 🤝 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to abide by its terms.

## 💡 Questions?

If you have questions about contributing, open an issue or reach out to the project maintainers via GitHub Discussions.

**Thank you for contributing! 🌟**
