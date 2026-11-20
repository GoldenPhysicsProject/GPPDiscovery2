"""For a Dirichlet series F with a(1)=1 let b be its convolution inverse, M_Y its inverse truncated at Y, and D=1-F M_Y. All identities here are coefficientwise. D starts at Y+1, so D^k starts at (Y+1)^k. Thus (-F' M_Y)(1+D+...+D^{k-1}) agrees with -F'/F below (Y+1)^k, by the geometric identity. At k=2 this is exact through X for Y=floor(sqrt X). This is the elementary short-inverse identity underlying Heath-Brown's decomposition. Y counts coefficients retained, whereas Alpöge's remark describes the number of theta lifts. No identification of those constructions is assumed.

The sign-sensitive project target suggests measuring what that identity costs on the critical line. Define E(Y)=sum_{n<=Y}|b(n)|²/n, exactly the infinite-height mean of |M_Y(1/2+it)|² by orthogonality of the finite exponential sum. Use the finite Euler factors of the Dirichlet series underlying each completed control. For plain zeta, b=mu gives E(Y)<=1+log Y. For F=zeta(s+u)zeta(s-u), b is the convolution of mu(n)n^u and mu(n)n^{-u}. For imaginary u (including zero), |b(n)|<=d(n). Since d(n)^2<=d_4(n) prime power by prime power, E(Y)<=(1+log Y)^4. For real u with theta=|u|>0, |b(n)|<=n^theta d(n), while |b(p)|=p^theta+p^{-theta}. Primes in (Y/2,Y] alone give E(Y) >>_theta Y^{2theta}/log Y by PNT. Hence log E(Y)/log Y tends to exactly 2theta, and tends to zero in the preceding cases. No zero data enter. This distinguishes real displacement from unitary phase twisting even at matched degree. The square-root cutoff identity survives all controls. This is coefficient growth on average over height. Recovering the signed, localized Weil pairing requires control of off-diagonal phases and the completion terms.

Reproduction: python3 experiments/short_reciprocal/check.py. X=4096, k=2, Y=64 for coefficient reconstruction. Largest absolute coefficient discrepancy among the four cases was 6.8e-13 (floating point). At Y=65536 the energies were 7.78605829 (zeta), 241.15381048 (zeta squared), 59.63484334 (imaginary shifts ±i/4), and 1375.61014297 (real shifts ±1/4). The growth exponents follow from the inequalities above, independently of this grid."""
from math import isqrt, log


def convolution(left, right, limit):
    out = [0.] * (limit + 1)
    for d, value in enumerate(left[1:limit + 1], 1):
        if value:
            for j in range(1, min(limit // d, len(right) - 1) + 1):
                out[d*j] += value * right[j]
    return out


def sieve(limit):
    composite = [False] * (limit + 1)
    mu = [1] * (limit + 1)
    mangoldt = [0.] * (limit + 1)
    for p in range(2, limit + 1):
        if composite[p]:
            continue
        for n in range(p, limit + 1, p):
            mu[n] *= -1
            composite[n] = True
        for n in range(p*p, limit + 1, p*p):
            mu[n] = 0
        power = p
        while power <= limit:
            mangoldt[power] = log(p)
            power *= p
    return mu, mangoldt


def model(label, shift, mu, mangoldt):
    limit = len(mu) - 1
    if shift is None:
        reciprocal = mu
        coeff = [1] * (X + 1)
        target = mangoldt[:X + 1]
    else:
        weight = [0] + [n**shift for n in range(1, limit + 1)]
        inverse = [0] + [1/w for w in weight[1:]]
        coeff = convolution(weight, inverse, X)
        reciprocal = convolution([m*w for m, w in zip(mu, weight)],
                                 [m*w for m, w in zip(mu, inverse)], limit)
        target = [0] + [mangoldt[n]*(weight[n]+inverse[n]) for n in range(1, X+1)]
    short = reciprocal[:isqrt(X) + 1]
    # 1 + D = 2 - F M, with units at coefficient index 1.
    correction = [-v for v in convolution(coeff, short, X)]
    correction[1] += 2
    derivative = [0] + [coeff[n]*log(n) for n in range(1, X+1)]
    recovered = convolution(convolution(derivative, short, X), correction, X)
    error = max(abs(recovered[n] - target[n]) for n in range(1, X+1))
    assert error < 1e-9, (label, error)
    energy = 0.
    print(label, 'max coefficient error', format(error, '.2g'))
    for n in range(1, limit + 1):
        energy += abs(reciprocal[n])**2 / n
        if n in (64, 1024, 16384, 65536):
            print(n, format(energy, '.8f'))


if __name__ == '__main__':
    X = 4096
    limit = 65536
    mu, mangoldt = sieve(limit)
    for label, shift in [('zeta', None), ('zeta squared', 0),
                         ('imaginary shifts', 0.25j), ('real shifts', 0.25)]:
        model(label, shift, mu, mangoldt)
