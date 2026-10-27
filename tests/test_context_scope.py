"""Scoped contexts must not drop registrations still in use."""

import asyncio

from python_template.core import context as context_mod
from python_template.core.context import (
    async_context_scope,
    context_scope,
    get_context,
)


def _registered(name: str) -> bool:
    manager = context_mod._context_manager
    return manager is not None and manager.get_context(name) is not None


def test_nested_same_name_scope_keeps_outer_registration() -> None:
    with context_scope("req-nested") as outer:
        with context_scope("req-nested") as inner:
            assert inner is outer
        assert _registered("req-nested")
        assert get_context("req-nested") is outer
    assert not _registered("req-nested")


def test_scope_does_not_delete_preexisting_context() -> None:
    existing = get_context("req-preexisting")
    with context_scope("req-preexisting"):
        pass
    assert get_context("req-preexisting") is existing
    context_mod._context_manager.delete_context("req-preexisting")  # type: ignore[union-attr]


def test_concurrent_async_scopes_keep_registration_until_last_exit() -> None:
    async def run() -> None:
        first_inside = asyncio.Event()
        release_first = asyncio.Event()

        async def first() -> None:
            async with async_context_scope("req-async"):
                first_inside.set()
                await release_first.wait()

        async def second() -> None:
            await first_inside.wait()
            async with async_context_scope("req-async"):
                pass
            assert _registered("req-async")
            release_first.set()

        await asyncio.gather(first(), second())

    asyncio.run(run())
    assert not _registered("req-async")
