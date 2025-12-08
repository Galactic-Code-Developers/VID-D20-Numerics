# Valamontes Interaction Diagrams (VID) — Reproducibility Package

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Zenodo](https://zenodo.org/badge/doi/10.5281/zenodo.17850442.svg)](https://doi.org/10.5281/zenodo.17850442)

This repository contains all components required to reproduce the numerical results associated with the **Valamontes Interaction Diagrams (VID)** framework, including:

- Construction of the 20×20 DLSFH Laplacian  
- Moore–Penrose pseudoinverse computation  
- Three-node VID example  
- ∞-sector convergence demonstrations  
- α-dependent ∞-sector convergence comparison  
- Fully reproducible environment and archived datasets  

---

## 1. Conda / Python Environment

Create and activate the environment:

```bash
conda create -n vid python=3.10
conda activate vid
pip install -r requirements.txt
```

Alternatively:

```bash
conda env create -f environment.yml
conda activate vid
```

---

## 2. Install the VID Numerics Package

Install locally:

```bash
pip install -e .
```

Use in Python:

```python
from vid_numerics import build_dlsfh_laplacian, compute_pseudoinverse
```

---

## 3. Reproduction Commands (Three-Node Example)

### Build the DLSFH Laplacian
```bash
python scripts/build_DLSFH.py --N=20 --out=Delta20.npy
```

### Compute the pseudoinverse
```bash
python scripts/compute_pseudoinverse.py --in Delta20.npy --out=Delta20_pinv.npy
```

### Run the three-node VID notebook
```bash
jupyter notebook notebooks/three_node_example.ipynb
```

(Or execute via `papermill`.)

---

## 4. Default Parameters Used in Figures

- Coherence parameters  
- Infinity-sector truncation `N`  
- Convergence tolerance `ε`  
- Random seed for reproducibility  

All exact values appear inside notebooks and scripts.

---

## 5. Reproducibility Runtimes

Typical runtimes on an 8-core CPU:

- Laplacian construction: < 0.05 s  
- Pseudoinverse computation: 0.2–0.4 s  
- Three-node example: 0.3–0.5 s  
- Infinity-sector convergence: ≤ 1.2 s  

---

## 6. Precomputed Data and Figures (Zenodo DOI)

All numerical datasets and figure outputs are available at:

**https://doi.org/10.5281/zenodo.17850442**

Includes:

- `Delta20.npy`  
- `Delta20_pinv.npy`  
- All figure data used in the VID paper  
- Default parameter files  

---

## 7. Notebooks

See detailed descriptions in:  
[`notebooks/README.md`](notebooks/README.md)

Available notebooks:

- `three_node_example.ipynb`  
- `infinity_sector_convergence.ipynb`  
- `infinity_alpha_comparison.ipynb`  

---

## 8. Repository Structure

```
scripts/
    build_DLSFH.py
    compute_pseudoinverse.py
    utils.py

notebooks/
    three_node_example.ipynb
    infinity_sector_convergence.ipynb
    infinity_alpha_comparison.ipynb
    README.md

data/
    Delta20.npy
    Delta20_pinv.npy
    parameters.json

vid_numerics/
    __init__.py
    laplacian.py
    pseudoinverse.py

tests/
    test_laplacian.py

requirements.txt
environment.yml
LICENSE
pyproject.toml
README.md
```

---

## 9. Running the Test Suite

```bash
pytest tests/
```

---

## 10. Citation

If you use this code or its numerical outputs, please cite:

**Valamontes, A. (2025). _From Feynman Diagrams to Valamontes Interaction Diagrams (VID)._**
