# Example App

This application demonstrates using `my-package-neerajlalji` with different dependency sources.

## Installation

You must use one of the following commands to sync dependencies:

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

## Notes

- You **must** specify either `--extra prod` or `--extra local` when running `uv sync`
- The two extras are mutually exclusive (cannot be used together)
- `prod` uses version 0.1.1 from TestPyPI
- `local` uses the editable package from `../my-package-neerajlalji`
- Swapping `extras` doesn't regenerate the lock file [useful]
