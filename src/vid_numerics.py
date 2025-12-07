#!/usr/bin/env python3
# vid_numerics.py
# Exact numerical backend for "Diagrammatic Quantum Geometry Beyond Feynman Diagrams"
# Produces all figures used in the paper + Zenodo archive
# DOI 10.5281/zenodo.14915950

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh

# ------------------------------------------------------------------
# Settings — make plots look exactly like the paper
# ------------------------------------------------------------------
mpl.rcParams['axes.autolimit_mode'] = 'round_numbers'
mpl.rcParams['axes.xmargin'] = 0.02
mpl.rcParams['axes.ymargin'] = 0.05
mpl.rcParams['legend.handlelength'] = 1.8
mpl.rcParams['legend.borderpad'] = 0.4
mpl.rcParams['figure.dpi'] = 200
mpl.rcParams['savefig.dpi'] = 300
mpl.rcParams['savefig.bbox'] = 'tight'
mpl.rcParams['savefig.facecolor'] = 'white'

os.makedirs("figures", exist_ok=True)

# ------------------------------------------------------------------
# 1. Dodecahedral graph Laplacian (20×20) and its pseudoinverse
# ------------------------------------------------------------------
# Adjacency list of the regular dodecahedral graph (20 vertices, degree 3)
adj = [
    [1, 4, 19],   [0, 2, 9],    [1, 3, 11],   [2, 4, 13],   [0, 3, 8],
    [6, 9, 14],   [5, 7, 15],   [6, 8, 16],   [4, 7, 17],   [1, 5, 18],
    [11, 15, 19], [2, 10, 12],  [11, 13, 16], [3, 12, 17],  [5, 18, 19],
    [6, 10, 18],   [7, 12, 19],   [8, 13, 18],  [9, 14, 17],  [0, 10, 14]
]

n = 20
rows = []
cols = []
for i in range(n):
    rows.extend([i]*3)
    cols.extend(adj[i])
A = csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n,n))
D = csr_matrix((np.full(n, 3.0), (range(n), range(n))), shape=(n,n))
L = D - A                                  # graph Laplacian

# Moore–Penrose pseudoinverse (null space = constant vector)
w, v = eigsh(L, k=6, which='SM')             # smallest eigenvalues
L_pinv = np.linalg.pinv(L.toarray() + 1e-12*np.eye(n))   # stable

# Save diagnostics
np.savez("figures/dodecahedron_laplacian.npz",
