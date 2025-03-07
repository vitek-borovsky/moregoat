#!/usr/bin/env sh
cd $(dirname $0)

set -eu

python -m pytest tests/
