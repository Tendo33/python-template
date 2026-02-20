"""Tests for settings module."""

from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import ValidationError

from python_template.utils.setting import Settings, get_settings, reload_settings


def test_get_settings_uses_singleton_cache() -> None:
    """get_settings should return the same cached instance."""
    get_settings.cache_clear()
    first = get_settings()
    second = get_settings()
    assert first is second


def test_reload_settings_supports_custom_env_file(tmp_path: Path) -> None:
    """reload_settings should rebuild settings from the provided env file."""
    env_file = tmp_path / ".env.test"
    env_file.write_text(
        "APP_NAME=from-env\nLOG_LEVEL=debug\nENVIRONMENT=production\n",
        encoding="utf-8",
    )

    settings = reload_settings(env_file=env_file)
    assert settings.app_name == "from-env"
    assert settings.log_level == "DEBUG"
    assert settings.environment == "production"

    get_settings.cache_clear()


def test_settings_environment_validation() -> None:
    """Settings should reject invalid environment values."""
    with pytest.raises(ValidationError):
        Settings(environment="invalid")
