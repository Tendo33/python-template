"""Tests for AI docs sync and validation scripts."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_script_module(script_name: str):
    path = ROOT / "scripts" / f"{script_name}.py"
    spec = importlib.util.spec_from_file_location(script_name, path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_sync_ai_adapters_is_up_to_date() -> None:
    module = load_script_module("sync_ai_adapters")
    issues = module.sync_adapters(ROOT, check=True)
    assert issues == []


def test_check_ai_docs_reports_no_issues() -> None:
    module = load_script_module("check_ai_docs")
    issues = module.collect_issues(ROOT)
    assert issues == []
