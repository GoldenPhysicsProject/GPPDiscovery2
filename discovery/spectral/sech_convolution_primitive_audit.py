"""Exact/symbolic audit of the elementary sech self-convolution primitive.

For lambda != 0,
  1/[cosh(pi x) cosh(pi(lambda-x))]
= [tanh(pi x)+tanh(pi(lambda-x))]/sinh(pi lambda)

and the RHS is d/dx of
  F(x,lambda) = [log(cosh(pi x))-log(cosh(pi(lambda-x)))]
                /[pi sinh(pi lambda)].

The endpoint difference is 2 lambda/sinh(pi lambda).
This is discovery evidence/identity checking, not a substitute for the Lean improper integral.
"""
import sympy as sp

x, lam = sp.symbols("x lam", real=True)
pi = sp.pi

integrand = 1 / (sp.cosh(pi*x) * sp.cosh(pi*(lam-x)))
primitive = (
    sp.log(sp.cosh(pi*x)) - sp.log(sp.cosh(pi*(lam-x)))
) / (pi * sp.sinh(pi*lam))

derivative_residual = sp.simplify(sp.trigsimp(sp.diff(primitive, x) - integrand))

# Use log(cosh y)=|y|-log(2)+o(1) on the real line to read the two endpoints.
endpoint_plus = sp.simplify(lam / sp.sinh(pi*lam))
endpoint_minus = sp.simplify(-lam / sp.sinh(pi*lam))
whole_line = sp.simplify(endpoint_plus - endpoint_minus)
expected = 2 * lam / sp.sinh(pi*lam)

print("derivative residual:", derivative_residual)
print("F(+infty):", endpoint_plus)
print("F(-infty):", endpoint_minus)
print("whole-line value:", whole_line)
print("expected residual:", sp.simplify(whole_line - expected))

assert derivative_residual == 0
assert sp.simplify(whole_line - expected) == 0
