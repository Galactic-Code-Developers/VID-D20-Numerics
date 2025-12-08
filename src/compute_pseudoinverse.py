#!/usr/bin/env python3
import argparse
import numpy as np

def compute_pseudoinverse(L: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    """
    Compute Moore–Penrose pseudoinverse using SVD.

    L = U Σ V^T  →  L⁺ = V Σ⁺ U^T

    Zero singular values (for Laplacians) are handled by threshold `tol`.
    """
    U, S, Vt = np.linalg.svd(L, full_matrices=False)

    # Build Σ⁺
    S_inv = np.zeros_like(S)
    for i, s in enumerate(S):
        if s > tol:
            S_inv[i] = 1.0 / s
        else:
            S_inv[i] = 0.0

    L_pinv = (Vt.T * S_inv) @ U.T
    return L_pinv

def main():
    parser = argparse.ArgumentParser(description="Compute pseudoinverse of Laplacian")
    parser.add_argument("--in", dest="infile", required=True, help="Input .npy file (Laplacian)")
    parser.add_argument("--out", dest="outfile", required=True, help="Output .npy file (pseudoinverse)")
    parser.add_argument("--tol", type=float, default=1e-12, help="SVD tolerance")

    args = parser.parse_args()

    L = np.load(args.infile)
    L_pinv = compute_pseudoinverse(L, args.tol)

    np.save(args.out, L_pinv)
    print(f"[+] Saved pseudoinverse L⁺ → {args.out}")

if __name__ == "__main__":
    main()
