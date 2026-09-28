#!/usr/bin/env python3
"""Literal CCM prolate k_lambda vacuum-gap diagnostic, arbitrary precision.

No zeta-zero ordinates are used.

Implements the Connes--Consani--Moscovici prolate trial state

    PW_lambda h = -d/dx((lambda^2-x^2)h') + (2*pi*lambda*x)^2 h,
    k_lambda(u) = sqrt(u) sum_{n>=1} h_lambda(nu),

where h_lambda is the unique (up to scale) linear combination of the n=0
and n=4 even prolate modes with vanishing integral.

Two numerical details matter critically:

1. The prolate eigenproblem is solved with mpmath eigsy in the orthonormal
   even Legendre basis.  Float64 prolate vectors create an O(1e-30)
   Rayleigh floor after squaring, which is already much larger than the
   finite Weil gaps at c>=11.

2. Fourier coefficients of k_lambda are evaluated ANALYTICALLY.  Since the
   Galerkin h_lambda is a finite Legendre polynomial, k_lambda(e^y) is a
   finite piecewise sum of exponentials.  The log-Fourier integrals are
   therefore elementary exponentials, so no float quadrature is needed.

This makes the diagnostic capable in principle of following the tiny finite
Weil gaps rather than hitting an unrelated double-precision floor.
"""

from __future__ import annotations

import argparse
import json
import time

import mpmath as mp
import connes_cvs as cc


def sector_matrix(Q, parity: str):
    dim = Q.rows
    N = (dim - 1) // 2
    invsqrt2 = 1 / mp.sqrt(2)
    if parity == "even":
        V = mp.matrix(dim, N + 1)
        V[N, 0] = 1
        for k in range(1, N + 1):
            V[N + k, k] = invsqrt2
            V[N - k, k] = invsqrt2
    else:
        V = mp.matrix(dim, N)
        for k in range(1, N + 1):
            V[N + k, k - 1] = invsqrt2
            V[N - k, k - 1] = -invsqrt2
    return V, V.T * Q * V


def leg_a(l: int):
    return mp.mpf(l + 1) / mp.sqrt((2 * l + 1) * (2 * l + 3))


def leg_b(l: int):
    if l == 0:
        return mp.mpf("0")
    return mp.mpf(l) / mp.sqrt((2 * l - 1) * (2 * l + 1))


def legendre_power_polynomials(lmax: int):
    """P_l(z) in the monomial basis, all coefficients as mp.mpf."""
    P = [[mp.mpf(1)]]
    if lmax == 0:
        return P
    P.append([mp.mpf(0), mp.mpf(1)])
    for l in range(1, lmax):
        # P_{l+1} = ((2l+1) z P_l - l P_{l-1})/(l+1)
        out = [mp.mpf(0)] * (l + 2)
        fac1 = mp.mpf(2 * l + 1) / (l + 1)
        fac2 = mp.mpf(l) / (l + 1)
        for j, val in enumerate(P[l]):
            out[j + 1] += fac1 * val
        for j, val in enumerate(P[l - 1]):
            out[j] -= fac2 * val
        P.append(out)
    return P


def p_even_at_zero(l: int):
    """Exact P_l(0) for even l."""
    if l % 2:
        return mp.mpf(0)
    r = l // 2
    return ((-1) ** r) * mp.binomial(2 * r, r) / (mp.mpf(4) ** r)


def prolate_zero_integral_power_coeffs(c: int, lmax: int):
    """Return monomial coefficients of h_lambda(x) in z=x/lambda.

    The even Legendre Galerkin matrix is symmetric and tridiagonal.
    The first and third even eigenvectors are the n=0 and n=4 prolate modes.

    Because only P_0 has nonzero integral, the combination

        v4[0] v0 - v0[0] v4

    has exactly zero integral in the finite Galerkin representation.
    """
    if lmax % 2:
        lmax += 1
    lam = mp.sqrt(c)
    gamma = 2 * mp.pi * c
    ls = list(range(0, lmax + 1, 2))
    m = len(ls)

    M = mp.matrix(m)
    for i, l in enumerate(ls):
        M[i, i] = (
            l * (l + 1)
            + gamma**2 * (leg_a(l) ** 2 + leg_b(l) ** 2)
        )
        if i + 1 < m:
            off = gamma**2 * leg_a(l) * leg_a(l + 1)
            M[i, i + 1] = off
            M[i + 1, i] = off

    eigvals, eigvecs = mp.eigsy(M)

    # Orient the selected eigenvectors by their value at z=0.
    p0 = []
    for l in ls:
        p0.append(mp.sqrt(mp.mpf(2 * l + 1) / 2) * p_even_at_zero(l))

    for col in (0, 2):
        val0 = mp.fsum(eigvecs[i, col] * p0[i] for i in range(m))
        if val0 < 0:
            for i in range(m):
                eigvecs[i, col] = -eigvecs[i, col]

    v0 = [eigvecs[i, 0] for i in range(m)]
    v4 = [eigvecs[i, 2] for i in range(m)]
    comb = [v4[0] * v0[i] - v0[0] * v4[i] for i in range(m)]
    norm = mp.sqrt(mp.fsum(x * x for x in comb))
    comb = [x / norm for x in comb]

    # Standard Legendre coefficients of
    # h_lambda(x)=lambda^(-1/2) sum comb_l phi_l(x/lambda).
    legcoef = [mp.mpf(0)] * (lmax + 1)
    for i, l in enumerate(ls):
        legcoef[l] = (
            comb[i]
            * mp.sqrt(mp.mpf(2 * l + 1) / 2)
            / mp.sqrt(lam)
        )

    polys = legendre_power_polynomials(lmax)
    power = [mp.mpf(0)] * (lmax + 1)
    for l in ls:
        a_l = legcoef[l]
        if a_l == 0:
            continue
        for j, q in enumerate(polys[l]):
            power[j] += a_l * q

    # h is even; remove exact/roundoff odd noise.
    for j in range(1, len(power), 2):
        power[j] = mp.mpf(0)

    # Integral over x in [-lambda,lambda] is exactly 2 lambda * legcoef[0].
    h_integral = 2 * lam * legcoef[0]

    return eigvals, power, h_integral


