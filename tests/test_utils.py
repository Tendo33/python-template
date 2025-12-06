"""Tests for utility modules."""

import pytest
from pathlib import Path
from python_template.utils.file_utils import (
    read_text_file,
    write_text_file,
    ensure_directory,
    get_file_size,
    format_file_size
)
from python_template.utils.date_utils import (
    get_current_date,
    get_current_time,
    get_timestamp
)


class TestFileUtils:
    """Test cases for file utilities."""

    def test_write_and_read_text_file(self, temp_dir):
        """Test writing to and reading from a text file."""
        test_file = temp_dir / "test.txt"
        content = "Hello, World!"
        
        # Test write
        assert write_text_file(content, str(test_file))
        assert test_file.exists()
        
        # Test read
        read_content = read_text_file(str(test_file))
        assert read_content == content

    def test_ensure_directory(self, temp_dir):
        """Test directory creation."""
        new_dir = temp_dir / "subdir"
        result = ensure_directory(str(new_dir))
        assert result is not None
        assert new_dir.exists()
        assert new_dir.is_dir()

    def test_file_size(self, temp_dir):
        """Test file size functions."""
        test_file = temp_dir / "size_test.txt"
        content = "12345"  # 5 bytes
        write_text_file(content, str(test_file))
        
        size = get_file_size(str(test_file))
        assert size == 5
        
        formatted = format_file_size(size)
        assert formatted == "5.0 B"


class TestDateUtils:
    """Test cases for date utilities."""

    def test_get_current_date(self):
        """Test getting current date."""
        date_str = get_current_date()
        assert isinstance(date_str, str)
        assert len(date_str) > 0

    def test_get_current_time(self):
        """Test getting current time."""
        time_str = get_current_time()
        assert isinstance(time_str, str)
        assert len(time_str) > 0

    def test_get_timestamp(self):
        """Test getting timestamp."""
        ts = get_timestamp()
        assert isinstance(ts, str)
        assert "T" in ts  # ISO format
