# prevcurrnext

Iteration utils for "prev", "curr", and "next"-style for-loops.

## Install

```bash
pip install prevcurrnext
```

## Usage

The `prevcurrnext` function yields pairs of consecutive elements from an iterable, allowing you to see the "previous", "current", and "next" items for each element. It includes options to yield `None` at the beginning and/or end of the sequence for convenient boundary handling.

```python
from prevcurrnext import prevcurr

# Basic usage
for prev, curr in prevcurr([1, 2, 3, 4]):
    print(prev, curr)
# Output:
# None 1
# 1 2
# 2 3
# 3 4

# Customizing boundary behavior
# Adding None at the end
for prev, curr in prevcurr([1, 2, 3, 4], end_next_on_none=True):
    print(prev, curr)
# Output:
# None 1
# 1 2
# 2 3
# 3 4
# 4 None
```

### Parameters

- **`iterable`**: The iterable to process.
- **`start_prev_on_none`** *(optional)*: Whether to yield `None` for the "previous" item before the first element. Default is `True`.
- **`end_next_on_none`** *(optional)*: Whether to yield `None` for the "next" item after the last element. Default is `False`.

## Examples

```python
from prevcurr import prevcurr

# Standard iteration with previous and next items
for prev, curr in prevcurr([10, 20, 30]):
    print(f"Prev: {prev}, Curr: {curr}")

# Start without None for previous
for prev, curr in prevcurr([10, 20, 30], start_prev_on_none=False):
    print(f"Prev: {prev}, Curr: {curr}")

# Add None for next at the end
for prev, curr in prevcurr([10, 20, 30], end_next_on_none=True):
    print(f"Prev: {prev}, Curr: {curr}")
```

## Contributing

Contributions are welcome! If you find issues or have suggestions, please open an issue or submit a pull request on [GitHub](https://github.com/yourusername/prevcurr).

## Development Setup

#### If you use [Poetry](https://python-poetry.org/)

```bash
poetry install
poetry run pytest
```

#### Otherwise...

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .
pytest
```

## License

This project is licensed under the [MIT License](LICENSE).
