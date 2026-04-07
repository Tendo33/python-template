"""Tests for AI docs sync and validation scripts."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MINIMAL_REQUIRED_DOCS = [
    "ai_adapter_config.json",
    "ai_docs/START_HERE.md",
    "ai_docs/INDEX.md",
    "ai_docs/reference/verification.md",
    "ai_docs/reference/tool-entrypoints.md",
    "ai_docs/workflows/start-task.md",
]


def load_script_module(script_name: str):
    path = ROOT / "scripts" / f"{script_name}.py"
    spec = importlib.util.spec_from_file_location(script_name, path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_file(root: Path, relative_path: str, content: str = "") -> None:
    path = root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_minimal_ai_docs(root: Path) -> None:
    for relative_path in MINIMAL_REQUIRED_DOCS:
        if relative_path.endswith(".json"):
            write_file(
                root,
                relative_path,
                json.dumps({"enabled_adapter_sets": []}, indent=2) + "\n",
            )
            continue
        write_file(root, relative_path, "# placeholder\n")


def test_sync_ai_adapters_is_up_to_date() -> None:
    module = load_script_module("sync_ai_adapters")
    issues = module.sync_adapters(ROOT, check=True)
    assert issues == []


def test_check_ai_docs_reports_no_issues() -> None:
    module = load_script_module("check_ai_docs")
    issues = module.collect_issues(ROOT)
    assert issues == []


def test_check_ai_docs_respects_enabled_adapter_sets(tmp_path: Path) -> None:
    sync_module = load_script_module("sync_ai_adapters")
    check_module = load_script_module("check_ai_docs")

    write_minimal_ai_docs(tmp_path)
    write_file(
        tmp_path,
        "ai_adapter_config.json",
        json.dumps({"enabled_adapter_sets": []}, indent=2) + "\n",
    )
    check_module.REQUIRED_DOCS = MINIMAL_REQUIRED_DOCS

    assert sync_module.list_expected_adapter_files(tmp_path) == []
    assert check_module.collect_issues(tmp_path) == []


def test_check_ai_docs_reports_stale_generated_files(tmp_path: Path) -> None:
    sync_module = load_script_module("sync_ai_adapters")
    check_module = load_script_module("check_ai_docs")

    write_minimal_ai_docs(tmp_path)
    write_file(
        tmp_path,
        "ai_adapter_config.json",
        json.dumps({"enabled_adapter_sets": []}, indent=2) + "\n",
    )
    write_file(
        tmp_path,
        ".agents/rules/project-development.md",
        f"{sync_module.GENERATED_MARKER}\n",
    )
    check_module.REQUIRED_DOCS = MINIMAL_REQUIRED_DOCS

    issues = check_module.collect_issues(tmp_path)
    assert any(
        "Stale generated adapter should be removed or pruned" in issue
        for issue in issues
    )


def test_prune_stale_generated_files(tmp_path: Path) -> None:
    sync_module = load_script_module("sync_ai_adapters")

    write_file(
        tmp_path,
        "ai_adapter_config.json",
        json.dumps({"enabled_adapter_sets": []}, indent=2) + "\n",
    )
    write_file(
        tmp_path,
        ".agents/rules/project-development.md",
        f"{sync_module.GENERATED_MARKER}\n",
    )

    removed = sync_module.prune_stale_generated_files(tmp_path)

    assert removed == [".agents/rules/project-development.md"]
    assert not (tmp_path / ".agents").exists()
