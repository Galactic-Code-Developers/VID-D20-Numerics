"""
vid_numerics: core numerical utilities for Valamontes Interaction Diagrams (VID).
"""

from .laplacian import build_dlsfh_laplacian
from .pseudoinverse import compute_pseudoinverse

__all__ = [
    "build_dlsfh_laplacian",
    "compute_pseudoinverse",
]
