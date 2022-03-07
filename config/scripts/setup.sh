#!/bin/bash

set -e # exit immediatly if non-zero status is raised

if ! command -v poetry &> /dev/null
then
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
fi

source ~/.bash_profile

poetry install --no-root

source .venv/bin/activate

poe pre_commit_setup
