# VID Numerics — Notebook Guide

This directory contains the Jupyter notebooks used to reproduce the numerical
experiments for **Valamontes Interaction Diagrams (VID)**. Each notebook focuses
on a specific component of the VID numerical framework: Laplacian geometry,
nonperturbative amplitudes, and ∞-sector convergence behavior.

The notebooks are intended to be runnable in sequence, but each can also be used
independently.

---

## 1. `three_node_example.ipynb`

**Purpose:**  
Demonstrates the minimal three-node VID computation using the DLSFH Laplacian
(`Delta20.npy`) and its Moore–Penrose pseudoinverse (`Delta20_pinv.npy`).

**What it shows:**

- How to load the Laplacian and pseudoinverse  
- How to extract a 3-node subsystem  
- Computation of effective resistance:  
  $ R_{ij} = L^+_{ii} + L^+_{jj} - 2 L^+_{ij} $  
- Heatmap visualization of the 3×3 resistance (proxy for a local VID amplitude)

**Dependencies:**  
`numpy`, `matplotlib`

---

## 2. `infinity_sector_convergence.ipynb`

**Purpose:**  
Illustrates the **∞-sector convergence** using a finite-dimensional toy operator  
$ K = \alpha L^+ / \|L^+\|_2 $.

**Features:**

- Constructs partial sums $ S_N = \sum_{n=0}^{N} K^n $  
- Treats $ S_{N_{\max}} $ as the “∞-sector” reference solution  
- Computes two error metrics:  
  - Operator 2-norm $ \|S_N - S_{N_{\max}}\|_2 $  
  - Frobenius norm $ \|S_N - S_{N_{\max}}\|_F $  
- Produces log-scale convergence plots  
- Demonstrates how VID-style operator towers converge to stable nonperturbative objects

**Dependencies:**  
`numpy`, `matplotlib`

---

## 3. `infinity_alpha_comparison.ipynb`

**Purpose:**  
Shows how ∞-sector convergence depends on the **spectral radius** of the operator.

Uses the rescaled operator:

\[
K_\alpha = \alpha \frac{L^+}{\|L^+\|_2}, \qquad \alpha \in (0,1)
\]

**What it compares:**

- Error curves for α = **0.3, 0.5, 0.7, 0.9**
- Demonstrates:
  - Fast convergence when α is small  
  - Slower convergence as α → 1  
- Plots all curves on the same log-axis for direct comparison

**Dependencies:**  
`numpy`, `matplotlib`

---

## Running the Notebooks

From the repository root:

```bash
jupyter notebook notebooks/<notebook_name>.ipynb
