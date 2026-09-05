#!/usr/bin/env python3
"""Exact non-injectivity audit for reconstructing pre-sewing residues from a sewn product.

The generic nonzero-mu two-particle cut collapses two rational tree factors A(z), B(z)
into their product C(z)=A(z)B(z).  Master-topology subtraction, however, needs
factorwise residue information at additional uncut propagators before that collapse.

This script proves algebraically that no map depending only on C can recover such a
factorwise residue in general.  The ambiguity is the exact rational refactorization

    A -> h A,    B -> B/h,

which leaves C unchanged while changing Res[A,z=a] whenever h(a) != 1.  This is the
minimal algebraic obstruction behind the requirement to keep the extra denominators
and tree factors separate in the generic triple-cut lift.
"""
from __future__ import annotations

import sympy as sp

z, a, b, lam = sp.symbols("z a b lam")

# A has the extra uncut propagator z-a.  B is regular at z=a.
A = (z + b) / (z - a)
B = z**2 + 1
C = sp.factor(A * B)

# A nontrivial refactorization that is regular and nonzero at z=a generically.
h = 1 + lam * (z + 1)
A_tilde = sp.factor(h * A)
B_tilde = sp.factor(B / h)
C_tilde = sp.factor(A_tilde * B_tilde)

# The sewn object is exactly invariant.
assert sp.simplify(sp.together(C_tilde - C)) == 0

# But the factorwise residue at the extra propagator changes.
res_A = sp.simplify(sp.residue(A, z, a))
res_A_tilde = sp.simplify(sp.residue(A_tilde, z, a))
expected_res_A = a + b
expected_res_A_tilde = sp.expand((1 + lam * (a + 1)) * (a + b))
assert sp.simplify(res_A - expected_res_A) == 0
assert sp.simplify(res_A_tilde - expected_res_A_tilde) == 0

res_shift = sp.factor(res_A_tilde - res_A)
assert sp.simplify(res_shift - lam * (a + 1) * (a + b)) == 0
assert res_shift != 0

# A concrete exact witness rules out the possibility that this is only a symbolic
# branch issue: same sewn rational function, distinct factorwise residues.
witness = {a: sp.Rational(2), b: sp.Rational(3), lam: sp.Rational(5, 7)}
assert sp.simplify((C_tilde - C).subs(witness)) == 0
assert sp.simplify((res_A_tilde - res_A).subs(witness)) != 0

print("C(z) =", C)
print("Res[A,z=a] =", res_A)
print("Res[hA,z=a] =", res_A_tilde)
print("residue shift =", res_shift)
print("PASS: the sewn product is invariant under A->hA, B->B/h while factorwise residue data changes")
print("CONCLUSION: a master-topology projector requiring factorwise extra-propagator residues cannot factor through the collapsed two-particle sewing alone")
print("NEXT: retain the additional uncut denominators in the genuine generic nonzero-mu triple-cut lift")
