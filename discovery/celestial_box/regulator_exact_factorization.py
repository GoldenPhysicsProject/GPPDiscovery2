"""Exact algebraic factorization of the scalar-box regulator geometry.

For S,U,m>0 define
  R^2 = U/(U+4m),
  kappa^2 = 1 + 4m/U - 4m^2/(S U),
  q = (1-R)/(1+R),
  a = (kappa-1)/(kappa+1).

The script verifies exact identities exposing the O(m^2) endpoint/pole split.
"""
import sympy as sp

m, S, U = sp.symbols("m S U", positive=True)
R = sp.sqrt(U / (U + 4*m))
kappa = sp.sqrt(1 + 4*m/U - 4*m**2/(S*U))
q = (1 - R) / (1 + R)
a = (kappa - 1) / (kappa + 1)

q_exact = 4*m / (U * (sp.sqrt(1 + 4*m/U) + 1)**2)
a_exact = 4*m*(S-m) / (S*U*(kappa + 1)**2)
q_minus_a_exact = 8*m**2 / (
    S*(U+4*m)*(1+kappa*R)*(1+R)*(1+kappa)
)
h_exact = 2*m*U*(1+kappa) / (
    (U+4*m)*(1+kappa*R)*(1+R)*(S-m)
)

checks = {
    "q": sp.simplify(q - q_exact),
    "a": sp.simplify(a - a_exact),
    "kappaR_square": sp.simplify((kappa*R)**2 - (1 - 4*m**2/(S*(U+4*m)))),
    "q_minus_a": sp.simplify((q-a) - q_minus_a_exact),
    "q_over_a_minus_one": sp.simplify((q/a - 1) - h_exact),
}

for name, residual in checks.items():
    print(f"{name}: {sp.factor(residual)}")
    assert residual == 0

print("All exact factorization checks passed.")
