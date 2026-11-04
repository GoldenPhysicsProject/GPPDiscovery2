"""Golden Möbius map: exact conjugacy and unitary two-sheet controls.

Research-stage GPP numerical checks. Mathematical identities and the no-point-
spectrum result are analytic; numerical values are only independent regressions.
Requires NumPy and SciPy. No zeta-zero fitting occurs in this experiment.
"""

import numpy as np
from scipy.integrate import quad


PHI = (1 + np.sqrt(5)) / 2


def fixed_roots(a):
    root = (a + np.sqrt(a * a + 4)) / 2
    return root, -1 / root


def mobius(x, a=1):
    return a + 1 / x


def cross_ratio(x, a=1):
    positive, negative = fixed_roots(a)
    return (x - positive) / (x - negative)


def multiplier(a):
    positive, _ = fixed_roots(a)
    return -positive ** -2


def plus(u):
    return np.exp(-u * u) * (1 + 0.2 * np.cos(1.3 * u))


def minus(u):
    return np.exp(-0.5 * (u - 1) ** 2) * np.exp(0.4j * u)


def step_pair(a, u):
    shift = -2 * np.log(fixed_roots(a)[0])
    return minus(u + shift), plus(u + shift)


def norm_pair(apply_step=False, a=1):
    def density(u):
        pair = step_pair(a, u) if apply_step else (plus(u), minus(u))
        return abs(pair[0]) ** 2 + abs(pair[1]) ** 2
    return quad(density, -15, 15, epsabs=2e-13, epsrel=2e-13)[0]


def prime_shift(pair, p, u):
    return pair(u + np.log(p))


def golden_matrix(t):
    phase = np.exp(-2j * t * np.log(PHI))
    return phase * np.array([[0, 1], [1, 0]])


def main():
    print("Golden and adversarial integer-translation conjugacies:")
    x_samples = (-3, -1, -0.2, 0.2, 1, 2, 5)
    for a in (1, 2, 3):
        positive, negative = fixed_roots(a)
        kappa = multiplier(a)
        error = max(abs(cross_ratio(mobius(x, a), a) -
                        kappa * cross_ratio(x, a)) for x in x_samples)
        print(f"a={a} fixed+={positive:.12f}, fixed-={negative:.12f}, "
              f"kappa={kappa:.12f}, identity max residual={error:.3e}")
        assert error < 2e-14

    print("\nUnitary double-sheet L2 norm under a golden step:")
    n0, n1 = norm_pair(), norm_pair(True)
    print(f"before={n0:.15f}, after={n1:.15f}, difference={n1-n0:+.3e}")
    assert abs(n0 - n1) < 2e-12

    print("\nGolden step commutes with unweighted prime dilations:")
    offset = -2 * np.log(PHI)
    for p in (2, 3, 5, 7):
        for u in (-1.5, 0.1, 2.4):
            # U V_p psi = swap psi evaluated at u + log(p) + offset.
            uv = (minus(u + np.log(p) + offset),
                  plus(u + np.log(p) + offset))
            # V_p U psi = same arguments but opposite addition order.
            vu = (minus(u + offset + np.log(p)),
                  plus(u + offset + np.log(p)))
            assert max(abs(uv[0] - vu[0]), abs(uv[1] - vu[1])) < 2e-15
        print(f"[U_phi, V_{p}] = 0 (numerically); exact since translations commute")

    print("\nUnitarity of Fourier symbol vs nonreal spectral parameter:")
    for t in (0.0, 14.1347251417347, 14.1347251417347 + 0.3j):
        eigenvalues = np.linalg.eigvals(golden_matrix(t))
        print(f"t={t}, eigenvalue moduli="
              f"{[round(abs(x), 12) for x in eigenvalues]}")

    print("\nAnalytic no-go: U_phi^2 translates by -4 log(phi) on L2(R)^2. "
          "A nonzero L2 translation eigenfunction would have identical nonzero "
          "norm on infinitely many disjoint periods, impossible. "
          "Thus U_phi has no L2 point spectrum. This is not an RH argument.")


if __name__ == "__main__":
    main()
