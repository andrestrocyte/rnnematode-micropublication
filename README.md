# RNNematode BrainCAD reproducibility package

This repository contains the runnable scientific package for the RNNematode BrainCAD locomotion project. The project tests whether biologically inspired corrective modules improve recovery from perturbations in simulated locomotion. The main empirical result is that PPO-only corrective modules did not reliably learn fast recovery, while a teacher-guided cerebellar residual did.

## Main claim

In BrainCAD/ReflexBench, the corrective learning signal mattered more than the anatomical label of the module. A cerebellar-style residual became useful when trained to imitate a perturbation-trained teacher's correction; the same residual could then be switched on/off causally and distilled into cortex-only execution.

## Run the packaged check

This command validates the saved result tables, figure inputs, and video index. It does not retrain policies and does not require LaTeX, Jupyter, pandas, or matplotlib.

```bash
git clone https://github.com/andrestrocyte/rnnematode-micropublication.git
cd rnnematode-micropublication
./commands_session.sh
```

Expected output:

```text
RNNematode reproducibility check: OK
```

For a clean environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
./commands_session.sh
```

## Optional PDF rebuild

The PDFs are already included. To recompile them if `latexmk` is available:

```bash
./build.sh
```

If LaTeX is missing, `build.sh` still runs the artifact check and leaves the checked-in PDFs unchanged.

## Scientific artifacts

- `RNNematode-Micropublication.pdf`: short result summary.
- `report/RNNematode-TechnicalReport.pdf`: equations, controls, and extended tables.
- `Figures/RNNematode-Figures.svg`: main figure sheet.
- `Figures/RNNematode-Supplementary-Figures.svg`: supplementary checks.
- `derived_tables/`: CSV summaries used by the figures and report.
- `Codes/`: small notebooks for the model equations, headline results, and video index.
- `video_index/representative_video_index.csv`: representative-video metadata.
- `scripts/check_reproducibility.py`: dependency-light artifact validator.

## What is not included

This repository does not include heavy training checkpoints or rerun the full PPO experiments. It is a compact release with saved result tables and validation code. The notebooks and scripts are intended to check the submitted scientific outputs, not to regenerate every trained policy from scratch.

## License

The executable code is released under the MIT License. The scientific PDFs, figures, and tables are included for review and reproducibility of the reported result.
