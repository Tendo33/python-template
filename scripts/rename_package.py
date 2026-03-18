#!/usr/bin/env python3
"""Package rename script.

Usage:
    python scripts/rename_package.py <new_package_name>
    python scripts/rename_package.py --dry-run <new_package_name>

Example:
    python scripts/rename_package.py my_awesome_project

This script will:
    1. Rename src/python_template/ directory to src/<new_name>/
    2. Update all references in Python, TOML, Markdown, YAML, JSON,
       TypeScript, HTML, CSS, and AI config files (.mdc, .cursorrules)
    3. Update frontend/package.json name field
    4. Update frontend/index.html <title>
"""

import argparse
import io
import json
import re
import shutil
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

OLD_PACKAGE_NAME = "python_template"
OLD_PROJECT_NAME = "python-template"

SCAN_EXTENSIONS: set[str] = {
    # Python / backend
    ".py",
    ".toml",
    ".cfg",
    ".ini",
    # Documentation
    ".md",
    ".rst",
    ".txt",
    # Frontend
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".json",
    ".css",
    ".html",
    # Config / CI
    ".yaml",
    ".yml",
    ".mdc",
}

SCAN_EXACT_NAMES: set[str] = {
    "Makefile",
    "Dockerfile",
    ".gitignore",
    ".env.example",
    ".cursorrules",
    "components.json",
}

EXCLUDE_DIRS: set[str] = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".ruff_cache",
    ".pytest_cache",
    ".mypy_cache",
    "node_modules",
    "dist",
    "build",
    ".history",
    "logs",
    "htmlcov",
    ".tox",
    ".nox",
    "pnpm-lock.yaml",
}


def get_project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def validate_package_name(name: str) -> bool:
    """Return True if *name* is a valid Python package identifier."""
    import keyword

    if not name or not name.isidentifier():
        return False
    return not keyword.iskeyword(name)


def to_project_name(package_name: str) -> str:
    """Convert underscore package name to hyphenated project name."""
    return package_name.replace("_", "-")


def collect_files(root: Path) -> list[Path]:
    """Collect all text files that may contain package-name references."""
    files: list[Path] = []
    for item in root.rglob("*"):
        if any(part in EXCLUDE_DIRS for part in item.parts):
            continue
        if not item.is_file():
            continue
        if item.suffix in SCAN_EXTENSIONS or item.name in SCAN_EXACT_NAMES:
            files.append(item)
    return sorted(files)


def replace_in_content(
    content: str,
    old_package: str,
    new_package: str,
    old_project: str,
    new_project: str,
) -> str:
    """Replace package name and project name throughout *content*."""
    content = content.replace(old_package, new_package)
    content = content.replace(old_project, new_project)
    return content


def update_file(
    path: Path,
    old_package: str,
    new_package: str,
    old_project: str,
    new_project: str,
) -> bool:
    """Update a single file in-place. Return True if content changed."""
    try:
        original = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False
    except Exception:
        return False

    updated = replace_in_content(
        original, old_package, new_package, old_project, new_project
    )
    if updated == original:
        return False

    path.write_text(updated, encoding="utf-8")
    return True


def update_frontend_package_json(
    root: Path,
    new_project: str,
    *,
    dry_run: bool,
) -> bool:
    """Set the frontend package.json ``name`` field to *new_project*."""
    pkg_path = root / "frontend" / "package.json"
    if not pkg_path.exists():
        return False
    try:
        data = json.loads(pkg_path.read_text(encoding="utf-8"))
    except Exception:
        return False

    old_name = data.get("name", "")
    if old_name == new_project:
        return False

    data["name"] = new_project
    if not dry_run:
        pkg_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    return True


def update_frontend_html_title(
    root: Path,
    new_title: str,
    old_title_pattern: str,
    *,
    dry_run: bool,
) -> bool:
    """Replace <title>...</title> in frontend/index.html."""
    html_path = root / "frontend" / "index.html"
    if not html_path.exists():
        return False
    content = html_path.read_text(encoding="utf-8")
    new_content = re.sub(
        rf"<title>{re.escape(old_title_pattern)}</title>",
        f"<title>{new_title}</title>",
        content,
    )
    if new_content == content:
        new_content = re.sub(
            r"<title>[^<]*</title>",
            f"<title>{new_title}</title>",
            content,
        )
    if new_content == content:
        return False
    if not dry_run:
        html_path.write_text(new_content, encoding="utf-8")
    return True


