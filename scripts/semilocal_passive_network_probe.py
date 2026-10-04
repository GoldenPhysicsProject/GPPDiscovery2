#!/usr/bin/env python3
"""Semilocal Weil passive-network probe.

Zero-free experiment on the exact Connes--Consani--Moscovici truncated Weil matrix.
It audits the decomposition suggested by the Oct. 4 Arrow roadmap:

    Q = W02 - WR - WP
      = L_prime + (W02 - WR - 2 S I),

where
    L_prime = sum_{prime powers k <= lambda^2} (Lambda(k)/sqrt(k)) (2I - Omega_logk)
and Omega_y is the compressed T_y + T_y^* matrix on the interval.

The identity 2I-Omega_y >= 0 is the finite interval version of
||f-T_y f||^2 >= 0 after zero extension.

The script then resolves parity and tests the sharper candidate mechanism:
    A := -WR-WP = (L_prime-WR) - 2 S I.
If C := L_prime-WR is a passive Dirichlet network, then
  odd:  lambda_min(C_odd) > 2S  would give A_odd > 0;
  even: exactly one eigenvalue below 2S would give the observed Hodge-index inertia;
the rank-one pole vectors c,s in W02 then perform the final even/odd updates.

No zeta zeros are read anywhere.
"""

from __future__ import annotations
import argparse, json, math
from pathlib import Path
import mpmath as mp
import numpy as np


def von_mangoldt(k: int) -> mp.mpf:
    for p in range(2, k + 1):
        if k % p:
            continue
        if any(p % d == 0 for d in range(2, int(math.isqrt(p)) + 1)):
            continue
        m = k
        while m % p == 0:
            m //= p
        return mp.log(p) if m == 1 else mp.mpf("0")
    return mp.mpf("0")


def build(lam: float, N: int, dps: int):
    mp.mp.dps = dps
    lam = mp.mpf(lam)
    L = 2 * mp.log(lam)
    pi = mp.pi
    idx = list(range(-N, N + 1))
    dim = 2 * N + 1

    rho = lambda x: mp.exp(x / 2) / (mp.exp(x) - mp.exp(-x))

    K = int(mp.floor(lam**2 + mp.mpf("1e-30")))
    terms = [(k, von_mangoldt(k)) for k in range(2, K + 1)]
    terms = [(k, c) for k, c in terms if c != 0]

    def omega(n: int, m: int, y: mp.mpf):
        if n != m:
            return (
                mp.sin(2 * pi * m * y / L) - mp.sin(2 * pi * n * y / L)
            ) / (pi * (n - m))
        return 2 * (L - y) * mp.cos(2 * pi * n * y / L) / L

    alpha = {
        n: mp.quad(lambda x: mp.sin(2 * pi * n * x / L) * rho(x), [0, L]) / pi
        for n in range(0, N + 1)
    }
    for n in range(1, N + 1):
        alpha[-n] = -alpha[n]

    tail = mp.log((mp.exp(L) + 1) / (mp.exp(L) - 1)) / 2
    diagR = {}
    for n in range(0, N + 1):
        integ = mp.quad(
            lambda y: (
                mp.exp(y / 2)
                * 2
                * (1 - y / L)
                * mp.cos(2 * pi * n * y / L)
                - 2
            )
            / (mp.exp(y) - mp.exp(-y)),
            [0, L],
        )
        diagR[n] = mp.log(4 * pi) + mp.euler + integ - 2 * tail
        diagR[-n] = diagR[n]

    W02 = np.zeros((dim, dim), dtype=float)
    WR = np.zeros((dim, dim), dtype=float)
    WP = np.zeros((dim, dim), dtype=float)

    weights = [(k, c * mp.mpf(k) ** (-mp.mpf("0.5"))) for k, c in terms]
    S = sum((w for _, w in weights), mp.mpf("0"))

    for a, n in enumerate(idx):
        for b, m in enumerate(idx):
            w02 = (
                32
                * L
                * mp.sinh(L / 4) ** 2
                * (L**2 - 16 * pi**2 * m * n)
                / (
                    (L**2 + 16 * pi**2 * m**2)
                    * (L**2 + 16 * pi**2 * n**2)
                )
            )
            wr = diagR[n] if n == m else (alpha[m] - alpha[n]) / (n - m)
            wp = sum(w * omega(n, m, mp.log(k)) for k, w in weights)
            W02[a, b] = float(w02)
            WR[a, b] = float(wr)
            WP[a, b] = float(wp)

    S = float(S)
    I = np.eye(dim)
    Q = W02 - WR - WP
    Lprime = 2 * S * I - WP
    Rmass = W02 - WR - 2 * S * I
    A = -WR - WP
    C = Lprime - WR

    # Exact rank-two pole vectors: W02 = 1/2 cc^T - 1/2 ss^T.
    sh = float(mp.sinh(L / 4))
    Lf = float(L)
    amp = 8 * math.sqrt(Lf) * sh
    cvec = np.array([
        amp * Lf / (Lf**2 + 16 * math.pi**2 * n**2) for n in idx
    ])
    svec = np.array([
        amp * (4 * math.pi * n) / (Lf**2 + 16 * math.pi**2 * n**2) for n in idx
    ])

    return {
        "lambda": float(lam),
        "N": N,
        "L": Lf,
        "idx": idx,
        "prime_powers": [k for k, _ in weights],
        "S": S,
        "W02": W02,
        "WR": WR,
        "WP": WP,
        "Q": Q,
        "Lprime": Lprime,
        "Rmass": Rmass,
        "A": A,
        "C": C,
        "c": cvec,
        "s": svec,
    }


