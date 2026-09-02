"""High-precision curvature audit for the quadratically confined number gas.

Model:
    Z(beta, eta) = sum_{n>=1} exp(-beta log n - eta (log n)^2), eta > 0.

For the sufficient statistics (L, L^2), L = log n, the Fisher metric is the
Hessian of log Z.  In centered moments m_k = E[(L-E L)^k],

    D = det g = m2*m4 - m3^2 - m2^3.

Let H be the order-four centered moment Gram/Hankel matrix of
(1, Y, Y^2, Y^3), Y=L-E L:

    [[1,  0,  m2, m3],
     [0, m2,  m3, m4],
     [m2,m3,  m4, m5],
     [m3,m4,  m5, m6]].

The exact Hessian-surface scalar-curvature identity is

    R = (D^2 - det(H)) / (2 D^2)
      = 1/2 * (1 - det(H)/D^2).

Since H is a Gram matrix, det(H) >= 0, hence R <= 1/2 whenever D>0.
This script records an important correction: R is NOT sign-definite on the
quadratically confined number-gas parameter space.  Stable high-precision
examples occur with both R<0 and R>0.
"""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 60


def curvature(beta: float, eta: float, cutoff: int = 5000):
    if eta <= 0:
        raise ValueError("eta must be positive")
    beta = mp.mpf(beta)
    eta = mp.mpf(eta)

    logs = [mp.log(n) for n in range(1, cutoff + 1)]
    weights = [mp.e ** (-beta * L - eta * L * L) for L in logs]
    Z = mp.fsum(weights)
    probs = [w / Z for w in weights]
    mean = mp.fsum(p * L for p, L in zip(probs, logs))
    moments = {
        k: mp.fsum(p * (L - mean) ** k for p, L in zip(probs, logs))
        for k in range(2, 7)
    }

    m2, m3, m4 = moments[2], moments[3], moments[4]
    m5, m6 = moments[5], moments[6]
    D = m2 * m4 - m3 * m3 - m2**3
    H = mp.matrix(
        [
            [1, 0, m2, m3],
            [0, m2, m3, m4],
            [m2, m3, m4, m5],
            [m3, m4, m5, m6],
        ]
    )
    detH = mp.det(H)
    R = (D * D - detH) / (2 * D * D)
    return R, D, detH


def stable_value(beta: float, eta: float):
    values = []
    for cutoff in (1000, 5000, 20000):
        values.append(curvature(beta, eta, cutoff)[0])
    return values


def main():
    negative = stable_value(2.0, 0.5)
    positive = stable_value(0.0, 5.0)

    print("R(2, 0.5) cutoffs:")
    for value in negative:
        print(mp.nstr(value, 30))
    print("R(0, 5) cutoffs:")
    for value in positive:
        print(mp.nstr(value, 30))

    # Stable sign witnesses.
    assert max(negative) < mp.mpf("-0.90")
    assert min(positive) > mp.mpf("0.35")

    # Structural upper bound from det(H) >= 0, checked numerically here.
    for beta, eta in [(-5, 10), (0, 5), (2, 0.5), (10, 0.1)]:
        R, D, detH = curvature(beta, eta, 20000)
        assert D > 0
        assert detH >= 0
        assert R <= mp.mpf("0.5") + mp.mpf("1e-40")

    print("\nConclusion: curvature sign is not universal; the rigorous structural target is R <= 1/2, not R < 0.")


if __name__ == "__main__":
    main()
