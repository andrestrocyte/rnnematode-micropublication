# MyST micropublication submission

This folder contains the Impact Scholars micropublication source.

- Research type: Claim
- Title length: 88 characters
- Keywords: motor control, cerebellum, reinforcement learning, BrainCAD
- Main text word count: 806 words, excluding references and acknowledgments
- License: CC-BY-4.0

Andres de Vicente ORCID is included. Before final form submission, add ORCID IDs for Renee Vieira and Charlie Hou in the submission form or MyST frontmatter if required.

## Reproducing the figure and validation summaries

Run the notebooks in order:

1. `Codes/01_model_equations_and_action_decomposition.ipynb`
2. `Codes/02_reproduce_main_humanoid_results.ipynb`
3. `Codes/03_reflexbench_video_index.ipynb`

The notebooks use relative paths from the submission root and do not retrain policies. They reproduce the submitted figure summaries and summarize validation artifacts from saved BrainCAD/ReflexBench result tables.

Expected packaged artifacts:

- `derived_tables/humanoid20_key_results.csv`
- `video_index/representative_video_index.csv`