def parity_frames(N: int):
    d = 2 * N + 1
    E = np.zeros((d, N + 1))
    O = np.zeros((d, N))
    # index n=-N,...,N => array slot n+N
    E[N, 0] = 1.0
    for n in range(1, N + 1):
        E[N + n, n] = 1 / math.sqrt(2)
        E[N - n, n] = 1 / math.sqrt(2)
        O[N + n, n - 1] = 1 / math.sqrt(2)
        O[N - n, n - 1] = -1 / math.sqrt(2)
    return E, O


def eig(M):
    return np.linalg.eigvalsh((M + M.T) / 2)


def inertia(vals, tol=1e-11):
    return {
        "negative": int(np.sum(vals < -tol)),
        "zeroish": int(np.sum(np.abs(vals) <= tol)),
        "positive": int(np.sum(vals > tol)),
    }


def analyse(d):
    N = d["N"]
    E, O = parity_frames(N)
    out = {
        "lambda": d["lambda"],
        "N": N,
        "L": d["L"],
        "prime_powers": d["prime_powers"],
        "S": d["S"],
    }

    decomp = d["Q"] - (d["Lprime"] + d["Rmass"])
    pole_resid = d["W02"] - 0.5 * np.outer(d["c"], d["c"]) + 0.5 * np.outer(d["s"], d["s"])
    out["identity_residual_inf"] = float(np.max(np.abs(decomp)))
    out["pole_rank2_residual_inf"] = float(np.max(np.abs(pole_resid)))

    for name in ["Q", "Lprime", "Rmass", "A", "C", "WR"]:
        M = d[name]
        vals = eig(M)
        out[name] = {
            "min": float(vals[0]),
            "max": float(vals[-1]),
            "inertia": inertia(vals),
        }
        Me = E.T @ M @ E
        Mo = O.T @ M @ O
        ve = eig(Me)
        vo = eig(Mo) if N > 0 else np.array([])
        out[name]["even_min"] = float(ve[0])
        out[name]["even_inertia"] = inertia(ve)
        if len(vo):
            out[name]["odd_min"] = float(vo[0])
            out[name]["odd_inertia"] = inertia(vo)

    # Passive-network threshold test C - 2 S I = A.
    Ce = E.T @ d["C"] @ E
    Co = O.T @ d["C"] @ O
    ce = eig(Ce)
    co = eig(Co)
    threshold = 2 * d["S"]
    out["passive_threshold"] = {
        "2S": threshold,
        "C_even_below_2S": int(np.sum(ce < threshold - 1e-11)),
        "C_odd_below_2S": int(np.sum(co < threshold - 1e-11)),
        "C_even_lowest_minus_2S": float(ce[0] - threshold),
        "C_even_second_minus_2S": float(ce[1] - threshold) if len(ce) > 1 else None,
        "C_odd_lowest_minus_2S": float(co[0] - threshold),
    }

    # Rank-one pole update diagnostics in parity coordinates.
    Ae = E.T @ d["A"] @ E
    Ao = O.T @ d["A"] @ O
    cevec = E.T @ d["c"]
    soveс = O.T @ d["s"]
    # Solve only if numerically nonsingular.
    out["pole_scalar"] = {}
    try:
        out["pole_scalar"]["c_Ae_inv_c"] = float(cevec @ np.linalg.solve(Ae, cevec))
    except np.linalg.LinAlgError:
        out["pole_scalar"]["c_Ae_inv_c"] = None
    try:
        out["pole_scalar"]["s_Ao_inv_s"] = float(soveс @ np.linalg.solve(Ao, soveс))
    except np.linalg.LinAlgError:
        out["pole_scalar"]["s_Ao_inv_s"] = None

    # Alignment of the most negative mass direction with c/s and parity boundary vectors.
    vals, vecs = np.linalg.eigh((d["Rmass"] + d["Rmass"].T) / 2)
    v = vecs[:, 0]
    def ov(w):
        nw = np.linalg.norm(w)
        return float(abs(v @ w) / nw) if nw else 0.0
    out["Rmass_ground_alignment"] = {
        "with_c": ov(d["c"]),
        "with_s": ov(d["s"]),
        "parity_even_norm": float(np.linalg.norm(E.T @ v)),
        "parity_odd_norm": float(np.linalg.norm(O.T @ v)),
    }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dps", type=int, default=50)
    ap.add_argument("--output", default="results/semilocal_passive_network_probe.json")
    args = ap.parse_args()

    cases = [(1.5, 8), (2.0, 10), (2.5, 12), (3.0, 12), (3.6, 14), (4.2, 16)]
    results = []
    for lam, N in cases:
        print(f"[probe] lambda={lam} N={N}", flush=True)
        results.append(analyse(build(lam, N, args.dps)))

    out = {"status": "numerical probe, zero-free", "cases": results}
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2))

    md = path.with_suffix(".md")
    lines = [
        "# Semilocal passive-network probe",
        "",
        "Zero-free CCM matrix decomposition. Values near 1e-10 or below should be treated as numerical floor, not signs.",
        "",
        "| lambda | N | prime powers | min Lprime | neg Rmass | neg A | Codd-2S | Ceven below 2S | cAe^-1c | sAo^-1s |",
        "|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for x in results:
        ps = ",".join(map(str, x["prime_powers"]))
        p = x["passive_threshold"]
        sc = x["pole_scalar"]
        lines.append(
            f'| {x["lambda"]:.2f} | {x["N"]} | {ps} | '
            f'{x["Lprime"]["min"]:.3e} | {x["Rmass"]["inertia"]["negative"]} | '
            f'{x["A"]["inertia"]["negative"]} | {p["C_odd_lowest_minus_2S"]:.3e} | '
            f'{p["C_even_below_2S"]} | {sc["c_Ae_inv_c"] if sc["c_Ae_inv_c"] is not None else "NA"} | '
            f'{sc["s_Ao_inv_s"] if sc["s_Ao_inv_s"] is not None else "NA"} |'
        )
    md.write_text("\n".join(lines) + "\n")
    print(md.read_text())


if __name__ == "__main__":
    main()
