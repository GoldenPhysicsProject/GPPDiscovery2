#!/usr/bin/env python3
"""Numerical probe of the two-observable zeta Gibbs Fisher determinant.

For K(beta)=log zeta(beta), beta>1, canonical cumulants satisfy
    kappa_2 = K''
    kappa_3 = -K'''
    kappa_4 = K''''.
The covariance determinant of X=log n and X^2 is therefore
    D = kappa_2*kappa_4 + 2*kappa_2**3 - kappa_3**2.

This script probes two asymptotic regimes suggested by the exact formula:

critical (beta -> 1+):
    D(beta) ~ 4/(beta-1)^6,

low temperature (beta -> +infinity):
    D(beta) ~ [log(2) log(3) log(3/2)]^2 * 6^(-beta).

The second coefficient is the squared 3-point Vandermonde area for the
lowest three energies 0, log 2, log 3; two support points alone have rank-one
covariance for the observables X and X^2.
"""

import mpmath as mp

mp.mp.dps = 80


def cumulants(beta):
    K = lambda x: mp.log(mp.zeta(x))
    kappa2 = mp.diff(K, beta, 2)
    kappa3 = -mp.diff(K, beta, 3)
    kappa4 = mp.diff(K, beta, 4)
    det = kappa2 * kappa4 + 2 * kappa2**3 - kappa3**2
    return kappa2, kappa3, kappa4, det


def critical_ratio(beta):
    return cumulants(beta)[3] * (beta - 1) ** 6 / 4


LOW_T_COEFF = (mp.log(2) * mp.log(3) * mp.log(mp.mpf(3) / 2)) ** 2


def low_temperature_ratio(beta):
    return cumulants(beta)[3] * mp.power(6, beta) / LOW_T_COEFF


def main():
    print("critical coefficient target: 4")
    for beta in map(mp.mpf, ["1.01", "1.02", "1.05", "1.10"]):
        print(beta, mp.nstr(critical_ratio(beta), 20))

    print("\nlow-temperature coefficient:", mp.nstr(LOW_T_COEFF, 30))
    print("low-temperature ratio target: 1")
    for beta in map(mp.mpf, ["10", "15", "20", "25", "30", "40", "50"]):
        print(beta, mp.nstr(low_temperature_ratio(beta), 20))


if __name__ == "__main__":
    main()
