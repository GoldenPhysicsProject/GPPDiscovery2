"""Exact spectral-weight <-> continuous-sech chamber c=1 bridge.

Keep the representation-theoretic status honest: this does NOT prove that
P(lambda)=pi*lambda/sinh(pi*lambda) is the genuine SL(2,C) Plancherel measure.
It proves a different exact statement.

Using |Gamma(1+i lambda)|^2 = pi*lambda/sinh(pi*lambda), the continuous chamber
density
    rho_c(lambda) = 2^(2c-1)/(pi Gamma(2c)) |Gamma(c+i lambda)|^2
specializes at c=1 to
    rho_1(lambda) = 2 lambda/sinh(pi lambda)
                  = (2/pi) P(lambda).
Thus P has total mass pi/2, and its normalized version (2/pi)P is exactly the
c=1 chamber law.

The sine-over-sinh transform
    integral_0^infty sin(t x)/sinh(pi x) dx = 1/2 tanh(t/2)
implies after differentiation
    integral_0^infty x cos(t x)/sinh(pi x) dx = 1/4 sech^2(t/2),
so the full Fourier transform is
    integral_R P(lambda) exp(i t lambda) d lambda
      = (pi/2) sech^2(t/2),
and equivalently the characteristic function of rho_1 is exactly
    sech^2(t/2).

The numerical audit below checks normalization, the Gamma identity, and the
Fourier pair at nontrivial frequencies.  The analytic identities are the
promotion targets for Verify2.
"""

import mpmath as mp

mp.mp.dps = 50


def P(lam):
    if lam == 0:
        return mp.mpf(1)
    return mp.pi * lam / mp.sinh(mp.pi * lam)


def rho1(lam):
    if lam == 0:
        return 2 / mp.pi
    return 2 * lam / mp.sinh(mp.pi * lam)


def rho1_gamma(lam):
    return 2 / mp.pi * abs(mp.gamma(1 + 1j * lam)) ** 2


def phi1(t):
    return mp.sech(t / 2) ** 2


if __name__ == "__main__":
    norm = mp.quad(lambda x: rho1(x), [-mp.inf, 0, mp.inf])
    assert abs(norm - 1) < mp.mpf("1e-45")

    for lam in (mp.mpf("0.2"), mp.mpf("0.9"), mp.mpf("2.3")):
        assert abs(rho1(lam) - rho1_gamma(lam)) < mp.mpf("1e-45")
        assert abs(rho1(lam) - (2 / mp.pi) * P(lam)) < mp.mpf("1e-45")

    for t in (mp.mpf("0"), mp.mpf("0.4"), mp.mpf("1.3"), mp.mpf("2.7")):
        transform = mp.quad(
            lambda x: rho1(x) * mp.cos(t * x),
            [-mp.inf, 0, mp.inf],
        )
        assert abs(transform - phi1(t)) < mp.mpf("1e-45")
        print(
            "t=", t,
            " Fourier[rho1]=", mp.nstr(transform, 35),
            " sech^2(t/2)=", mp.nstr(phi1(t), 35),
        )

    print("rho1 normalization =", mp.nstr(norm, 35))
    print("all c=1 spectral-weight/chamber bridge checks passed")
