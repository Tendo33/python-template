# Installation Guide

This guide covers the installation and setup of the Python Template project.

## Prerequisites

Before installing, ensure you have:

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) package manager

## Installing uv

uv is a fast Python package manager that this template is designed to work with.

### macOS and Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Alternative: Install with pip

```bash
pip install uv
```

## Project Installation

### For Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/python-template.git
   cd python-template
   ```

2. **Install dependencies**:
   ```bash
   # Install all dependencies including development tools
   uv sync --dev

   # Install the package in development mode
   uv pip install -e .
   ```

3. **Verify installation**:
   ```bash
   # Test the CLI
   uv run python -m python_template.cli --help

   # Run tests
   uv run pytest
   ```

### For Production Use

1. **Install from PyPI** (when published):
   ```bash
   uv pip install python-template
   ```

2. **Install from source**:
   ```bash
   uv pip install git+https://github.com/yourusername/python-template.git
   ```

## Configuration

### Environment Variables

You can configure the application using environment variables:

```bash
# Application settings
export PYTHON_TEMPLATE_APP_DEBUG=true
export PYTHON_TEMPLATE_APP_NAME="my-app"

# Logging settings
export PYTHON_TEMPLATE_LOGGING_LEVEL=DEBUG
export PYTHON_TEMPLATE_LOGGING_FILE="app.log"

# Performance settings
export PYTHON_TEMPLATE_PERFORMANCE_TIMEOUT=60
export PYTHON_TEMPLATE_PERFORMANCE_MAX_RETRIES=5
```

### Configuration Files

Create a configuration file in JSON, TOML, or YAML format:

**config.toml**:
```toml
[app]
name = "my-app"
debug = true

[logging]
level = "INFO"
file = "logs/app.log"

[performance]
timeout = 30
max_retries = 3
```

**config.json**:
```json
{
  "app": {
    "name": "my-app",
    "debug": true
  },
  "logging": {
    "level": "INFO",
    "file": "logs/app.log"
  },
  "performance": {
    "timeout": 30,
    "max_retries": 3
  }
}
```

## Troubleshooting

### Common Issues

#### uv not found
- Ensure uv is installed and in your PATH
- Try restarting your terminal/shell
- On Windows, you may need to restart your terminal as Administrator

#### Import errors
- Ensure you've installed the package with `uv pip install -e .`
- Check that you're using the correct Python environment
- Verify dependencies are installed with `uv sync`

#### Permission errors
- On Unix systems, you may need to make scripts executable:
  ```bash
  chmod +x scripts/*.py
  ```

### Getting Help

If you encounter issues:

1. Check the [GitHub Issues](https://github.com/yourusername/python-template/issues)
2. Review the logs for error messages
3. Ensure all dependencies are up to date: `uv sync --upgrade`
