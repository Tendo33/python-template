# Python Template

[![CI](https://github.com/yourusername/python-template/workflows/CI/badge.svg)](https://github.com/yourusername/python-template/actions)
[![codecov](https://codecov.io/gh/yourusername/python-template/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/python-template)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

A modern Python project template featuring:

- 🚀 **[uv](https://github.com/astral-sh/uv)** - Ultra-fast Python package manager
- 🔧 **[ruff](https://github.com/astral-sh/ruff)** - Extremely fast Python linter and formatter
- 📝 **[loguru](https://github.com/Delgan/loguru)** - Modern logging library
- 🧪 **[pytest](https://pytest.org/)** - Comprehensive testing framework
- 🔄 **GitHub Actions** - Complete CI/CD pipeline
- 📦 **Modern project structure** - Following Python packaging best practices

## Features

### 🛠️ Modern Tool Stack

- **uv**: Lightning-fast package management and virtual environments
- **ruff**: All-in-one linting and formatting (replaces black, isort, flake8, etc.)
- **loguru**: Simplified, powerful logging with structured output support
- **pytest**: Advanced testing with coverage reporting and fixtures

### 📁 Clean Project Structure

```
python-template/
├── src/python_template/     # Source code (importable package)
│   ├── __init__.py          # Package initialization
│   ├── logger.py            # Logging setup and utilities
│   ├── utils/               # Utility modules
│   │   ├── file_utils.py    # File operations
│   │   ├── date_utils.py    # Date/time utilities
│   │   └── ...
│   └── models/              # Data models
├── tests/                   # Test suite
│   ├── conftest.py          # Pytest configuration and fixtures
│   ├── test_logger.py       # Logging tests
│   └── test_utils.py        # Utility tests
├── scripts/                 # Development scripts
│   ├── format.py            # Code formatting script
│   └── lint.py              # Linting script
├── docs/                    # Documentation
├── .github/workflows/       # CI/CD workflows
├── pyproject.toml           # Project configuration
└── README.md                # This file
```

### 🔧 Development Tools

- **Formatting**: Automated code formatting with ruff
- **Linting**: Comprehensive code quality checks
- **Testing**: Unit and integration tests with coverage
- **CI/CD**: GitHub Actions workflow for automated testing
- **Documentation**: Structured documentation setup

## Quick Start

### Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. **Install uv** (if not already installed):
   ```bash
   # macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

   # Or with pip
   pip install uv
   ```

2. **Clone and setup the project**:
   ```bash
   git clone https://github.com/yourusername/python-template.git
   cd python-template

   # Install dependencies
   uv sync --dev

   # Install the package in development mode
   uv pip install -e .
   ```

3. **Verify installation**:
   ```bash
   # Test the CLI
   uv run python -m python_template.cli --help

   # Run the demo
   uv run python -m python_template.cli demo
   ```

## Usage

### Command Line Interface

The template includes a CLI with several commands:

```bash
# Show help
python -m python_template.cli --help

# Show version
python -m python_template.cli version

# Run demonstration
python -m python_template.cli demo

# Show current configuration
python -m python_template.cli config
```

### As a Library

```python
from python_template import TemplateCore, get_logger, setup_logging

# Setup logging
setup_logging(level="INFO", log_file="app.log")
logger = get_logger(__name__)

# Create a core instance
core = TemplateCore("my-app", {
    "debug": True,
    "timeout": 30
})

# Use the core functionality
core.set_data("key", "value")
result = core.process_items(["hello", "world", 123])
logger.info(f"Processed: {result}")
```

### Configuration

The template supports multiple configuration sources:

1. **Default values** (in `config.py`)
2. **Configuration files** (JSON, TOML, YAML)
3. **Environment variables** (prefixed with `PYTHON_TEMPLATE_`)
4. **Runtime updates**

Example environment variables:
```bash
export PYTHON_TEMPLATE_APP_DEBUG=true
export PYTHON_TEMPLATE_LOGGING_LEVEL=DEBUG
export PYTHON_TEMPLATE_PERFORMANCE_TIMEOUT=60
```

## Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/python-template.git
cd python-template

# Install dependencies (including dev dependencies)
uv sync --dev

# Setup pre-commit hooks for automatic formatting (recommended)
python scripts/setup_pre_commit.py
```

### Development Workflow

#### Automatic Code Formatting with Pre-commit

**🎯 Recommended: Automatic formatting on every commit**

```bash
# Setup pre-commit hooks (one-time setup)
python scripts/setup_pre_commit.py

# Update hooks to latest versions
python scripts/setup_pre_commit.py --update

# Test hooks on all files
python scripts/setup_pre_commit.py --test

# Complete setup (install + update + test)
python scripts/setup_pre_commit.py --all
```

Once installed, `ruff format` will automatically run on every commit, ensuring consistent code formatting.

**Bypass hooks temporarily (if needed):**
```bash
git commit --no-verify
```

#### Manual Code Formatting

```bash
# Format code manually
python scripts/format.py

# Check formatting without changes
python scripts/format.py --check

# Show what would be changed
python scripts/format.py --diff
```

#### Linting

```bash
# Run linting
python scripts/lint.py

# Auto-fix issues
python scripts/lint.py --fix

# Comprehensive quality check
python scripts/lint.py --comprehensive
```

#### Testing

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=python_template

# Run specific test types
uv run pytest -m unit        # Unit tests only
uv run pytest -m integration # Integration tests only
uv run pytest -m "not slow"  # Exclude slow tests
```

#### Building

```bash
# Build the package
uv run python -m build

# Check the built package
uv run python -m twine check dist/*
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [uv](https://github.com/astral-sh/uv) - For ultra-fast package management
- [ruff](https://github.com/astral-sh/ruff) - For lightning-fast linting and formatting
- [loguru](https://github.com/Delgan/loguru) - For simplified, powerful logging
- [pytest](https://pytest.org/) - For comprehensive testing capabilities

---

**Ready to start your next Python project? Use this template and focus on building, not boilerplate!** 🚀
