#!/usr/bin/env python3
from pathlib import Path
import zipfile
root = Path(__file__).resolve().parents[1]
zip_path = root / 'RNNematode_micropublication_code.zip'
include_dirs = ['Codes', 'derived_tables', 'tables', 'Figures', 'myst_submission', 'scripts']
include_files = ['README.md', 'CODE_README.txt', 'commands_session.sh', 'build.sh', 'references.bib', 'VALIDATION.md', 'SUBMISSION_CHECKLIST.md', 'RNNematode-Contributions.csv', 'ISP_RNNematode_CRediT_contributors.csv', 'CITATION.cff', 'LICENSE', 'LICENSE-CC-BY-4.0.md']
if zip_path.exists():
    zip_path.unlink()
with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
    for d in include_dirs:
        base = root / d
        if base.exists():
            for path in base.rglob('*'):
                if path.is_file():
                    zf.write(path, path.relative_to(root))
    for f in include_files:
        path = root / f
        if path.exists():
            zf.write(path, path.relative_to(root))
print(zip_path)
