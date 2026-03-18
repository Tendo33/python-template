#!/usr/bin/env python3
"""Version update script.

Updates the version number in all relevant project files:
  - pyproject.toml
  - src/<package>/__init__.py  (auto-detected)
  - frontend/package.json      (if present)

Usage:
    python scripts/update_version.py <new_version>
    python scripts/update_version.py <new_version> --dry-run

Examples:
    python scripts/update_version.py 0.3.0
    python scripts/update_version.py 1.0.0 --dry-run
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class VersionTarget:
    """Describes a file + regex pair where the version lives."""

    path: Path
    pattern: str
    template: str
    optional: bool = False


@dataclass
class UpdateResult:
    status: str  # OK | SKIP | ERROR
    message: str
    old_version: str = ""


def project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def detect_package_dir(root: Path) -> Path | None:
    """Find the single package directory under src/."""
    src = root / "src"
    if not src.is_dir():
        return None
    candidates = [
        d
        for d in src.iterdir()
        if d.is_dir()
        and not d.name.startswith((".", "_"))
        and (d / "__init__.py").exists()
    ]
    if len(candidates) == 1:
        return candidates[0]
    return None


def validate_semver(version: str) -> bool:
    return bool(re.fullmatch(r"\d+\.\d+\.\d+", version))


def read_current_version(root: Path) -> str:
    content = (root / "pyproject.toml").read_text(encoding="utf-8")
    m = re.search(r'^version\s*=\s*"([^"]+)"', content, re.MULTILINE)
    if not m:
        raise ValueError("Cannot find version in pyproject.toml")
    return m.group(1)


def build_targets(root: Path) -> list[VersionTarget]:
    """Build the list of files to update, auto-detecting the package dir."""
    targets: list[VersionTarget] = [
        VersionTarget(
            path=root / "pyproject.toml",
            pattern=r'^version\s*=\s*"[^"]+"',
            template='version = "{v}"',
        ),
    ]

    pkg_dir = detect_package_dir(root)
    if pkg_dir:
        init_py = pkg_dir / "__init__.py"
        targets.append(
            VersionTarget(
                path=init_py,
                pattern=r'^__version__\s*=\s*"[^"]+"',
                template='__version__ = "{v}"',
            )
        )
    else:
        fallback = root / "src" / "python_template" / "__init__.py"
        targets.append(
            VersionTarget(
                path=fallback,
                pattern=r'^__version__\s*=\s*"[^"]+"',
                template='__version__ = "{v}"',
                optional=True,
            )
        )

    targets.append(
        VersionTarget(
            path=root / "frontend" / "package.json",
            pattern="__json_version__",
            template="{v}",
            optional=True,
        )
    )
    return targets


def update_text_target(target: VersionTarget, new_version: str) -> UpdateResult:
    """Apply a regex-based version replacement."""
    if not target.path.exists():
        label = "skipped (not found)" if target.optional else "MISSING"
        status = "SKIP" if target.optional else "ERROR"
        return UpdateResult(status, f"{label}: {target.path.name}")

    content = target.path.read_text(encoding="utf-8")
    m = re.search(target.pattern, content, re.MULTILINE)
    if not m:
        if target.optional:
            return UpdateResult("SKIP", f"pattern not found in {target.path.name}")
        return UpdateResult("ERROR", f"pattern not found in {target.path.name}")

    old_line = m.group(0)
    old_ver_m = re.search(r'"([^"]+)"', old_line)
    old_ver = old_ver_m.group(1) if old_ver_m else "?"

    new_line = target.template.format(v=new_version)
    updated = content[: m.start()] + new_line + content[m.end() :]

    if updated == content:
        return UpdateResult(
            "SKIP", f"already {new_version} in {target.path.name}", old_ver
        )

    target.path.write_text(updated, encoding="utf-8")
    return UpdateResult(
        "OK", f"{target.path.name}: {old_ver} -> {new_version}", old_ver
    )


def update_json_version(path: Path, new_version: str) -> UpdateResult:
    """Update the ``version`` field in a JSON file."""
    if not path.exists():
        return UpdateResult("SKIP", "frontend/package.json not found")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return UpdateResult("ERROR", f"JSON parse error: {exc}")

    old_ver = data.get("version", "?")
    if old_ver == new_version:
        return UpdateResult("SKIP", f"already {new_version} in {path.name}", old_ver)

    data["version"] = new_version
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return UpdateResult("OK", f"{path.name}: {old_ver} -> {new_version}", old_ver)


def run(new_version: str, *, dry_run: bool) -> int:
    root = project_root()
    current = read_current_version(root)

    print(f"\n{'=' * 55}")
    print("  Version Update")
    print(f"{'=' * 55}")
    print(f"  Current:  {current}")
    print(f"  Target:   {new_version}")
    if dry_run:
        print("  Mode:     DRY RUN")
    print(f"{'=' * 55}\n")

    targets = build_targets(root)
    has_error = False

    for target in targets:
        is_json = target.pattern == "__json_version__"

        if dry_run:
            label = target.path.name
            if not target.path.exists():
                if target.optional:
                    print(f"  [SKIP]    {label}  (not found)")
                else:
                    print(f"  [ERROR]   {label}  (MISSING)")
                    has_error = True
            else:
                print(f"  [DRY RUN] {label}  would update -> {new_version}")
            continue

        if is_json:
            result = update_json_version(target.path, new_version)
        else:
            result = update_text_target(target, new_version)

        tag = f"[{result.status}]".ljust(10)
        print(f"  {tag} {result.message}")
        if result.status == "ERROR":
            has_error = True

    print()
    if dry_run:
        print("[DRY RUN] No files modified. Re-run without --dry-run to apply.")
    elif has_error:
        print("[WARNING] Completed with errors — review output above.")
    else:
        print("[SUCCESS] Version updated to", new_version)
    print()
    return 1 if has_error else 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Update version in pyproject.toml, __init__.py, and frontend/package.json",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Examples:
    %(prog)s 0.3.0
    %(prog)s 1.0.0 --dry-run
""",
    )
    parser.add_argument("version", help="New version (MAJOR.MINOR.PATCH)")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    if not validate_semver(args.version):
        print(f"[ERROR] Invalid version: '{args.version}'  (expected X.Y.Z)")
        sys.exit(1)

    sys.exit(run(args.version, dry_run=args.dry_run))


if __name__ == "__main__":
    main()
