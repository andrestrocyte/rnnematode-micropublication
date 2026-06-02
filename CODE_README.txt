RNNematode micropublication code package

Purpose
-------
This code package reproduces the checks used in the micropublication from saved BrainCAD/ReflexBench result artifacts. It does not rerun training.

How to run
----------
1. Open a terminal.
2. Run the lightweight reviewer check:

   cd rnnematode-micropublication
   ./commands_session.sh

Expected output includes:

   RNNematode reproducibility check: OK

This validates the packaged result tables and video index. It does not retrain policies and does not require LaTeX or third-party Python packages.

Optional clean environment:

   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install -r requirements.txt
   ./commands_session.sh

Optional PDF rebuild:

   ./build.sh

If latexmk is installed, build.sh recompiles the micropublication and technical report. If LaTeX is missing, the checked-in PDFs remain usable.

Included notebooks
------------------
- Codes/01_model_equations_and_action_decomposition.ipynb
  Minimal action-composition example for cortex, teacher, and residual.
- Codes/02_reproduce_main_humanoid_results.ipynb
  Replots headline Humanoid fall/return AUC results from saved CSVs.
- Codes/03_reflexbench_video_index.ipynb
  Lists representative saved videos from the packaged index.

Packaged data
-------------
- derived_tables/humanoid20_key_results.csv
- derived_tables/cross_environment_summary_micropublication.csv
- derived_tables/morphology_vs_benefit.csv
- video_index/representative_video_index.csv
- Figures/RNNematode-Figures.svg
