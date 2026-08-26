"""Exact symbolic audit of the final scalar-box prefactor obstruction.

Codex/GPT discovery track.  No numerical evidence is used here: SymPy verifies the
algebraic expansion of D0 after ell_U=log(m/U), ell_S=log(m/S).  The remaining analytic
lemma for Lean is m*log(m)^2 -> 0 from m -> 0+.
"""
import sympy as sp

L, u, s, m, U = sp.symbols("L u s m U", real=True)
pi = sp.pi
ellU = L - u
ellS = L - s
D0 = ellU * ellS + sp.Rational(1, 2) * ellU**2 - pi**2 / 6
expanded = (
    sp.Rational(3, 2) * L**2
    - (s + 2*u) * L
    + u*s
    + sp.Rational(1, 2) * u**2
    - pi**2 / 6
)
assert sp.expand(D0 - expanded) == 0

# delta/2 = 2m/U.  This isolates the only genuinely new asymptotic monomial.
prefactor_term = sp.expand((2*m/U) * expanded)
coeff_L2 = sp.expand(prefactor_term).coeff(L, 2)
coeff_L1 = sp.expand(prefactor_term).coeff(L, 1)
assert sp.simplify(coeff_L2 - 3*m/U) == 0
assert sp.simplify(coeff_L1 + 2*m*(s + 2*u)/U) == 0

print("D0 =", expanded)
print("(delta/2) D0 =", prefactor_term)
print("Only new singular monomial: m * log(m)^2; all other terms are m*log(m) or m.")
