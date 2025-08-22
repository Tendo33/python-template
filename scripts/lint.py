#!/usr/bin/env python3
"""Code linting script using ruff.

This script provides a convenient way to lint Python code using ruff.
"""

import subprocess
import sys
from pathlib import Path
from typing import List, Optional


def run_command(cmd: List[str], cwd: Optional[Path] = None) -> int:
    """Run a command and return the exit code.

    Args:
        cmd: Command to run as a list of strings
        cwd: Working directory for the command

    Returns:
        Exit code of the command
    """
    try:
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd=cwd, check=False, capture_output=False)
        return result.returncode
    except FileNotFoundError:
        print(f"Error: Command '{cmd[0]}' not found. Please ensure it's installed.")
        return 1


def lint_code(
    paths: Optional[List[str]] = None,
    fix: bool = False,
    show_source: bool = False,
    output_format: str = "text",
    project_root: Optional[Path] = None,
) -> int:
    """Lint Python code using ruff.

    Args:
        paths: List of paths to lint (defaults to src/ and tests/)
        fix: Automatically fix fixable issues
        show_source: Show source code for each error
        output_format: Output format (text, json, github, gitlab, etc.)
        project_root: Root directory of the project

    Returns:
        Exit code (0 for success, non-zero for error)
    """
    if project_root is None:
        project_root = Path(__file__).parent.parent

    if paths is None:
        paths = ["src/", "tests/", "scripts/"]

    # Filter paths to only existing ones
    existing_paths = []
    for path in paths:
        full_path = project_root / path
        if full_path.exists():
            existing_paths.append(str(full_path))

    if not existing_paths:
        print("No valid paths found to lint.")
        return 1

    # Build ruff check command
    cmd = ["ruff", "check"]

    if fix:
        cmd.append("--fix")

    if show_source:
        cmd.append("--show-source")

    if output_format != "text":
        cmd.extend(["--output-format", output_format])

    cmd.extend(existing_paths)

    return run_command(cmd, cwd=project_root)


def check_imports(
    paths: Optional[List[str]] = None, project_root: Optional[Path] = None
) -> int:
    """Check and fix import sorting using ruff.

    Args:
        paths: List of paths to check imports
        project_root: Root directory of the project

    Returns:
        Exit code (0 for success, non-zero for error)
    """
    if project_root is None:
        project_root = Path(__file__).parent.parent

    if paths is None:
        paths = ["src/", "tests/", "scripts/"]

    # Filter paths to only existing ones
    existing_paths = []
    for path in paths:
        full_path = project_root / path
        if full_path.exists():
            existing_paths.append(str(full_path))

    if not existing_paths:
        print("No valid paths found to check imports.")
        return 1

    print("Checking import sorting...")

    # Check import sorting specifically
    cmd = ["ruff", "check", "--select", "I", "--fix"]
    cmd.extend(existing_paths)

    return run_command(cmd, cwd=project_root)


def run_comprehensive_check(
    paths: Optional[List[str]] = None,
    fix: bool = False,
    project_root: Optional[Path] = None,
) -> int:
    """Run comprehensive code quality checks.

    Args:
        paths: List of paths to check
        fix: Automatically fix fixable issues
        project_root: Root directory of the project

    Returns:
        Exit code (0 for success, non-zero for error)
    """
    if project_root is None:
        project_root = Path(__file__).parent.parent

    print("🔍 Running comprehensive code quality checks...\n")

    # Step 1: Check imports
    print("📦 Checking import sorting...")
    import_exit_code = check_imports(paths, project_root)

    # Step 2: Run linting
    print("\n🔎 Running linting checks...")
    lint_exit_code = lint_code(
        paths=paths, fix=fix, show_source=True, project_root=project_root
    )

    # Step 3: Check formatting
    print("\n📝 Checking code formatting...")
    format_cmd = [
        sys.executable,
        str(project_root / "scripts" / "format.py"),
        "--check",
    ]
    if paths:
        format_cmd.extend(paths)

    format_exit_code = run_command(format_cmd, cwd=project_root)

    # Summary
    print("\n" + "=" * 50)
    print("📊 QUALITY CHECK SUMMARY")
    print("=" * 50)

    checks = [
        ("Import sorting", import_exit_code),
        ("Linting", lint_exit_code),
        ("Formatting", format_exit_code),
    ]

    all_passed = True
    for check_name, exit_code in checks:
        status = "✅ PASS" if exit_code == 0 else "❌ FAIL"
        print(f"{check_name:<20} {status}")
        if exit_code != 0:
            all_passed = False

    print("=" * 50)

    if all_passed:
        print("🎉 All quality checks passed!")
        return 0
    else:
        print("⚠️  Some quality checks failed. Please review and fix the issues above.")
        if not fix:
            print("💡 Tip: Use --fix to automatically fix some issues.")
        return 1


def main() -> int:
    """Main entry point for the lint script.

    Returns:
        Exit code
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="Lint Python code using ruff",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/lint.py                     # Lint src/, tests/, scripts/
  python scripts/lint.py --fix              # Lint and auto-fix issues
  python scripts/lint.py --comprehensive    # Run all quality checks
  python scripts/lint.py src/               # Lint only src/ directory
  python scripts/lint.py --format json      # Output in JSON format
  python scripts/lint.py --show-source      # Show source code for errors
        """,
    )

    parser.add_argument(
        "paths", nargs="*", help="Paths to lint (default: src/, tests/, scripts/)"
    )

    parser.add_argument(
        "--fix", action="store_true", help="Automatically fix fixable issues"
    )

    parser.add_argument(
        "--show-source", action="store_true", help="Show source code for each error"
    )

    parser.add_argument(
        "--format",
        choices=["text", "json", "github", "gitlab", "junit"],
        default="text",
        help="Output format (default: text)",
    )

    parser.add_argument(
        "--comprehensive",
        action="store_true",
        help="Run comprehensive quality checks (linting + formatting + imports)",
    )

    parser.add_argument(
        "--imports-only", action="store_true", help="Only check import sorting"
    )

    parser.add_argument(
        "--project-root",
        type=Path,
        help="Root directory of the project (default: parent of script directory)",
    )

    args = parser.parse_args()

    # Determine project root
    project_root = args.project_root
    if project_root is None:
        project_root = Path(__file__).parent.parent

    if not project_root.exists():
        print(f"Error: Project root does not exist: {project_root}")
        return 1

    print(f"Project root: {project_root}")

    # Run the appropriate command
    try:
        if args.comprehensive:
            exit_code = run_comprehensive_check(
                paths=args.paths if args.paths else None,
                fix=args.fix,
                project_root=project_root,
            )
        elif args.imports_only:
            exit_code = check_imports(
                paths=args.paths if args.paths else None, project_root=project_root
            )
        else:
            exit_code = lint_code(
                paths=args.paths if args.paths else None,
                fix=args.fix,
                show_source=args.show_source,
                output_format=args.format,
                project_root=project_root,
            )

        if exit_code == 0:
            print("✅ Linting completed successfully!")
        else:
            print("❌ Linting found issues.")

        return exit_code

    except KeyboardInterrupt:
        print("\n⚠️  Linting interrupted by user.")
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
