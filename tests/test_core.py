"""Tests for the core module.

This module contains unit tests for the TemplateCore class and related functionality.
"""

import pytest

from python_template.core import TemplateCore


class TestTemplateCore:
    """Test cases for TemplateCore class."""

    def test_initialization(self):
        """Test TemplateCore initialization."""
        core = TemplateCore("test-core")

        assert core.name == "test-core"
        assert core.is_initialized is True
        assert isinstance(core.config, dict)
        assert core.config["debug"] is False  # default value

    def test_initialization_with_config(self):
        """Test TemplateCore initialization with custom config."""
        config = {"debug": True, "timeout": 60, "custom_setting": "test_value"}

        core = TemplateCore("test-core", config)

        assert core.config["debug"] is True
        assert core.config["timeout"] == 60
        assert core.config["custom_setting"] == "test_value"
        assert core.config["max_retries"] == 3  # default value

    def test_invalid_config_types(self):
        """Test that invalid config types raise ValueError."""
        invalid_configs = [
            {"debug": "true"},  # should be bool
            {"timeout": "30"},  # should be number
            {"max_retries": -1},  # should be non-negative
        ]

        for config in invalid_configs:
            with pytest.raises(ValueError):
                TemplateCore("test-core", config)

    def test_status_property(self):
        """Test the status property."""
        core = TemplateCore("test-core", {"debug": True})
        status = core.status

        assert isinstance(status, dict)
        assert status["name"] == "test-core"
        assert status["initialized"] is True
        assert isinstance(status["config"], dict)
        assert isinstance(status["data_keys"], list)

    def test_data_operations(self):
        """Test data setting, getting, and removing operations."""
        core = TemplateCore("test-core")

        # Test setting data
        core.set_data("key1", "value1")
        core.set_data("key2", 42)
        core.set_data("key3", [1, 2, 3])

        # Test getting data
        assert core.get_data("key1") == "value1"
        assert core.get_data("key2") == 42
        assert core.get_data("key3") == [1, 2, 3]
        assert core.get_data("nonexistent") is None
        assert core.get_data("nonexistent", "default") == "default"

        # Test removing data
        assert core.remove_data("key1") is True
        assert core.get_data("key1") is None
        assert core.remove_data("nonexistent") is False

    def test_clear_data(self):
        """Test clearing all data."""
        core = TemplateCore("test-core")

        # Add some data
        core.set_data("key1", "value1")
        core.set_data("key2", "value2")

        # Verify data exists
        assert len(core.status["data_keys"]) == 2

        # Clear data
        core.clear_data()

        # Verify data is cleared
        assert len(core.status["data_keys"]) == 0
        assert core.get_data("key1") is None

    def test_operations_before_initialization(self):
        """Test that operations fail before initialization."""
        # Create a core instance but simulate non-initialization
        core = TemplateCore("test-core")
        core._initialized = False

        with pytest.raises(RuntimeError, match="not initialized"):
            core.set_data("key", "value")

        with pytest.raises(RuntimeError, match="not initialized"):
            core.get_data("key")

        with pytest.raises(RuntimeError, match="not initialized"):
            core.remove_data("key")

        with pytest.raises(RuntimeError, match="not initialized"):
            core.clear_data()

    def test_process_items_strings(self):
        """Test processing string items."""
        core = TemplateCore("test-core")

        items = ["  hello  ", "WORLD", "python"]
        processed = core.process_items(items)

        expected = ["HELLO", "WORLD", "PYTHON"]
        assert processed == expected

    def test_process_items_numbers(self):
        """Test processing numeric items."""
        core = TemplateCore("test-core")

        items = [1, 2.5, 10]
        processed = core.process_items(items)

        expected = [2, 5.0, 20]
        assert processed == expected

    def test_process_items_mixed(self):
        """Test processing mixed type items."""
        core = TemplateCore("test-core")

        items = ["hello", 42, 3.14, None, [1, 2, 3]]
        processed = core.process_items(items)

        expected = ["HELLO", 84, 6.28, "None", "[1, 2, 3]"]
        assert processed == expected

    def test_process_items_invalid_input(self):
        """Test process_items with invalid input."""
        core = TemplateCore("test-core")

        with pytest.raises(TypeError, match="Items must be a list"):
            core.process_items("not a list")

    def test_process_items_debug_mode(self):
        """Test process_items in debug mode with errors."""
        core = TemplateCore("test-core", {"debug": True})

        # Mock an item that will cause an error during processing
        class ErrorItem:
            def __str__(self):
                raise ValueError("Test error")

        items = ["good", ErrorItem()]

        # In debug mode, errors should be raised
        with pytest.raises(ValueError, match="Test error"):
            core.process_items(items)

    def test_process_items_non_debug_mode(self):
        """Test process_items in non-debug mode with errors."""
        core = TemplateCore("test-core", {"debug": False})

        # Mock an item that will cause an error during processing
        class ErrorItem:
            def __str__(self):
                raise ValueError("Test error")

        items = ["good", ErrorItem(), "also_good"]
        processed = core.process_items(items)

        # In non-debug mode, error items should be skipped
        expected = ["GOOD", "ALSO_GOOD"]
        assert processed == expected

    def test_batch_operation_sum(self):
        """Test batch sum operation."""
        core = TemplateCore("test-core")

        data = [1, 2, 3, 4, 5]
        result = core.batch_operation("sum", data)

        assert result["operation"] == "sum"
        assert result["result"] == 15
        assert result["total_items"] == 5
        assert result["batches_processed"] >= 1
        assert result["errors"] == []

    def test_batch_operation_count(self):
        """Test batch count operation."""
        core = TemplateCore("test-core")

        data = ["a", "b", "c"]
        result = core.batch_operation("count", data)

        assert result["operation"] == "count"
        assert result["result"] == 3
        assert result["total_items"] == 3
        assert result["batches_processed"] == 1

    def test_batch_operation_validate(self):
        """Test batch validate operation."""
        core = TemplateCore("test-core")

        data = [1, None, "test", None, 42]
        result = core.batch_operation("validate", data)

        assert result["operation"] == "validate"
        assert result["result"]["valid_items"] == 3
        assert result["result"]["invalid_items"] == 2
        assert result["result"]["validity_ratio"] == 0.6

    def test_batch_operation_invalid_operation(self):
        """Test batch operation with invalid operation type."""
        core = TemplateCore("test-core")

        with pytest.raises(ValueError, match="Invalid operation"):
            core.batch_operation("invalid_op", [1, 2, 3])

    def test_batch_operation_custom_batch_size(self):
        """Test batch operation with custom batch size."""
        core = TemplateCore("test-core")

        data = list(range(100))
        result = core.batch_operation("sum", data, batch_size=10)

        assert result["batch_size"] == 10
        assert result["batches_processed"] == 10
        assert result["result"] == sum(data)

    def test_batch_operation_before_initialization(self):
        """Test batch operation before initialization."""
        core = TemplateCore("test-core")
        core._initialized = False

        with pytest.raises(RuntimeError, match="not initialized"):
            core.batch_operation("sum", [1, 2, 3])

    def test_string_representation(self):
        """Test string representation of TemplateCore."""
        core = TemplateCore("test-core")

        str_repr = str(core)
        assert "TemplateCore" in str_repr
        assert "test-core" in str_repr
        assert "initialized=True" in str_repr

    def test_repr_representation(self):
        """Test repr representation of TemplateCore."""
        core = TemplateCore("test-core", {"debug": True})

        repr_str = repr(core)
        assert "TemplateCore" in repr_str
        assert "test-core" in repr_str
        assert "debug" in repr_str


