#!/usr/bin/env python3
"""Controls for the strong-log-concavity Fisher-zero counterexample.

No Riemann-zero data are used.
"""

import json
import math
import cmath


def phi(t: complex, A: float, eps: float, b: float) -> complex:
    num = cmath.exp(-(t*t)/(2*A))
    num *= 1 + eps * math.exp(-(b*b)/(2*A)) * cmath.cosh(b*t/A)
    den = 1 + eps * math.exp(-(b*b)/(2*A))
    return num / den


def main() -> None:
    A, eps, b = 12.0, 0.1, 1.0
    curvature_upper = -A + eps*b*b/(1-eps)
    C0 = math.exp(b*b/(2*A))/eps
    a = math.acosh(C0)
    t0 = (A/b) * complex(a, math.pi)
    t1 = (A/b) * complex(-a, math.pi)

    out = {
        "uses_riemann_zero_data": False,
        "A": A,
        "eps": eps,
        "b": b,
        "log_density_curvature_upper_bound": curvature_upper,
        "C0": C0,
        "arcosh_C0": a,
        "first_complex_zero": [t0.real, t0.imag],
        "reflected_complex_zero": [t1.real, t1.imag],
        "abs_phi_at_first_zero": abs(phi(t0, A, eps, b)),
        "abs_phi_at_reflected_zero": abs(phi(t1, A, eps, b)),
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
