"""High-precision audit of the real dilogarithm derivative and Spence identity.

Codex/GPT Golden Physics discovery track.

We use only the real power series

    L2(x) = sum_{k>=1} x^k / k^2,   |x| < 1,

and its termwise derivative

    L2'(x) = sum_{k>=1} x^(k-1)/k = -log(1-x)/x,   0 < x < 1.

The script checks convergence independently in the function and derivative sums,
and then verifies that

    F(x) = L2(x) + L2(1-x) + log(x) log(1-x)

is constant and equals pi^2/6.
"""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 100


def li2_series(x: mp.mpf, nmax: int) -> mp.mpf:
    return mp.fsum(x**k / (mp.mpf(k) ** 2) for k in range(1, nmax + 1))


def li2_deriv_series(x: mp.mpf, nmax: int) -> mp.mpf:
    return mp.fsum(x ** (k - 1) / mp.mpf(k) for k in range(1, nmax + 1))


def deriv_closed(x: mp.mpf) -> mp.mpf:
    return -mp.log(1 - x) / x


def spence_F(x: mp.mpf, nmax: int) -> mp.mpf:
    return (
        li2_series(x, nmax)
        + li2_series(1 - x, nmax)
        + mp.log(x) * mp.log(1 - x)
    )


def run() -> None:
    xs = [
        mp.mpf("0.01"),
        mp.mpf("0.1"),
        mp.mpf("0.25"),
        mp.mpf("0.5"),
        mp.mpf("0.75"),
        mp.mpf("0.9"),
        mp.mpf("0.99"),
    ]
    cutoffs = [500, 2000, 10000, 50000]
    target = mp.pi**2 / 6

    print("Real Li2 derivative / Spence audit")
    print(f"precision = {mp.mp.dps} digits")
    print()

    for nmax in cutoffs:
        print(f"cutoff N={nmax}")
        max_deriv_err = mp.mpf("0")
        max_spence_err = mp.mpf("0")
        for x in xs:
            d_err = abs(li2_deriv_series(x, nmax) - deriv_closed(x))
            s_err = abs(spence_F(x, nmax) - target)
            max_deriv_err = max(max_deriv_err, d_err)
            max_spence_err = max(max_spence_err, s_err)
            print(
                "  x={}  deriv_err={}  spence_err={}".format(
                    mp.nstr(x, 8), mp.nstr(d_err, 12), mp.nstr(s_err, 12)
                )
            )
        print("  max derivative error:", mp.nstr(max_deriv_err, 20))
        print("  max Spence error:   ", mp.nstr(max_spence_err, 20))
        print()

    # Direct analytic cancellation check for F'(x), using the closed derivative.
    print("Closed-form F'(x) residuals")
    for x in xs:
        # d/dx L2(1-x) = +log(x)/(1-x)
        residual = (
            deriv_closed(x)
            + mp.log(x) / (1 - x)
            + (mp.log(1 - x) / x - mp.log(x) / (1 - x))
        )
        print("  x={}  residual={}".format(mp.nstr(x, 8), mp.nstr(abs(residual), 20)))


if __name__ == "__main__":
    run()
