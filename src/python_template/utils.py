"""Utility functions module.

This module provides various utility functions that can be used
throughout the application.
"""

import hashlib
import json
import time
from datetime import datetime, timezone
from functools import wraps
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from .logger import get_logger

logger = get_logger(__name__)


def timing_decorator(func: Callable) -> Callable:
    """Decorator to measure function execution time.

    Args:
        func: Function to be decorated

    Returns:
        Decorated function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            logger.debug(
                f"Function '{func.__name__}' executed in {execution_time:.4f} seconds"
            )

    return wrapper


def retry_decorator(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Exception, ...] = (Exception,),
) -> Callable:
    """Decorator to retry function execution on failure.

    Args:
        max_retries: Maximum number of retry attempts
        delay: Initial delay between retries in seconds
        backoff: Multiplier for delay after each retry
        exceptions: Tuple of exception types to catch

    Returns:
        Decorator function
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
                            f"Function '{func.__name__}' failed (attempt {attempt + 1}/"
                            f"{max_retries + 1}): {e}. Retrying in {current_delay:.2f}s"
                        )
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        logger.error(
                            f"Function '{func.__name__}' failed after "
                            f"{max_retries + 1} attempts: {e}"
                        )

            raise last_exception

        return wrapper

    return decorator


def safe_json_loads(json_str: str, default: Any = None) -> Any:
    """Safely parse JSON string.

    Args:
        json_str: JSON string to parse
        default: Default value to return on parse error

    Returns:
        Parsed JSON data or default value
    """
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, TypeError) as e:
        logger.debug(f"Failed to parse JSON: {e}")
        return default


def safe_json_dumps(obj: Any, default: Any = None, **kwargs) -> Optional[str]:
    """Safely serialize object to JSON string.

    Args:
        obj: Object to serialize
        default: Default serializer for non-serializable objects
        **kwargs: Additional arguments for json.dumps

    Returns:
        JSON string or None on error
    """
    try:
        return json.dumps(obj, default=default, ensure_ascii=False, **kwargs)
    except (TypeError, ValueError) as e:
        logger.debug(f"Failed to serialize to JSON: {e}")
        return None


def calculate_file_hash(file_path: Union[str, Path], algorithm: str = "sha256") -> str:
    """Calculate hash of a file.

    Args:
        file_path: Path to the file
        algorithm: Hash algorithm to use

    Returns:
        Hex digest of the file hash

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If algorithm is not supported
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        hasher = hashlib.new(algorithm)
    except ValueError:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}") from None

    logger.debug(f"Calculating {algorithm} hash for: {file_path}")

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hasher.update(chunk)

    hash_value = hasher.hexdigest()
    logger.debug(f"File hash ({algorithm}): {hash_value}")
    return hash_value


def ensure_directory(directory_path: Union[str, Path]) -> Path:
    """Ensure directory exists, create if it doesn't.

    Args:
        directory_path: Path to the directory

    Returns:
        Path object of the directory
    """
    dir_path = Path(directory_path)
    dir_path.mkdir(parents=True, exist_ok=True)
    logger.debug(f"Ensured directory exists: {dir_path}")
    return dir_path


def get_file_size(file_path: Union[str, Path]) -> int:
    """Get file size in bytes.

    Args:
        file_path: Path to the file

    Returns:
        File size in bytes

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    size = file_path.stat().st_size
    logger.debug(f"File size: {file_path} = {size} bytes")
    return size


def format_file_size(size_bytes: int) -> str:
    """Format file size in human-readable format.

    Args:
        size_bytes: Size in bytes

    Returns:
        Formatted size string
    """
    if size_bytes == 0:
        return "0 B"

    size_names = ["B", "KB", "MB", "GB", "TB"]
    import math

    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)

    return f"{s} {size_names[i]}"


def get_timestamp(include_timezone: bool = True) -> str:
    """Get current timestamp as ISO format string.

    Args:
        include_timezone: Whether to include timezone information

    Returns:
        ISO format timestamp string
    """
    if include_timezone:
        return datetime.now(timezone.utc).isoformat()
    else:
        return datetime.now().isoformat()


def parse_timestamp(timestamp_str: str) -> datetime:
    """Parse ISO format timestamp string to datetime object.

    Args:
        timestamp_str: ISO format timestamp string

    Returns:
        datetime object

    Raises:
        ValueError: If timestamp format is invalid
    """
    try:
        return datetime.fromisoformat(timestamp_str)
    except ValueError as e:
        logger.error(f"Invalid timestamp format: {timestamp_str}")
        raise ValueError(f"Invalid timestamp format: {e}") from e