@pytest.mark.integration
class TestTemplateCoreIntegration:
    """Integration tests for TemplateCore."""

    def test_complete_workflow(self):
        """Test a complete workflow using TemplateCore."""
        # Initialize with custom config
        config = {
            "debug": False,
            "timeout": 10,
            "max_retries": 2,
            "buffer_size": 100,
        }

        core = TemplateCore("workflow-test", config)

        # Verify initialization
        assert core.is_initialized
        assert core.config["debug"] is False

        # Add some data
        core.set_data("user_data", {"name": "test", "age": 30})
        core.set_data("session_id", "abc123")

        # Process some items
        raw_data = ["  item1  ", "ITEM2", 42, 3.14, None]
        processed_data = core.process_items(raw_data)

        # Store processed data
        core.set_data("processed_data", processed_data)

        # Run batch operations
        numeric_data = [1, 2, 3, 4, 5] * 20  # 100 items
        sum_result = core.batch_operation("sum", numeric_data, batch_size=25)

        # Verify results
        assert sum_result["operation"] == "sum"
        assert sum_result["result"] == 300  # (1+2+3+4+5) * 20
        assert sum_result["batches_processed"] == 4

        # Check final status
        status = core.status
        assert len(status["data_keys"]) == 3
        assert "user_data" in status["data_keys"]
        assert "session_id" in status["data_keys"]
        assert "processed_data" in status["data_keys"]

    @pytest.mark.slow
    def test_large_data_processing(self):
        """Test processing large amounts of data."""
        core = TemplateCore("large-data-test", {"buffer_size": 1000})

        # Generate large dataset
        large_dataset = list(range(10000))

        # Process in batches
        result = core.batch_operation("sum", large_dataset, batch_size=1000)

        # Verify result
        expected_sum = sum(large_dataset)
        assert result["result"] == expected_sum
        assert result["batches_processed"] == 10
        assert result["total_items"] == 10000
