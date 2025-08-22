"""Python Template - A modern Python project template with loguru, ruff, and uv.

This package provides a complete Python project template with modern tooling
including loguru for logging, ruff for linting and formatting, and uv for
package management.
"""



__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"
__description__ = "A modern Python project template with loguru, ruff, and uv"

# 导出主要的公共API
from .core import TemplateCore
from .logger import get_logger, setup_logging

__all__ = [
    "TemplateCore",
    "get_logger",
    "setup_logging",
    "__version__",
]