def exp_integral(alpha, lo, hi):
    if hi <= lo:
        return mp.mpc(0)
    return (mp.exp(alpha * hi) - mp.exp(alpha * lo)) / alpha


def k_fourier_coeff(k: int, c: int, power):
    """Exact log-Fourier coefficient of k_lambda on [-A,A].

    k_lambda(e^y)
      = e^(y/2) sum_{1<=n<=lambda/e^y} h_lambda(n e^y).

    With h_lambda(z)=sum_m power[m] z^m in z=x/lambda, each active
    summand is a finite sum of exp((m+1/2)y).  Its support is
    y <= log(lambda/n), giving an elementary integral.
    """
    lam = mp.sqrt(c)
    L = mp.log(c)
    A = L / 2
    omega = 2 * mp.pi * k / L
    lo = -A

    total = mp.mpc(0)
    for n in range(1, c + 1):
        hi = mp.log(lam / n)
        if hi <= lo:
            continue
        n_over_lam = mp.mpf(n) / lam
        for m, coeff in enumerate(power):
            if coeff == 0:
                continue
            alpha = mp.mpf(m) + mp.mpf("0.5") - 1j * omega
            total += (
                coeff
                * (n_over_lam ** m)
                * exp_integral(alpha, lo, hi)
            )

    # Centered y to CCM x=y+A basis contributes exp(-i omega A)=(-1)^k.
    return ((-1) ** k) * total / mp.sqrt(L)


def prolate_fourier_vector(c: int, N: int, lmax: int):
    eigvals, power, h_integral = prolate_zero_integral_power_coeffs(c, lmax)

    coeffs_complex = [k_fourier_coeff(k, c, power) for k in range(-N, N + 1)]
    total_power = mp.fsum(abs(z) ** 2 for z in coeffs_complex)
    odd_power = mp.fsum(mp.im(z) ** 2 for z in coeffs_complex)
    odd_fraction = odd_power / total_power if total_power else mp.nan

    # Orthogonal projection to inversion-even sector = real part in centered basis.
    vals = [mp.re(z) for z in coeffs_complex]
    v = mp.matrix(vals)
    norm = mp.sqrt((v.T * v)[0])
    if norm == 0:
        raise RuntimeError("prolate k_lambda projection vanished")
    v /= norm

    diag = {
        "lambda": mp.nstr(mp.sqrt(c), 30),
        "prolate_gamma": mp.nstr(2 * mp.pi * c, 30),
        "prolate_eig0": mp.nstr(eigvals[0], 30),
        "prolate_eig4": mp.nstr(eigvals[2], 30),
        "h_integral": mp.nstr(h_integral, 30),
        "k_odd_fraction": mp.nstr(odd_fraction, 30),
    }
    return v, diag


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--c", type=int, required=True)
    p.add_argument("--N", type=int, default=28)
    p.add_argument("--T", type=int, default=300)
    p.add_argument("--dps", type=int, default=100)
    p.add_argument("--lmax", type=int, default=140)
    p.add_argument("--out", default="result.json")
    a = p.parse_args()

    mp.mp.dps = a.dps
    t0 = time.time()

    Q = cc.build_galerkin_matrix(a.c, N=a.N, T=a.T, dps=a.dps)
    Ve, Qe = sector_matrix(Q, "even")
    eig, U = mp.eigsy(Qe)
    l1, l2 = eig[0], eig[1]
    gap = l2 - l1

    vp, diag = prolate_fourier_vector(a.c, a.N, a.lmax)
    ve = Ve.T * vp
    ve /= mp.sqrt((ve.T * ve)[0])

    ray = (ve.T * Qe * ve)[0]
    resvec = Qe * ve - ray * ve
    res = mp.sqrt((resvec.T * resvec)[0])

    ground = U[:, 0]
    ov = abs((ground.T * ve)[0])
    angle_def = 1 - ov**2

    rex = ray - l1
    dist2 = abs(l2 - ray)
    ray_bound = rex / gap if gap != 0 else mp.inf
    dk = res / dist2 if dist2 != 0 else mp.inf

    rec = dict(
        c=a.c,
        N=a.N,
        T=a.T,
        dps=a.dps,
        lmax=a.lmax,
        L=mp.nstr(mp.log(a.c), 30),
        lam1=mp.nstr(l1, 40),
        lam2=mp.nstr(l2, 40),
        gap=mp.nstr(gap, 40),
        prolate_rayleigh=mp.nstr(ray, 40),
        rayleigh_excess=mp.nstr(rex, 40),
        residual_norm=mp.nstr(res, 40),
        overlap=mp.nstr(ov, 40),
        one_minus_overlap_sq=mp.nstr(angle_def, 40),
        rayleigh_excess_over_gap=mp.nstr(ray_bound, 40),
        residual_over_dist2=mp.nstr(dk, 40),
        seconds=round(time.time() - t0, 1),
        uses_zero_data=False,
        analytic_fourier=True,
        arbitrary_precision_prolate=True,
        **diag,
    )
    open(a.out, "w").write(json.dumps(rec))
    print(json.dumps(rec), flush=True)


if __name__ == "__main__":
    main()
