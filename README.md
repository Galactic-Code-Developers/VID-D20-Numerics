# Valamontes Interaction Diagrams (VID) — Reproducibility Package

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Zenodo](https://zenodo.org/badge/doi/10.5281/zenodo.17850442.svg)](https://doi.org/10.5281/zenodo.17850442)

Python 3.10+

License: MIT

Zenodo DOI: https://doi.org/10.5281/zenodo.17850442


---


## Overview


This repository contains all components required to reproduce the numerical results associated with the Valamontes Interaction Diagrams (VID) framework, including:


- Construction of the 20×20 DLSFH Laplacian

- Moore–Penrose pseudoinverse computation

- Three-node VID example

- Infinity-sector convergence demonstrations

- Alpha-dependent infinity-sector convergence comparison

- Fully reproducible environment and archived datasets


---


## Quick Start (Three-Node Example)


### 1. Conda / Python Environment


conda create -n vid python=3.10

conda activate vid

pip install -r requirements.txt


Alternatively (exact reproducibility):


conda env create -f environment.yml

conda activate vid


---


### 2. Install the VID Numerics Package


pip install -e .


Python usage:


from vid_numerics import build_dlsfh_laplacian, compute_pseudoinverse


---


### 3. Reproduction Commands


python scripts/build_DLSFH.py --N=20 --out=Delta20.npy

python scripts/compute_pseudoinverse.py --in Delta20.npy --out=Delta20_pinv.npy

jupyter notebook notebooks/three_node_example.ipynb


Papermill execution:


papermill notebooks/three_node_example.ipynb out.ipynb

-p coherence 0.30

-p truncation_N 50

-p eps_inf 1e-6


---


## Default Parameters


- Coherence parameter: 0.30

- Infinity-sector truncation: N = 50

- Convergence tolerance: eps_inf = 1e-6

- Spectral cutoff: 0.01

- Random seed: 42


---


## Reproducibility Runtimes


- Laplacian construction: < 0.05 s

- Pseudoinverse computation: 0.2–0.4 s

- Three-node example: 0.3–0.5 s

- Infinity-sector convergence: ≤ 1.2 s


---


## Zenodo Archives


Numerical data and figures:

https://doi.org/10.5281/zenodo.17850442


Software archive:

https://zenodo.org/records/17859720


---


## Repository Structure


scripts/, notebooks/, data/, vid_numerics/, tests/, requirements.txt, environment.yml, LICENSE, pyproject.toml


---


## Tests


pytest tests/


---


## Citation


Valamontes, A. (2025). *From Feynman Diagrams to Valamontes Interaction Diagrams (VID).*

Zenodo DOI: https://doi.org/10.5281/zenodo.17850442


