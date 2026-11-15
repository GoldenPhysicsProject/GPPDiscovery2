#!/usr/bin/env python3
"""Exact Lie closure test for the SU(3) holonomy construction in HP1/S4.

Requires: sympy.  No floating-point approximations are used.
"""
import sympy as sp

I = sp.I


def matrix_unit(i: int, j: int) -> sp.Matrix:
    e = sp.zeros(3)
    e[i, j] = 1
    return e


X = I * sp.diag(1, 2, -3)
Y = I * (
    matrix_unit(0, 1)
    + matrix_unit(1, 0)
    + matrix_unit(1, 2)
    + matrix_unit(2, 1)
)


def bracket(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.simplify(a * b - b * a)


def real_coordinates(a: sp.Matrix) -> sp.Matrix:
    """Embed 3x3 complex matrices into Q^18, preserving real rank."""
    return sp.Matrix(
        [sp.re(sp.expand(a[i, j])) for i in range(3) for j in range(3)]
        + [sp.im(sp.expand(a[i, j])) for i in range(3) for j in range(3)]
    )


def rank(matrices: list[sp.Matrix]) -> int:
    return sp.Matrix.hstack(*(real_coordinates(a) for a in matrices)).rank()


assert X.H == -X and Y.H == -Y
assert sp.trace(X) == 0 and sp.trace(Y) == 0

basis = [X, Y]
ranks = [rank(basis)]
for _ in range(6):
    candidates = [bracket(a, b) for a in tuple(basis) for b in tuple(basis)]
    for candidate in candidates:
        if rank([*basis, candidate]) > len(basis):
            assert candidate.H == -candidate
            assert sp.trace(candidate) == 0
            basis.append(candidate)
    ranks.append(rank(basis))
    if ranks[-1] == 8:
        break

assert ranks == [2, 3, 5, 8], ranks
assert len(basis) == 8
print("PASS: generators are traceless and skew-Hermitian.")
print("PASS: exact Lie closure dimensions:", ranks)
print("PASS: Lie(X,Y) = su(3), dimension 8.")
