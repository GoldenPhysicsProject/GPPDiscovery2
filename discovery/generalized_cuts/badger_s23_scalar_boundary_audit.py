#!/usr/bin/env python3
"""Exact s23 mixed-scalar boundary/pole audit in Badger's bubble variables.

Use the four-point bubble choice K1=p2+p3, chi=p2.  In units S1=s23=1,
choose spinor matrices

    p2 = diag(1,0),  p3 = diag(0,1),  K1 = I.

Then K1^flat=p3 and Badger eq. (39) becomes

    l1 = [[1-y, (y(1-y)-mu2)/t],
          [t,   y                    ]],

whose determinant is mu2.  For the left tree with scalar momentum -l1 the
remaining scalar propagator is

    D = (-l1+p2)^2-mu2 = -y.

Combining this with the independently certified invariant tree reduction

    A_S = -2 - 2 D/S1 - 2 mu2/D

gives

    A_S = 2 y - 2 + 2 mu2/y.

Hence the polynomial Inf_y boundary is 2y-2 and the mass-dependent 1/y term is
a finite-y pole/residue.  Restoring dimensions replaces D=-y by D=-S1*y and
2 mu2/y by 2 mu2/(S1*y).

This is an exact algebraic audit of the left mixed-helicity scalar tree only;
it does not yet evaluate the second tree or the triangle-subtraction moments.
"""

from __future__ import annotations

import sympy as sp


y, t, mu2 = sp.symbols("y t mu2", nonzero=True)

p2 = sp.Matrix([[1, 0], [0, 0]])
p3 = sp.Matrix([[0, 0], [0, 1]])
K1 = p2 + p3

l1 = sp.Matrix([
    [1 - y, (y * (1 - y) - mu2) / t],
    [t, y],
])


def sq(p: sp.Matrix):
    """Minkowski square in bispinor form, with the present unit convention."""
    return sp.factor(p.det())


def main() -> None:
    assert K1 == sp.eye(2)
    assert sp.simplify(sq(K1) - 1) == 0
    assert sp.simplify(sq(l1) - mu2) == 0
    assert sp.simplify(sq(l1 - K1) - mu2) == 0

    D = sp.factor(sq(-l1 + p2) - mu2)
    assert sp.simplify(D + y) == 0

    invariant_tree = sp.factor(-2 - 2 * D - 2 * mu2 / D)
    badger_boundary_form = sp.factor(2 * y - 2 + 2 * mu2 / y)
    assert sp.simplify(invariant_tree - badger_boundary_form) == 0

    polynomial_boundary = 2 * y - 2
    pole_part = 2 * mu2 / y
    assert sp.simplify(invariant_tree - polynomial_boundary - pole_part) == 0
    assert sp.simplify(y * pole_part - 2 * mu2) == 0

    print("det(l1) =", sq(l1))
    print("det(l1-K1) =", sq(l1 - K1))
    print("D_left =", D)
    print("A_S =", invariant_tree)
    print("Inf_y polynomial part =", polynomial_boundary)
    print("finite-y pole part =", pole_part)
    print("PASS: D_left=-y and A_S=(2y-2)+2 mu2/y exactly at S1=1")


if __name__ == "__main__":
    main()
