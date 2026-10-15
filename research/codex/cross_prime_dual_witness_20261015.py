#!/usr/bin/env python3
"""Arithmetic KMS half-density dual witness; exact finite-window identity.

For any finite trigonometric correction H with frequencies |u| >= 2L,
sup_t (P_L(t)-H(t)) is bounded below by C_L from the autocorrelation
of f_L(x)=a exp(-(L-|x|)/2). This script computes *diagnostic floats*
for C_L using a sieve for Λ(n). The proof is mathematical (Fourier
inversion + PNT), not an Arb/Lean certificate.

Research provenance: Codex/GPT under Daniel Toupin, Oct 15, 2026;
motivated by Grok S27 invisible lifts and Zhu's one-stroke method.
RH and GRH remain open.
"""
import argparse
import math


def mangoldt_sieve(N):
    """Numerical Λ(n); includes *all* prime powers."""
    out = [0.0] * (N + 1)
    prime = bytearray(b"\x01") * (N + 1)
    prime[0] = prime[1] = 0
    for p in range(2, math.isqrt(N) + 1):
        if prime[p]:
            for k in range(p * p, N + 1, p):
                prime[k] = 0
    for p in range(2, N + 1):
        if prime[p]:
            power = p
            while power <= N:
                out[power] = math.log(p)
                power *= p
    return out


def witness(L, lambdas=None):
    """Positive dual lower bound on sup(P_L-H). L must be >0."""
    assert L > 0
    X = math.exp(2 * L)
    Y = math.exp(L)
    if lambdas is None:
        lambdas = mangoldt_sieve(math.floor(X) + 2)
    S = math.fsum(lambdas[n] * math.log(X / n)
                  for n in range(max(2, math.floor(Y) + 1), math.ceil(X))
                  if Y < n < X and lambdas[n] > 0)
    return math.exp(-L) * S / (1 - math.exp(-L))


def witness_alpha(L, alpha, lambdas=None):
    """General exponential-layer lower bound; alpha>0."""
    assert L > 0 and alpha > 0
    X = math.exp(2 * L)
    Y = math.exp(L)
    if lambdas is None:
        lambdas = mangoldt_sieve(math.floor(X) + 2)
    a2 = alpha / (1 - math.exp(-2 * alpha * L))
    S = math.fsum(lambdas[n] * (n ** (alpha - .5)) * math.log(X/n)
                  for n in range(max(2, math.floor(Y) + 1), math.ceil(X))
                  if Y < n < X and lambdas[n] > 0)
    return 2 * a2 * math.exp(-2 * alpha * L) * S


def run():
    ap = argparse.ArgumentParser()
    ap.add_argument("--L-max", type=int, default=6)
    args = ap.parse_args()
    assert 1 <= args.L_max <= 7
    lam = mangoldt_sieve(math.ceil(math.exp(2 * args.L_max)) + 2)
    print("L   bound C_L       C_L/e^L     asymptotic")
    for L in range(1, args.L_max + 1):
        c = witness(L, lam)
        print(f"{L:<3d} {c:14.8f} {c/math.exp(L):11.7f}   1.0000000")
    L = args.L_max
    print(f"\nalpha comparison at L={L}; asymptotic optimal alpha=1/2")
    for alpha in (.1, .25, .5, .75, 1., 1.5):
        c = witness_alpha(L, alpha, lam)
        theory = 2 * alpha / (alpha + .5)**2
        print(f"alpha={alpha:4.2f}: C_alpha/e^L={c/math.exp(L):.7f} theory={theory:.7f}")


if __name__ == "__main__":
    run()
