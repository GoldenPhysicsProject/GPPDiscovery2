"""Numerical fixed-step de Bruijn-Newman heat-flow test (not RH proof).

See Rodgers--Tao arXiv:1801.05914. H_0(z) = xi(1/2+i*z/2)/8, and
H_lambda(z) = integral_0^infty exp(lambda*u*u) Phi(u) cos(z*u) du.

Each step lambda -> lambda+delta multiplies every Fourier mode by
exp(delta*u*u). Thus k repeated equal steps compose *exactly* to H_(k*delta).

Requires NumPy and SciPy. Run alongside zero_meta_rule_theta_probe.py.
"""

from functools import lru_cache
from math import pi

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

from zero_meta_rule_theta_probe import xi_from_eta


INTEGER_MODES = np.arange(1, 6, dtype=np.float64)


def phi(u: float) -> float:
    n = INTEGER_MODES
    return float(np.sum((2 * pi * pi * n**4 * np.exp(9 * u)
                         - 3 * pi * n**2 * np.exp(5 * u))
                        * np.exp(-pi * n * n * np.exp(4 * u))))


@lru_cache(maxsize=2500)
def h_debruijn(lam: float, z: float) -> float:
    f = lambda u: np.exp(lam * u * u) * phi(u) * np.cos(z * u)
    return quad(f, 0, 1.6, epsabs=8e-16, epsrel=1e-13, limit=250)[0]


def h_prime(lam: float, z: float) -> float:
    f = lambda u: -u * np.exp(lam * u * u) * phi(u) * np.sin(z * u)
    return quad(f, 0, 1.6, epsabs=8e-16, epsrel=1e-13, limit=250)[0]


def h_second(lam: float, z: float) -> float:
    f = lambda u: -u * u * np.exp(lam * u * u) * phi(u) * np.cos(z * u)
    return quad(f, 0, 1.6, epsabs=8e-16, epsrel=1e-13, limit=250)[0]


def zero_ordinate(lam: float, index: int) -> float:
    if index == 1:
        z_lo, z_hi = 27.0, 29.0
    elif index == 2:
        z_lo, z_hi = 41.0, 43.0
    else:
        raise ValueError("This low-height probe only brackets zeros 1 and 2")
    z = brentq(lambda z: h_debruijn(lam, z), z_lo, z_hi, xtol=1e-12)
    return z / 2


def main():
    print("H_0(z) == xi(1/2+i*z/2)/8 independent evaluator check:")
    for z in (6.0, 20.0, 28.0, 40.0):
        theta_value = h_debruijn(0, z)
        xi_value = (xi_from_eta(z / 2) / 8).real
        print(f"z={z:.1f}, H_0={theta_value:.15e}, "
              f"xi/8={xi_value:.15e}, abs_error={abs(theta_value-xi_value):.3e}")
        assert abs(theta_value - xi_value) < 4e-14

    delta = 0.05
    print("\nFixed additive running-coupling steps delta_lambda = 0.05:")
    results = []
    for k in range(6):
        lam = k * delta
        g1, g2 = zero_ordinate(lam, 1), zero_ordinate(lam, 2)
        results.append((g1, g2))
        print(f"k={k}, lambda={lam:.2f}, gamma_1={g1:.10f}, gamma_2={g2:.10f}")

    print("\nZero-flow identity from partial_lambda H = -partial_z^2 H:")
    for index in (1, 2):
        z = 2 * results[0][index - 1]
        predicted_slope = 0.5 * h_second(0, z) / h_prime(0, z)
        observed_slope = (zero_ordinate(0.001, index)
                          - zero_ordinate(0, index)) / 0.001
        print(f"zero {index}: implicit d_gamma/d_lambda={predicted_slope:.9f}, "
              f"first-step slope={observed_slope:.9f}")
        assert abs(predicted_slope - observed_slope) < 4e-5

    print("\nReminder: lambda-flow moves zeros of different functions, "
          "not gamma_n -> gamma_(n+1); RH iff the flow's reality "
          "threshold Lambda_DN<=0, and Rodgers--Tao proved Lambda_DN>=0.")


if __name__ == "__main__":
    main()
