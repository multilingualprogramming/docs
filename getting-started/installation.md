---
layout: page
title: "Installation"
description: "Detailed installation instructions for all platforms."
category: "Getting Started"
permalink: /getting-started/installation/
prev_page:
  title: "Getting Started"
  url: /getting-started/
next_page:
  title: "Quick Start"
  url: /getting-started/quick-start/
---

## System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| Python | 3.12+ | 3.12.x or 3.13.x |
| RAM | 256 MB | 512 MB (with WASM) |
| Disk | 50 MB | 150 MB (with WASM) |
| OS | Windows, Linux, macOS | Any |

---

## Installation Options

### Option 1 — Python Only (Minimal)

```bash
pip install multilingualprogramming
```

- Full 17-language support
- Python execution backend
- No WASM acceleration
- ~50 MB install size

### Option 2 — Python + WASM (Recommended)

```bash
pip install multilingualprogramming[wasm]
```

- Full 17-language support
- 50–100x speedup on matrix, crypto, scientific operations
- Automatic fallback to Python if WASM unavailable
- ~150 MB install size
- Requires: `wasmtime` (auto-installed)

### Option 3 — Maximum Performance

```bash
pip install multilingualprogramming[performance]
```

- All WASM features
- NumPy-optimized fallbacks
- Hybrid WASM + NumPy execution
- ~250 MB install size

---

## Platform-Specific Instructions

### Linux

```bash
# Ensure Python 3.12+
python3 --version

# Install
python3 -m pip install multilingualprogramming[wasm]

# Verify
python3 -c "from multilingualprogramming.runtime.backend_selector import BackendSelector; print('OK')"
```

### macOS

```bash
# Install Python 3.12 via Homebrew (optional)
brew install python@3.12

# Install
python3 -m pip install multilingualprogramming[wasm]

# Verify
python3 -c "import multilingualprogramming; print('OK')"
```

### Windows

```powershell
# PowerShell (run as standard user)
python -m pip install multilingualprogramming[wasm]

# Verify
python -c "import multilingualprogramming; print('OK')"
```

> **Note**: If `python` is not found, try `py -3.12` or ensure Python is on your PATH.

---

## Virtual Environments

Using a virtual environment is recommended:

```bash
# Create virtual environment
python -m venv ml-env

# Activate
source ml-env/bin/activate      # Linux/macOS
ml-env\Scripts\activate         # Windows

# Install
pip install multilingualprogramming[wasm]

# Deactivate when done
deactivate
```

With conda:

```bash
conda create -n ml-env python=3.12
conda activate ml-env
pip install multilingualprogramming[wasm]
```

---

## Docker

```dockerfile
FROM python:3.12-slim

WORKDIR /app
RUN pip install multilingualprogramming[wasm]

COPY . .
CMD ["python", "-m", "multilingualprogramming", "repl"]
```

```bash
docker build -t multilingual-app .
docker run -it multilingual-app
```

---

## Build from Source

For development or contribution:

```bash
git clone https://github.com/johnsamuelwrites/multilingual.git
cd multilingual

# Install in development mode with all extras
pip install -e ".[dev,wasm]"

# Run tests
python -m pytest -q

# Run lint
python -m pylint $(git ls-files '*.py')
```

---

## Verify Installation

### Quick check

```bash
python -c "import multilingualprogramming; print('OK')"
python -m multilingualprogramming --version
```

### Full verification

```python
#!/usr/bin/env python3
import sys
import platform
from multilingualprogramming.runtime.backend_selector import BackendSelector

print(f"Python: {sys.version}")
print(f"Platform: {platform.system()} {platform.machine()}")

selector = BackendSelector()
print(f"WASM Available: {selector.is_wasm_available()}")
print(f"Backend: {selector.backend}")
```

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| roman | >=3.3 | Roman numeral support |
| python-dateutil | >=2.8 | Multilingual date/time parsing |
| wasmtime | >=1.0.0 | WASM execution (optional) |
| numpy | any | Optimized numeric fallbacks (optional) |

---

## Uninstalling

```bash
# Remove the package
pip uninstall multilingualprogramming

# Remove WASM support only (keep the package)
pip uninstall wasmtime
```

---

## Troubleshooting

### `ModuleNotFoundError: No module named 'multilingualprogramming'`

Ensure you installed for the correct Python version:

```bash
which python && python --version
pip install multilingualprogramming
```

### WASM not available on macOS ARM64

WASM runs via emulation on Apple Silicon. Use Python fallback:

```python
from multilingualprogramming.runtime.backend_selector import BackendSelector, Backend
selector = BackendSelector(prefer_backend=Backend.PYTHON)
```

### Windows `ImportError`

Install Visual C++ Redistributables from Microsoft, or:

```bash
pip install --upgrade wasmtime
```

### Python version too old

```
ERROR: Requires Python >= 3.12
```

Upgrade Python to 3.12+, then reinstall.
