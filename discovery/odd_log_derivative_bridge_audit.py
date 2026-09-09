#!/usr/bin/env python3
"""Executable audit for the odd Weierstrass log/derivative bridge.

For
    O_N(x) = prod_{k=0}^{N-1} (1 + x^2/(2k+1)^2),
we check simultaneously

    O_N(x) -> cosh(pi x/2),
    log O_N(x) -> log cosh(pi x/2),
    d/dx log O_N(x)
      = sum_{k=0}^{N-1} 2x/((2k+1)^2+x^2)
      -> (pi/2) tanh(pi x/2).

The audit also exposes the leading tail scales suggested by the elementary
large-k expansion:

    N * (log cosh(pi x/2) - log O_N(x)) -> x^2/4,
    N * ((pi/2)tanh(pi x/2) - d log O_N/dx) -> x/2.

These limits are numerical/discovery evidence here, not promoted as formal
proofs.  They identify useful explicit-tail targets for the Lean lane.
"""

from __future__ import annotations

import math


def row(x: float, n_terms: int) -> tuple[float, ...]:
    log_partial = 0.0
    deriv_partial = 0.0
    for k in range(n_terms):
        odd = 2 * k + 1
        u = x * x / (odd * odd)
        log_partial += math.log1p(u)
        deriv_partial += 2.0 * x / (odd * odd + x * x)

    target_log = math.log(math.cosh(math.pi * x / 2.0))
    target_deriv = (math.pi / 2.0) * math.tanh(math.pi * x / 2.0)
    log_tail = target_log - log_partial
    deriv_tail = target_deriv - deriv_partial
    return (
        log_partial,
        target_log,
        log_tail,
        n_terms * log_tail,
        x * x / 4.0,
        deriv_partial,
        target_deriv,
        deriv_tail,
        n_terms * deriv_tail,
        x / 2.0,
    )


def main() -> None:
    xs = (0.25, 0.5, 1.0, 2.0)
    ns = (10, 100, 1000, 10000)
    print(
        "x,N,log_partial,log_target,log_tail,N_log_tail,x2_over_4,"
        "deriv_partial,deriv_target,deriv_tail,N_deriv_tail,x_over_2"
    )
    for x in xs:
        for n_terms in ns:
            vals = row(x, n_terms)
            print(
                f"{x:g},{n_terms}," + ",".join(f"{v:.16g}" for v in vals)
            )


if __name__ == "__main__":
    main()
