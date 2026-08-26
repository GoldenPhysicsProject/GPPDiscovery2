#!/usr/bin/env python3
"""High-precision audit of the branch-free real dilogarithm inversion identity.

Codex/GPT Golden Physics discovery track.

For real x < 1 define

    Li2_R(x) = - integral_0^x log(1-t)/t dt,

with the removable t=0 value understood by continuity.  On the negative axis this is
single-valued and real, so the inversion relation needed by the regulated scalar box is

    Li2_R(-x) + Li2_R(-1/x) = -pi^2/6 - 1/2 log(x)^2,   x > 0.

The script independently checks:
  * integral = power series on |x| < 1;
  * the reciprocal inversion identity over many decades in x;
  * x <-> 1/x symmetry of the residual.

No complex polylogarithm or branch convention is used.
"""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 90


def kernel(t: mp.mpf) -> mp.mpf:
    if t == 0:
        return mp.mpf(1)
    return -mp.log1p(-t) / t


def li2_real_integral(x: mp.mpf) -> mp.mpf:
    x = mp.mpf(x)
    if x == 0:
        return mp.mpf(0)
    # Parameterize the segment t = x u.  For x < 1, 1-xu stays positive.
    return x * mp.quad(lambda u: kernel(x * u), [0, 1])


def li2_series(x: mp.mpf, n: int = 20000) -> mp.mpf:
    x = mp.mpf(x)
    return mp.fsum(x**k / (mp.mpf(k) ** 2) for k in range(1, n + 1))


def inversion_residual(x: mp.mpf) -> mp.mpf:
    x = mp.mpf(x)
    return (
        li2_real_integral(-x)
        + li2_real_integral(-1 / x)
        + mp.pi**2 / 6
        + mp.log(x) ** 2 / 2
    )


def main() -> None:
    series_points = [
        mp.mpf("-0.95"), mp.mpf("-0.5"), mp.mpf("-0.1"),
        mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("0.95"),
    ]
    max_series = mp.mpf(0)
    print("integral/series checks")
    for x in series_points:
        # 20k terms is intentionally independent of the quadrature representation.
        r = abs(li2_real_integral(x) - li2_series(x))
        max_series = max(max_series, r)
        print(f"x={mp.nstr(x,8):>8} residual={mp.nstr(r,8)}")

    inversion_points = [
        mp.mpf("1e-8"), mp.mpf("1e-4"), mp.mpf("0.01"),
        mp.mpf("0.1"), mp.mpf("0.3"), mp.mpf("1"),
        mp.mpf("3"), mp.mpf("10"), mp.mpf("1e2"),
        mp.mpf("1e4"), mp.mpf("1e8"),
    ]
    max_inv = mp.mpf(0)
    max_sym = mp.mpf(0)
    print("\ninversion checks")
    for x in inversion_points:
        r = inversion_residual(x)
        rsym = inversion_residual(1 / x)
        max_inv = max(max_inv, abs(r))
        max_sym = max(max_sym, abs(r - rsym))
        print(
            f"x={mp.nstr(x,8):>10} residual={mp.nstr(r,8)} "
            f"symmetry={mp.nstr(r-rsym,8)}"
        )

    print("\nsummary")
    print("max integral-series residual:", mp.nstr(max_series, 12))
    print("max inversion residual:", mp.nstr(max_inv, 12))
    print("max x<->1/x residual mismatch:", mp.nstr(max_sym, 12))

    # Series convergence at x=0.95 is only geometric, so the independent 20k-term
    # audit is expected around 1e-90 at the chosen precision.  Keep conservative gates.
    if max_series > mp.mpf("1e-70"):
        raise AssertionError("real dilogarithm integral/series audit failed")
    if max_inv > mp.mpf("1e-70") or max_sym > mp.mpf("1e-70"):
        raise AssertionError("real dilogarithm inversion audit failed")
    print("PASS: branch-free real inversion identity audited at high precision.")


if __name__ == "__main__":
    main()
