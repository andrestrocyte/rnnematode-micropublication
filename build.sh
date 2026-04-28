#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if ! command -v latexmk >/dev/null 2>&1; then
  echo "latexmk is not installed. The prebuilt PDFs are already included."
  exit 0
fi

latexmk -pdf -interaction=nonstopmode RNNematode-Micropublication.tex
(cd report && latexmk -pdf -interaction=nonstopmode RNNematode-TechnicalReport.tex)
