"""Command line interface module.

This module provides a command line interface for the python-template package.
"""



import sys
from typing import List, Optional

from .config import get_config
from .core import TemplateCore
from .logger import get_logger, setup_logging

logger = get_logger(__name__)


def main(args: Optional[List[str]] = None) -> int:
    """Main entry point for CLI.
    
    Args:
        args: Command line arguments (defaults to sys.argv[1:])
        
    Returns:
        Exit code (0 for success, non-zero for error)
    """
    if args is None:
        args = sys.argv[1:]
    
    try:
        # 设置日志
        setup_logging(level="INFO")
        
        # 获取配置
        config = get_config()
        
        # 处理命令行参数
        if not args:
            return show_help()
        
        command = args[0].lower()
        
        if command in ("-h", "--help", "help"):
            return show_help()
        elif command in ("-v", "--version", "version"):
            return show_version()
        elif command == "demo":
            return run_demo()
        elif command == "config":
            return show_config()
        else:
            logger.error(f"Unknown command: {command}")
            return show_help()
    
    except KeyboardInterrupt:
        logger.info("Operation cancelled by user")
        return 1
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        return 1


def show_help() -> int:
    """Show help message.
    
    Returns:
        Exit code 0
    """
    help_text = """
Python Template CLI

Usage:
    python-template [command] [options]

Commands:
    help, -h, --help     Show this help message
    version, -v, --version  Show version information
    demo                 Run demonstration
    config               Show current configuration

Examples:
    python-template demo
    python-template version
    python-template config
    """
    
    print(help_text.strip())
    return 0


def show_version() -> int:
    """Show version information.
    
    Returns:
        Exit code 0
    """
    from . import __version__
    
    print(f"Python Template v{__version__}")
    print("A modern Python project template with loguru, ruff, and uv")
    return 0


def show_config() -> int:
    """Show current configuration.
    
    Returns:
        Exit code 0
    """
    config = get_config()
    
    print("Current Configuration:")
    print("=" * 50)
    
    config_dict = config.to_dict()
    for section, values in config_dict.items():
        print(f"\n[{section}]")
        if isinstance(values, dict):
            for key, value in values.items():
                print(f"  {key} = {value}")
        else:
            print(f"  {values}")
    
    return 0


def run_demo() -> int:
    """Run demonstration of the template functionality.
    
    Returns:
        Exit code 0 on success, 1 on error
    """
    try:
        logger.info("Starting Python Template demonstration")
        
        # 创建TemplateCore实例
        logger.info("Creating TemplateCore instance...")
        core = TemplateCore("demo-instance", {
            "debug": True,
            "timeout": 10,
            "max_retries": 2,
        })
        
        # 演示数据操作
        logger.info("Demonstrating data operations...")
        core.set_data("example_key", "example_value")
        core.set_data("number", 42)
        core.set_data("list", [1, 2, 3, 4, 5])
        
        # 显示状态
        status = core.status
        logger.info(f"Core status: {status}")
        
        # 演示数据处理
        logger.info("Processing sample data...")
        sample_data = ["hello", "world", 123, 456.78, "python"]
        processed = core.process_items(sample_data)
        logger.info(f"Processed data: {processed}")
        
        # 演示批处理操作
        logger.info("Running batch operations...")
        numeric_data = list(range(1, 101))  # 1-100
        
        # 求和操作
        sum_result = core.batch_operation("sum", numeric_data)
        logger.info(f"Sum operation result: {sum_result}")
        
        # 计数操作
        count_result = core.batch_operation("count", sample_data)
        logger.info(f"Count operation result: {count_result}")
        
        # 验证操作
        validation_data = [1, None, "test", None, 42, "", 0]
        validate_result = core.batch_operation("validate", validation_data)
        logger.info(f"Validation operation result: {validate_result}")
        
        logger.info("Demonstration completed successfully!")
        return 0
        
    except Exception as e:
        logger.exception(f"Demonstration failed: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
