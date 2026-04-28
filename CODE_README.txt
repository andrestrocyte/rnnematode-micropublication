RNNematode micropublication code package

Purpose
-------
This code package reproduces the figures and tables used in the micropublication from saved BrainCAD/ReflexBench result artifacts. It does not rerun training.

How to run
----------
1. Open a terminal.
2. Run:

   cd rnnematode-micropublication
   ./commands_session.sh

Included notebooks
------------------
- Codes/01_model_equations_and_action_decomposition.ipynb
  Minimal action-composition example for cortex, teacher, and residual.
- Codes/02_reproduce_main_humanoid_results.ipynb
  Replots headline Humanoid fall/return AUC results from saved CSVs.
- Codes/03_reflexbench_video_index.ipynb
  Lists representative saved videos.

Data access
-----------
The notebooks read saved result artifacts already present in the repository:
- paper/experiments/sc_ncap/results/humanoid_teacher_guided_20seed_campaign/20260421_rerun/analysis/
- paper/neurips_2026/tables/
- paper/experiments/sc_ncap/results/*_perturbation_sanity_summary.json
- paper/experiments/sc_ncap/results/representative_videos/

No proprietary software is required. The package uses Python, pandas, numpy, matplotlib, nbformat, openpyxl, and LaTeX for local rebuilding.
