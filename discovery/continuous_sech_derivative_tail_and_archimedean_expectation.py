"""Executable audits for two exact continuous-sech chamber identities.

1. For c >= 0 and |x| >= 1, the frequency derivative kernel

       D_c(t,x) = x sin(tx) c/(|x| sinh(pi |x|))

   obeys the parameter-independent exponential tail

       |D_c(t,x)| <= [2c/(1-exp(-2pi))] exp(-pi |x|).

2. If P(lam)=pi*lam/sinh(pi*lam) and rho_1=(2/pi)P is the normalized
   c=1 chamber law, the focused-paper digamma integral implies

       E_{rho_1}[Re psi(1/2+i Lambda/2)]
         = 1/2 + psi(1/2)
         = 1/2 - EulerGamma - 2 log 2.

The script checks both numerically at high precision. It is an audit, not a
substitute for Lean formalization of the analytic identities.
"""

import mpmath as mp

mp.mp.dps = 70


def levy_density(c, x):
    if x == 0:
        return mp.mpf("0")
    return c / (abs(x) * mp.sinh(mp.pi * abs(x)))


def derivative_kernel(c, t, x):
    return x * mp.sin(t * x) * levy_density(c, x)


def sharp_tail(c, x):
    assert abs(x) >= 1
    return (2 * c / (1 - mp.e ** (-2 * mp.pi))) * mp.e ** (-mp.pi * abs(x))


def P(lam):
    if lam == 0:
        return mp.mpf("1")
    return mp.pi * lam / mp.sinh(mp.pi * lam)


def rho1(lam):
    return 2 * P(lam) / mp.pi


def archimedean_observable(lam):
    return mp.re(mp.digamma(mp.mpf("0.5") + 0.5j * lam))


def main():
    worst = mp.mpf("0")
    worst_args = None
    for c in [mp.mpf("0.2"), mp.mpf("1"), mp.mpf("2.7")]:
        for t in [mp.mpf("-9"), mp.mpf("-2.3"), mp.mpf("0.4"), mp.mpf("7.7")]:
            for k in range(1201):
                x = mp.mpf("1") + mp.mpf(k) / 100
                for xx in (x, -x):
                    ratio = abs(derivative_kernel(c, t, xx)) / sharp_tail(c, xx)
                    if ratio > worst:
                        worst = ratio
                        worst_args = (c, t, xx)
                    assert ratio <= 1 + mp.mpf("1e-60")

    norm = mp.quad(lambda x: rho1(x), [-mp.inf, 0, mp.inf])
    expectation = mp.quad(
        lambda x: rho1(x) * archimedean_observable(x),
        [-mp.inf, 0, mp.inf],
    )
    target = mp.mpf("0.5") + mp.digamma(mp.mpf("0.5"))
    target_elementary = mp.mpf("0.5") - mp.euler - 2 * mp.log(2)

    print("worst tail ratio:", mp.nstr(worst, 40), "at", worst_args)
    print("rho1 normalization:", mp.nstr(norm, 60))
    print("Archimedean expectation:", mp.nstr(expectation, 60))
    print("closed form:", mp.nstr(target, 60))
    print("elementary form:", mp.nstr(target_elementary, 60))
    print("absolute error:", mp.nstr(abs(expectation - target), 10))

    assert abs(norm - 1) < mp.mpf("1e-55")
    assert abs(expectation - target) < mp.mpf("1e-55")
    assert abs(target - target_elementary) < mp.mpf("1e-60")


if __name__ == "__main__":
    main()
