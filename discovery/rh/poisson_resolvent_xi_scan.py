#!/usr/bin/env python3
"""Zero-free Poisson-resolvent diagnostic for finite zeta spectral triples.

For the reversal-even finite Weil ground vector c_k, its centered entire
Fourier transform can be written

    F_j(z) = 2 sin(z L/2)/sqrt(L) * S_j(z),
    S_j(z) = sum_{k=-N}^N c_k/(z - 2*pi*k/L),

with removable singularities at the free lattice points.

At positive height omega we compare the logarithmic derivative of the shifted
scattering ratio

    Theta_j,omega(z)=F_j(z-i omega)/F_j(z+i omega)

against the zero-independent completed-zeta target

    Theta_xi,omega(z)
      = xi(1/2-omega-i z)/xi(1/2+omega-i z).

On the real axis,

    (1/i) d_x log Theta_j,omega(x)
      = (1/i)[B_j(x-i omega)-B_j(x+i omega)],

and the target equals

    2 Re (xi'/xi)(1/2+omega-i x).

No Riemann-zero ordinates or root finding are used.
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


def xi_entire(s):
    """Entire xi evaluation with the zeta pole analytically cancelled.

    We use zeta(s)=eta(s)/(1-2^(1-s)) and keep
        (s-1)/(1-2^(1-s))
    as one removable factor.  This is stable at s=1, which occurs in the
    omega=1/2, x=0 diagnostic and defeated the naive xi'/xi formula.
    """
    log2 = mp.log(2)
    t = s - 1
    if abs(t) < mp.mpf("1e-8"):
        # Bernoulli expansion of t/(1-exp(-log(2)t)).
        # Keeping the linear term is essential: ratio'(0)=1/2.
        # A constant removable-value patch gives a WRONG xi'/xi(1).
        ratio = (
            1 / log2
            + t / 2
            + log2 * t**2 / 12
            - log2**3 * t**4 / 720
            + log2**5 * t**6 / 30240
            - log2**7 * t**8 / 1209600
        )
    else:
        ratio = t / (-mp.expm1(-t * log2))
    return (
        mp.mpf("0.5")
        * s
        * ratio
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.altzeta(s)
    )


def xi_logder(s):
    """xi'/xi evaluated from the entire xi, including removable points."""
    x = xi_entire(s)
    return mp.diff(xi_entire, s) / x


def finite_logder(z, coeff, L):
    """F'/F for F=2 sin(zL/2)/sqrt(L) sum c_k/(z-a_k)."""
    N = (len(coeff) - 1) // 2
    S = mp.mpc(0)
    Sp = mp.mpc(0)
    for k in range(-N, N + 1):
        a = 2 * mp.pi * k / L
        den = z - a
        ck = coeff[k + N]
        S += ck / den
        Sp -= ck / (den * den)
    return (L / 2) * (mp.cos(z * L / 2) / mp.sin(z * L / 2)) + Sp / S


def pfinite(x, omega, coeff, L):
    bm = finite_logder(x - 1j * omega, coeff, L)
    bp = finite_logder(x + 1j * omega, coeff, L)
    val = (bm - bp) / (1j)
    return mp.re(val)


def ptarget(x, omega):
    s = mp.mpf("0.5") + omega - 1j * x
    return 2 * mp.re(xi_logder(s))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--c", type=int, required=True)
    ap.add_argument("--N", type=int, default=28)
    ap.add_argument("--T", type=int, default=300)
    ap.add_argument("--dps", type=int, default=70)
    ap.add_argument("--xmax", type=float, default=50.0)
    ap.add_argument("--nx", type=int, default=101)
    ap.add_argument("--omegas", default="0.25,0.5,1.0,2.0")
    ap.add_argument("--out", default="result.json")
    a = ap.parse_args()

    mp.mp.dps = a.dps
    t0 = time.time()

    Q = cc.build_galerkin_matrix(a.c, N=a.N, T=a.T, dps=a.dps)
    Ve, Qe = sector_matrix(Q, "even")
    eig, U = mp.eigsy(Qe)
    ground_even = U[:, 0]
    full = Ve * ground_even

    # Normalize in the ordinary L2/Fourier coefficient norm.
    norm = mp.sqrt((full.T * full)[0])
    full /= norm
    coeff = [mp.mpf(full[i]) for i in range(full.rows)]
    L = mp.log(a.c)

    xs = [mp.mpf(a.xmax) * j / (a.nx - 1) for j in range(a.nx)]
    omegas = [mp.mpf(s.strip()) for s in a.omegas.split(",") if s.strip()]

    rows = []
    for om in omegas:
        err2 = mp.mpf(0)
        target2 = mp.mpf(0)
        max_abs = mp.mpf(0)
        max_rel = mp.mpf(0)
        min_fin = mp.inf
        min_tar = mp.inf
        for x in xs:
            pf = pfinite(x, om, coeff, L)
            pt = ptarget(x, om)
            e = pf - pt
            err2 += e * e
            target2 += pt * pt
            max_abs = max(max_abs, abs(e))
            if abs(pt) > mp.mpf("1e-30"):
                max_rel = max(max_rel, abs(e / pt))
            min_fin = min(min_fin, pf)
            min_tar = min(min_tar, pt)
        rms_rel = mp.sqrt(err2 / target2) if target2 else mp.nan
        rows.append({
            "omega": mp.nstr(om, 20),
            "rms_relative_error": mp.nstr(rms_rel, 30),
            "max_absolute_error": mp.nstr(max_abs, 30),
            "max_pointwise_relative_error": mp.nstr(max_rel, 30),
            "min_finite_poisson_density": mp.nstr(min_fin, 30),
            "min_target_density": mp.nstr(min_tar, 30),
        })

    rec = {
        "c": a.c,
        "N": a.N,
        "T": a.T,
        "dps": a.dps,
        "xmax": a.xmax,
        "nx": a.nx,
        "L": mp.nstr(L, 30),
        "ground_eigenvalue": mp.nstr(eig[0], 30),
        "uses_zero_data": False,
        "uses_root_finding": False,
        "rows": rows,
        "seconds": round(time.time() - t0, 1),
    }
    open(a.out, "w").write(json.dumps(rec))
    print(json.dumps(rec), flush=True)


if __name__ == "__main__":
    main()
