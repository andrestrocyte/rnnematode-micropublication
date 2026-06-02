RNNematode BrainCAD code package

Purpose
-------
This package checks the saved BrainCAD/ReflexBench result artifacts used in the figures and report. It does not rerun training.

Quick run
---------

   ./commands_session.sh

Expected output:

   RNNematode reproducibility check: OK

The quick check uses only the Python standard library. Optional notebook execution uses the packages in requirements.txt.

Optional full PDF rebuild
-------------------------

   ./build.sh

If latexmk is installed, build.sh recompiles the short report and technical report. If LaTeX is missing, the existing PDFs remain usable.

Included notebooks
------------------
- Codes/01_model_equations_and_action_decomposition.ipynb
- Codes/02_reproduce_main_humanoid_results.ipynb
- Codes/03_reflexbench_video_index.ipynb

Packaged data
-------------
- derived_tables/humanoid20_key_results.csv
- derived_tables/cross_environment_summary_micropublication.csv
- derived_tables/morphology_vs_benefit.csv
- video_index/representative_video_index.csv
- Figures/RNNematode-Figures.svg
