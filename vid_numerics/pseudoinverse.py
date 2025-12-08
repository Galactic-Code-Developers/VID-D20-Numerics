from __future__ import annotations

import numpy as np


def compute_pseudoinverse(L: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    """
    Compute the Moore–Penrose pseudoinverse of a matrix using SVD.

    Parameters
    ----------
    L : np.ndarray
        Input matrix (e.g., Laplacian).
    tol : float, optional
        Singular values below this threshold are treated as zero.

    Returns
    -------
    np.ndarray
        Pseudoinverse of L.
    """
    U, S, Vt = np.linalg.svd(L, full_matrices=False)

    S_inv = np.zeros_like(S)
    for i, s in enumerate(S):
        if s > tol:
            S_inv[i] = 1.0 / s
        else:
            S_inv[i] = 0.0

    L_pinv = (Vt.T * S_inv) @ U.T
    return L_pinv
