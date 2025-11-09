# Example App

This application demonstrates using `my-package-neerajlalji` with different dependency sources.

## Installation

### Production Mode
Install the package from TestPyPI:
```bash
uv sync --extra prod
```

### Local Development Mode
Install the package from the local directory (editable):
```bash
uv sync --extra local
```

### Development with Testing Tools
Install with dev tools (linters, formatters, type checkers) and test dependencies:

```bash
# Local development with all dev and test tools
uv sync --extra local --group dev --group test

# Or production with dev tools for debugging
uv sync --extra prod --group dev --group test

# Alternatively, you can use --all-groups to include all optional groups:
uv sync --extra local --all-groups
uv sync --extra prod --all-groups
```


### CI/CD (Testing Only)
Install only test dependencies for CI pipeline:
```bash
uv sync --extra prod --group test
```

## Dependency Groups

This project uses separate dependency groups:

- **Core dependencies**: `httpx` - always installed
- **`test` group**: `pytest`, `pytest-cov` - testing and coverage tools
- **`dev` group**: `ruff`, `mypy`, `pip` - linting, type checking, and dev tools
- **`prod` extra**: Uses `my-package-neerajlalji==0.1.1` from TestPyPI
- **`local` extra**: Uses editable package from `../my-package-neerajlalji`

## Usage

Run the application:
```bash
uv run main.py
```

Run tests:
```bash
uv run pytest
```

Run linter:
```bash
uv run ruff check .
```


## Pre-commit Hooks

This project uses pre-commit to automatically run checks before commits.

### Setup pre-commit:
```bash
# Install dev dependencies first
uv sync --extra local --group dev

# Install the git hook scripts
uv run pre-commit install
```

### What pre-commit runs:
- **Basic checks**: trailing whitespace, end-of-file fixer, YAML/TOML validation, large file detection
- **Ruff**: Auto-fixes linting issues and formats code
- **mypy**: Type checking

### Manual runs:
```bash
# Run against all files
uv run pre-commit run --all-files

# Run against staged files only
uv run pre-commit run
```

Once installed, these checks run automatically on `git commit`!

## Notes

- You **must** specify either `--extra prod` or `--extra local` when running `uv sync`
- The two extras are mutually exclusive (cannot be used together)
- Development dependencies (test/dev groups) are optional and not installed by default
- Swapping `extras` doesn't regenerate the lock file [useful]
