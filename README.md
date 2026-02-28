# PHYS 258 — Damped and Driven Torsional Oscillator

This repository contains raw data, analysis code (Python + Jupyter), a lab logbook (PDF), the LaTeX report source, the compiled report PDF, and generated figures for a damped and driven torsional oscillator lab.

## Structure
- `data/raw/` — raw measurement files (not modified)
- `src/` — reusable analysis code (labtools module)
- `notebooks/` — exploration + analysis notebooks
- `results/figures/` — generated plots
- `results/tables/` — extracted tables / summaries
- `report/` — compiled report PDF + LaTeX source in `report/src/`

## Reproducibility
1. Create an environment (see `requirements.txt` or `environment.yml`).
2. Run the analysis notebook(s) in `notebooks/` (and/or scripts in `scripts/`) to regenerate figures and tables.

## Note on AI assistance
Portions of the code were written with AI assistance for scaffolding and refactoring; all outputs were reviewed, tested, and adapted as needed by me.