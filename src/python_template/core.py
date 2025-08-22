"""Core functionality module.

This module contains the main business logic and core functionality
of the python-template package.
"""



from typing import Any, Dict, List, Optional

from .logger import get_logger

logger = get_logger(__name__)


class TemplateCore:
    """Core template functionality class.
    
    This class provides the main functionality for the python template,
    demonstrating best practices for class design and implementation.
    """
    
    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None) -> None:
        """Initialize the TemplateCore instance.
        
        Args:
            name: Name identifier for this instance
            config: Optional configuration dictionary
        """
        self.name = name
        self.config = config or {}
        self._initialized = False
        self._data: Dict[str, Any] = {}
        
        logger.info(f"Initializing TemplateCore instance: {name}")
        self._initialize()
    
    def _initialize(self) -> None:
        """Internal initialization method."""
        try:
            # 执行初始化逻辑
            self._setup_defaults()
            self._validate_config()
            self._initialized = True
            logger.info(f"TemplateCore '{self.name}' initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize TemplateCore '{self.name}': {e}")
            raise
    
    def _setup_defaults(self) -> None:
        """Setup default configuration values."""
        defaults = {
            "debug": False,
            "timeout": 30,
            "max_retries": 3,
            "buffer_size": 1024,
        }
        
        # 合并默认配置和用户配置
        for key, value in defaults.items():
            if key not in self.config:
                self.config[key] = value
                logger.debug(f"Set default config: {key} = {value}")
    
    def _validate_config(self) -> None:
        """Validate the configuration."""
        required_types = {
            "debug": bool,
            "timeout": (int, float),
            "max_retries": int,
            "buffer_size": int,
        }
        
        for key, expected_type in required_types.items():
            if key in self.config:
                value = self.config[key]
                if not isinstance(value, expected_type):
                    raise ValueError(
                        f"Config '{key}' must be of type {expected_type}, "
                        f"got {type(value)}"
                    )
                    
        # 验证数值范围
        if self.config.get("timeout", 0) <= 0:
            raise ValueError("Timeout must be positive")
        
        if self.config.get("max_retries", 0) < 0:
            raise ValueError("Max retries cannot be negative")
        
        if self.config.get("buffer_size", 0) <= 0:
            raise ValueError("Buffer size must be positive")
    
    @property
    def is_initialized(self) -> bool:
        """Check if the instance is properly initialized."""
        return self._initialized
    
    @property
    def status(self) -> Dict[str, Any]:
        """Get current status information."""
        return {
            "name": self.name,
            "initialized": self._initialized,
            "config": self.config.copy(),
            "data_keys": list(self._data.keys()),
        }
    
    def set_data(self, key: str, value: Any) -> None:
        """Set data value by key.
        
        Args:
            key: Data key
            value: Data value
        """
        if not self._initialized:
            raise RuntimeError("TemplateCore not initialized")
        
        logger.debug(f"Setting data: {key} = {value}")
        self._data[key] = value
    
    def get_data(self, key: str, default: Any = None) -> Any:
        """Get data value by key.
        
        Args:
            key: Data key
            default: Default value if key not found
            
        Returns:
            Data value or default
        """
        if not self._initialized:
            raise RuntimeError("TemplateCore not initialized")
        
        value = self._data.get(key, default)
        logger.debug(f"Getting data: {key} = {value}")
        return value
    
    def remove_data(self, key: str) -> bool:
        """Remove data by key.
        
        Args:
            key: Data key to remove
            
        Returns:
            True if key was removed, False if key didn't exist
        """
        if not self._initialized:
            raise RuntimeError("TemplateCore not initialized")
        
        if key in self._data:
            del self._data[key]
            logger.debug(f"Removed data key: {key}")
            return True
        
        logger.debug(f"Data key not found: {key}")
        return False
    
    def clear_data(self) -> None:
        """Clear all data."""
        if not self._initialized:
            raise RuntimeError("TemplateCore not initialized")
        
        keys_count = len(self._data)
        self._data.clear()
        logger.info(f"Cleared {keys_count} data entries")
    
    def process_items(self, items: List[Any]) -> List[Any]:
        """Process a list of items.
        
        This is a sample method demonstrating how to process data
        with proper error handling and logging.
        
        Args:
            items: List of items to process
            
        Returns:
            List of processed items
        """
        if not self._initialized:
            raise RuntimeError("TemplateCore not initialized")
        
        if not isinstance(items, list):
            raise TypeError("Items must be a list")
        
        logger.info(f"Processing {len(items)} items")
        processed_items = []
        
        for i, item in enumerate(items):
            try:
                # 示例处理逻辑
                if isinstance(item, str):
                    processed_item = item.strip().upper()
                elif isinstance(item, (int, float)):
                    processed_item = item * 2
                else:
                    processed_item = str(item)
                
                processed_items.append(processed_item)
                logger.debug(f"Processed item {i}: {item} -> {processed_item}")
                
            except Exception as e:
                logger.error(f"Failed to process item {i} ({item}): {e}")
                if self.config.get("debug", False):
                    raise
                # 在非调试模式下，跳过有问题的项
                continue
        
        logger.info(f"Successfully processed {len(processed_items)} items")
        return processed_items
    
    def batch_operation(
        self,
        operation: str,
        data: List[Any],
        batch_size: Optional[int] = None
    ) -> Dict[str, Any]:
        """Perform batch operation on data.
        
        Args:
            operation: Operation type ('sum', 'count', 'validate')
            data: Data to process
            batch_size: Optional batch size for processing
            
        Returns:
            Operation results
        """
        if not self._initialized:
            raise RuntimeError("TemplateCore not initialized")
        
        if batch_size is None:
            batch_size = self.config.get("buffer_size", 1024)
        
        logger.info(f"Starting batch operation '{operation}' on {len(data)} items")
        
        valid_operations = ["sum", "count", "validate"]
        if operation not in valid_operations:
            raise ValueError(f"Invalid operation. Must be one of: {valid_operations}")
        
        results = {
            "operation": operation,
            "total_items": len(data),
            "batch_size": batch_size,
            "batches_processed": 0,
            "result": None,
            "errors": [],
        }
        
        try:
            if operation == "sum":
                total = 0
                for i in range(0, len(data), batch_size):
                    batch = data[i:i + batch_size]
                    batch_sum = sum(x for x in batch if isinstance(x, (int, float)))
                    total += batch_sum
                    results["batches_processed"] += 1
                    logger.debug(f"Processed batch {results['batches_processed']}")
                
                results["result"] = total
                
            elif operation == "count":
                count = len(data)
                results["result"] = count
                results["batches_processed"] = 1
                
            elif operation == "validate":
                valid_count = 0
                for i in range(0, len(data), batch_size):
                    batch = data[i:i + batch_size]
                    batch_valid = sum(1 for x in batch if x is not None)
                    valid_count += batch_valid
                    results["batches_processed"] += 1
                
                results["result"] = {
                    "valid_items": valid_count,
                    "invalid_items": len(data) - valid_count,
                    "validity_ratio": valid_count / len(data) if data else 0,
                }
            
            logger.info(f"Batch operation '{operation}' completed successfully")
            
        except Exception as e:
            error_msg = f"Batch operation '{operation}' failed: {e}"
            logger.error(error_msg)
            results["errors"].append(error_msg)
            raise
        
        return results
    
    def __str__(self) -> str:
        """String representation of the instance."""
        return f"TemplateCore(name='{self.name}', initialized={self._initialized})"
    
    def __repr__(self) -> str:
        """Developer representation of the instance."""
        return (
            f"TemplateCore(name='{self.name}', "
            f"config={self.config}, "
            f"initialized={self._initialized})"
        )
