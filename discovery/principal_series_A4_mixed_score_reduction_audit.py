#!/usr/bin/env python3
"""A4 reduction through symmetric/antisymmetric Barnes score identities.

Codex/GPT discovery audit only. No Claude-owned material is used.

Let

  p(t) = 8 t/sinh(2*pi*t),
  D(t) = Re psi(1/2+i t) - psi(1/2),
  q(t) = Im psi(1/2+i t) = (pi/2)tanh(pi*t).

Then A4 = (1/4) E[D^4]. The two-parameter Barnes normalization is

  K(r,h) = (r^2-h^2)/(2 r (2r+1)).

At r=1/2,h=0 its exact derivative ratios are

  K_rrrr/K = -24,
  K_rrhh/K = -112,
  K_hhhh/K = 0.

Using the exact phase-sector identities

  E[q^4] = pi^2/6,
  E[q q''] = -2*pi^2/3,
  E[R4] = -16*pi^2,

where R4 is the fourth symmetric logarithmic score, Faa di Bruno algebra
reduces the fourth raw digamma moment to

  E[D^4]
    = 2 E[D^2 q^2]
      + 4 E[D q D']
      - E[(D')^2]
      + 25/2 - 3*pi^2/2.

Thus the A4 proof is reduced to three one-dimensional mixed expectations.
High-precision quadrature + PSLQ gives the sharply constrained candidates

  E[D^2 q^2] = 1/2 - 2 log(2) + 4 log(2)^2,
  E[D q D']   = -3 + 4 log(2) + pi^2/6,
  E[(D')^2]   = 16 log(2) - 2*pi^2/3.

Substitution yields exactly

  A4 = 3/8 - log(2) + 2 log(2)^2 - pi^2/24.

IMPORTANT: the Barnes derivative reduction is exact symbolic algebra. The three
mixed expectation evaluations are, in this file, high-precision discovery
identities supported by PSLQ; they still require analytic proofs before A4 is
promoted to a theorem.
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp


def p(t: mp.mpf) -> mp.mpf:
    if t == 0:
        return 4 / mp.pi
    return 8 * t / mp.sinh(2 * mp.pi * t)


def D(t: mp.mpf) -> mp.mpf:
    z = mp.mpf("0.5") + 1j * t
    return mp.re(mp.digamma(z)) - mp.digamma(mp.mpf("0.5"))


def Dp(t: mp.mpf) -> mp.mpf:
    z = mp.mpf("0.5") + 1j * t
    return -mp.im(mp.polygamma(1, z))


def q(t: mp.mpf) -> mp.mpf:
    return (mp.pi / 2) * mp.tanh(mp.pi * t)


def even_expectation(f):
    return 2 * mp.quad(lambda x: p(x) * f(x), [0, 0.5, 1, 2, 4, mp.inf])


def main() -> None:
    mp.mp.dps = 90

    # Exact Barnes derivative ratios.
    r, h = sp.symbols("r h", positive=True, real=True)
    Krh = (r**2 - h**2) / (2 * r * (2 * r + 1))
    base = {r: sp.Rational(1, 2), h: 0}
    K0 = sp.simplify(Krh.subs(base))

    ratios = {
        "rrrr": sp.simplify(sp.diff(Krh, r, 4).subs(base) / K0),
        "rrhh": sp.simplify(sp.diff(Krh, r, 2, h, 2).subs(base) / K0),
        "hhhh": sp.simplify(sp.diff(Krh, h, 4).subs(base) / K0),
    }
    assert ratios == {"rrrr": -24, "rrhh": -112, "hhhh": 0}

    # Exact elimination of R4 and the remaining fourth-score nuisance term.
    # Denote A=E[D^2 q^2], B=E[D q D'], C=E[(D')^2], X=E[D^4].
    A, B, C, X, G = sp.symbols("A B C X G", real=True)
    pi2 = sp.pi**2

    # Symmetric rrrr identity after E[q^4]=pi^2/6 and E[R4]=-16*pi^2:
    eq_sym = sp.Eq(16 * X - 96 * A + 8 * G - 8 * pi2, -24)

    # Mixed rrhh identity after E[q^4], E[q q''], E[R4] are inserted:
    eq_mix = sp.Eq(-32 * A + 32 * B - 8 * C + 4 * G - 16 * pi2, -112)

    G_from_mix = sp.solve(eq_mix, G)[0]
    X_from_barnes = sp.simplify(sp.solve(eq_sym.subs(G, G_from_mix), X)[0])
    X_target_reduction = sp.simplify(2 * A + 4 * B - C + sp.Rational(25, 2) - 3 * pi2 / 2)
    assert sp.simplify(X_from_barnes - X_target_reduction) == 0

    # High-precision numerical mixed expectations.
    EA = even_expectation(lambda t: D(t) ** 2 * q(t) ** 2)
    EB = even_expectation(lambda t: D(t) * q(t) * Dp(t))
    EC = even_expectation(lambda t: Dp(t) ** 2)
    EX = even_expectation(lambda t: D(t) ** 4)

    cand_A = mp.mpf("0.5") - 2 * mp.log(2) + 4 * mp.log(2) ** 2
    cand_B = -3 + 4 * mp.log(2) + mp.pi**2 / 6
    cand_C = 16 * mp.log(2) - 2 * mp.pi**2 / 3
    cand_X = 2 * cand_A + 4 * cand_B - cand_C + mp.mpf(25) / 2 - 3 * mp.pi**2 / 2
    cand_A4 = mp.mpf(3) / 8 - mp.log(2) + 2 * mp.log(2) ** 2 - mp.pi**2 / 24

    for lhs, rhs in ((EA, cand_A), (EB, cand_B), (EC, cand_C), (EX, cand_X)):
        assert abs(lhs - rhs) < mp.mpf("1e-65")
    assert abs(EX / 4 - cand_A4) < mp.mpf("1e-65")

    # Independent PSLQ recovery with a deliberately small basis.
    rel_A = mp.pslq(mp.matrix([EA, 1, mp.log(2), mp.log(2) ** 2, mp.pi**2]),
                    tol=mp.mpf("1e-60"), maxcoeff=10000, maxsteps=10000)
    rel_B = mp.pslq(mp.matrix([EB, 1, mp.log(2), mp.log(2) ** 2, mp.pi**2]),
                    tol=mp.mpf("1e-60"), maxcoeff=10000, maxsteps=10000)
    rel_C = mp.pslq(mp.matrix([EC, 1, mp.log(2), mp.log(2) ** 2, mp.pi**2]),
                    tol=mp.mpf("1e-60"), maxcoeff=10000, maxsteps=10000)

    assert rel_A == [-2, 1, -4, 8, 0]
    assert rel_B == [-6, -18, 24, 0, 1]
    assert rel_C == [-3, 0, 48, 0, -2]

    print("Barnes ratios:", ratios)
    print("Exact reduction:")
    print("  E[D^4] = 2 E[D^2 q^2] + 4 E[D q D'] - E[(D')^2] + 25/2 - 3*pi^2/2")
    print("Mixed expectations (90-digit quadrature):")
    print("  E[D^2 q^2] =", mp.nstr(EA, 60))
    print("  PSLQ:", rel_A)
    print("  E[D q D']   =", mp.nstr(EB, 60))
    print("  PSLQ:", rel_B)
    print("  E[(D')^2]   =", mp.nstr(EC, 60))
    print("  PSLQ:", rel_C)
    print("  E[D^4]      =", mp.nstr(EX, 60))
    print("  A4           =", mp.nstr(EX / 4, 60))
    print("PASS: exact Barnes A4 reduction; three mixed evaluations remain analytic proof targets")


if __name__ == "__main__":
    main()
