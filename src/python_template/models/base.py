"""Base models and mixins for Pydantic models.

Provides common configurations and reusable mixins for all Pydantic models.
为所有Pydantic模型提供通用配置和可复用的Mixin。
"""

from datetime import datetime
from typing import Any, Dict

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict, Field


class BaseModel(PydanticBaseModel):
    """Base model with common Pydantic v2 configuration.

    基础模型，包含通用的Pydantic v2配置。

    This model provides sensible defaults for all project models:
    - Allows population by field name or alias
    - Uses snake_case for field names
    - Validates assignments
    - Allows arbitrary types when needed

    该模型为所有项目模型提供合理的默认配置。
    """

    model_config = ConfigDict(
        # Allow population by field name or alias
        populate_by_name=True,
        # Validate field values when they are assigned
        validate_assignment=True,
        # Use snake_case for JSON schema field names
        alias_generator=None,
        # Strict mode for better type safety
        strict=False,
        # Allow extra fields (can be set to 'forbid' for stricter validation)
        extra="ignore",
    )

    def model_dump_json_safe(self) -> Dict[str, Any]:
        """Dump model to JSON-safe dictionary.

        转储模型为JSON安全的字典。

        Returns:
            Dictionary with JSON-serializable values
        """
        return self.model_dump(mode="json")


class TimestampMixin(BaseModel):
    """Mixin for adding timestamp fields to models.

    为模型添加时间戳字段的Mixin。

    Provides created_at and updated_at fields that can be included
    in any model that needs timestamp tracking.

    提供created_at和updated_at字段，可用于任何需要时间戳追踪的模型。

    Example:
        >>> from datetime import datetime
        >>> from pydantic import Field
        >>>
        >>> class Article(TimestampMixin):
        ...     title: str
        ...     content: str
        >>>
        >>> article = Article(title="Hello", content="World", created_at=datetime.now())
    """

    created_at: datetime = Field(
        default_factory=datetime.now,
        description="Timestamp when the record was created / 记录创建时间戳",
    )
    updated_at: datetime = Field(
        default_factory=datetime.now,
        description="Timestamp when the record was last updated / 记录最后更新时间戳",
    )

    def touch(self) -> None:
        """Update the updated_at timestamp to current time.

        更新updated_at时间戳为当前时间。
        """
        self.updated_at = datetime.now()
