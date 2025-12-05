"""Configuration management module.

This module provides configuration management functionality,
including loading from files, environment variables, and validation.
"""

import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from utils import get_logger

logger = get_logger(__name__)


class ConfigManager:
    """Configuration manager for handling application settings.

    Supports loading configuration from:
    - Default values
    - Configuration files (JSON, TOML)
    - Environment variables
    - Runtime updates
    """

    def __init__(self, config_file: Optional[Union[str, Path]] = None) -> None:
        """Initialize the configuration manager.

        Args:
            config_file: Optional path to configuration file
        """
        self._config: Dict[str, Any] = {}
        self._defaults: Dict[str, Any] = {}
        self._config_file = Path(config_file) if config_file else None
        self._env_prefix = "PYTHON_TEMPLATE_"

        logger.debug("Initializing ConfigManager")
        self._load_defaults()

        if self._config_file:
            self._load_from_file()

        self._load_from_env()

    def _load_defaults(self) -> None:
        """Load default configuration values."""
        self._defaults = {
            # 应用程序设置
            "app": {
                "name": "python-template",
                "version": "0.1.0",
                "debug": False,
                "environment": "development",
            },
            # 日志设置
            "logging": {
                "level": "INFO",
                "format": "standard",
                "file": None,
                "rotation": "10 MB",
                "retention": "1 week",
                "json_format": False,
            },
            # 性能设置
            "performance": {
                "timeout": 30,
                "max_retries": 3,
                "buffer_size": 1024,
                "concurrent_workers": 4,
            },
            # 安全设置
            "security": {
                "secret_key": None,
                "api_key": None,
                "ssl_verify": True,
                "allowed_hosts": ["localhost", "127.0.0.1"],
            },
        }

        # 复制默认值到当前配置
        self._config = self._deep_copy_dict(self._defaults)
        logger.debug("Loaded default configuration")

    def _load_from_file(self) -> None:
        """Load configuration from file."""
        if not self._config_file or not self._config_file.exists():
            logger.warning(f"Config file not found: {self._config_file}")
            return

        try:
            file_extension = self._config_file.suffix.lower()

            if file_extension == ".json":
                import json

                with open(self._config_file, encoding="utf-8") as f:
                    file_config = json.load(f)

            elif file_extension == ".toml":
                try:
                    import tomllib  # Python 3.11+
                except ImportError:
                    import tomli as tomllib  # Fallback for older Python versions

                with open(self._config_file, "rb") as f:
                    file_config = tomllib.load(f)

            elif file_extension in [".yml", ".yaml"]:
                try:
                    import yaml

                    with open(self._config_file, encoding="utf-8") as f:
                        file_config = yaml.safe_load(f)
                except ImportError:
                    logger.error("PyYAML not installed, cannot load YAML config")
                    return

            else:
                logger.error(f"Unsupported config file format: {file_extension}")
                return

            # 合并文件配置
            self._merge_config(file_config)
            logger.info(f"Loaded configuration from: {self._config_file}")

        except Exception as e:
            logger.error(f"Failed to load config file {self._config_file}: {e}")
            raise

    def _load_from_env(self) -> None:
        """Load configuration from environment variables."""
        env_config = {}

        for key, value in os.environ.items():
            if key.startswith(self._env_prefix):
                # 移除前缀并转换为小写
                config_key = key[len(self._env_prefix) :].lower()

                # 处理嵌套键 (例如: PYTHON_TEMPLATE_APP_DEBUG -> app.debug)
                if "_" in config_key:
                    keys = config_key.split("_")
                    current = env_config

                    for k in keys[:-1]:
                        if k not in current:
                            current[k] = {}
                        current = current[k]

                    # 尝试转换值类型
                    current[keys[-1]] = self._convert_env_value(value)
                else:
                    env_config[config_key] = self._convert_env_value(value)

        if env_config:
            self._merge_config(env_config)
            logger.debug("Loaded configuration from environment variables")

    def _convert_env_value(self, value: str) -> Any:
        """Convert environment variable string to appropriate type."""
        # 布尔值
        if value.lower() in ("true", "yes", "1", "on"):
            return True
        elif value.lower() in ("false", "no", "0", "off"):
            return False

        # 数字
        try:
            if "." in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            pass

        # 列表 (逗号分隔)
        if "," in value:
            return [item.strip() for item in value.split(",")]

        # 字符串
        return value

    def _merge_config(self, new_config: Dict[str, Any]) -> None:
        """Merge new configuration with existing configuration."""
        self._config = self._deep_merge_dict(self._config, new_config)

    def _deep_copy_dict(self, source: Dict[str, Any]) -> Dict[str, Any]:
        """Deep copy a dictionary."""
        result = {}
        for key, value in source.items():
            if isinstance(value, dict):
                result[key] = self._deep_copy_dict(value)
            elif isinstance(value, list):
                result[key] = value.copy()
            else:
                result[key] = value
        return result

    def _deep_merge_dict(
        self, base: Dict[str, Any], update: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Deep merge two dictionaries."""
        result = self._deep_copy_dict(base)

        for key, value in update.items():
            if (
                key in result
                and isinstance(result[key], dict)
                and isinstance(value, dict)
            ):
                result[key] = self._deep_merge_dict(result[key], value)
            else:
                result[key] = value

        return result

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key.

        Supports nested keys using dot notation (e.g., 'app.debug').

        Args:
            key: Configuration key
            default: Default value if key not found

        Returns:
            Configuration value
        """
        keys = key.split(".")
        current = self._config

        try:
            for k in keys:
                current = current[k]
            return current
        except (KeyError, TypeError):
            logger.debug(f"Configuration key not found: {key}")
            return default

    def set(self, key: str, value: Any) -> None:
        """Set configuration value by key.

        Supports nested keys using dot notation.

        Args:
            key: Configuration key
            value: Value to set
        """
        keys = key.split(".")
        current = self._config

        # 创建嵌套结构
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]

        current[keys[-1]] = value
        logger.debug(f"Set configuration: {key} = {value}")

    def has(self, key: str) -> bool:
        """Check if configuration key exists.

        Args:
            key: Configuration key

        Returns:
            True if key exists, False otherwise
        """
        return self.get(key, object()) is not object()

    def get_section(self, section: str) -> Dict[str, Any]:
        """Get entire configuration section.

        Args:
            section: Section name

        Returns:
            Section configuration dictionary
        """
        section_config = self.get(section, {})
        if not isinstance(section_config, dict):
            logger.warning(f"Section '{section}' is not a dictionary")
            return {}

        return section_config

    def update(self, config_dict: Dict[str, Any]) -> None:
        """Update configuration with dictionary.

        Args:
            config_dict: Dictionary to merge with current configuration
        """
        self._merge_config(config_dict)
        logger.debug("Updated configuration from dictionary")

    def reset_to_defaults(self) -> None:
        """Reset configuration to default values."""
        self._config = self._deep_copy_dict(self._defaults)
        logger.info("Reset configuration to defaults")

    def validate_required(self, required_keys: List[str]) -> None:
        """Validate that required configuration keys are present.

        Args:
            required_keys: List of required configuration keys

        Raises:
            ValueError: If any required key is missing
        """
        missing_keys = []

        for key in required_keys:
            if not self.has(key):
                missing_keys.append(key)

        if missing_keys:
            raise ValueError(f"Missing required configuration keys: {missing_keys}")

        logger.debug("All required configuration keys are present")

    def to_dict(self) -> Dict[str, Any]:
        """Get complete configuration as dictionary.

        Returns:
            Complete configuration dictionary
        """
        return self._deep_copy_dict(self._config)

    def __str__(self) -> str:
        """String representation of configuration."""
        return f"ConfigManager(config_file={self._config_file})"

    def __repr__(self) -> str:
        """Developer representation of configuration."""
        return (
            f"ConfigManager(config_file={self._config_file}, "
            f"keys={list(self._config.keys())})"
        )


# 全局配置实例
config = ConfigManager()


def get_config() -> ConfigManager:
    """Get the global configuration manager instance.

    Returns:
        Global ConfigManager instance
    """
    return config


def setup_config(config_file: Optional[Union[str, Path]] = None) -> ConfigManager:
    """Setup and return a new configuration manager.

    Args:
        config_file: Optional path to configuration file

    Returns:
        New ConfigManager instance
    """
    return ConfigManager(config_file)
