"""Regression tests for public package APIs."""

from __future__ import annotations

import importlib
from pathlib import Path

from python_template import utils


def test_models_module_can_be_imported() -> None:
    """`python_template.models` should always be importable."""
    models_module = importlib.import_module("python_template.models")
    assert hasattr(models_module, "BaseModel")
    assert hasattr(models_module, "User")


def test_utils_exposes_logging_setup() -> None:
    """`setup_logging` is documented and must be exported from utils."""
    assert callable(utils.setup_logging)


def test_utils_get_settings_returns_settings_instance() -> None:
    """`get_settings` should return a configured settings object."""
    settings = utils.get_settings()
    assert settings is not None
    assert settings.app_name


def test_read_text_file_supports_default_value(tmp_path: Path) -> None:
    """Missing text files should return provided default."""
    fallback = "fallback-text"
    result = utils.read_text_file(tmp_path / "missing.txt", default=fallback)
    assert result == fallback


def test_read_json_supports_default_value(tmp_path: Path) -> None:
    """Missing JSON files should return provided default."""
    fallback = {"status": "missing"}
    result = utils.read_json(tmp_path / "missing.json", default=fallback)
    assert result == fallback
