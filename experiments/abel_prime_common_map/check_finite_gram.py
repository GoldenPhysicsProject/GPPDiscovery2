"""Reproducible standard-library checks for the 2026-11-16 common Abel-prime map.

This is an algebraic/finite numerical sanity check only; analytic theorems are in
research/abel_prime_common_map_2026_11_16.md. No RH inference.
"""
import math


def abel_pair(epsilon, xi, eta):
    """Exactly ε∫exp(-ε|u|)exp(i(eta-xi)u)du for real frequencies."""
    return 2 * epsilon**2 / (epsilon**2 + (eta - xi)**2)


def rational_gram(frequencies):
    return [
        [2 / (1 + (b - a)**2) for b in frequencies]
        for a in frequencies
    ]


def cholesky_min_pivot(matrix):
    """Minimal strictly positive Cholesky pivot; not an eigenvalue bound."""
    n = len(matrix)
    lower = [[0.0] * n for _ in range(n)]
    pivots = []
    for i in range(n):
        for j in range(i + 1):
            acc = matrix[i][j] - sum(
                lower[i][k] * lower[j][k] for k in range(j)
            )
            if i == j:
                if acc <= 0:
                    raise ArithmeticError("Nonpositive pivot")
                lower[i][j] = math.sqrt(acc)
                pivots.append(acc)
            else:
                lower[i][j] = acc / lower[j][j]
    return min(pivots)


def prime_bounds(p):
    q = 1 / math.sqrt(p)
    return 1 / (1 + q), 1 / (1 - q)


def defect_multiplier(p, phase):
    q = 1 / math.sqrt(p)
    return 2 * q * (math.cos(phase) - q) / (
        1 - 2 * q * math.cos(phase) + q*q
    )


def run():
    taus = (0.0, 1.0, -1.0, 0.5)
    gram = rational_gram(taus)
    pivot = cholesky_min_pivot(gram)
    assert pivot > 1e-8

    # Two prime-channel basis vectors b_0 and b_1. Their exact H norms are
    # both 2, and the target direct-sum Gram norm is 4.
    d = math.log(3) - math.log(2)
    rows = []
    for e in (0.1, 0.03, 0.01, 0.003):
        cross = abel_pair(e, math.log(2), math.log(3) + e)
        actual = 4 + 2*cross
        assert actual >= 4
        assert abs(actual - 4) < 20 * e*e / (d*d)
        rows.append((e, cross, actual))
    assert rows[-1][1] < rows[0][1]

    # The p=2 endpoint may not be excluded; these are exact analytical
    # endpoint evaluations subject to floating-point roundoff.
    for p in (2, 3, 5):
        q = 1 / math.sqrt(p)
        lo, hi = prime_bounds(p)
        assert math.isclose(lo, 1/(1+q))
        assert math.isclose(hi, 1/(1-q))
        assert math.isclose(defect_multiplier(p, 0), 2*q/(1-q))
        assert math.isclose(defect_multiplier(p, math.pi), -2*q/(1+q))
        assert defect_multiplier(p, 0) > 0 > defect_multiplier(p, math.pi)

    c2 = (math.log(2)/2) / (1+1/math.sqrt(2))**2
    assert c2 > 0
    print("Status: PASS (floating-point sanity checks, not proof)")
    print("Rational-frequency 4x4 Gram min Cholesky pivot:", f"{pivot:.12g}")
    print("ε | cross-prime inner product | joint Abel norm² (target=4)")
    for e, cross, actual in rows:
        print(f"{e:.3f} | {cross:.12g} | {actual:.12g}")
    print("p=2 sharp resolvent lower/upper:", prime_bounds(2))
    print("p=2 signed defect min/max:",
          defect_multiplier(2, math.pi), defect_multiplier(2, 0))
    print("Uniform finite-rank norm-defect floor c_2:", f"{c2:.12g}")


if __name__ == "__main__":
    run()
