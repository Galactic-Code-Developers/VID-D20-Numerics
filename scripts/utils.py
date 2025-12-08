#!/usr/bin/env python3
"""
Utility helpers for VID numerics: graph builders, Laplacian factory, and seed control.
"""

from __future__ import annotations

import argparse
import os
import random
from typing import Optional

import numpy as np


# ----------------------------------------------------------------------
# Random seed control
# ----------------------------------------------------------------------

def set_seed(seed: Optional[int] = None) -> int:
    """
    Set the global random seed for numpy and Python's random module.

    Parameters
    ----------
    seed : int or None
        If None, a seed is drawn from np.random.SeedSequence().entropy.
        If int, that value is used directly.

    Returns
    -------
    int
        The seed actually used.
    """
    if seed is None:
        # use system entropy to generate a seed
        seed = int(np.random.SeedSequence().entropy)

    random.seed(seed)
    np.random.seed(seed)
    return seed


# ----------------------------------------------------------------------
# Graph / Laplacian builders
# ----------------------------------------------------------------------

def build_cycle_laplacian(N: int) -> np.ndarray:
    """
    Construct the N×N Laplacian of a simple cycle graph (ring).

    Each node has degree 2 and is connected to its two neighbors.
    L = D - A, where D[i,i] = 2 and
    A[i,(i±1)%N] = 1.

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
    Construct the N×N DLSFH Laplacian used in the VID numerics.

    For now this is implemented as the cycle Laplacian, but this function
    is the single entry point and can be upgraded later to the full
    DLSFH geometry without changing the rest of the code.

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


# ----------------------------------------------------------------------
# I/O helpers
# ----------------------------------------------------------------------

def save_matrix(path: str, mat: np.ndarray) -> None:
    """
    Save a matrix as a .npy file, creating directories if needed.

    Parameters
    ----------
    path : str
        Output file path (should end in .npy).
    mat : np.ndarray
        Matrix to save.
    """
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    np.save(path, mat)


def load_matrix(path: str) -> np.ndarray:
    """
    Load a matrix from a .npy file.

    Parameters
    ----------
    path : str
        Input file path.

    Returns
    -------
    np.ndarray
        Loaded matrix.
    """
    return np.load(path)


# ----------------------------------------------------------------------
# CLI helper (optional)
# ----------------------------------------------------------------------

def _cli_build_and_save():
    """
    Small command-line interface to build and save a DLSFH Laplacian.

    Example:
        python -m scripts.utils --N 20 --out data/Delta20.npy
    """
    parser = argparse.ArgumentParser(description="Build and save DLSFH Laplacian")
    parser.add_argument("--N", type=int, required=True, help="Matrix size")
    parser.add_argument("--out", type=str, required=True, help="Output .npy file")
    args = parser.parse_args()

    L = build_dlsfh_laplacian(args.N)
    save_matrix(args.out, L)
    print(f"[utils] Saved DLSFH Laplacian ({args.N}×{args.N}) → {args.out}")


if __name__ == "__main__":
    _cli_build_and_save()
