# RNNematode micropublication

This repository contains the public micropublication package for Team RNNematode from the Neuromatch Impact Scholars Program. The project asks a narrow question: when a locomotor controller is perturbed, does a biologically inspired corrective module help by itself, or does it need a structured teacher signal? In our BrainCAD/ReflexBench experiments, PPO-only corrective circuits did not reliably learn fast recovery, while a teacher-guided cerebellar residual did.

Public repository: https://github.com/andrestrocyte/rnnematode-micropublication

## Main claim

Teacher-guided corrective residuals support reflex-like recovery in simulated locomotion. The result is not presented as a new distillation algorithm or a biological proof. The main point is simpler: in this BrainCAD setting, the learning signal mattered more than the anatomical label of the module.

## Read first

- `RNNematode-Micropublication.pdf` is the short micropublication.
- `myst_submission/index.md` is the MyST Markdown source for submission.
- `report/RNNematode-TechnicalReport.pdf` gives the longer technical report with equations, controls, and extra tables.
- `Figures/RNNematode-Figures.svg` and `Figures/RNNematode-Supplementary-Figures.svg` are the submitted figure sheets.

## Build the package

The generated PDFs are already included. To rebuild them locally:

```bash
./build.sh
```

This requires a working LaTeX installation with `latexmk`. The build compiles the existing sources; it does not rerun training.

## Reproduce the lightweight figure checks

```bash
./commands_session.sh
```

The notebooks in `Codes/` use the saved CSV tables included in this repository. They are intended as brief, readable checks rather than a full training pipeline.

## Videos

Representative MP4s are stored under `videos/`. The index files list environment, method, perturbation tier, and relative video path. The main comparison to inspect is:

- `baseline_off`: nominal cortex-only baseline.
- `imitation_off`: same student checkpoint with the residual disabled.
- `imitation_on`: teacher-guided residual enabled.
- `consolidated_off`: cortex-only policy after supervised consolidation.

The videos are qualitative evidence that the perturbations and policy differences are visible, not a replacement for the AUC statistics in the paper.

## Repository layout

- `myst_submission/`: MyST Markdown source for the micropublication.
- `report/`: longer technical report.
- `Figures/`: SVG, PDF, and PNG figure exports.
- `derived_tables/`: CSV summaries used by the figures and report.
- `tables/`: LaTeX table fragments.
- `Codes/`: small documented notebooks.
- `videos/`: representative MP4s and video indices.
- `scripts/`: release validation and packaging helpers.

## Authorship and citation

Equal-contributing scholars: Andrés de Vicente, Renee Vieira, and Charlie Hou. Andrés ORCID: https://orcid.org/0000-0003-4995-4473. Raymond Chua is acknowledged as senior mentor.

Author roles are listed in `ISP_RNNematode_CRediT_contributors.csv`. Citation metadata is in `CITATION.cff`.

## Licenses

Code is released under the MIT License. Text and figures are released under CC BY 4.0; see `LICENSE-CC-BY-4.0.md`.
