"""Regression tests for the stable public package API."""

from __future__ import annotations

import importlib

import pytest

from python_template import utils


def test_utils_wildcard_exports_core_symbols() -> None:
    expected = {
        "get_logger",
        "setup_logging",
        "configure_json_logging",
        "Settings",
        "get_settings",
        "reload_settings",
        "ensure_directory",
        "read_text_file",
        "write_text_file",
        "read_json",
        "write_json",
        "safe_json_loads",
        "safe_json_dumps",
        "get_timestamp",
        "parse_timestamp",
        "format_datetime",
        "parse_datetime",
        "get_current_date",
        "get_current_time",
    }
    assert set(utils.__all__) == expected


def test_utils_exposes_stable_core_functions() -> None:
    assert callable(utils.setup_logging)
    assert callable(utils.read_json)
    assert callable(utils.read_text_file)


def test_legacy_module_paths_raise_import_error() -> None:
    legacy_modules = [
        "python_template.utils.setting",
        "python_template.utils.context",
        "python_template.utils.protocols",
        "python_template.utils.logger_util",
    ]

    for module_name in legacy_modules:
        with pytest.raises(ModuleNotFoundError):
            importlib.import_module(module_name)
