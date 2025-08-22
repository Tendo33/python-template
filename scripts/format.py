#!/usr/bin/env python3
"""Code formatting script using ruff.

This script provides a convenient way to format Python code using ruff.
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
        result = subprocess.run(
            cmd,
            cwd=cwd,
            check=False,
            capture_output=False
        )
        return result.returncode
    except FileNotFoundError:
        print(f"Error: Command '{cmd[0]}' not found. Please ensure it's installed.")
        return 1


def format_code(
    paths: Optional[List[str]] = None,
    check_only: bool = False,
    diff: bool = False,
    project_root: Optional[Path] = None
) -> int:
    """Format Python code using ruff.
    
    Args:
        paths: List of paths to format (defaults to src/ and tests/)
        check_only: Only check formatting, don't modify files
        diff: Show diff of changes that would be made
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
        print("No valid paths found to format.")
        return 1
    
    # Build ruff format command
    cmd = ["ruff", "format"]
    
    if check_only:
        cmd.append("--check")
    
    if diff:
        cmd.append("--diff")
    
    cmd.extend(existing_paths)
    
    return run_command(cmd, cwd=project_root)


def main() -> int:
    """Main entry point for the format script.
    
    Returns:
        Exit code
    """
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Format Python code using ruff",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/format.py                    # Format src/, tests/, scripts/
  python scripts/format.py --check           # Check formatting without changes
  python scripts/format.py --diff            # Show formatting changes
  python scripts/format.py src/              # Format only src/ directory
  python scripts/format.py src/ tests/       # Format specific directories
        """
    )
    
    parser.add_argument(
        "paths",
        nargs="*",
        help="Paths to format (default: src/, tests/, scripts/)"
    )
    
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check formatting without making changes"
    )
    
    parser.add_argument(
        "--diff",
        action="store_true",
        help="Show diff of changes that would be made"
    )
    
    parser.add_argument(
        "--project-root",
        type=Path,
        help="Root directory of the project (default: parent of script directory)"
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
    
    # Run formatting
    try:
        exit_code = format_code(
            paths=args.paths if args.paths else None,
            check_only=args.check,
            diff=args.diff,
            project_root=project_root
        )
        
        if exit_code == 0:
            if args.check:
                print("✅ All files are properly formatted!")
            else:
                print("✅ Code formatting completed successfully!")
        else:
            if args.check:
                print("❌ Some files need formatting. Run without --check to fix them.")
            else:
                print("❌ Code formatting failed.")
        
        return exit_code
        
    except KeyboardInterrupt:
        print("\n⚠️  Formatting interrupted by user.")
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
