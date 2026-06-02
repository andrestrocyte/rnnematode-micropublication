# RNNematode micropublication package

This repository contains the Neuromatch Impact Scholars micropublication package for Team RNNematode. The project asks a narrow question: when a simulated locomotor controller is perturbed, does a biologically inspired corrective module help by itself, or does it need a structured teacher signal? In our BrainCAD/ReflexBench experiments, PPO-only corrective circuits did not reliably learn fast recovery, while a teacher-guided cerebellar residual did.

Public repository: https://github.com/andrestrocyte/rnnematode-micropublication

## Main claim

Teacher-guided corrective residuals support reflex-like recovery in simulated locomotion. The result is not presented as a new distillation algorithm or as biological proof. The main point is simpler: in this BrainCAD setting, the learning signal mattered more than the anatomical label of the module.

## Quick reproducibility check

This is the recommended reviewer command. It validates the packaged CSV tables, figure inputs, and video index without retraining policies and without requiring LaTeX:

```bash
cd path/to/rnnematode-micropublication
./commands_session.sh
```

Expected success message:

```text
RNNematode reproducibility check: OK
```

For a clean Python environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
./commands_session.sh
```

## Optional PDF rebuild

```bash
./build.sh
```

`build.sh` first runs the same lightweight artifact check. If `latexmk` is installed, it also recompiles the micropublication and technical-report PDFs. If LaTeX is missing, the checked-in PDFs remain usable.

## Read first

- `RNNematode-Micropublication.pdf`: compact micropublication.
- `myst_submission/index.md`: MyST source for the micropublication.
- `report/RNNematode-TechnicalReport.pdf`: longer report with equations, controls, and extra tables.
- `Figures/RNNematode-Figures.svg`: main figure sheet in SVG.
- `Figures/RNNematode-Supplementary-Figures.svg`: supplementary figure sheet in SVG.

## Reproducing figures and validation summaries

The notebooks in `Codes/` use saved result artifacts included in this repository. They are short checks, not a full training pipeline:

- `Codes/01_model_equations_and_action_decomposition.ipynb`: minimal cortex/teacher/residual equations.
- `Codes/02_reproduce_main_humanoid_results.ipynb`: reproduces headline Humanoid AUC summaries from `derived_tables/humanoid20_key_results.csv`.
- `Codes/03_reflexbench_video_index.ipynb`: summarizes the representative-video index in `video_index/representative_video_index.csv`.

## Videos

The lightweight public package includes video indices rather than all MP4 files. The index records environment, method, perturbation tier, and relative video path for representative runs. The videos are qualitative validation artifacts; the main evidence is the paired ON/OFF AUC analysis in the paper.

## Repository layout

- `myst_submission/`: MyST Markdown source for submission.
- `report/`: technical report source and PDF.
- `Figures/`: SVG/PDF/PNG figure exports.
- `derived_tables/`: CSV summaries used by figures and reports.
- `tables/`: LaTeX table fragments.
- `Codes/`: documented notebooks.
- `video_index/`: representative video index.
- `scripts/`: lightweight release validation.
- `RNNematode_micropublication_code.zip`: submission-ready code archive.

## Authorship and citation

Equal-contributing scholars: Andrés de Vicente, Renee Vieira, and Charlie Hou. Andrés ORCID: https://orcid.org/0000-0003-4995-4473. Raymond Chua is acknowledged as senior mentor.

Author roles are listed in `ISP_RNNematode_CRediT_contributors.csv`. Citation metadata is in `CITATION.cff` in the public repository.

## Licenses

Code is released under the MIT License. Text and figures are released under CC BY 4.0 in the public repository.
