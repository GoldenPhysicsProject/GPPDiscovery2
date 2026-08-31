#!/usr/bin/env python3
"""Stable numerical check of the raised-box real outer Beta integral.

For delta < 1,
    integral_0^1 x^(-delta) (1-x)^(2-delta) dx = B(1-delta, 3-delta).

The substitution x=t^(1/(1-delta)) removes the x=0 singularity and remains
numerically stable close to delta=1 from below.
"""

import mpmath as mp

mp.mp.dps = 80


def outer_beta_regularized(delta: mp.mpf) -> mp.mpf:
    if not delta < 1:
        raise ValueError("delta must be < 1")
    q = 1 / (1 - delta)
    f = lambda t: q * (1 - t**q) ** (2 - delta)
    return mp.quad(f, [0, 1])


def outer_beta_exact(delta: mp.mpf) -> mp.mpf:
    return mp.beta(1 - delta, 3 - delta)


def nested_majorant_exact(delta: mp.mpf) -> mp.mpf:
    return mp.gamma(1 - delta) ** 2 / mp.gamma(4 - 2 * delta)


def nested_majorant_from_slices(delta: mp.mpf) -> mp.mpf:
    return outer_beta_regularized(delta) / ((1 - delta) * (2 - delta))


if __name__ == "__main__":
    deltas = [mp.mpf("0.1"), mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99")]
    tol = mp.mpf("1e-50")
    for delta in deltas:
        numeric = outer_beta_regularized(delta)
        exact = outer_beta_exact(delta)
        nested_numeric = nested_majorant_from_slices(delta)
        nested_exact = nested_majorant_exact(delta)
        outer_err = abs(numeric - exact)
        nested_err = abs(nested_numeric - nested_exact)
        print(
            f"delta={mp.nstr(delta, 4)} "
            f"outer_err={mp.nstr(outer_err, 6)} "
            f"nested_err={mp.nstr(nested_err, 6)}"
        )
        assert outer_err < tol
        assert nested_err < tol
