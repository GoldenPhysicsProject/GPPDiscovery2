"""Executable audit for the derivative kernel in the continuous-sech Levy program.

For
    nu_c(x) = c / (|x| sinh(pi |x|)),
    K_c(t,x) = (1-cos(tx)) nu_c(x),
we have away from x=0
    d/dt K_c(t,x) = D_c(t,x) := x sin(tx) nu_c(x).

The point of this audit is the domination needed for differentiation under the
integral, uniformly for |t| <= T:

  |D_c(t,x)| <= c T / pi                  for |x| <= 1,
  |D_c(t,x)| <= 4 c exp(-pi |x|)          for |x| >= 1.

The first bound uses |sin u| <= |u| and sinh y >= y.  For the second,
|sin u| <= 1 and, for y >= pi,
    sinh y = exp(y)(1-exp(-2y))/2 >= exp(y)/4.
Thus an explicit L1 majorant has total integral
    2 c T / pi + 8 c exp(-pi) / pi.

This script is an executable numerical audit only; the inequalities above are
analytic and are intended for Lean promotion.  It does not prove the final
sine-over-sinh transform or the Levy-Khintchine exponent identity.
"""

import math


def levy_density(c: float, x: float) -> float:
    if x == 0.0:
        return 0.0
    return c / (abs(x) * math.sinh(math.pi * abs(x)))


def derivative_kernel(c: float, t: float, x: float) -> float:
    return x * math.sin(t * x) * levy_density(c, x)


def core_majorant(c: float, T: float) -> float:
    return c * T / math.pi


def tail_majorant(c: float, x: float) -> float:
    return 4.0 * c * math.exp(-math.pi * abs(x))


def total_majorant_integral(c: float, T: float) -> float:
    return 2.0 * c * T / math.pi + 8.0 * c * math.exp(-math.pi) / math.pi


def audit(c: float, t: float) -> None:
    assert c >= 0.0
    T = abs(t)

    # Dense core audit, omitting x=0 where the totalized density is set to 0.
    for j in range(1, 10_000):
        x = -1.0 + 2.0 * j / 10_000.0
        lhs = abs(derivative_kernel(c, t, x))
        rhs = core_majorant(c, T)
        assert lhs <= rhs * (1.0 + 1e-12)

    # Representative two-sided tail audit.
    for a in (1.0, 1.1, 1.5, 2.0, 3.0, 5.0, 8.0):
        rhs = tail_majorant(c, a)
        assert abs(derivative_kernel(c, t, a)) <= rhs * (1.0 + 1e-12)
        assert abs(derivative_kernel(c, t, -a)) <= rhs * (1.0 + 1e-12)

    print(
        f"c={c:g} t={t:g} "
        f"core={core_majorant(c,T):.16g} "
        f"L1_majorant={total_majorant_integral(c,T):.16g}"
    )


if __name__ == "__main__":
    for chamber, frequency in ((0.25, 0.8), (0.7, 1.3), (1.2, -2.1)):
        audit(chamber, frequency)
    print("all derivative-kernel domination checks passed")
