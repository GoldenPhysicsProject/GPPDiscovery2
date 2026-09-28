#!/usr/bin/env python3
"""Literal CCM prolate k_lambda vacuum-gap diagnostic.

Implements the "educated guess" of Connes--Consani--Moscovici, Zeta
Spectral Triples, eqs. (7.5)--(7.6), without zeta-zero data:

    PW_lambda = -d/dx ((lambda^2-x^2)d/dx) + (2 pi lambda x)^2,
    k_lambda(u) = E(h_lambda)(u)
                = sqrt(u) sum_{n>=1} h_lambda(nu),

where h_lambda is the (unique up to scale) linear combination of the n=0
and n=4 even prolate modes with vanishing integral.

The prolate modes are computed by a stable Legendre-Galerkin diagonalization
rather than scipy.special.pro_ang1.  In the orthonormal Legendre basis,
multiplication by z^2 is tridiagonal on each parity sector, so the
discretization is symmetric and zero-independent.

For u in [lambda^-1,lambda], h_lambda is the time-limited prolate profile
on [-lambda,lambda], so the E-sum has at most lambda^2 terms.

The script projects the even part of k_lambda into the same finite Weil basis
as connes-cvs and measures its overlap, Rayleigh excess, residual, and
excitation gap relative to the true finite even ground state.

No Riemann-zero ordinates are used.
"""

from __future__ import annotations

import argparse
import json
import math
import time

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss, legval
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


def _a(l: int) -> float:
    """Coefficient of phi_{l+1} in z phi_l for orthonormal Legendre phi."""
    return (l + 1) / math.sqrt((2 * l + 1) * (2 * l + 3))


def _b(l: int) -> float:
    """Coefficient of phi_{l-1} in z phi_l."""
    if l == 0:
        return 0.0
    return l / math.sqrt((2 * l - 1) * (2 * l + 1))


def prolate_zero_integral_coeffs(lam: float, lmax: int = 180):
    """Return standard-Legendre coefficients of normalized h_lambda.

    Scale x=lambda*z.  Up to an irrelevant additive constant in the
    eigenvalue, the prolate operator becomes

        -d_z((1-z^2)d_z) + gamma^2 z^2, gamma=2*pi*lambda^2.

    On the even orthonormal Legendre basis phi_l, l=0,2,..., z^2 couples only
    l to l and l+/-2.

    The first and third even eigenvectors are the modes labelled n=0 and n=4.
    Since all Legendre modes l>0 integrate to zero, the integral of an
    eigenfunction is determined only by its l=0 coefficient.  Hence

        h_lambda ~ v4[0] h0 - v0[0] h4

    has *exactly* vanishing integral in this Galerkin representation.
    """
    if lmax % 2:
        lmax += 1
    ls = np.arange(0, lmax + 1, 2, dtype=int)
    m = len(ls)

    z2 = np.zeros((m, m), dtype=float)
    for i, l in enumerate(ls):
        z2[i, i] = _a(int(l)) ** 2 + _b(int(l)) ** 2
        if i + 1 < m:
            off = _a(int(l)) * _a(int(l) + 1)
            z2[i, i + 1] = off
            z2[i + 1, i] = off

    gamma = 2.0 * math.pi * lam * lam
    op = np.diag(ls * (ls + 1)).astype(float) + (gamma * gamma) * z2
    eigvals, eigvecs = np.linalg.eigh(op)

    # Orient n=0 and n=4 modes so their value at z=0 is positive.
    p0 = np.zeros(m)
    for i, l in enumerate(ls):
        unit = np.zeros(int(l) + 1)
        unit[int(l)] = 1.0
        p0[i] = math.sqrt((2 * int(l) + 1) / 2.0) * legval(0.0, unit)
    for col in (0, 2):
        if float(np.dot(eigvecs[:, col], p0)) < 0:
            eigvecs[:, col] *= -1

    v0 = eigvecs[:, 0]
    v4 = eigvecs[:, 2]
    comb = v4[0] * v0 - v0[0] * v4
    comb /= np.linalg.norm(comb)

    # Standard Legendre coefficients for the x-normalized function
    # h_lambda(x)=lambda^{-1/2} sum c_l phi_l(x/lambda).
    coeff = np.zeros(lmax + 1, dtype=float)
    for i, l in enumerate(ls):
        coeff[int(l)] = (
            comb[i] * math.sqrt((2 * int(l) + 1) / 2.0) / math.sqrt(lam)
        )

    # Because the standard P_0 coefficient is zero, integral is exactly zero
    # up to floating arithmetic.
    integral = 2.0 * lam * coeff[0]
    return eigvals, coeff, integral


