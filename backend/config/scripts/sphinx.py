"""Sphinx docs configuration helpers."""

from shutil import rmtree
from typing import Dict

from .poetry_tools import poe, poetry_run
from .utils import PROJECT_ROOT, run


def change_conf_path() -> None:
    """Add root absolute path to os.path in `docs/conf.py`.

    TODO:
        Edit the right lines instead of just appending new ones.
    """
    with open(f"{PROJECT_ROOT}/docs/conf.py", "a") as conf:
        conf.write("\n")
        conf.write("\nimport os")
        conf.write("\nimport sys")
        conf.write("\nsys.path.insert(0, os.path.abspath('..'))")
        conf.write("\n")
        conf.write('\nhtml_theme = "sphinx_rtd_theme"')


def docs_setup(project_metadata: Dict[str, str]) -> None:
    """Create /docs folder for Sphinx autodocumentation.

    Args:
        project_name: Name set at `pyproject.toml` metadata
    """
    rmtree("docs", ignore_errors=True)

    extensions = (
        f"sphinx.ext.{ext}"
        for ext in (
            "autodoc",
            "autosectionlabel",
            "todo",
            "viewcode",
            "githubpages",
            "napoleon",
        )
    )

    run(
        " ".join(
            (
                "sphinx-quickstart docs",
                "--no-sep",
                f'--project "{project_metadata["name"]}"',
                '--author "Tukey Data"',
                f'--release {project_metadata["version"]}',
                "--language en",
                f'--extensions {",".join(extensions)}',
                # '-d html_theme="sphinx_rtd_theme"'
            )
        )
    )

    change_conf_path()
    poe("docs")


if __name__ == "__main__":
    rmtree("docs/source", ignore_errors=True)

    poetry_run(
        f"sphinx-apidoc -f -o {PROJECT_ROOT}/docs/source {PROJECT_ROOT} {PROJECT_ROOT}/config"
    )
    run("make html", cwd="docs")
