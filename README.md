# Valamontes Interaction Diagrams (VID) — Reproducibility Package

This repository contains all components required to reproduce the numerical results associated with the VID framework, including:

- Construction of the 20×20 DLSFH Laplacian  
- Moore–Penrose pseudoinverse computation  
- Three-node VID example  
- Default parameters used in figures  
- Reproducibility notes and environment instructions  

---

## 1. Conda / Python Environment

Create and activate the environment:

    conda create -n vid python=3.10
    conda activate vid
    pip install -r requirements.txt

Exact package versions may be pinned (example set):

    numpy==1.25.0
    scipy==1.11.0
    matplotlib==3.8.0
    networkx==3.1
    tqdm==4.66.1
    papermill==2.4.0

Alternatively, use:

    conda env create -f environment.yml
    conda activate vid

---

## 2. Reproduction Commands (Three-Node Example)

### Build the DLSFH Laplacian

    python scripts/build_DLSFH.py --N=20 --out=Delta20.npy

### Compute the pseudoinverse

    python scripts/compute_pseudoinverse.py --in Delta20.npy --out Delta20_pinv.npy

### Run the three-node VID example

    python notebooks/three_node_example.ipynb

(Or execute non-interactively using papermill.)

---

## 3. Default Parameters Used in Figures

- Coherence parameters  
- Infinity-sector truncation `N`  
- Convergence tolerance `ε`  
- Random seed for reproducibility  

All exact values appear inside notebooks and scripts.

---

## 4. Reproducibility Runtimes

Typical runtimes on an 8-core CPU:

- DLSFH Laplacian construction: < 0.05 s  
- Pseudoinverse computation: 0.2–0.4 s  
- Three-node example: 0.3–0.5 s  
- Infinity-sector convergence: ≤ 1.2 s  

---

## 5. License

- Code: **MIT License**  
- Notebooks: **CC-BY 4.0**  

---

## 6. Precomputed Data and Figures (Zenodo DOI)

Precomputed numerical data and figures are available at:

    Zenodo DOI: (insert DOI here)

Includes:

- `Delta20.npy`  
- `Delta20_pinv.npy`  
- All figure data  
- Default parameter files  

---

## 7. Repository Structure

    scripts/
        build_DLSFH.py
        compute_pseudoinverse.py
        utils.py

    notebooks/
        three_node_example.ipynb
        infinity_sector_convergence.ipynb
        coherence_flow_demo.ipynb

    data/
        Delta20.npy
        Delta20_pinv.npy
        parameters.json

    requirements.txt
    environment.yml
    README.md

---

## 8. Citation

If you use this code or its numerical outputs, please cite:

**Valamontes, A. (2025). From Feynman Diagrams to Valamontes Interaction Diagrams (VID).**

