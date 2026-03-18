# SDK Usage Guide

This project uses the standard `src` layout.

## Install Locally

```bash
uv pip install -e .
```

or:

```bash
pip install -e .
```

## Import Pattern

Import from package root, never from `src`.

```python
from python_template.utils import read_json
```

Do **not** write:

```python
from src.python_template.utils import read_json
```

## Why This Works

1. Editable install (`-e`) links the package under `src/`.
2. Pytest config includes:

```toml
[tool.pytest.ini_options]
pythonpath = ["src"]
```

So tests can also import `python_template` directly.

## Path Note

`pythonpath` only affects `import`. It does not change file read/write base path.
Use `pathlib` with explicit roots for robust file paths.
