# Usage Guide

This guide covers how to use the Python Template in various scenarios.

## Command Line Interface

The template provides a comprehensive CLI for common operations.

### Basic Commands

```bash
# Show help
python -m python_template.cli --help

# Show version information
python -m python_template.cli version

# Run the demonstration
python -m python_template.cli demo

# Display current configuration
python -m python_template.cli config
```

### CLI Output Examples

**Version command**:
```
$ python -m python_template.cli version
Python Template v0.1.0
A modern Python project template with loguru, ruff, and uv
```

**Demo command**:
```
$ python -m python_template.cli demo
2025-08-22 17:05:30 | INFO     | Starting Python Template demonstration
2025-08-22 17:05:30 | INFO     | Creating TemplateCore instance...
2025-08-22 17:05:30 | INFO     | Demonstrating data operations...
...
```

## Using as a Library

### Basic Usage

```python
from python_template import TemplateCore, get_logger, setup_logging

# Setup logging first
setup_logging(level="INFO")
logger = get_logger(__name__)

# Create a core instance
core = TemplateCore("my-application", {
    "debug": False,
    "timeout": 30,
    "max_retries": 3
})

logger.info("Application started")
```

### Core Functionality

#### Data Management

```python
# Set data
core.set_data("user_id", "12345")
core.set_data("session", {"token": "abc123", "expires": "2024-01-01"})

# Get data
user_id = core.get_data("user_id")
session = core.get_data("session", {})  # with default

# Remove data
core.remove_data("user_id")

# Clear all data
core.clear_data()
```

#### Data Processing

```python
# Process various data types
items = ["  hello  ", "WORLD", 42, 3.14, None]
processed = core.process_items(items)
# Result: ["HELLO", "WORLD", 84, 6.28, "None"]

# Batch operations
numbers = list(range(1, 1001))  # 1-1000

# Sum operation
result = core.batch_operation("sum", numbers)
print(f"Sum: {result['result']}")  # Sum: 500500

# Count operation
result = core.batch_operation("count", items)
print(f"Count: {result['result']}")  # Count: 5

# Validation operation
mixed_data = [1, None, "test", None, 42, "", 0]
result = core.batch_operation("validate", mixed_data)
print(f"Valid items: {result['result']['valid_items']}")
```

### Configuration Management

#### Using ConfigManager

```python
from python_template.config import ConfigManager, get_config

# Create a custom config manager
config = ConfigManager("config.toml")

# Get configuration values
app_name = config.get("app.name", "default-app")
debug_mode = config.get("app.debug", False)
log_level = config.get("logging.level", "INFO")

# Set configuration values
config.set("app.environment", "production")
config.set("performance.workers", 4)

# Get entire sections
app_config = config.get_section("app")
logging_config = config.get_section("logging")

# Validate required keys
try:
    config.validate_required([
        "app.name",
        "logging.level",
        "performance.timeout"
    ])
except ValueError as e:
    print(f"Configuration error: {e}")
```

#### Environment-based Configuration

```python
import os
from python_template.config import setup_config

# Set environment variables
os.environ["PYTHON_TEMPLATE_APP_DEBUG"] = "true"
os.environ["PYTHON_TEMPLATE_LOGGING_LEVEL"] = "DEBUG"

# Create config that reads from environment
config = setup_config()

# Verify environment settings were applied
assert config.get("app.debug") is True
assert config.get("logging.level") == "DEBUG"
```

### Logging

#### Basic Logging

```python
from python_template.logger import setup_logging, get_logger

# Setup logging with file output
setup_logging(
    level="DEBUG",
    log_file="app.log",
    rotation="10 MB",
    retention="7 days"
)

# Get a logger
logger = get_logger("my_module")

# Log messages
logger.debug("Debug information")
logger.info("Application started")
logger.warning("This is a warning")
logger.error("An error occurred")
logger.critical("Critical system error")
```

#### Structured Logging

```python
from python_template.logger import configure_json_logging, get_logger

# Setup JSON logging
configure_json_logging(
    level="INFO",
    log_file="structured.log",
    extra_fields={
        "service": "my-service",
        "version": "1.0.0",
        "environment": "production"
    }
)

logger = get_logger("api")

# Log with context
logger.info(
    "User action performed",
    user_id="12345",
    action="login",
    ip_address="192.168.1.1"
)
```

#### Function Logging Decorator

