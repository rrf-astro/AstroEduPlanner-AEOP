# tests/conftest.py
"""
Pytest configuration and shared fixtures for AstroEduPlanner (AEOP) tests.

Provides:
- A custom 'network' marker for tests that require external services.
- A '--no-network' CLI option to skip network-dependent tests in offline CI.
"""

import pytest


def pytest_addoption(parser):
    """Add --no-network option to pytest CLI."""
    parser.addoption(
        "--no-network",
        action="store_true",
        default=False,
        help="Skip tests that require external network services (Nominatim, SIMBAD).",
    )


def pytest_configure(config):
    """Register the 'network' marker."""
    config.addinivalue_line(
        "markers",
        "network: mark test as requiring external network services (Nominatim, SIMBAD, etc.).",
    )


def pytest_collection_modifyitems(config, items):
    """Automatically skip 'network' tests when --no-network is passed."""
    if config.getoption("--no-network"):
        skip_network = pytest.mark.skip(reason="Skipped: --no-network flag set")
        for item in items:
            if "network" in item.keywords:
                item.add_marker(skip_network)
