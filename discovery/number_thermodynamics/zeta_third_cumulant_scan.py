#!/usr/bin/env python3
"""High-precision scan of the zeta Gibbs third cumulant on beta>1.

This is discovery code, not a proof of positivity.

For Z(beta)=zeta(beta) and energy E_n=log n,
  kappa_3(E) = <(E-<E>)^3>
             = -Z'''/Z + 3 Z' Z''/Z^2 - 2 (Z'/Z)^3
             = - d^3/d beta^3 log Z.

The script scans a geometric grid near beta=1 and a linear grid farther out.
"""

import mpmath as mp

mp.mp.dps = 80


def kappa3(beta):
    z = mp.zeta(beta)
    z1 = mp.diff(mp.zeta, beta, 1)
    z2 = mp.diff(mp.zeta, beta, 2)
    z3 = mp.diff(mp.zeta, beta, 3)
    return -z3 / z + 3 * z1 * z2 / z**2 - 2 * (z1 / z) ** 3


def main():
    near = [mp.mpf(1) + mp.power(10, -6 + 5 * j / 80) for j in range(81)]
    far = [mp.mpf("1.1") + mp.mpf("0.05") * j for j in range(1, 379)]
    grid = near + far
    vals = [(b, kappa3(b)) for b in grid]
    bmin, vmin = min(vals, key=lambda bv: bv[1])
    print("points:", len(vals))
    print("minimum sampled kappa3:", mp.nstr(vmin, 40))
    print("at beta:", mp.nstr(bmin, 30))
    print("all sampled positive:", all(v > 0 for _, v in vals))
    for b in map(mp.mpf, ["1.01", "1.05", "1.1", "1.2", "1.5", "2", "3", "5", "10", "20"]):
        print(mp.nstr(b, 8), mp.nstr(kappa3(b), 30))


if __name__ == "__main__":
    main()
