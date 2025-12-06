"""Decorator utilities module.

提供常用的装饰器函数。
"""

import time
import traceback
from functools import wraps
from typing import Any, Callable, Optional, Tuple

from .logger_util import get_logger

logger = get_logger(__name__)


def timing_decorator(func: Callable) -> Callable:
    """计算函数执行时间的装饰器。

    Args:
        func: 要装饰的函数

    Returns:
        装饰后的函数
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.error(f"Exception in {func.__name__}: {e}")
            logger.debug(f"Traceback:\n{traceback.format_exc()}")
            raise
        finally:
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            logger.info(
                f"⏱️  Function '{func.__name__}' executed in {execution_time:.4f} seconds"
            )

    return wrapper


def retry_decorator(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Exception, ...] = (Exception,),
) -> Callable:
    """失败重试装饰器。

    Args:
        max_retries: 最大重试次数
        delay: 初始延迟时间(秒)
        backoff: 延迟时间的倍增系数
        exceptions: 要捕获的异常类型元组

    Returns:
        装饰器函数
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None

            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_retries:
                        logger.warning(
                            f"🔄 Function '{func.__name__}' failed (attempt {attempt + 1}/"
                            f"{max_retries + 1}): {e}. Retrying in {current_delay:.2f}s"
                        )
                        logger.debug(f"Traceback:\n{traceback.format_exc()}")
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        logger.error(
                            f"❌ Function '{func.__name__}' failed after "
                            f"{max_retries + 1} attempts: {e}"
                        )
                        logger.debug(f"Traceback:\n{traceback.format_exc()}")

            raise last_exception

        return wrapper

    return decorator


def catch_exceptions(
    default_return: Any = None,
    log_traceback: bool = True,
    reraise: bool = False,
) -> Callable:
    """捕获异常的装饰器。

    Args:
        default_return: 发生异常时的默认返回值
        log_traceback: 是否记录完整的 traceback
        reraise: 是否重新抛出异常

    Returns:
        装饰器函数
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Exception in {func.__name__}: {e}")
                if log_traceback:
                    logger.debug(f"Traceback:\n{traceback.format_exc()}")

                if reraise:
                    raise

                return default_return

        return wrapper

    return decorator


def log_calls(log_args: bool = True, log_result: bool = True) -> Callable:
    """记录函数调用的装饰器。

    Args:
        log_args: 是否记录参数
        log_result: 是否记录返回值

    Returns:
        装饰器函数
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__

            if log_args:
                logger.debug(f"📞 Calling {func_name} with args={args}, kwargs={kwargs}")
            else:
                logger.debug(f"📞 Calling {func_name}")

            try:
                result = func(*args, **kwargs)

                if log_result:
                    logger.debug(f"✅ {func_name} returned: {result}")
                else:
                    logger.debug(f"✅ {func_name} completed")

                return result

            except Exception as e:
                logger.error(f"❌ Exception in {func_name}: {e}")
                logger.debug(f"Traceback:\n{traceback.format_exc()}")
                raise

        return wrapper

    return decorator


def deprecated(reason: str = "", alternative: Optional[str] = None) -> Callable:
    """标记函数为已弃用的装饰器。

    Args:
        reason: 弃用原因
        alternative: 推荐的替代方案

    Returns:
        装饰器函数
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            message = f"⚠️  Function '{func.__name__}' is deprecated"
            if reason:
                message += f": {reason}"
            if alternative:
                message += f". Use '{alternative}' instead"

            logger.warning(message)

            return func(*args, **kwargs)

        return wrapper

    return decorator


def singleton(cls):
    """单例模式装饰器。

    Args:
        cls: 要装饰的类

    Returns:
        装饰后的类
    """
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
            logger.debug(f"Created singleton instance of {cls.__name__}")
        return instances[cls]

    return get_instance


class ContextTimer:
    """上下文管理器,用于计时代码块执行时间。

    Example:
        with ContextTimer("数据处理"):
            # 执行耗时操作
            process_data()
    """

    def __init__(self, name: str = "operation", log_level: str = "INFO"):
        """初始化计时器。

        Args:
            name: 操作名称
            log_level: 日志级别
        """
        self.name = name
        self.log_level = log_level.upper()
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        """开始计时。"""
        self.start_time = time.perf_counter()
        logger.debug(f"⏱️  Starting timer for: {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """停止计时并记录结果。"""
        self.end_time = time.perf_counter()
        execution_time = self.end_time - self.start_time

        if exc_type is not None:
            logger.error(
                f"❌ Operation '{self.name}' failed after {execution_time:.4f} seconds"
            )
            logger.debug(f"Traceback:\n{traceback.format_exc()}")
        else:
            log_func = getattr(logger, self.log_level.lower(), logger.info)
            log_func(
                f"✅ Operation '{self.name}' completed in {execution_time:.4f} seconds"
            )

    @property
    def elapsed_time(self) -> Optional[float]:
        """获取已经过的时间。

        Returns:
            已经过的时间(秒),如果未开始则返回 None
        """
        if self.start_time is None:
            return None

        end_time = self.end_time or time.perf_counter()
        return end_time - self.start_time
