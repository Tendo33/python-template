"""Core tests for file utility helpers."""

from pathlib import Path

from python_template.utils.file_utils import (
    ensure_directory,
    read_text_file,
    write_text_file,
)


def test_ensure_directory_creates_nested_path(tmp_path: Path) -> None:
    target = tmp_path / "a" / "b" / "c"
    result = ensure_directory(target)
    assert result == target
    assert target.exists()
    assert target.is_dir()


def test_write_and_read_text_file_roundtrip(tmp_path: Path) -> None:
    target = tmp_path / "notes" / "hello.txt"
    content = "hello template"

    written = write_text_file(content, target)
    loaded = read_text_file(target)

    assert written == len(content)
    assert loaded == content


def test_read_text_file_returns_default_when_missing(tmp_path: Path) -> None:
    fallback = "default-value"
    loaded = read_text_file(tmp_path / "missing.txt", default=fallback)
    assert loaded == fallback


def test_write_text_file_without_parent_creation_returns_none(tmp_path: Path) -> None:
    target = tmp_path / "missing" / "folder" / "out.txt"
    written = write_text_file("x", target, create_dirs=False)
    assert written is None
