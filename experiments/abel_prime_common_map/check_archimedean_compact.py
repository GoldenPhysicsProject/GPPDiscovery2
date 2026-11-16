"""Reproducible numerical cross-checks for the fixed-window Weil compactness note.

Checks the exact real-place tail k(L), the positive Fourier multiplier's
series and digamma identities, its monotonic growth, and the quantitative
finite-codimension bound. This is FLOATING POINT, not interval certification
or a proof of RH. Requires mpmath. No zeta zeros are used.

Run: python experiments/abel_prime_common_map/check_archimedean_compact.py
"""
import math
import mpmath as mp

mp.mp.dps = 45


def weight(t):
    """e^(-t/2)/(1 - e^(-2t)), t > 0."""
    t = mp.mpf(t)
    return mp.exp(-t / 2) / (-mp.expm1(-2*t))


def tail_exact(L):
    z = mp.exp(-mp.mpf(L)/2)
    return mp.log((1 + z)/(1 - z)) + 2*mp.atan(z)


def multiplier_series(x, count):
    x = mp.mpf(x)
    return 2*mp.fsum([
        x*x / ((2*k + mp.mpf("0.5")) *
            ((2*k + mp.mpf("0.5"))**2 + x*x))
        for k in range(count)
    ])


def multiplier_series_tail_upper(x, count):
    """Analytic upper bound for the omitted positive tail, count >= 2.

    For k >= count, 2 x²/[a_k(a_k²+x²)] <= x²/(4 k³).
    Sum_{k=count}∞ k^-3 <= 1/[2(count-1)²].
    """
    assert count >= 2
    return mp.mpf(x)**2/(8*(count-1)**2)


def multiplier_digamma(x):
    return (mp.re(mp.digamma(mp.mpf("0.25") + 1j*mp.mpf(x)/2))
            - mp.digamma(mp.mpf("0.25")))


def von_mangoldt(n):
    if n < 2:
        return mp.mpf(0)
    # Entirely deterministic exact-integer prime-power test.
    p = None
    t = n
    k = 2
    while k*k <= t:
        if t % k == 0:
            p = k
            while t % k == 0:
                t //= k
            return mp.log(p) if t == 1 else mp.mpf(0)
        k += 1
    return mp.log(n)  # n is prime


def perturbation_bound(L):
    L = mp.mpf(L)
    C = -mp.euler-mp.log(mp.pi)-mp.pi/2-3*mp.log(2)
    nmax = int(mp.floor(mp.exp(L)))
    return abs(C)+4*mp.sinh(L/2) + 2*mp.fsum(
        von_mangoldt(n)/mp.sqrt(n) for n in range(2,nmax+1)
    )


def threshold_R(L):
    M = perturbation_bound(L)
    lo = mp.mpf(0)
    hi = mp.mpf(2)
    while multiplier_digamma(hi) <= 2*M:
        hi *= 2
    for _ in range(100):
        mid = (lo+hi)/2
        if multiplier_digamma(mid) > 2*M:
            hi = mid
        else:
            lo = mid
    # Take a strict margin for finite-precision reporting.
    R = hi*mp.mpf("1.0001")
    assert multiplier_digamma(R) > 2*M
    rank = int(mp.ceil(2*mp.mpf(L)*R/mp.pi))
    return M, R, rank


def main():
    for L in ("0.125", "0.72", "1.0"):
        L = mp.mpf(L)
        k = tail_exact(L)
        numerical = 2*mp.quad(weight, [L, mp.inf])
        assert abs(k-numerical) < mp.mpf("1e-30")
        M, R, rank = threshold_R(L)
        assert multiplier_digamma(R)>2*M
        margin = multiplier_digamma(R)*(1-L*R/(mp.pi*(rank+1)))-M
        assert margin > 0
        print("L=", L, "k(L)=",mp.nstr(k,13),
              "M_L=",mp.nstr(M,12),
              "R=",mp.nstr(R,12),
              "codimension<=",rank,
              "positive_margin=",mp.nstr(margin,6))

    previous = -1
    for x in [1, 2, 5, 10, 25, 100]:
        value = multiplier_digamma(x)
        part = multiplier_series(x, 1500)
        err = value - part
        err_bound = multiplier_series_tail_upper(x, 1500)
        assert 0 < err < err_bound
        assert value > previous
        previous = value
        print("frequency=",x,
              "a(frequency)=",mp.nstr(value,13),
              "series_tail=",mp.nstr(err,8),
              "tail_upper=",mp.nstr(err_bound,8))

    print("PASS: numerical cross-check only; rigorous statements require analytic proofs and Lean.")


if __name__ == "__main__":
    main()
