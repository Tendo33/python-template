"""Loguru logging configuration module.

This module provides a centralized logging configuration using loguru,
a modern and powerful logging library for Python.
"""

import sys
from pathlib import Path
from typing import Any, Dict, Optional

from loguru import logger


def setup_logging(
    level: str = "INFO",
    format_string: Optional[str] = None,
    log_file: Optional[str] = None,
    rotation: str = "10 MB",
    retention: str = "1 week",
    compression: str = "gz",
    serialize: bool = False,
    backtrace: bool = True,
    diagnose: bool = True,
    enqueue: bool = False,
    catch: bool = True,
) -> None:
    """Setup loguru logging configuration.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format_string: Custom format string for log messages
        log_file: Path to log file (optional)
        rotation: Log rotation policy
        retention: Log retention policy
        compression: Compression format for rotated logs
        serialize: Whether to serialize logs as JSON
        backtrace: Whether to include backtrace in exception logs
        diagnose: Whether to include variable values in exception logs
        enqueue: Whether to enqueue log messages
        catch: Whether to catch errors during logging
    """
    # 移除默认的处理器
    logger.remove()

    # 默认格式字符串
    if format_string is None:
        if serialize:
            format_string = "{message}"
        else:
            format_string = (
                "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                "<level>{level: <8}</level> | "
                "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
                "<level>{message}</level>"
            )

    # 控制台输出处理器
    logger.add(
        sys.stderr,
        level=level,
        format=format_string,
        backtrace=backtrace,
        diagnose=diagnose,
        enqueue=enqueue,
        catch=catch,
        serialize=serialize,
    )

    # 文件输出处理器（如果指定了日志文件）
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

        logger.add(
            log_path,
            level=level,
            format=format_string,
            rotation=rotation,
            retention=retention,
            compression=compression,
            backtrace=backtrace,
            diagnose=diagnose,
            enqueue=enqueue,
            catch=catch,
            serialize=serialize,
        )


def get_logger(name: Optional[str] = None) -> Any:
    """Get a logger instance.

    Args:
        name: Logger name (optional)

    Returns:
        Logger instance
    """
    if name:
        return logger.bind(name=name)
    return logger


def configure_json_logging(
    level: str = "INFO",
    log_file: Optional[str] = None,
    extra_fields: Optional[Dict[str, Any]] = None,
) -> None:
    """Configure JSON structured logging.

    Args:
        level: Logging level
        log_file: Path to log file
        extra_fields: Additional fields to include in JSON logs
    """
    if extra_fields is None:
        extra_fields = {}

    # JSON格式化函数
    def json_formatter(record: Dict[str, Any]) -> str:
        """Format log record as JSON."""
        import json

        # 基础字段
        log_entry = {
            "timestamp": record["time"].isoformat(),
            "level": record["level"].name,
            "logger": record["name"],
            "module": record["module"],
            "function": record["function"],
            "line": record["line"],
            "message": record["message"],
        }

        # 添加额外字段
        log_entry.update(extra_fields)

        # 如果有异常信息，添加异常详情
        if record.get("exception"):
            log_entry["exception"] = {
                "type": record["exception"].type.__name__,
                "value": str(record["exception"].value),
                "traceback": record["exception"].traceback,
            }

        return json.dumps(log_entry, ensure_ascii=False)

    # 重新配置日志
    setup_logging(
        level=level,
        format_string=json_formatter,
        log_file=log_file,
        serialize=True,
    )


def log_function_calls(func):
    """Decorator to log function calls with parameters and return values.

    Args:
        func: Function to be decorated

    Returns:
        Decorated function
    """
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        func_logger = get_logger(f"{func.__module__}.{func.__name__}")

        # 记录函数调用
        func_logger.debug(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")

        try:
            # 执行函数
            result = func(*args, **kwargs)

            # 记录返回值
            func_logger.debug(f"{func.__name__} returned: {result}")

            return result
        except Exception as e:
            # 记录异常
            func_logger.exception(f"Exception in {func.__name__}: {e}")
            raise

    return wrapper


# 预配置的日志器实例
default_logger = get_logger("python_template")


# 便捷的日志函数
def debug(message: str, **kwargs) -> None:
    """Log debug message."""
    default_logger.debug(message, **kwargs)


def info(message: str, **kwargs) -> None:
    """Log info message."""
    default_logger.info(message, **kwargs)


def warning(message: str, **kwargs) -> None:
    """Log warning message."""
    default_logger.warning(message, **kwargs)


def error(message: str, **kwargs) -> None:
    """Log error message."""
    default_logger.error(message, **kwargs)


def critical(message: str, **kwargs) -> None:
    """Log critical message."""
    default_logger.critical(message, **kwargs)


def exception(message: str, **kwargs) -> None:
    """Log exception with traceback."""
    default_logger.exception(message, **kwargs)
