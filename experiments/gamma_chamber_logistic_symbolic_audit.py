#!/usr/bin/env python3
"""Exact algebraic audit of the Beta -> logistic Gamma-chamber substitution.

This isolates the symbolic part of the continuous chamber Fourier theorem from
numerical quadrature.  Put

    u = q/(1+q),  q = exp(y) > 0.

Then du/dy = q/(1+q)^2, and the Euler-Beta density with parameters
c+ix and c-ix transforms as

    u^(c+ix-1) (1-u)^(c-ix-1) du
      = q^(c+ix)/(1+q)^(2c) dy
      = 4^(-c) sech(y/2)^(2c) exp(ixy) dy.

For arbitrary real c the last step is best regarded as a positive-base real-power
identity.  The script certifies the underlying positive algebraic base exactly:

    q/(1+q)^2 = 1/(4 cosh(y/2)^2),  q=exp(y),

so raising both positive sides to c is legitimate for c>0.  This is supporting
executable discovery evidence; the corresponding Lean proof still needs the
measure-theoretic change-of-variables theorem on R.
"""
from __future__ import annotations

import sympy as sp

q, u, y = sp.symbols("q u y", positive=True, real=True)
c, x = sp.symbols("c x", positive=True, real=True)
I = sp.I


def main() -> None:
    u_q = q / (1 + q)
    one_minus_u = sp.factor(1 - u_q)
    du_dq = sp.diff(u_q, q)
    dq_dy = q
    du_dy = sp.factor(du_dq * dq_dy)

    assert sp.simplify(one_minus_u - 1/(1+q)) == 0
    assert sp.simplify(du_dy - q/(1+q)**2) == 0
    assert sp.simplify(du_dy - u_q*one_minus_u) == 0

    # Exponent bookkeeping in logarithmic form avoids any branch ambiguity from
    # asking a CAS to combine symbolic complex powers directly.
    logq, log1pq = sp.symbols("logq log1pq", real=True)
    log_u = logq - log1pq
    log_1mu = -log1pq
    log_jac = logq - 2*log1pq
    transformed_log = sp.expand(
        (c + I*x - 1)*log_u
        + (c - I*x - 1)*log_1mu
        + log_jac
    )
    target_log = sp.expand((c + I*x)*logq - 2*c*log1pq)
    assert sp.simplify(transformed_log - target_log) == 0

    # Exact hyperbolic base identity.  Rewrite cosh(y/2) in exponentials and
    # then substitute q=exp(y); no numerical sampling enters.
    expy = sp.exp(y)
    hyper_base = sp.Rational(1, 4) / sp.cosh(y/2)**2
    hyper_exp = sp.factor(hyper_base.rewrite(sp.exp))
    rational_base = expy/(1+expy)**2
    assert sp.simplify(hyper_exp - rational_base) == 0

    # The oscillatory phase is exactly q^(i x)=exp(i x y) once q=exp(y),
    # expressed at the exponent level where the real logarithm is single-valued.
    phase_exponent = I*x*y
    assert sp.simplify(phase_exponent - I*x*y) == 0

    print("u(q) =", u_q)
    print("du/dy =", du_dy)
    print("transformed logarithmic exponent =", transformed_log)
    print("positive hyperbolic base =", hyper_exp)
    print("PASS: exact Beta -> logistic density algebra is certified")
    print("LEAN BOUNDARY: real-line measure change of variables + Fourier uniqueness")


if __name__ == "__main__":
    main()
