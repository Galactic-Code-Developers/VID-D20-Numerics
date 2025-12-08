#!/usr/bin/env python3
import argparse
import numpy as np

def build_dlsfh_laplacian(N: int) -> np.ndarray:
    """
    Construct the N×N DLSFH Laplacian used in the VID numerics.

    This version uses the simplest consistent model:
    - Graph is a ring (cycle graph) with uniform unit weights.
    - Laplacian L = D - A, where:
        D[i,i] = degree (always 2 for cycle)
        A[i,(i±1)%N] = 1

    This can be replaced later with any DLSFH-specific adjacency rule.
    """
    L = np.zeros((N, N), dtype=float)

    for i in range(N):
        L[i, i] = 2.0  # degree of each node in a ring
        L[i, (i - 1) % N] = -1.0
        L[i, (i + 1) % N] = -1.0

    return L

def main():
    parser = argparse.ArgumentParser(description="Build N×N DLSFH Laplacian")
    parser.add_argument("--N", type=int, required=True, help="Matrix size")
    parser.add_argument("--out", type=str, required=True, help="Output .npy file")

    args = parser.parse_args()

    L = build_dlsfh_laplacian(args.N)
    np.save(args.out, L)

    print(f"[+] Saved DLSFH Laplacian ({args.N}×{args.N}) → {args.out}")

if __name__ == "__main__":
    main()
