# Continuous Integration for Python Projects

A comprehensive study repository for implementing modern CI/CD pipelines in Python projects using GitHub Actions.

## Project Architecture

```
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions workflow definition
├── src/
│   └── ci_with_python/      # Python package source
│       ├── __init__.py      # Package initialization
│       └── models.py        # Sample module with testable functions
├── tests/                   # Test suite
│   └── test_user.py         # Unit tests
│   └── test_course_class.py # Unit tests
├── pyproject.toml           # Build system configuration
├── setup.cfg                # Package metadata and options
├── setup.py                 # Setuptools compatibility script
├── requirements.txt         # Development dependencies
└── README.md                # Project documentation
```

## Key Configuration Files Deep Dive

1. `pyproject.toml` (PEP 621 Compliant)

```toml
[build-system]
requires = ["setuptools>=42.0", "wheel"]
build-backend = "setuptools.build_meta"
```

2. `setup.py` (Minimal Implementation)

```py
from setuptools import setup

if __name__ == '__main__':
  setup()
```

3. `setup.cfg`

```toml
[metadata]
name = ci_with_python
version = 0.1.0
author = Matheus Alves
description = CI Implementation Example
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/MalvzMK1/ci-with-python
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.8
install_requires =
    requests>=2.25.1

[options.extras_require]
test =
    pytest>=6.2.5
    pytest-cov>=2.12.1
```

## Development Workflow Guide

### Installation

```bash
pip install -e .
```