def rename_src_directory(root: Path, new_package: str) -> bool:
    """Rename src/<OLD>/ to src/<new_package>/."""
    old_dir = root / "src" / OLD_PACKAGE_NAME
    new_dir = root / "src" / new_package
    if not old_dir.exists():
        print(f"  [ERROR] Source directory does not exist: {old_dir}")
        return False
    if new_dir.exists():
        print(f"  [ERROR] Target directory already exists: {new_dir}")
        return False
    shutil.move(str(old_dir), str(new_dir))
    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rename package across the entire project (backend + frontend + AI configs)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Examples:
    python scripts/rename_package.py my_new_package
    python scripts/rename_package.py --dry-run my_new_package
""",
    )
    parser.add_argument(
        "new_package_name",
        help="New package name (snake_case, e.g. my_awesome_project)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing anything",
    )
    parser.add_argument(
        "-y",
        "--yes",
        action="store_true",
        help="Skip interactive confirmation",
    )
    args = parser.parse_args()

    new_package = args.new_package_name
    new_project = to_project_name(new_package)
    dry_run: bool = args.dry_run
    root = get_project_root()

    if not validate_package_name(new_package):
        print(f"[ERROR] Invalid package name: '{new_package}'")
        print("  Must start with a letter/underscore, contain only [a-zA-Z0-9_],")
        print("  and not be a Python keyword.")
        sys.exit(1)

    old_dir = root / "src" / OLD_PACKAGE_NAME
    if not old_dir.exists():
        print(f"[ERROR] Package directory not found: {old_dir}")
        print("  The package may have been renamed already.")
        sys.exit(1)

    # --- Scan ---
    print(f"\n{'=' * 62}")
    print("  Package Rename Tool")
    print(f"{'=' * 62}")
    print(f"  Root:        {root}")
    print(f"  Package:     {OLD_PACKAGE_NAME} -> {new_package}")
    print(f"  Project:     {OLD_PROJECT_NAME} -> {new_project}")
    if dry_run:
        print("  Mode:        DRY RUN (no files will be modified)")
    print(f"{'=' * 62}\n")

    all_files = collect_files(root)
    files_with_hits: list[Path] = []
    for fp in all_files:
        try:
            text = fp.read_text(encoding="utf-8")
        except Exception:
            continue
        if OLD_PACKAGE_NAME in text or OLD_PROJECT_NAME in text:
            files_with_hits.append(fp)

    print(f"[1/4] Directory rename:  src/{OLD_PACKAGE_NAME}/ -> src/{new_package}/")
    print(f"[2/4] Text replacement:  {len(files_with_hits)} files")
    for fp in files_with_hits:
        print(f"       {fp.relative_to(root)}")

    fe_pkg = root / "frontend" / "package.json"
    fe_html = root / "frontend" / "index.html"
    print(
        f"[3/4] Frontend name:     {'frontend/package.json' if fe_pkg.exists() else '(not found)'}"
    )
    print(
        f"[4/4] Frontend title:    {'frontend/index.html' if fe_html.exists() else '(not found)'}"
    )
    print()

    if dry_run:
        print("[DRY RUN] No changes made. Re-run without --dry-run to apply.")
        sys.exit(0)

    if not args.yes:
        answer = input("Proceed? (y/N): ").strip().lower()
        if answer != "y":
            print("Aborted.")
            sys.exit(0)

    # --- Execute ---
    print()
    updated = 0
    for fp in files_with_hits:
        if update_file(
            fp, OLD_PACKAGE_NAME, new_package, OLD_PROJECT_NAME, new_project
        ):
            updated += 1
            print(f"  [OK] {fp.relative_to(root)}")

    if update_frontend_package_json(root, new_project, dry_run=False):
        updated += 1
        print("  [OK] frontend/package.json  (name field)")

    title_stem = new_project.replace("-", " ").title()
    if update_frontend_html_title(root, title_stem, "Python Template", dry_run=False):
        updated += 1
        print("  [OK] frontend/index.html  (<title>)")

    print()
    if not rename_src_directory(root, new_package):
        print("[ERROR] Directory rename failed. Check manually.")
        sys.exit(1)
    print(f"  [OK] src/{OLD_PACKAGE_NAME}/ -> src/{new_package}/")

    print(f"\n{'=' * 62}")
    print(f"  Done — {updated} files updated, directory renamed")
    print(f"{'=' * 62}")
    print()
    print("Next steps:")
    print("  1. Review changes:      git diff")
    print("  2. Reinstall package:   uv pip install -e .")
    print("  3. Run tests:           uv run pytest")
    print(
        "  4. Commit:              git add -A && git commit -m 'chore: rename package'"
    )
    print()


if __name__ == "__main__":
    main()
