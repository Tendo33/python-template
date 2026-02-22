"""Core tests for JSON utility helpers."""

import json
from pathlib import Path

from python_template.utils.json_utils import (
    read_json,
    safe_json_dumps,
    safe_json_loads,
    write_json,
)


def test_write_and_read_json_roundtrip(tmp_path: Path) -> None:
    target = tmp_path / "payload" / "data.json"
    payload = {"name": "template", "count": 2}

    ok = write_json(payload, target)
    loaded = read_json(target)

    assert ok is True
    assert loaded == payload


def test_read_json_returns_default_for_invalid_file(tmp_path: Path) -> None:
    target = tmp_path / "bad.json"
    target.write_text("{invalid}", encoding="utf-8")

    fallback = {"status": "invalid"}
    loaded = read_json(target, default=fallback)

    assert loaded == fallback


def test_safe_json_loads_returns_default_for_bad_input() -> None:
    fallback = {"ok": False}
    loaded = safe_json_loads("{bad", default=fallback)
    assert loaded == fallback


def test_safe_json_dumps_returns_fallback_for_unserializable_value() -> None:
    class Unserializable:
        pass

    dumped = safe_json_dumps(Unserializable(), fallback="fallback")
    assert dumped == "fallback"


def test_safe_json_dumps_can_serialize_with_custom_default() -> None:
    class Payload:
        def __init__(self, value: str) -> None:
            self.value = value

    dumped = safe_json_dumps(
        Payload("ok"),
        default=lambda obj: {"value": obj.value},
        indent=None,
    )

    assert dumped is not None
    assert json.loads(dumped) == {"value": "ok"}
