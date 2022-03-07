"""Command utils for general project setup-scripts"""

import os
import subprocess as subp
from pathlib import Path
from typing import Any

PROJECT_ROOT = os.getenv("PDM_PROJECT_ROOT") or Path().absolute()


def run(cmd: str, **kwargs: Any) -> None:
    """Run command with shell string command by default

    Args:
        cmd (str): Shell command string
    """
    subp.run(cmd, shell=True, **kwargs)
