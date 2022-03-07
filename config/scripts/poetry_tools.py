from typing import Any

from .utils import PROJECT_ROOT, run


def poe(cmd: str, **kwargs: Any) -> None:
    """Run poetry command

    Args:
        cmd (str): PDM command from custom scripts or env libs
    """
    run(f"poe {cmd}", check=True, **kwargs)


def poetry_run(cmd: str, **kwargs: Any) -> None:
    """Run poetry command

    Args:
        cmd (str): PDM command from custom scripts or env libs
    """
    run(f"poetry run {cmd}", check=True, **kwargs)


def poetry_setup() -> None:
    """Install packages, configure pre-commit and other presets"""
    run(f"{PROJECT_ROOT}/config/scripts/setup.sh")
