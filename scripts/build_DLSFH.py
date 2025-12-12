"""
build_DLSFH.py

Construct the 20×20 DLSFH Laplacian using the dodecahedral graph
and save it as L_dlsfh.npy. Also prints basic diagnostics.
"""

from typing import Tuple

import numpy as np
import networkx as nx

from utils import save_matrix, print_spectrum_report, timed


# ---------------------------------------------------------------------------
# Core constructor
# ---------------------------------------------------------------------------

def build_dlsfh_graph() -> nx.Graph:
    """
    Build the base DLSFH graph.

    Returns
    -------
    networkx.Graph
        Undirected 20-vertex 3-regular dodecahedral graph.
    """
    # Standard dodecahedral graph (20 vertices, degree 3).
    G = nx.dodecahedral_graph()
    # Ensure nodes are relabeled 0..19 in order
    mapping = {old: i for i, old in enumerate(sorted(G.nodes()))}
    G = nx.relabel_nodes(G, mapping)
    return G


def build_laplacian(G: nx.Graph) -> np.ndarray:
    """
    Construct the combinatorial Laplacian L = D - A of the graph G.

    Parameters
    ----------
    G : networkx.Graph
        Undirected graph.

    Returns
    -------
    np.ndarray
        Laplacian matrix as a dense NumPy array of shape (n, n).
    """
    L = nx.laplacian_matrix(G).astype(float).toarray()
    return L


@timed
def build_and_save_L_dlsfh() -> Tuple[np.ndarray, str]:
    """
    Build the DLSFH Laplacian and save it to disk.

    Returns
    -------
    (np.ndarray, str)
        (L, path_to_file)
    """
    G = build_dlsfh_graph()
    L = build_laplacian(G)
    path = save_matrix(L, "L_dlsfh.npy")
    print(f"L_dlsfh constructed: shape={L.shape}, saved to {path}")
    print_spectrum_report(L, name="L_dlsfh", k=5)
    return L, path


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    build_and_save_L_dlsfh()
