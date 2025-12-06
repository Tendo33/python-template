"""Settings module using Pydantic for configuration management.

This module provides a comprehensive settings system that:
- Loads configuration from environment variables
- Supports .env file loading
- Provides type-safe configuration with validation
- Organizes settings into logical groups
- Implements singleton pattern for global access

使用Pydantic实现的配置管理模块，支持从环境变量和.env文件加载配置。
"""

from functools import lru_cache
from pathlib import Path
from typing import List, Optional

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Application settings / 应用程序配置."""

    name: str = Field(default="python-template", description="Application name")
    version: str = Field(default="0.1.0", description="Application version")
    debug: bool = Field(default=False, description="Debug mode")
    environment: str = Field(
        default="development",
        description="Environment (development/staging/production)",
    )

    @field_validator("environment")
    @classmethod
    def validate_environment(cls, v: str) -> str:
        """Validate environment value / 验证环境变量值."""
        allowed = ["development", "staging", "production"]
        if v not in allowed:
            raise ValueError(f"Environment must be one of {allowed}")
        return v


class LoggingSettings(BaseSettings):
    """Logging settings / 日志配置."""

    level: str = Field(default="INFO", description="Logging level")
    format: str = Field(default="standard", description="Log format (standard/json)")
    file: str = Field(default="", description="Log file path (empty for stdout only)")
    rotation: str = Field(default="10 MB", description="Log rotation size")
    retention: str = Field(default="1 week", description="Log retention period")
    json_format: bool = Field(default=False, description="Use JSON format for logs")

    @field_validator("level")
    @classmethod
    def validate_level(cls, v: str) -> str:
        """Validate logging level / 验证日志级别."""
        allowed = ["TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"]
        v_upper = v.upper()
        if v_upper not in allowed:
            raise ValueError(f"Logging level must be one of {allowed}")
        return v_upper

    @field_validator("format")
    @classmethod
    def validate_format(cls, v: str) -> str:
        """Validate log format / 验证日志格式."""
        allowed = ["standard", "json"]
        if v not in allowed:
            raise ValueError(f"Log format must be one of {allowed}")
        return v


class PerformanceSettings(BaseSettings):
    """Performance settings / 性能配置."""

    timeout: int = Field(default=30, ge=1, description="Request timeout in seconds")
    max_retries: int = Field(default=3, ge=0, description="Maximum retry attempts")
    buffer_size: int = Field(default=1024, ge=64, description="Buffer size in bytes")
    concurrent_workers: int = Field(
        default=4, ge=1, description="Number of concurrent workers"
    )


class SecuritySettings(BaseSettings):
    """Security settings / 安全配置."""

    secret_key: str = Field(default="", description="Secret key for encryption")
    api_key: str = Field(default="", description="API key for external services")
    ssl_verify: bool = Field(default=True, description="Verify SSL certificates")
    allowed_hosts: List[str] = Field(
        default_factory=lambda: ["localhost", "127.0.0.1"],
        description="Allowed hosts",
    )

    @field_validator("secret_key")
    @classmethod
    def validate_secret_key(cls, v: str) -> str:
        """Validate secret key in production / 在生产环境验证密钥."""
        # Note: This validation would typically check environment
        # For now, we just warn if empty
        if not v:
            import warnings

            warnings.warn(
                "SECRET_KEY is not set. This is insecure in production!",
                UserWarning,
                stacklevel=2,
            )
        return v


class Settings(BaseSettings):
    """Main settings class combining all configuration groups.

    主配置类，整合所有配置组。

    Configuration priority (highest to lowest):
    1. Environment variables
    2. .env file
    3. Default values

    配置优先级（从高到低）：
    1. 环境变量
    2. .env 文件
    3. 默认值
    """

    # Nested settings / 嵌套配置
    app: AppSettings = Field(default_factory=AppSettings)
    logging: LoggingSettings = Field(default_factory=LoggingSettings)
    performance: PerformanceSettings = Field(default_factory=PerformanceSettings)
    security: SecuritySettings = Field(default_factory=SecuritySettings)

    model_config = SettingsConfigDict(
        # Look for .env file in project root
        env_file=".env",
        env_file_encoding="utf-8",
        # Allow nested env vars like APP__NAME=myapp
        env_nested_delimiter="__",
        # Case sensitive environment variables
        case_sensitive=False,
        # Extra fields are forbidden
        extra="forbid",
    )

    @classmethod
    def from_env_file(cls, env_file: Optional[Path] = None) -> "Settings":
        """Load settings from a specific .env file.

        从指定的.env文件加载配置。

        Args:
            env_file: Path to .env file. If None, uses default .env

        Returns:
            Settings instance
        """
        if env_file:
            return cls(_env_file=str(env_file))
        return cls()

    def get_project_root(self) -> Path:
        """Get project root directory.

        获取项目根目录。

        Returns:
            Path to project root
        """
        # Assuming this file is in src/utils/
        current_file = Path(__file__).resolve()
        # Go up: setting.py -> utils -> src -> project_root
        return current_file.parent.parent.parent

    def get_log_file_path(self) -> Optional[Path]:
        """Get absolute path to log file if configured.

        获取日志文件的绝对路径（如果已配置）。

        Returns:
            Path to log file or None
        """
        if not self.logging.file:
            return None

        log_path = Path(self.logging.file)
        if log_path.is_absolute():
            return log_path

        # Relative path - make it relative to project root
        return self.get_project_root() / log_path


# Singleton instance / 单例实例
_settings: Optional[Settings] = None


@lru_cache
def get_settings() -> Settings:
    """Get global settings instance (singleton).

    获取全局配置实例（单例模式）。

    This function is cached to ensure only one Settings instance exists.
    该函数使用缓存确保只存在一个Settings实例。

    Returns:
        Settings instance

    Example:
        >>> from utils.setting import get_settings
        >>> settings = get_settings()
        >>> print(settings.app.name)
        python-template
    """
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings


def reload_settings(env_file: Optional[Path] = None) -> Settings:
    """Reload settings from environment/file.

    重新加载配置。

    This clears the cache and creates a new Settings instance.
    This is useful for testing or when configuration changes at runtime.

    这会清除缓存并创建新的Settings实例。
    在测试或运行时配置更改时很有用。

    Args:
        env_file: Optional path to .env file

    Returns:
        New Settings instance
    """
    global _settings
    get_settings.cache_clear()
    _settings = Settings.from_env_file(env_file) if env_file else Settings()
    return _settings


# Convenience function for direct access / 便捷访问函数
def get_app_settings() -> AppSettings:
    """Get application settings / 获取应用配置."""
    return get_settings().app


def get_logging_settings() -> LoggingSettings:
    """Get logging settings / 获取日志配置."""
    return get_settings().logging


def get_performance_settings() -> PerformanceSettings:
    """Get performance settings / 获取性能配置."""
    return get_settings().performance


def get_security_settings() -> SecuritySettings:
    """Get security settings / 获取安全配置."""
    return get_settings().security
