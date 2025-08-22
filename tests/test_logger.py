"""Tests for the logger module.

This module contains unit tests for logging functionality using loguru.
"""

import pytest
from loguru import logger

from python_template.logger import (
    configure_json_logging,
    critical,
    debug,
    error,
    exception,
    get_logger,
    info,
    log_function_calls,
    setup_logging,
    warning,
)


class TestLoggerSetup:
    """Test cases for logger setup functionality."""

    def test_setup_logging_default(self, caplog):
        """Test setup_logging with default parameters."""
        setup_logging()

        # Test that we can log messages
        test_logger = get_logger("test")
        test_logger.info("Test message")

        # Verify logger configuration (basic check)
        assert len(logger._core.handlers) > 0

    def test_setup_logging_custom_level(self):
        """Test setup_logging with custom log level."""
        setup_logging(level="DEBUG")

        test_logger = get_logger("test")

        # This is a basic test - in a real scenario, you'd want to capture
        # and verify the actual log output
        test_logger.debug("Debug message")
        test_logger.info("Info message")

    def test_setup_logging_with_file(self, temp_dir):
        """Test setup_logging with file output."""
        log_file = temp_dir / "test.log"

        setup_logging(
            level="INFO", log_file=str(log_file), rotation="1 MB", retention="1 day"
        )

        test_logger = get_logger("test")
        test_logger.info("Test file logging")

        # Verify log file was created
        assert log_file.exists()

        # Verify log content
        log_content = log_file.read_text()
        assert "Test file logging" in log_content

    def test_setup_logging_json_format(self, temp_dir):
        """Test setup_logging with JSON serialization."""
        log_file = temp_dir / "test_json.log"

        setup_logging(level="INFO", log_file=str(log_file), serialize=True)

        test_logger = get_logger("test")
        test_logger.info("JSON test message")

        # Basic verification that file exists
        assert log_file.exists()

    def test_get_logger_with_name(self):
        """Test get_logger with custom name."""
        named_logger = get_logger("custom_name")

        # Test that logger works
        named_logger.info("Named logger test")

        # Basic verification that we get a logger object
        assert named_logger is not None

    def test_get_logger_without_name(self):
        """Test get_logger without name parameter."""
        default_logger = get_logger()

        # Test that logger works
        default_logger.info("Default logger test")

        # Basic verification that we get a logger object
        assert default_logger is not None


class TestJSONLogging:
    """Test cases for JSON logging functionality."""

    def test_configure_json_logging(self, temp_dir):
        """Test JSON logging configuration."""
        log_file = temp_dir / "json_test.log"

        extra_fields = {"service": "test-service", "version": "1.0.0"}

        configure_json_logging(
            level="INFO", log_file=str(log_file), extra_fields=extra_fields
        )

        test_logger = get_logger("json_test")
        test_logger.info("JSON test message")

        # Verify log file exists
        assert log_file.exists()

    def test_configure_json_logging_no_extra_fields(self, temp_dir):
        """Test JSON logging without extra fields."""
        log_file = temp_dir / "json_simple.log"

        configure_json_logging(level="DEBUG", log_file=str(log_file))

        test_logger = get_logger("json_simple")
        test_logger.debug("Simple JSON message")

        assert log_file.exists()


class TestLogDecorator:
    """Test cases for logging decorator."""

    def test_log_function_calls_decorator(self):
        """Test the log_function_calls decorator."""

        @log_function_calls
        def sample_function(x, y, z=10):
            return x + y + z

        # Call the decorated function
        result = sample_function(1, 2, z=3)

        # Verify the function still works correctly
        assert result == 6

    def test_log_function_calls_with_exception(self):
        """Test log_function_calls decorator with exception."""

        @log_function_calls
        def failing_function():
            raise ValueError("Test exception")

        # Verify exception is still raised and logged
        with pytest.raises(ValueError, match="Test exception"):
            failing_function()

    def test_log_function_calls_preserves_metadata(self):
        """Test that decorator preserves function metadata."""

        @log_function_calls
        def documented_function():
            """This function has documentation."""
            return "result"

        # Verify function name and docstring are preserved
        assert documented_function.__name__ == "documented_function"
        assert "documentation" in documented_function.__doc__


class TestConvenienceLoggingFunctions:
    """Test cases for convenience logging functions."""

    def test_debug_function(self):
        """Test debug convenience function."""
        debug("Debug test message")
        # No exception should be raised

    def test_info_function(self):
        """Test info convenience function."""
        info("Info test message")
        # No exception should be raised

    def test_warning_function(self):
        """Test warning convenience function."""
        warning("Warning test message")
        # No exception should be raised

    def test_error_function(self):
        """Test error convenience function."""
        error("Error test message")
        # No exception should be raised

    def test_critical_function(self):
        """Test critical convenience function."""
        critical("Critical test message")
        # No exception should be raised

    def test_exception_function(self):
        """Test exception convenience function."""
        try:
            raise ValueError("Test exception for logging")
        except ValueError:
            exception("Exception occurred")
        # No exception should be raised by the logging call

    def test_convenience_functions_with_kwargs(self):
        """Test convenience functions with keyword arguments."""
        info("Test message with context", user_id=123, action="test")
        debug("Debug with extra data", component="logger", level="test")
        # No exceptions should be raised


class TestLoggerIntegration:
    """Integration tests for logger functionality."""

    def test_multiple_loggers_different_names(self):
        """Test creating multiple loggers with different names."""
        logger1 = get_logger("service1")
        logger2 = get_logger("service2")
        logger3 = get_logger()  # default logger

        # Test that all loggers work
        logger1.info("Service 1 message")
        logger2.info("Service 2 message")
        logger3.info("Default logger message")

        # All should work without exceptions
        assert logger1 is not None
        assert logger2 is not None
        assert logger3 is not None

    def test_logging_with_file_rotation(self, temp_dir):
        """Test logging with file rotation settings."""
        log_file = temp_dir / "rotation_test.log"

        setup_logging(
            level="INFO",
            log_file=str(log_file),
            rotation="100 bytes",  # Very small rotation for testing
            retention="2 files",
        )

        test_logger = get_logger("rotation_test")

        # Write enough logs to potentially trigger rotation
        for i in range(20):
            test_logger.info(f"Log message number {i} with some additional content")

        # Verify main log file exists
        assert log_file.exists()

    @pytest.mark.integration
    def test_complete_logging_workflow(self, temp_dir):
        """Test a complete logging workflow."""
        log_file = temp_dir / "complete_test.log"

        # Setup logging
        setup_logging(
            level="DEBUG",
            log_file=str(log_file),
            rotation="10 MB",
            retention="7 days",
            compression="gz",
        )

        # Create loggers for different components
        app_logger = get_logger("app")
        db_logger = get_logger("database")
        api_logger = get_logger("api")

        # Simulate application activity
        app_logger.info("Application started")

        # Simulate database operations
        db_logger.debug("Connecting to database")
        db_logger.info("Database connection established")

        # Simulate API requests
        api_logger.info("Processing API request", endpoint="/users", method="GET")
        api_logger.warning("Rate limit approaching", requests_remaining=5)

        # Simulate error scenario
        try:
            raise ConnectionError("Database connection lost")
        except ConnectionError:
            db_logger.exception("Database error occurred")

        app_logger.info("Application shutting down")

        # Verify log file exists and has content
        assert log_file.exists()
        assert log_file.stat().st_size > 0

        # Verify log content contains expected messages
        log_content = log_file.read_text()
        assert "Application started" in log_content
        assert "Database connection established" in log_content
        assert "Processing API request" in log_content
