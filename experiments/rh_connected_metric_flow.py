#!/usr/bin/env python3
"""
Experimental audit of the current RH closure frontier.

Zero-data-free pieces:
  1. causal-shift zeta metric flow on the CCM interval;
  2. connected projection against the two pole vectors;
  3. optional massive/Archimedean diagonal insertions.

This script is diagnostic only. It does not claim RH.
"""
import math
import numpy as np
from scipy.linalg import eigh, null_space

def Vmat(L, N, y):
    idx = np.arange(-N, N + 1)
    n = np.broadcast_to(idx[:, None], (2*N+1, 2*N+1))
    m = np.broadcast_to(idx[None, :], (2*N+1, 2*N+1))
    d = m - n
    V = np.empty(d.shape, dtype=complex)
    mask = d == 0
    V[mask] = (L-y)/L * np.exp(-2j*np.pi*m[mask]*y/L)
    dd = d[~mask]
    mm = m[~mask]
    V[~mask] = (
        np.exp(-2j*np.pi*mm*y/L)
        * (1 - np.exp(2j*np.pi*dd*y/L))
        / (2j*np.pi*dd)
    )
    return V

def pole_vectors(L, N):
    idx = np.arange(-N, N + 1)
    pref = 8*math.sqrt(L)*math.sinh(L/4)
    c = pref * L / (L*L + 16*math.pi**2*idx**2)
    s = pref * (4*math.pi*idx) / (L*L + 16*math.pi**2*idx**2)
    return c.astype(complex), s.astype(complex)

def metric_flow(lam, N, beta=1.0, diagonal_weight=None):
    L = 2*math.log(lam)
    Kmax = int(math.floor(math.exp(L) - 1e-12))
    dim = 2*N + 1
    Z = np.zeros((dim, dim), dtype=complex)
    Zd = np.zeros_like(Z)
    for k in range(1, Kmax + 1):
        y = math.log(k)
        V = Vmat(L, N, y)
        w = k**(-beta/2)
        Z += w*V
        if k > 1:
            Zd += -0.5*math.log(k)*w*V

    if diagonal_weight is None:
        A = np.eye(dim)
    else:
        idx = np.arange(-N, N + 1)
        freq = 2*np.pi*idx/L
        A = np.diag(diagonal_weight(freq))

    G = Z.conj().T @ A @ Z
    Gd = Zd.conj().T @ A @ Z + Z.conj().T @ A @ Zd
    vals, U = eigh(G)
    thresh = max(vals[-1]*1e-13, 1e-14)
    invsqrt = U @ np.diag([1/math.sqrt(v) if v > thresh else 0 for v in vals]) @ U.conj().T

    K = invsqrt @ Gd @ invsqrt
    K = (K + K.conj().T)/2

    c, s = pole_vectors(L, N)
    # Correct connected constraints after passing to g = G^{1/2} f:
    # c^* f = s^* f = 0 becomes (G^{-1/2} c)^* g = (G^{-1/2} s)^* g = 0.
    ct = invsqrt @ c
    st = invsqrt @ s
    Q = null_space(np.vstack([ct.conj(), st.conj()]))
    Kc = Q.conj().T @ K @ Q
    return L, np.linalg.eigvalsh(K), np.linalg.eigvalsh(Kc), np.linalg.cond(Z)

def massive_weight(power):
    def f(freq):
        return (freq*freq + 0.25)**power
    return f

if __name__ == "__main__":
    print("plain zeta-gauge metric flow")
    for lam, N in [(3,30),(5,60),(8,60),(12,60),(20,80),(30,60),(40,70),(50,80)]:
        L, full, conn, cond = metric_flow(lam, N)
        print(
            f"lambda={lam:>3} L={L:7.4f} N={N:>3} "
            f"full=[{full[0]: .6g},{full[-1]: .6g}] "
            f"connected=[{conn[0]: .6g},{conn[-1]: .6g}] "
            f"cond(Z)={cond:.3e}"
        )

    print("\nnaive K0 insertions (diagnostic no-go)")
    for power in [0.5, 1.0, -0.5, -1.0]:
        print(f"power={power}")
        for lam, N in [(5,30),(12,60),(20,80)]:
            L, full, conn, _ = metric_flow(lam, N, diagonal_weight=massive_weight(power))
            print(f"  lambda={lam:>2}: connected=[{conn[0]: .6g},{conn[-1]: .6g}]")
