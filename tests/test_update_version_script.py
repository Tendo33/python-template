"""Tests for the version update maintenance script."""

from __future__ import annotations

import importlib.util
from pathlib import Path


def _load_update_version_module():
    script_path = Path(__file__).resolve().parents[1] / "scripts" / "update_version.py"
    spec = importlib.util.spec_from_file_location("update_version_script", script_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_update_all_updates_required_and_env_files(tmp_path: Path) -> None:
    """The script should update all available target files."""
    module = _load_update_version_module()
    updater = module.VersionUpdater(tmp_path)

    (tmp_path / "src" / "python_template").mkdir(parents=True)
    (tmp_path / "pyproject.toml").write_text('version = "0.1.0"\n', encoding="utf-8")
    (tmp_path / "src" / "python_template" / "__init__.py").write_text(
        '__version__ = "0.1.0"\n',
        encoding="utf-8",
    )
    (tmp_path / ".env.example").write_text("APP_VERSION=0.1.0\n", encoding="utf-8")

    messages = updater.update_all("0.2.0", dry_run=False)
    assert not any("[ERROR]" in msg for msg in messages)

    assert 'version = "0.2.0"' in (tmp_path / "pyproject.toml").read_text(
        encoding="utf-8"
    )
    assert '__version__ = "0.2.0"' in (
        tmp_path / "src" / "python_template" / "__init__.py"
    ).read_text(encoding="utf-8")
    assert "APP_VERSION=0.2.0" in (tmp_path / ".env.example").read_text(
        encoding="utf-8"
    )


def test_update_all_allows_missing_optional_env_file(tmp_path: Path) -> None:
    """Missing optional .env.example should not cause an error."""
    module = _load_update_version_module()
    updater = module.VersionUpdater(tmp_path)

    (tmp_path / "src" / "python_template").mkdir(parents=True)
    (tmp_path / "pyproject.toml").write_text('version = "0.1.0"\n', encoding="utf-8")
    (tmp_path / "src" / "python_template" / "__init__.py").write_text(
        '__version__ = "0.1.0"\n',
        encoding="utf-8",
    )

    messages = updater.update_all("0.2.0", dry_run=False)
    assert not any("[ERROR]" in msg for msg in messages)
    assert any("Optional file not found" in msg for msg in messages)
