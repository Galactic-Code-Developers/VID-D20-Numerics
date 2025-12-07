
import numpy as np
import networkx as nx
import scipy.linalg as la
import matplotlib.pyplot as plt
from pathlib import Path


def build_dodecahedral_laplacian():
    """Return adjacency matrix A and Laplacian L for the dodecahedral graph (20 nodes)."""
    G = nx.dodecahedral_graph()
    A = nx.to_numpy_array(G, dtype=float)
    degree = np.sum(A, axis=1)
    L = np.diag(degree) - A
    return A, L


def spectral_decomposition(L):
    """Eigenvalues and eigenvectors of symmetric Laplacian L (20x20)."""
    vals, vecs = la.eigh(L)
    return vals, vecs


def pseudoinverse_from_spectrum(L, tol=1e-12):
    """Compute pseudoinverse L^+ via spectral decomposition."""
    vals, vecs = spectral_decomposition(L)
    inv_vals = np.zeros_like(vals)
    for i, lam in enumerate(vals):
        if lam > tol:
            inv_vals[i] = 1.0 / lam
    L_plus = (vecs * inv_vals) @ vecs.T
    return L_plus, vals, vecs


def effective_resistance_matrix(L_plus):
    """Effective resistance matrix R_ij = L^+_ii + L^+_jj - 2 L^+_ij."""
    diag = np.diag(L_plus)
    R = diag[:, None] + diag[None, :] - 2.0 * L_plus
    return R


def three_node_toy_example(kappa=1.0, eta=0.5):
    """Replicate the 3-node coherence-gradient toy model from the appendix."""
    # Path graph L
    L = np.array([[1.0, -1.0, 0.0],
                  [-1.0,  2.0, -1.0],
                  [0.0,  -1.0, 1.0]])
    # D = -kappa L
    D = -kappa * L

    # Coherence profile C = [1, 0, -1]
    C = np.array([1.0, 0.0, -1.0])
    G = np.zeros((3, 3))
    edges = [(0, 1), (1, 2)]
    for i, j in edges:
        d = C[i] - C[j]
        G[i, i] += d * d
        G[j, j] += d * d
        G[i, j] -= d * d
        G[j, i] -= d * d

    H_toy = D + eta * G
    evals, evecs = la.eigh(H_toy)

    return {
        "L": L,
        "D": D,
        "G": G,
        "H_toy": H_toy,
        "evals": evals,
        "evecs": evecs,
    }


def infty_sector_convergence_demo(rho=0.25, M=12):
    """Demonstrate norm convergence of an ∞-sector series T = sum rho^m A."""
    A, L = build_dodecahedral_laplacian()
    norms = []
    partial_norms = []
    T_partial = np.zeros_like(A)
    for m in range(1, M + 1):
        T_m = (rho ** m) * A
        T_partial = T_partial + T_m
        norms.append(la.norm(T_m, 2))
        partial_norms.append(la.norm(T_partial, 2))
    return np.array(norms), np.array(partial_norms)


def plot_infty_convergence(norms, partial_norms, outpath):
    steps = np.arange(1, len(norms) + 1)
    plt.figure()
    plt.semilogy(steps, norms, 'o-', label='||T^{(m)}||')
    plt.semilogy(steps, partial_norms, 's--', label='||∑_{k=1}^m T^{(k)}||')
    plt.xlabel('m')
    plt.ylabel('Operator norm (2-norm)')
    plt.title('∞-sector convergence on the dodecahedral cell')
    plt.grid(True, which='both', ls=':')
    plt.legend()
    outpath = Path(outpath)
    outpath.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()


def main():
    base = Path(__file__).resolve().parents[1]

    print("[1] Building dodecahedral Laplacian Δ20...")
    A, L = build_dodecahedral_laplacian()
    print("    A shape:", A.shape)
    print("    L shape:", L.shape)

    print("[2] Spectral decomposition and pseudoinverse Δ^+...")
    L_plus, vals, vecs = pseudoinverse_from_spectrum(L)
    print("    eigenvalues (rounded):", np.round(vals, 6))

    print("[3] Effective-resistance matrix...")
    R = effective_resistance_matrix(L_plus)
    print("    R[0,1] ≈", R[0, 1])

    print("[4] Three-node toy coherence-gradient example...")
    toy = three_node_toy_example()
    print("    H_toy eigenvalues:", np.round(toy["evals"], 6))

    print("[5] ∞-sector convergence demo...")
    norms, partial_norms = infty_sector_convergence_demo()
    fig_path = base / "figures" / "infty_convergence.png"
    plot_infty_convergence(norms, partial_norms, fig_path)
    print(f"    Saved convergence plot to {fig_path}")


if __name__ == "__main__":
    main()
