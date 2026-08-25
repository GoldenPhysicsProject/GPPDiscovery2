"""
General prime-gas Hankel/Vandermonde witness audit.

For the positive discrete measure

    dnu_beta = sum_{n>=2} Lambda(n) log(n) n^{-beta} delta_{log n},

the k x k Hankel moment determinant has the Cauchy-Binet expansion

    H_k(beta) = sum_{n_1<...<n_k} prod_i w_{n_i}
                prod_{i<j}(x_j-x_i)^2,

with x_n=log n and w_n=Lambda(n) log n n^{-beta}.
Therefore any k distinct prime support points give an explicit strict lower bound.
This script checks the witness formed by the first k primes against independent
prime-power moment truncations. It is numerical evidence only; the infinite-measure
Cauchy-Binet bridge belongs in GPPVerify2.
"""

import math
import mpmath as mp

mp.mp.dps = 70


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def prime_power_moments(beta, rmax, cutoff):
    moments = [mp.mpf("0") for _ in range(rmax + 1)]
    for p in primes_upto(cutoff):
        lp = mp.log(p)
        pk = p
        while pk <= cutoff:
            x = mp.log(pk)
            w = lp * x * mp.power(pk, -beta)
            xr = mp.mpf(1)
            for r in range(rmax + 1):
                moments[r] += w * xr
                xr *= x
            pk *= p
    return moments


def hankel_det(beta, k, cutoff):
    m = prime_power_moments(beta, 2 * (k - 1), cutoff)
    M = mp.matrix(k)
    for i in range(k):
        for j in range(k):
            M[i, j] = m[i + j]
    return mp.det(M)


def first_prime_witness(beta, k):
    ps = primes_upto(100)[:k]
    xs = [mp.log(p) for p in ps]
    # At a prime p: Lambda(p) log p p^{-beta} = (log p)^2 p^{-beta}.
    weights = [mp.log(p) ** 2 * mp.power(p, -beta) for p in ps]
    vand = mp.mpf(1)
    for i in range(k):
        for j in range(i + 1, k):
            vand *= xs[j] - xs[i]
    return ps, mp.fprod(weights) * vand**2


def main():
    cutoff = 50_000
    betas = [mp.mpf("2"), mp.mpf("3"), mp.mpf("5"), mp.mpf("10")]
    for k in (2, 3, 4):
        ps, _ = first_prime_witness(mp.mpf(2), k)
        print(f"\nk={k}, witness primes={ps}")
        for beta in betas:
            H = hankel_det(beta, k, cutoff)
            _, L = first_prime_witness(beta, k)
            ratio = H / L
            ok = H > L > 0
            print(
                f"beta={mp.nstr(beta, 4):>4}  "
                f"H_k={mp.nstr(H, 18):>22}  "
                f"L={mp.nstr(L, 18):>22}  "
                f"H/L={mp.nstr(ratio, 15):>18}  "
                f"{'PASS' if ok else 'FAIL'}"
            )
            if not ok:
                raise SystemExit(1)


if __name__ == "__main__":
    main()
