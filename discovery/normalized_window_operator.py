"""Finite multi-window Schur/Gershgorin diagnostic with honest controls.

Purpose: test proposed global window Gram matrices numerically, never certify
the infinite-dimensional Weil positivity theorem from finite floats.

For symmetric M with strictly positive scalar diagonal D, set
T = D^-1/2 (M-D) D^-1/2. The exact criterion is lambda_min(T)>=-1.
Sufficient but not necessary conditions are ||T||_op<=1 and the
Gershgorin row sum max_i sum_j |T_ij|<=1. In particular a large
positive eigenvalue of T may violate ||T||<=1 although I+T is PSD.

The real prime cross blocks can have zero *block* eigenvalues despite
strictly positive scalar diagonal entries. Project true block nulls
before using any purported block inverse.
"""

from __future__ import annotations

import numpy as np


def analyze_cross_coupling_operator(M: np.ndarray,
                                    relative_tolerance: float = 1e-11) -> dict:
    M = np.asarray(M, dtype=float)
    if M.ndim != 2 or M.shape[0] != M.shape[1]:
        raise ValueError("Expected a square real matrix")
    if not np.all(np.isfinite(M)):
        raise ValueError("Expected finite real entries")
    n = M.shape[0]
    scale = max(1.0, float(np.linalg.norm(M, ord=2)))
    tolerance = relative_tolerance * n * scale
    symmetry_error = float(np.max(np.abs(M-M.T)))
    if symmetry_error > tolerance:
        raise ValueError("Not symmetric; eigvalsh would silently ignore a triangle")
    M = (M+M.T)/2.0
    diag = np.diag(M).copy()
    if np.any(diag <= 0):
        raise ValueError("Strict positive scalar diagonal required; use block-null analysis")
    inv = 1.0 / np.sqrt(diag)
    B = M-np.diag(diag)
    T = inv[:,None] * B * inv[None,:]
    eigT = np.linalg.eigvalsh(T)
    eigM = np.linalg.eigvalsh(M)
    tnorm = float(np.max(np.abs(eigT)))
    rows = np.sum(np.abs(T),axis=1)
    # A dimensionless threshold relevant to I+T.
    tolT = relative_tolerance * max(1,n)
    return {
        "dimension": n,
        "min_eig_M": float(eigM[0]),
        "min_eig_T": float(eigT[0]),
        "max_eig_T": float(eigT[-1]),
        "norm_T": tnorm,
        "max_normalized_row_sum": float(np.max(rows)),
        "numeric_psd_M": bool(eigM[0] >= -tolerance),
        "numeric_psd_by_normalized_spectrum": bool(eigT[0] >= -1.0-tolT),
        "sufficient_operator_norm": bool(tnorm <= 1.0+tolT),
        "sufficient_gershgorin": bool(np.max(rows) <= 1.0+tolT),
        "symmetry_error": symmetry_error,
        "numeric_tolerance": tolerance,
        "disclaimer": "floating-point diagnostic, not interval-certified",
    }


def tests():
    def same(a,b,tol=1e-12):
        assert abs(a-b) <= tol, (a,b)

    pairwise_misses_global = np.full((3,3),-.6)
    np.fill_diagonal(pairwise_misses_global,1.0)
    result = analyze_cross_coupling_operator(pairwise_misses_global)
    same(result["min_eig_M"],-.2)
    assert not result["numeric_psd_M"]
    assert not result["sufficient_gershgorin"]

    notebooklm_example = np.array([[1., .7, .7],[.7,1.,-.7],[.7,-.7,1.]])
    result = analyze_cross_coupling_operator(notebooklm_example)
    same(result["min_eig_M"],-.4)
    assert not result["numeric_psd_M"]

    # This is PSD but the OPERATOR-NORM and Gershgorin sufficient tests FAIL.
    # M=ones has eigenvalues 3,0,0. T=M-I has eigenvalues 2,-1,-1.
    matrix_psd_with_large_positive_T = np.ones((3,3))
    result = analyze_cross_coupling_operator(matrix_psd_with_large_positive_T)
    same(result["min_eig_M"],0)
    same(result["min_eig_T"],-1)
    same(result["norm_T"],2)
    assert result["numeric_psd_M"]
    assert result["numeric_psd_by_normalized_spectrum"]
    assert not result["sufficient_operator_norm"]
    assert not result["sufficient_gershgorin"]

    positive_row_dominant = np.full((3,3),-.2)
    np.fill_diagonal(positive_row_dominant,1.0)
    result = analyze_cross_coupling_operator(positive_row_dominant)
    assert result["numeric_psd_M"]
    assert result["sufficient_operator_norm"]
    assert result["sufficient_gershgorin"]

    # Real symmetry and scalar diagonal hypotheses must be enforced.
    for bad in (np.array([[1.,2.],[0.,1.]]),
                np.array([[0.,1.],[1.,1.]])):
        try:
            analyze_cross_coupling_operator(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid input silently accepted")

    # PSD sharp local prime threshold block: one block null, but its
    # scalar diagonal entries are positive. No block inverse exists.
    local = np.array([[1.,-.5],[-.5,.25]])
    same(np.linalg.eigvalsh(local)[0],0)
    result = analyze_cross_coupling_operator(local)
    assert result["numeric_psd_M"]
    same(result["min_eig_T"],-1)

    print("PASS: negative 3-window example despite positive pairs")
    print("PASS: NotebookLM frustrated-triangle control")
    print("PASS: PSD matrix may fail both sufficient tests")
    print("PASS: normalized row dominance correctly certifies positive control")
    print("PASS: non-symmetric / singular scalar diagonal inputs rejected")
    print("PASS: sharp prime block null is not confused with positive definite block")


if __name__ == "__main__":
    tests()