def h_eval(x: np.ndarray, lam: float, coeff: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    z = x / lam
    out = np.zeros_like(z)
    mask = np.abs(z) <= 1.0 + 5e-14
    if np.any(mask):
        zz = np.clip(z[mask], -1.0, 1.0)
        out[mask] = legval(zz, coeff)
    return out


def k_eval_log(y: np.ndarray, lam: float, coeff: np.ndarray) -> np.ndarray:
    """Evaluate k_lambda(exp y)=sqrt(u) sum h_lambda(nu)."""
    y = np.asarray(y, dtype=float)
    u = np.exp(y)
    out = np.zeros_like(u)
    max_n = int(math.floor(lam * lam + 1e-10))
    for n in range(1, max_n + 1):
        mask = n * u <= lam * (1.0 + 5e-14)
        if np.any(mask):
            out[mask] += h_eval(n * u[mask], lam, coeff)
    return np.sqrt(u) * out


def prolate_fourier_vector(
    c: int,
    N: int,
    lmax: int = 180,
    quad_n: int = 1200,
):
    """Project the even part of literal k_lambda into the CCM Fourier basis."""
    lam = math.sqrt(c)
    L = math.log(c)
    A = L / 2.0

    peigs, coeff, h_integral = prolate_zero_integral_coeffs(lam, lmax=lmax)

    gx, gw = leggauss(quad_n)
    y = A * gx
    w = A * gw

    kp = k_eval_log(y, lam, coeff)
    km = k_eval_log(-y, lam, coeff)
    ke = 0.5 * (kp + km)
    ko = 0.5 * (kp - km)

    even_norm2 = float(np.dot(w, ke * ke))
    odd_norm2 = float(np.dot(w, ko * ko))
    odd_fraction = odd_norm2 / max(even_norm2 + odd_norm2, 1e-300)

    coeffs = [0.0] * (2 * N + 1)
    for k in range(0, N + 1):
        omega = 2.0 * math.pi * k / L
        integ = float(np.dot(w, ke * np.cos(omega * y)))
        ak = ((-1) ** k) * integ / math.sqrt(L)
        coeffs[N + k] = ak
        coeffs[N - k] = ak

    v = mp.matrix([mp.mpf(str(x)) for x in coeffs])
    norm = mp.sqrt((v.T * v)[0])
    if norm == 0:
        raise RuntimeError("prolate k_lambda projection vanished")
    v /= norm

    diag = {
        "lambda": lam,
        "prolate_gamma": 2.0 * math.pi * lam * lam,
        "prolate_eig0": float(peigs[0]),
        "prolate_eig4": float(peigs[2]),
        "h_integral": h_integral,
        "k_odd_fraction": odd_fraction,
        "projected_even_norm2": even_norm2,
    }
    return v, diag


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--c", type=int, required=True)
    p.add_argument("--N", type=int, default=28)
    p.add_argument("--T", type=int, default=300)
    p.add_argument("--dps", type=int, default=70)
    p.add_argument("--lmax", type=int, default=180)
    p.add_argument("--quad", type=int, default=1200)
    p.add_argument("--out", default="result.json")
    a = p.parse_args()

    mp.mp.dps = a.dps
    t0 = time.time()

    Q = cc.build_galerkin_matrix(a.c, N=a.N, T=a.T, dps=a.dps)
    Ve, Qe = sector_matrix(Q, "even")
    eig, U = mp.eigsy(Qe)
    l1, l2 = eig[0], eig[1]
    gap = l2 - l1

    vp, diag = prolate_fourier_vector(
        a.c, a.N, lmax=a.lmax, quad_n=a.quad
    )
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
        quad=a.quad,
        L=float(mp.log(a.c)),
        lam1=mp.nstr(l1, 30),
        lam2=mp.nstr(l2, 30),
        gap=mp.nstr(gap, 30),
        prolate_rayleigh=mp.nstr(ray, 30),
        rayleigh_excess=mp.nstr(rex, 30),
        residual_norm=mp.nstr(res, 30),
        overlap=mp.nstr(ov, 30),
        one_minus_overlap_sq=mp.nstr(angle_def, 30),
        rayleigh_excess_over_gap=mp.nstr(ray_bound, 30),
        residual_over_dist2=mp.nstr(dk, 30),
        seconds=round(time.time() - t0, 1),
        uses_zero_data=False,
        **diag,
    )
    open(a.out, "w").write(json.dumps(rec))
    print(json.dumps(rec), flush=True)


if __name__ == "__main__":
    main()
