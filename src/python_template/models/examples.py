"""Example Pydantic models for common use cases.

提供常见用例的Pydantic模型示例。

This module contains example models that demonstrate best practices
for using Pydantic in various scenarios.
"""

from typing import Any, Generic, List, Optional, TypeVar

from pydantic import Field, field_validator

from .base import BaseModel, TimestampMixin

T = TypeVar("T")


class User(TimestampMixin):
    """User model with validation.

    用户模型，包含验证。

    Example:
        >>> user = User(
        ...     id=1,
        ...     username="john_doe",
        ...     email="john@example.com",
        ...     full_name="John Doe",
        ... )
        >>> print(user.username)
        john_doe
        >>> print(user.is_active)
        True
    """

    id: int = Field(..., description="User ID / 用户ID", ge=1)
    username: str = Field(
        ...,
        description="Username / 用户名",
        min_length=3,
        max_length=50,
        pattern=r"^[a-zA-Z0-9_]+$",
    )
    email: str = Field(
        ...,
        description="Email address / 邮箱地址",
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    )
    full_name: Optional[str] = Field(
        None, description="Full name / 全名", max_length=100
    )
    is_active: bool = Field(
        default=True, description="Whether user is active / 用户是否激活"
    )

    @field_validator("username")
    @classmethod
    def username_alphanumeric(cls, v: str) -> str:
        """Validate that username contains only alphanumeric characters and underscores.

        验证用户名仅包含字母数字和下划线。
        """
        if not v.replace("_", "").isalnum():
            raise ValueError("Username must be alphanumeric (with underscores allowed)")
        return v


class ApiResponse(BaseModel, Generic[T]):
    """Generic API response model.

    通用API响应模型。

    Example:
        >>> response = ApiResponse(
        ...     success=True, message="Operation completed", data={"result": 42}
        ... )
        >>> print(response.success)
        True
        >>> print(response.data)
        {'result': 42}
    """

    success: bool = Field(
        ..., description="Whether the operation succeeded / 操作是否成功"
    )
    message: str = Field(
        default="", description="Response message / 响应消息", max_length=500
    )
    data: Optional[T] = Field(None, description="Response data / 响应数据")
    error_code: Optional[str] = Field(
        None, description="Error code if failed / 失败时的错误代码"
    )


class PaginatedResponse(BaseModel, Generic[T]):
    """Paginated response model.

    分页响应模型。

    Example:
        >>> response = PaginatedResponse(
        ...     items=[1, 2, 3], total=100, page=1, page_size=10
        ... )
        >>> print(response.total_pages)
        10
        >>> print(response.has_next)
        True
    """

    items: List[T] = Field(default_factory=list, description="List of items / 项目列表")
    total: int = Field(..., description="Total number of items / 项目总数", ge=0)
    page: int = Field(..., description="Current page number / 当前页码", ge=1)
    page_size: int = Field(
        ..., description="Number of items per page / 每页项目数", ge=1, le=100
    )

    @property
    def total_pages(self) -> int:
        """Calculate total number of pages.

        计算总页数。
        """
        return (self.total + self.page_size - 1) // self.page_size

    @property
    def has_next(self) -> bool:
        """Check if there is a next page.

        检查是否有下一页。
        """
        return self.page < self.total_pages

    @property
    def has_prev(self) -> bool:
        """Check if there is a previous page.

        检查是否有上一页。
        """
        return self.page > 1


class ConfigModel(BaseModel):
    """Example configuration model.

    配置模型示例。

    Demonstrates how to use Pydantic for application configuration
    with validation and type safety.

    演示如何使用Pydantic进行应用配置，包含验证和类型安全。

    Example:
        >>> config = ConfigModel(app_name="MyApp", debug=True, max_connections=50)
        >>> print(config.app_name)
        MyApp
        >>> config.max_connections = 150  # Will raise validation error
        Traceback (most recent call last):
            ...
        ValidationError: ...
    """

    app_name: str = Field(
        default="python-template",
        description="Application name / 应用名称",
        min_length=1,
        max_length=100,
    )
    debug: bool = Field(default=False, description="Debug mode / 调试模式")
    max_connections: int = Field(
        default=10,
        description="Maximum number of connections / 最大连接数",
        ge=1,
        le=100,
    )
    timeout: float = Field(
        default=30.0,
        description="Request timeout in seconds / 请求超时（秒）",
        gt=0,
        le=300,
    )
    allowed_hosts: List[str] = Field(
        default_factory=lambda: ["localhost", "127.0.0.1"],
        description="List of allowed hosts / 允许的主机列表",
    )
    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata / 额外的元数据"
    )

    @field_validator("app_name")
    @classmethod
    def validate_app_name(cls, v: str) -> str:
        """Validate application name format.

        验证应用名称格式。
        """
        if not v.replace("-", "").replace("_", "").isalnum():
            raise ValueError(
                "App name must contain only alphanumeric characters, hyphens, and underscores"
            )
        return v
