"""
utils.py

Shared utilities for the Valamontes Interaction Diagrams (VID) numerics:
- Data directory management
- Save / load matrices
- Spectral diagnostics
- Effective resistance computation
"""

import os
import time
from typing import Tuple

import numpy as np


# ---------------------------------------------------------------------------
# Global data directory
# ---------------------------------------------------------------------------

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def ensure_data_dir() -> str:
    """
    Ensure that the data directory exists and return its path.
    """
    if not os.path.isdir(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)
    return DATA_DIR


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def save_matrix(matrix: np.ndarray, filename: str) -> str:
    """
    Save a NumPy matrix to the data directory as .npy.

    Parameters
    ----------
    matrix : np.ndarray
        Matrix to save.
    filename : str
        File name, e.g. 'L_dlsfh.npy'.

    Returns
    -------
    str
        Full path to the saved file.
    """
    data_dir = ensure_data_dir()
    path = os.path.join(data_dir, filename)
    np.save(path, matrix)
    return path


def load_matrix(filename: str) -> np.ndarray:
    """
    Load a NumPy matrix from the data directory.

    Parameters
    ----------
    filename : str
        File name, e.g. 'L_dlsfh.npy'.

    Returns
    -------
    np.ndarray
        Loaded matrix.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    """
    path = os.path.join(ensure_data_dir(), filename)
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Matrix file not found: {path}")
    return np.load(path)


# ---------------------------------------------------------------------------
# Diagnostics
# ---------------------------------------------------------------------------

def spectrum_summary(L: np.ndarray, k: int = 10) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute and return the smallest and largest eigenvalues of a symmetric matrix.

    Parameters
    ----------
    L : np.ndarray
        Symmetric matrix (e.g. Laplacian).
    k : int, optional
        Number of eigenvalues at each end to report (if available).

    Returns
    -------
    (np.ndarray, np.ndarray)
        (smallest_eigs, largest_eigs)
    """
    vals = np.linalg.eigvalsh(L)
    k = min(k, len(vals))
    return vals[:k], vals[-k:]


def print_spectrum_report(L: np.ndarray, name: str = "L", k: int = 5) -> None:
    """
    Print a compact spectral report for a symmetric matrix.

    Parameters
    ----------
    L : np.ndarray
        Symmetric matrix (e.g. Laplacian).
    name : str, optional
        Label to print.
    k : int, optional
        Number of eigenvalues at each end to display.
    """
    smallest, largest = spectrum_summary(L, k=k)
    print(f"=== Spectrum summary for {name} (n={L.shape[0]}) ===")
    print(f"Smallest {len(smallest)} eigenvalues:")
    print(smallest)
    print(f"Largest {len(largest)} eigenvalues:")
    print(largest)
    print("--------------------------------------------------")


# ---------------------------------------------------------------------------
# Effective resistance
# ---------------------------------------------------------------------------

def effective_resistance_matrix(L_pinv: np.ndarray) -> np.ndarray:
    """
    Compute the effective-resistance matrix R from the Laplacian pseudoinverse L^+.

    For an undirected connected graph,
        R_ij = L^+_{ii} + L^+_{jj} - 2 L^+_{ij}.

    Parameters
    ----------
    L_pinv : np.ndarray
        Moore–Penrose pseudoinverse of the graph Laplacian.

    Returns
    -------
    np.ndarray
        Effective-resistance matrix R of the same shape as L_pinv.
    """
    diag = np.diag(L_pinv).reshape(-1, 1)
    R = diag + diag.T - 2.0 * L_pinv
    return R


# ---------------------------------------------------------------------------
# Simple timing decorator
# ---------------------------------------------------------------------------

def timed(fn):
    """
    Decorator to time a function call and print the elapsed time.

    Usage
    -----
    @timed
    def my_function(...):
        ...
    """
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = fn(*args, **kwargs)
        t1 = time.time()
        elapsed = t1 - t0
        print(f"[TIMING] {fn.__name__} completed in {elapsed:.4f} s")
        return result
    return wrapper
