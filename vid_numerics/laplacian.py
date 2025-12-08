from __future__ import annotations

import numpy as np


def build_cycle_laplacian(N: int) -> np.ndarray:
    """
    Construct the N×N Laplacian of a cycle graph.

    Parameters
    ----------
    N : int
        Number of nodes.

    Returns
    -------
    np.ndarray
        N×N Laplacian matrix.
    """
    if N < 3:
        raise ValueError("Cycle Laplacian requires N >= 3")

    L = np.zeros((N, N), dtype=float)
    for i in range(N):
        L[i, i] = 2.0
        L[i, (i - 1) % N] = -1.0
        L[i, (i + 1) % N] = -1.0
    return L


def build_dlsfh_laplacian(N: int) -> np.ndarray:
    """
    Wrapper for the DLSFH Laplacian.

    Currently implemented as the cycle Laplacian; this function is the
    single abstraction point that can be upgraded to the full DLSFH
    geometry later.

    Parameters
    ----------
    N : int
        Number of nodes.

    Returns
    -------
    np.ndarray
        N×N Laplacian matrix.
    """
    return build_cycle_laplacian(N)
