"""Prime-gas directed-KL orientation diagnostic.

For p_beta(n)=n^{-beta}/zeta(beta), beta>1, define
    D(beta||gamma)=sum p_beta log(p_beta/p_gamma).
With A(beta)=log zeta(beta),
    D(beta||gamma)=A(gamma)-A(beta)-(gamma-beta) A'(beta).
Hence
    D(beta||gamma)-D(gamma||beta)
      = 2(A(gamma)-A(beta))-(gamma-beta)(A'(beta)+A'(gamma))
      = integral_beta^gamma (beta+gamma-2t) A''(t) dt.
Since A''(t)=Var_t(log n)=g(t), strict decrease of g on (1,infty)
forces this asymmetry to be strictly positive whenever beta<gamma.

This script numerically cross-checks the closed form, the integral identity,
and the predicted orientation on a grid.  It is discovery support only; the
strict monotonicity input is proved separately in GPPVerify2.
"""

import mpmath as mp

mp.mp.dps = 60


def A(beta):
    return mp.log(mp.zeta(beta))


def Ap(beta):
    return mp.diff(A, beta)


def g(beta):
    return mp.diff(A, beta, 2)


def kl(beta, gamma):
    return A(gamma) - A(beta) - (gamma - beta) * Ap(beta)


def asym_closed(beta, gamma):
    return kl(beta, gamma) - kl(gamma, beta)


def asym_integral(beta, gamma):
    return mp.quad(lambda t: (beta + gamma - 2*t) * g(t), [beta, gamma])


def paired_integral(beta, gamma):
    mid = (beta + gamma) / 2
    return mp.quad(
        lambda t: (beta + gamma - 2*t) * (g(t) - g(beta + gamma - t)),
        [beta, mid],
    )


def check_pair(beta, gamma):
    assert 1 < beta < gamma
    d1 = asym_closed(beta, gamma)
    d2 = asym_integral(beta, gamma)
    d3 = paired_integral(beta, gamma)
    tol = mp.mpf("1e-45")
    assert abs(d1 - d2) < tol
    assert abs(d1 - d3) < tol
    assert d1 > 0
    assert kl(beta, gamma) > kl(gamma, beta)
    return d1


if __name__ == "__main__":
    grid = [
        (mp.mpf("1.05"), mp.mpf("1.10")),
        (mp.mpf("1.10"), mp.mpf("1.5")),
        (mp.mpf("1.25"), mp.mpf("2")),
        (mp.mpf("1.5"), mp.mpf("3")),
        (mp.mpf("2"), mp.mpf("5")),
        (mp.mpf("3"), mp.mpf("10")),
    ]
    for beta, gamma in grid:
        delta = check_pair(beta, gamma)
        print(f"beta={mp.nstr(beta,8)} gamma={mp.nstr(gamma,8)}  KL asymmetry={mp.nstr(delta,20)}")
    print("all directed-KL orientation checks passed")
