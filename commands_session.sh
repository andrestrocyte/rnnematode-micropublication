#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

./build.sh

if command -v jupyter >/dev/null 2>&1; then
  for nb in Codes/*.ipynb; do
    jupyter nbconvert --to notebook --execute --inplace "$nb"
  done
else
  echo "jupyter is not installed; skipping notebook execution."
fi
