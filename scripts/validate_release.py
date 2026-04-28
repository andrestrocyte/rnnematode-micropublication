#!/usr/bin/env python3
from pathlib import Path
import re, sys
root = Path(__file__).resolve().parents[1]
required = [
    'RNNematode-Micropublication.pdf',
    'report/RNNematode-TechnicalReport.pdf',
    'myst_submission/index.md',
    'ISP_RNNematode_CRediT_contributors.csv',
    'RNNematode_micropublication_code.zip',
]
missing = [p for p in required if not (root / p).exists()]
if missing:
    raise SystemExit('Missing required files: ' + ', '.join(missing))
bad_terms = ['chat' + 'gpt', 'co' + 'dex', 'ai ' + 'generated', 'as an ' + 'ai', 'language ' + 'model', '/Users/deviandr/' + 'ncap_project']
pattern = re.compile('|'.join(re.escape(t) for t in bad_terms), re.I)
hits = []
for path in root.rglob('*'):
    if path.is_file() and path.suffix.lower() in {'.md', '.tex', '.csv', '.json', '.yml', '.txt', '.py', '.ipynb', '.cff'}:
        text = path.read_text(errors='ignore')
        if pattern.search(text):
            hits.append(str(path.relative_to(root)))
if hits:
    raise SystemExit('Found local or unwanted markers in: ' + ', '.join(hits[:20]))
print('Release validation passed.')
