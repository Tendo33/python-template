"""Utils package - 常用工具函数集合。

这个包提供了各种常用的工具函数,包括:
- logger_util: 日志配置和管理
- json_utils: JSON 读写和序列化
- file_utils: 文件操作
- decorator_utils: 装饰器工具
- date_utils: 日期时间处理
- common_utils: 通用工具函数
"""

# Logger utilities
from .logger_util import (
    configure_json_logging,
    critical,
    debug,
    error,
    exception,
    get_logger,
    info,
    log_function_calls,
    setup_logging,
    warning,
)

# JSON utilities
from .json_utils import (
    merge_json_files,
    pretty_print_json,
    read_json,
    safe_json_dumps,
    safe_json_loads,
    validate_json_schema,
    write_json,
)

# File utilities
from .file_utils import (
    calculate_file_hash,
    copy_file,
    delete_file,
    ensure_directory,
    format_file_size,
    get_file_size,
    list_files,
    move_file,
    read_text_file,
    sanitize_filename,
    write_text_file,
)

# Decorator utilities
from .decorator_utils import (
    ContextTimer,
    catch_exceptions,
    deprecated,
    log_calls,
    retry_decorator,
    singleton,
    timing_decorator,
)

# Date utilities
from .date_utils import (
    add_days,
    add_hours,
    add_minutes,
    format_datetime,
    from_unix_timestamp,
    get_current_date,
    get_current_time,
    get_month_start,
    get_time_difference,
    get_timestamp,
    get_unix_timestamp,
    get_week_start,
    humanize_timedelta,
    is_weekend,
    parse_datetime,
    parse_timestamp,
)

# Common utilities
from .common_utils import (
    batch_process,
    chunk_list,
    deep_copy_dict,
    deep_merge_dict,
    filter_dict,
    flatten_dict,
    generate_uuid,
    merge_dicts,
    remove_empty_values,
    remove_none_values,
    retry_on_exception,
    safe_get,
    safe_set,
    unflatten_dict,
    validate_email,
)

# 常用函数快捷导出
__all__ = [
    # Logger
    "get_logger",
    "setup_logging",
    "configure_json_logging",
    "log_function_calls",
    "debug",
    "info",
    "warning",
    "error",
    "critical",
    "exception",
    # JSON
    "read_json",
    "write_json",
    "safe_json_loads",
    "safe_json_dumps",
    "merge_json_files",
    "pretty_print_json",
    "validate_json_schema",
    # File
    "ensure_directory",
    "get_file_size",
    "format_file_size",
    "calculate_file_hash",
    "copy_file",
    "move_file",
    "delete_file",
    "list_files",
    "read_text_file",
    "write_text_file",
    "sanitize_filename",
    # Decorators
    "timing_decorator",
    "retry_decorator",
    "catch_exceptions",
    "log_calls",
    "deprecated",
    "singleton",
    "ContextTimer",
    # Date/Time
    "get_timestamp",
    "parse_timestamp",
    "format_datetime",
    "parse_datetime",
    "get_current_date",
    "get_current_time",
    "add_days",
    "add_hours",
    "add_minutes",
    "get_time_difference",
    "is_weekend",
    "get_week_start",
    "get_month_start",
    "humanize_timedelta",
    "get_unix_timestamp",
    "from_unix_timestamp",
    # Common
    "chunk_list",
    "flatten_dict",
    "unflatten_dict",
    "merge_dicts",
    "filter_dict",
    "validate_email",
    "generate_uuid",
    "deep_copy_dict",
    "deep_merge_dict",
    "safe_get",
    "safe_set",
    "remove_none_values",
    "remove_empty_values",
    "batch_process",
    "retry_on_exception",
]
