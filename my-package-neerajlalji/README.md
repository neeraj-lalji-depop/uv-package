# my-package-neerajlalji

A Python package for demonstration purposes.

## Publishing to TestPyPI

### 1. Set up your API token

Read your TestPyPI API token securely:
```bash
read -s API_TOKEN
```

Export it for uv to use:
```bash
export UV_PUBLISH_TOKEN=$API_TOKEN
```

### 2. Build and publish

Whenever you want to push a new version:

```bash
uv build
uv publish --publish-url https://test.pypi.org/legacy/ dist/*
```

This will:
1. Build the distribution packages (wheel and source distribution)
2. Publish them to TestPyPI
