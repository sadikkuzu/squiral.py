#!/usr/bin/env bash

set -euxo pipefail

uv lock --upgrade
uv sync --group dev
echo "squiral" | uv pip compile --no-deps --no-header --no-annotate - -o squiral.txt
uv run pre-commit autoupdate
uv run pre-commit run --all-files --color=always