```python
from python_template.logger import log_function_calls

@log_function_calls
def process_user_data(user_id: str, data: dict) -> dict:
    """Process user data with automatic logging."""
    # Function logic here
    result = {"processed": True, "user_id": user_id}
    return result

# Usage - function calls and returns will be automatically logged
result = process_user_data("12345", {"name": "John"})
```

#### Convenience Logging Functions

```python
from python_template.logger import debug, info, warning, error, critical, exception

# Use convenience functions for quick logging
info("Application starting", component="main")
debug("Processing request", request_id="req-123")
warning("Rate limit approaching", remaining=5)

try:
    # Some operation that might fail
    risky_operation()
except Exception:
    exception("Operation failed")  # Logs exception with traceback
```

### Utility Functions

#### File Operations

```python
from python_template.utils import (
    calculate_file_hash,
    get_file_size,
    format_file_size,
    ensure_directory
)

# Calculate file hash
hash_value = calculate_file_hash("data.txt", "sha256")
print(f"File hash: {hash_value}")

# Get and format file size
size = get_file_size("data.txt")
formatted_size = format_file_size(size)
print(f"File size: {formatted_size}")

# Ensure directory exists
data_dir = ensure_directory("data/processed/")
```

#### Data Processing

```python
from python_template.utils import (
    chunk_list,
    flatten_dict,
    unflatten_dict,
    merge_dicts
)

# Split large lists into chunks
large_list = list(range(1000))
chunks = chunk_list(large_list, chunk_size=100)
print(f"Split into {len(chunks)} chunks")

# Flatten nested dictionaries
nested = {
    "app": {"name": "test", "debug": True},
    "db": {"host": "localhost", "port": 5432}
}
flat = flatten_dict(nested)
# Result: {"app.name": "test", "app.debug": True, "db.host": "localhost", "db.port": 5432}

# Unflatten back to nested
nested_again = unflatten_dict(flat)
```

#### Decorators

```python
from python_template.utils import timing_decorator, retry_decorator

@timing_decorator
@retry_decorator(max_retries=3, delay=1.0, backoff=2.0)
def unreliable_api_call():
    """Function that might fail and should be retried with timing."""
    # API call logic here
    pass

# Usage - will automatically retry on failure and log execution time
result = unreliable_api_call()
```

#### Context Managers

```python
from python_template.utils import ContextTimer

# Time code execution
with ContextTimer("data_processing"):
    # Long-running operation
    process_large_dataset()

# Logs: "Operation 'data_processing' completed in 2.3456 seconds"
```

## Advanced Usage

### Custom Configuration Sources

```python
from python_template.config import ConfigManager

# Create config with multiple sources
config = ConfigManager("app.toml")

# Add runtime configuration
config.update({
    "runtime": {
        "started_at": "2025-08-22T17:05:30+08:00",
        "process_id": 12345
    }
})

# Use in application
if config.get("app.debug"):
    logger.setLevel("DEBUG")
```

### Error Handling

```python
from python_template.core import TemplateCore
from python_template.logger import get_logger

logger = get_logger(__name__)

try:
    core = TemplateCore("app", {"invalid_config": "value"})
except ValueError as e:
    logger.error(f"Configuration error: {e}")
    # Handle configuration errors
except Exception as e:
    logger.exception(f"Unexpected error: {e}")
    # Handle other errors
```

### Performance Monitoring

```python
from python_template.utils import ContextTimer
from python_template.logger import get_logger

logger = get_logger("performance")

# Monitor operation performance
with ContextTimer("database_query") as timer:
    result = execute_complex_query()

    # Check if operation was slow
    if timer.elapsed_time > 5.0:
        logger.warning(
            f"Slow query detected: {timer.elapsed_time:.2f}s",
            query_type="complex",
            threshold=5.0
        )
```

## Best Practices

### 1. Logging Strategy

- Use structured logging for production systems
- Include relevant context in log messages
- Use appropriate log levels
- Configure log rotation to prevent disk space issues

### 2. Configuration Management

- Use environment variables for deployment-specific settings
- Keep sensitive data in environment variables, not config files
- Validate required configuration at startup
- Use reasonable defaults

### 3. Error Handling

- Use specific exception types
- Log errors with sufficient context
- Implement retry logic for transient failures
- Fail fast for configuration errors

### 4. Performance

- Use batch operations for large datasets
- Monitor performance-critical operations
- Implement timeouts for external operations
- Use appropriate data structures

### 5. Testing

- Test with realistic data sizes
- Mock external dependencies
- Test error conditions
- Use fixtures for common test data
