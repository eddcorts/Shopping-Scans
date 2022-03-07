"""Checks Python version, installs pdm if it doesn't exist and run setup

Raises:
    LookupError: Python version is lower than the required
"""


if __name__ == "__main__":
    import sys

    from .poetry_tools import poetry_setup

    # from .sphinx import docs_setup
    # from .toml_tools import pyproject_setup

    major, minor, *_ = sys.version_info

    PYTHON_VERSION = float(f"{major}.{minor}")
    REQUIRED_PY_VER = 3.8

    if PYTHON_VERSION < REQUIRED_PY_VER:
        raise LookupError(f"Upgrade your Python version to any >= {REQUIRED_PY_VER}!")

    poetry_setup()
    # docs_setup()
