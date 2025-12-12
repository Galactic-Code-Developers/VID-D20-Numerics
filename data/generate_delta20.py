"""
generate_delta20.py

Generates:
- Delta20.npy          : 20×20 DLSFH Laplacian
- Delta20_pinv.npy     : Moore–Penrose pseudoinverse
- parameters.json      : Global VID numerical parameters
"""

import json
import os
import numpy as np
import networkx as nx
from scipy.linalg import pinvh


# -----------------------------
# Configuration
# -----------------------------

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

SEED = 42
KAPPA = 0.30
N_TRUNC = 50
EPS_INF = 1e-10


# -----------------------------
# Build DLSFH Laplacian
# -----------------------------

def build_delta20() -> np.ndarray:
    """
    Construct the 20-vertex DLSFH Laplacian (dodecahedral graph).
    """
    G = nx.dodecahedral_graph()
    mapping = {old: i for i, old in enumerate(sorted(G.nodes()))}
    G = nx.relabel_nodes(G, mapping)

    Delta = nx.laplacian_matrix(G).astype(float).toarray()
    return Delta


# -----------------------------
# Main generation
# -----------------------------

def main():
    # Set seed for reproducibility
    np.random.seed(SEED)

    # Build Delta20
    Delta20 = build_delta20()
    np.save(os.path.join(DATA_DIR, "Delta20.npy"), Delta20)

    # Compute pseudoinverse
    Delta20_pinv = pinvh(Delta20, cond=1e12)
    np.save(os.path.join(DATA_DIR, "Delta20_pinv.npy"), Delta20_pinv)

    # Parameter block
    params = {
        "lattice": "DLSFH (20-vertex dodecahedral graph)",
        "operator": "Delta20 (graph Laplacian)",
        "pseudoinverse": "Delta20_pinv (Moore–Penrose)",
        "coherence_coupling_kappa": KAPPA,
        "truncation_depth_N": N_TRUNC,
        "epsilon_infinity": EPS_INF,
        "random_seed": SEED,
        "smoothing": "none",
        "normalization": "SGCV coherence normalization",
        "units": {
            "Delta": "dimensionless graph Laplacian",
            "Delta_pinv": "dimensionless propagator",
            "path_length": "graph-edge units"
        }
    }

    with open(os.path.join(DATA_DIR, "parameters.json"), "w") as f:
        json.dump(params, f, indent=2)

    print("Generated:")
    print("  data/Delta20.npy")
    print("  data/Delta20_pinv.npy")
    print("  data/parameters.json")


if __name__ == "__main__":
    main()
