
# VID D20 Numerics

Reproducible numerical backend for

> From Feynman Diagrams to Valamontes Interaction Diagrams (VID)

This repository provides:
- Construction of the 20×20 dodecahedral Laplacian Δ₍₂₀₎
- Spectral decomposition and pseudoinverse Δ⁺
- Effective-resistance matrix on the dodecahedral cell
- Three-node toy coherence-gradient example
- A simple ∞-sector convergence study and plot

## Requirements

- Python ≥ 3.9
- `numpy`
- `scipy`
- `networkx`
- `matplotlib`

Install with:

```bash
pip install numpy scipy networkx matplotlib
```

## Usage

From the repository root:

```bash
python -m src.vid_numerics
```

This will:

1. Build the dodecahedral graph and Laplacian Δ₂₀
2. Compute eigenvalues/eigenvectors and the pseudoinverse Δ⁺
3. Compute the effective-resistance matrix
4. Run the 3-node toy example
5. Generate an ∞-sector convergence plot and save it to `figures/infty_convergence.png`

Typical runtimes are ≤ 1.2 seconds on a 2024 laptop (single thread).

## Notebooks

A companion Jupyter notebook is provided in `notebooks/vid_d20_numerics.ipynb`,
mirroring the steps in `src/vid_numerics.py` for interactive exploration.
