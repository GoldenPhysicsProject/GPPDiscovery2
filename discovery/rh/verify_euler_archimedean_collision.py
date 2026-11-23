#!/usr/bin/env python3
"""Zero-free verification of the Euler–Archimedean collision decomposition.

No zeta zero table is read.  The script compares
    Q = W02 - WR - WP
against
    Q = 2 M_L I + sum Lambda(n)/sqrt(n) D_log(n)
        - integral_0^L w_inf(y) D_y dy,
where D_y = 2 I - q(y).

It also checks the integral and closed forms of M_L and samples the
positive-semidefinite collision matrices D_y.
"""

import argparse
import mpmath as mp


def von_mangoldt(n: int):
    """Lambda(n), exactly by detecting prime powers using integer trial division."""
    if n < 2:
        return mp.mpf("0")
    # Find the first prime divisor.
    p = None
    x = n
    d = 2
    while d * d <= x:
        if x % d == 0:
            p = d
            break
        d += 1 if d == 2 else 2
    if p is None:
        return mp.log(n)  # prime
    while x % p == 0:
        x //= p
    if x == 1:
        return mp.log(p)
    return mp.mpf("0")


def q_entry(L, y, n, m):
    if n == m:
        return 2 * (1 - y / L) * mp.cos(2 * mp.pi * n * y / L)
    return (
        mp.sin(2 * mp.pi * m * y / L)
        - mp.sin(2 * mp.pi * n * y / L)
    ) / (mp.pi * (n - m))


def D_entry(L, y, n, m):
    return (mp.mpf(2) if n == m else mp.mpf(0)) - q_entry(L, y, n, m)


def w02_entry(L, n, m):
    return (
        32
        * L
        * mp.sinh(L / 4) ** 2
        * (L**2 - 16 * mp.pi**2 * m * n)
        / ((L**2 + 16 * mp.pi**2 * m**2) * (L**2 + 16 * mp.pi**2 * n**2))
    )


def rho(y):
    return mp.e ** (y / 2) / (mp.e**y - mp.e ** (-y))


def r_density(y):
    return 1 / (mp.e**y - mp.e ** (-y))


def w_inf(y):
    return 2 * mp.cosh(y / 2) - rho(y)


def tau_L(L):
    return mp.mpf("0.5") * mp.log((mp.e**L + 1) / (mp.e**L - 1))


def c0():
    return mp.log(4 * mp.pi) + mp.euler


def wr_entry(L, n, m):
    # Keep the singular pieces combined before quadrature.
    q0 = mp.mpf(2) if n == m else mp.mpf(0)

    def integrand(y):
        return rho(y) * q_entry(L, y, n, m) - r_density(y) * q0

    val = mp.quad(integrand, [0, L])
    if n == m:
        val += c0() - 2 * tau_L(L)
    return val


def prime_power_terms(L):
    upper = int(mp.floor(mp.e**L))
    out = []
    for n in range(2, upper + 1):
        lam = von_mangoldt(n)
        if lam:
            out.append((n, lam / mp.sqrt(n)))
    return out


def wp_entry(L, n, m, terms):
    return mp.fsum(c * q_entry(L, mp.log(k), n, m) for k, c in terms)


def S_L(terms):
    return mp.fsum(c for _, c in terms)


def int_wr(L):
    return mp.quad(lambda y: w_inf(y) + r_density(y), [0, L])


def int_wr_closed(L):
    q = mp.e ** (-L / 2)
    return (
        2 * (mp.e ** (L / 2) - mp.e ** (-L / 2))
        + mp.log(1 + q)
        - mp.mpf("0.5") * mp.log(1 + q * q)
        + mp.atan(q)
        - mp.mpf("0.5") * mp.log(2)
        - mp.pi / 4
    )


def M_integral(L, terms):
    return int_wr(L) - (c0() - 2 * tau_L(L)) / 2 - S_L(terms)


def M_closed(L, terms):
    q = mp.e ** (-L / 2)
    return (
        2 * (mp.e ** (L / 2) - mp.e ** (-L / 2))
        - S_L(terms)
        + mp.atanh(q)
        - mp.mpf("0.5") * mp.atan(mp.sinh(L / 2))
        - mp.mpf("0.5") * mp.log(2)
        - mp.mpf("0.5") * c0()
    )


def collision_entry(L, n, m, terms, M):
    out = 2 * M if n == m else mp.mpf(0)
    out += mp.fsum(c * D_entry(L, mp.log(k), n, m) for k, c in terms)
    out -= mp.quad(lambda y: w_inf(y) * D_entry(L, y, n, m), [0, L])
    return out


def direct_entry(L, n, m, terms):
    return w02_entry(L, n, m) - wr_entry(L, n, m) - wp_entry(L, n, m, terms)


def matrix_from(fun, N):
    inds = list(range(-N, N + 1))
    return mp.matrix([[fun(n, m) for m in inds] for n in inds])


def min_eigenvalue_real_symmetric(A):
    vals, _ = mp.eigsy(A)
    return min(vals)


def run_case(L_string, N):
    L = mp.mpf(L_string)
    terms = prime_power_terms(L)
    Mint = M_integral(L, terms)
    Mcl = M_closed(L, terms)
    Qd = matrix_from(lambda n, m: direct_entry(L, n, m, terms), N)
    Qc = matrix_from(lambda n, m: collision_entry(L, n, m, terms, Mcl), N)

    dim = 2 * N + 1
    residual = max(abs(Qd[i, j] - Qc[i, j]) for i in range(dim) for j in range(dim))

    samples = [L / 7, L / 3, L / 2, 5 * L / 6]
    dmins = []
    for y in samples:
        D = matrix_from(lambda n, m: D_entry(L, y, n, m), N)
        dmins.append((y, min_eigenvalue_real_symmetric(D)))

    print(f"L={mp.nstr(L, 20)} N={N} prime-powers={len(terms)}")
    print("S_L =", mp.nstr(S_L(terms), 45))
    print("M_L (integral) =", mp.nstr(Mint, 45))
    print("M_L (closed)   =", mp.nstr(Mcl, 45))
    print("|M_int-M_closed| =", mp.nstr(abs(Mint - Mcl), 12))
    print("max matrix residual =", mp.nstr(residual, 12))
    print("min eig Q_direct =", mp.nstr(min_eigenvalue_real_symmetric(Qd), 20))
    for y, ev in dmins:
        print("min eig D_y at y/L=",
              mp.nstr(y / L, 8), ":", mp.nstr(ev, 16))
    print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--N", type=int, default=2)
    parser.add_argument("--L", action="append", default=None,
                        help="Decimal support length; repeat for multiple cases.")
    args = parser.parse_args()
    mp.mp.dps = args.dps
    cases = args.L or ["1.2", "2.0", "3.0"]
    for Ls in cases:
        run_case(Ls, args.N)


if __name__ == "__main__":
    main()