def chunk_list(data: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split list into chunks of specified size.

    Args:
        data: List to split
        chunk_size: Size of each chunk

    Returns:
        List of chunks

    Raises:
        ValueError: If chunk_size is not positive
    """
    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive")

    chunks = []
    for i in range(0, len(data), chunk_size):
        chunks.append(data[i : i + chunk_size])

    logger.debug(f"Split list of {len(data)} items into {len(chunks)} chunks")
    return chunks


def flatten_dict(
    nested_dict: Dict[str, Any], separator: str = ".", prefix: str = ""
) -> Dict[str, Any]:
    """Flatten nested dictionary.

    Args:
        nested_dict: Nested dictionary to flatten
        separator: Separator for nested keys
        prefix: Prefix for keys

    Returns:
        Flattened dictionary
    """
    flattened = {}

    for key, value in nested_dict.items():
        new_key = f"{prefix}{separator}{key}" if prefix else key

        if isinstance(value, dict):
            flattened.update(flatten_dict(value, separator, new_key))
        else:
            flattened[new_key] = value

    return flattened


def unflatten_dict(
    flattened_dict: Dict[str, Any], separator: str = "."
) -> Dict[str, Any]:
    """Unflatten dictionary back to nested structure.

    Args:
        flattened_dict: Flattened dictionary
        separator: Separator used in flattened keys

    Returns:
        Nested dictionary
    """
    unflattened = {}

    for key, value in flattened_dict.items():
        keys = key.split(separator)
        current = unflattened

        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]

        current[keys[-1]] = value

    return unflattened


def merge_dicts(*dicts: Dict[str, Any]) -> Dict[str, Any]:
    """Merge multiple dictionaries.

    Args:
        *dicts: Dictionaries to merge

    Returns:
        Merged dictionary
    """
    merged = {}

    for d in dicts:
        if isinstance(d, dict):
            merged.update(d)

    return merged


def filter_dict(
    data: Dict[str, Any],
    allowed_keys: Optional[List[str]] = None,
    excluded_keys: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Filter dictionary by allowed or excluded keys.

    Args:
        data: Dictionary to filter
        allowed_keys: List of allowed keys (whitelist)
        excluded_keys: List of excluded keys (blacklist)

    Returns:
        Filtered dictionary
    """
    if allowed_keys is not None:
        return {k: v for k, v in data.items() if k in allowed_keys}

    if excluded_keys is not None:
        return {k: v for k, v in data.items() if k not in excluded_keys}

    return data.copy()


def validate_email(email: str) -> bool:
    """Basic email validation.

    Args:
        email: Email address to validate

    Returns:
        True if email format is valid, False otherwise
    """
    import re

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def generate_uuid() -> str:
    """Generate UUID4 string.

    Returns:
        UUID4 string
    """
    import uuid

    return str(uuid.uuid4())


def sanitize_filename(filename: str) -> str:
    """Sanitize filename by removing/replacing invalid characters.

    Args:
        filename: Original filename

    Returns:
        Sanitized filename
    """
    import re

    # 移除或替换无效字符
    sanitized = re.sub(r'[<>:"/\\|?*]', "_", filename)

    # 移除控制字符
    sanitized = re.sub(r"[\x00-\x1f\x7f-\x9f]", "", sanitized)

    # 限制长度
    if len(sanitized) > 255:
        name, ext = Path(sanitized).stem, Path(sanitized).suffix
        max_name_len = 255 - len(ext)
        sanitized = name[:max_name_len] + ext

    return sanitized.strip()


class ContextTimer:
    """Context manager for timing code execution."""

    def __init__(self, name: str = "operation"):
        """Initialize timer.

        Args:
            name: Name of the operation being timed
        """
        self.name = name
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        """Start timing."""
        self.start_time = time.perf_counter()
        logger.debug(f"Starting timer for: {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Stop timing and log result."""
        self.end_time = time.perf_counter()
        execution_time = self.end_time - self.start_time
        logger.info(
            f"Operation '{self.name}' completed in {execution_time:.4f} seconds"
        )

    @property
    def elapsed_time(self) -> Optional[float]:
        """Get elapsed time.

        Returns:
            Elapsed time in seconds or None if not completed
        """
        if self.start_time is None:
            return None

        end_time = self.end_time or time.perf_counter()
        return end_time - self.start_time
