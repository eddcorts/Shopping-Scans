"""Tools for generating `pyproject.toml` file"""
import re
import sys
from typing import Any, Dict, MutableMapping

import toml
from toml.encoder import TomlPreserveInlineDictEncoder  # type: ignore

from .utils import PROJECT_ROOT


def retrieve_toml() -> MutableMapping[str, Any]:
    """Read preset toml file

    Returns:
        Dict containing parsed preset toml file
    """
    return toml.load(f"{PROJECT_ROOT}/config/pyproject_presets.toml")


def write_toml(data: MutableMapping[str, Any]) -> None:
    """Dump dict into toml file

    Args:
        data: Dict containing toml data
    """
    with open(f"{PROJECT_ROOT}/pyproject.toml", "w+") as file:
        toml.dump(data, file, TomlPreserveInlineDictEncoder())  # type: ignore


def root_name() -> str:
    """Retrieve project root's folder name

    Returns:
        Project folder name
    """
    return re.sub(r"-", " ", str(PROJECT_ROOT).split("/")[-1].title())


def pyproject_setup(python_version: float) -> Dict[str, str]:
    """Retrieve project data and compiles preset into `pyproject.toml`

    Args:
        python_version: Version of current running Python interpreter

    Return:
        Project metadata
    """
    print(f"Using Python ${python_version} environment for pdm (from {sys.executable})")
    default_name = root_name()

    print("-----------------------")
    project_data = {
        "name": input(f"The project name [default: '{default_name}']: ")
        or default_name,
        "description": input("Project description: "),
        "version": "0.0.1",
    }
    print("-----------------------")

    presets = retrieve_toml()
    presets["project"].update(project_data)

    write_toml(presets)

    return project_data
