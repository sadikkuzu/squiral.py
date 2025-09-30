#!/usr/bin/env bash

set -euxo pipefail

python -m pip install --upgrade pip
pip install pip-tools
pip-compile -vU requirements-tool.in
pip install -r requirements-tool.txt
pip-compile -vU
pip-compile -vU requirements-dev.in
pip install -r requirements-dev.txt
pre-commit autoupdate
pre-commit run --all-files --color=always
uv lock --upgrade
