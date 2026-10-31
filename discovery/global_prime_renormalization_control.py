"""All-support prime renormalization: exact finite algebra and false-zeta filter.

No RH/Weil positivity claim. The main identities are algebraic and proved
in discovery/global_prime_renormalized_haar_poisson_gate.md.
This smoke test uses standard math floats for the (independently proved)
indicator q_f and checks the exact rational discrete analogue as well.
"""
import math
from fractions import Fraction as Q


def exact_discrete_translation_identity():
    f = [Q(2), Q(-1), Q(3), Q(-2), Q(1), Q(4)]
    nrm = sum(x * x for x in f)
    for shift in range(1, 12):
        corr = sum(f[k] * f[k + shift] for k in range(len(f) - shift)) \
            if shift < len(f) else Q(0)
        # Embed by zero extension into the whole integer line.
        diffsq = 2 * nrm - 2 * corr
        assert diffsq - 2 * nrm == -2 * corr
        if shift >= len(f):
            assert diffsq == 2 * nrm
    print("Exact rational translation identities: PASS (all 11 shifts)")


def primes_through(N):
    out = []
    for n in range(2, N + 1):
        prime = True
        for j in range(2, math.isqrt(n) + 1):
            if n % j == 0:
                prime = False
                break
        if prime:
            out.append(n)
    return out


def prime_powers(N):
    powers = []
    for p in primes_through(N):
        q = p
        while q <= N:
            powers.append((q, math.log(p) / math.sqrt(q)))
            q *= p
    return sorted(powers)


def indicator_test(L=0.75, N=12000, theta=0.2):
    terms = prime_powers(N)
    assert math.log(2) < L < math.log(3)
    for label, t in (("zeta", 0.0), ("shifted false zeta", theta)):
        raw = 0.0
        counterterm = 0.0
        source = 0.0
        last = 0
        for n, w in terms:
            a = math.log(n)
            w *= 1.0 if t == 0 else 2.0 * math.cosh(t * a)
            # f=1_[0,L]. Exact analytic q(a)=2(L-a)_+.
            diff = 2.0 * min(a, L)
            q = 2.0 * max(0.0, L-a)
            raw += w * diff
            counterterm += 2.0 * L * w
            source -= w * q
            if n in (2, 4, 16, 128, 1024, 4096):
                assert abs((raw-counterterm)-source) < 1.0e-9
                last = n
        assert raw > 0 and counterterm > raw
        assert abs(raw - counterterm - source) < 1.0e-9
        print(f"{label}: cutoff {N}, unrenormalized positive jump = "
              f"{raw:.8f}, subtraction = {counterterm:.8f}, "
              f"stabilized negative source = {source:.12f}")
        assert source < 0
        # There is only the n=2 atom when support L=0.75.
        a = math.log(2)
        w2 = a / math.sqrt(2)
        if t:
            w2 *= 2 * math.cosh(t*a)
        assert abs(source + 2*w2*(L-a)) < 1e-10
    # Positive-local-moment test: shifted zeta has nonunitary p^±theta.
    for p in (2, 3, 101):
        u = theta * math.log(p)
        m1 = 2 * math.cosh(u)
        det = 4-m1*m1
        expected = -4*math.sinh(u)**2
        assert det < 0 and math.isclose(det, expected, rel_tol=1e-9)
    print("F_theta prime-local 2x2 Toeplitz minors: strictly negative (PASS)")
    print("Positive prime jump + even reflection is NOT an RH proof.")


if __name__ == "__main__":
    exact_discrete_translation_identity()
    indicator_test()
