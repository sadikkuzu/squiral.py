#!/usr/bin/env bash

set -euxo pipefail

uv lock --upgrade
uv sync --group dev
uv run pre-commit autoupdate
uv run pre-commit run --all-files --color=always
