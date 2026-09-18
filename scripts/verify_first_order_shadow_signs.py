#!/usr/bin/env python3
"""
Symbolic checks for the 2026-09-18 first-order RH sign program.

Checks:
1. two-channel CAR/Koszul shadow Dirac square;
2. parity grading anticommutation;
3. grading-twisted negative-square completion;
4. exact determinant of the two-channel completed block;
5. exact four-prime Haar-even negative vector at centered boundary z=0.

This script is research-side verification only. It makes no RH claim.
"""

import itertools
import sympy as sp


def two_channel_car():
    # Basis |00>, |10>, |01>, |11>.
    c1 = sp.Matrix([
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
    ])
    a1 = c1.T

    c2 = sp.Matrix([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, -1, 0, 0],
    ])
    a2 = c2.T

    I4 = sp.eye(4)
    Z4 = sp.zeros(4)

    assert c1 * c1 == Z4
    assert c2 * c2 == Z4
    assert a1 * a1 == Z4
    assert a2 * a2 == Z4
    assert c1 * c2 + c2 * c1 == Z4
    assert a1 * a2 + a2 * a1 == Z4
    assert c1 * a1 + a1 * c1 == I4
    assert c2 * a2 + a2 * c2 == I4
    assert c1 * a2 + a2 * c1 == Z4
    assert c2 * a1 + a1 * c2 == Z4

    return c1, c2, a1, a2


def check_two_channel_shadow_dirac():
    c1, c2, a1, a2 = two_channel_car()

    z1, z2, w1, w2, m = sp.symbols("z1 z2 w1 w2 m")
    E = z1 * w1 + z2 * w2

    D = z1 * c1 + z2 * c2 + w1 * a1 + w2 * a2
    Gamma = sp.diag(1, -1, -1, 1)
    I4 = sp.eye(4)

    assert sp.simplify(D * D - E * I4) == sp.zeros(4)
    assert sp.simplify(Gamma * D + D * Gamma) == sp.zeros(4)
    assert Gamma * Gamma == I4
    assert sp.factor(D.det()) == E**2

    completed = D + sp.I * m * Gamma
    shell = E - m**2

    assert sp.simplify(completed * completed - shell * I4) == sp.zeros(4)
    assert sp.factor(completed.det()) == shell**2

    return {
        "shadow_energy": E,
        "shadow_det": sp.factor(D.det()),
        "completed_det": sp.factor(completed.det()),
    }


def mobius_cube(n):
    """Binary occupation cube: commuting nilpotent subset-addition shifts."""
    dim = 2**n
    M = sp.eye(dim)

    for j in range(n):
        S = sp.zeros(dim)
        for A in range(dim):
            if not ((A >> j) & 1):
                S[A | (1 << j), A] = 1
        M = M * (sp.eye(dim) - S)

    J = sp.zeros(dim)
    full = (1 << n) - 1
    for A in range(dim):
        J[full ^ A, A] = 1

    return M, J


def check_four_prime_haar_even_negative():
    n = 4
    M, J = mobius_cube(n)
    dim = 2**n

    x = sp.zeros(dim, 1)
    full = (1 << n) - 1

    # x=(empty+full)-sum_{|A|=2} e_A
    x[0] = 1
    x[full] = 1
    for A in range(dim):
        if A.bit_count() == 2:
            x[A] = -1

    assert J * x == x

    q = (x.T * M * x)[0]
    norm2 = (x.T * x)[0]

    assert q == -3
    assert norm2 == 8

    # J-self-adjointness of the centered finite Mobius bulk.
    assert M.T * J == J * M

    return {
        "quadratic_form": q,
        "norm_squared": norm2,
        "rayleigh_quotient": sp.Rational(q, norm2),
    }


def middle_layer_formula(m):
    """n=2m, x=(empty+full)-middle layer."""
    n = 2 * m
    C = sp.binomial(n, m)
    return sp.simplify(3 + C - 2 * ((-1) ** m) * C)


def main():
    shadow = check_two_channel_shadow_dirac()
    negative = check_four_prime_haar_even_negative()

    print("two-channel shadow energy:", shadow["shadow_energy"])
    print("two-channel det:", shadow["shadow_det"])
    print("graded completed det:", shadow["completed_det"])
    print("four-prime Haar-even q:", negative["quadratic_form"])
    print("four-prime norm^2:", negative["norm_squared"])
    print("four-prime Rayleigh:", negative["rayleigh_quotient"])

    for m in range(1, 7):
        print(f"n={2*m}, middle-layer q={middle_layer_formula(m)}")


if __name__ == "__main__":
    main()
