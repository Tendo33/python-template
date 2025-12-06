"""Pytest configuration and fixtures."""

import shutil
from pathlib import Path

import pytest


@pytest.fixture
def temp_dir(tmp_path):
    """Create a temporary directory for testing."""
    return tmp_path


@pytest.fixture(autouse=True)
def cleanup_logs(temp_dir):
    """Cleanup log files after tests."""
    yield
    # Cleanup logic if needed, though tmp_path is auto-cleaned by pytest
