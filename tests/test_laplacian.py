import numpy as np

from vid_numerics.laplacian import build_dlsfh_laplacian


def test_cycle_laplacian_basic_properties():
    N = 20
    L = build_dlsfh_laplacian(N)

    # shape
    assert L.shape == (N, N)

    # symmetry
    assert np.allclose(L, L.T)

    # each row sums to zero (Laplacian property)
    row_sums = L.sum(axis=1)
    assert np.allclose(row_sums, np.zeros(N))

    # diagonal entries are 2 for a simple cycle graph
    assert np.allclose(np.diag(L), 2.0)


def test_eigen_zero_mode():
    N = 20
    L = build_dlsfh_laplacian(N)

    # all-ones vector should be in kernel of L
    ones = np.ones(N)
    v = L @ ones
    assert np.allclose(v, np.zeros(N))
