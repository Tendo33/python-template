"""Pytest configuration and fixtures.

This module contains shared fixtures and configuration for all tests.
"""

import tempfile
from pathlib import Path
from typing import Any, Dict

import pytest

from python_template.config import ConfigManager
from python_template.core import TemplateCore
from python_template.logger import setup_logging


@pytest.fixture(scope="session", autouse=True)
def setup_test_logging():
    """Setup logging for tests."""
    setup_logging(
        level="DEBUG",
        format_string=(
            "<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | "
            "<cyan>{name}:{function}:{line}</cyan> | <level>{message}</level>"
        ),
    )


@pytest.fixture
def temp_dir():
    """Create a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)


@pytest.fixture
def sample_config() -> Dict[str, Any]:
    """Provide sample configuration for tests."""
    return {
        "app": {
            "name": "test-app",
            "version": "0.1.0",
            "debug": True,
        },
        "logging": {
            "level": "DEBUG",
            "format": "test",
        },
        "performance": {
            "timeout": 5,
            "max_retries": 1,
            "buffer_size": 512,
        },
    }


@pytest.fixture
def config_manager(sample_config) -> ConfigManager:
    """Create a ConfigManager instance with test configuration."""
    config = ConfigManager()
    config.update(sample_config)
    return config


@pytest.fixture
def template_core() -> TemplateCore:
    """Create a TemplateCore instance for testing."""
    return TemplateCore(
        "test-core",
        {
            "debug": True,
            "timeout": 5,
            "max_retries": 1,
            "buffer_size": 512,
        },
    )


@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {
        "strings": ["hello", "world", "python", "testing"],
        "numbers": [1, 2, 3, 4, 5],
        "mixed": ["test", 42, 3.14, True, None],
        "empty": [],
        "nested": {"level1": {"level2": {"value": "nested_value"}}},
    }


@pytest.fixture
def json_file(temp_dir):
    """Create a temporary JSON file for testing."""
    import json

    test_data = {
        "app": {
            "name": "json-test",
            "debug": False,
        },
        "test_value": 42,
    }

    json_file = temp_dir / "test_config.json"
    with open(json_file, "w") as f:
        json.dump(test_data, f)

    return json_file


@pytest.fixture
def test_files(temp_dir):
    """Create test files for file operations."""
    files = {}

    # 创建文本文件
    text_file = temp_dir / "test.txt"
    text_file.write_text("Hello, World!\nThis is a test file.\n")
    files["text"] = text_file

    # 创建二进制文件
    binary_file = temp_dir / "test.bin"
    binary_file.write_bytes(b"\x00\x01\x02\x03\x04\x05")
    files["binary"] = binary_file

    # 创建大文件
    large_file = temp_dir / "large.txt"
    large_content = "A" * 10000  # 10KB 文件
    large_file.write_text(large_content)
    files["large"] = large_file

    return files


@pytest.fixture
def mock_env_vars(monkeypatch):
    """Mock environment variables for testing."""
    env_vars = {
        "PYTHON_TEMPLATE_APP_DEBUG": "true",
        "PYTHON_TEMPLATE_APP_NAME": "env-test",
        "PYTHON_TEMPLATE_LOGGING_LEVEL": "WARNING",
        "PYTHON_TEMPLATE_PERFORMANCE_TIMEOUT": "15",
    }

    for key, value in env_vars.items():
        monkeypatch.setenv(key, value)

    return env_vars


# Pytest 插件钩子


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line("markers", "integration: marks tests as integration tests")
    config.addinivalue_line("markers", "unit: marks tests as unit tests")


def pytest_collection_modifyitems(config, items):
    """Modify test items during collection."""
    # 自动为慢测试添加标记
    for item in items:
        if "slow" in item.nodeid:
            item.add_marker(pytest.mark.slow)

        # 根据测试名称自动添加单元测试标记
        if "test_unit" in item.name or item.fspath.basename.startswith("test_unit"):
            item.add_marker(pytest.mark.unit)

        # 根据测试名称自动添加集成测试标记
        if "test_integration" in item.name or item.fspath.basename.startswith(
            "test_integration"
        ):
            item.add_marker(pytest.mark.integration)


@pytest.fixture(scope="session")
def test_session_data():
    """Session-scoped test data."""
    return {
        "session_id": "test-session-123",
        "start_time": "2025-08-22T17:05:30+08:00",
        "test_environment": "pytest",
    }
