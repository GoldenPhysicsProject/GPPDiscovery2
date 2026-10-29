"""Exact rational falsifier for local-to-global Weil/prime sewing.

No claim about the actual completed Weil form. This is a *necessary*
constraint on any proposed global completion of the sharp positive local
prime-threshold crossed block described in the 2026-10-28 GPP-bridge note.

For x in (0,1), L>0, the N=1 local block is

    B = [[L^2*x/(1-x), -L*x], [-L*x, x*(1-x)]]

and q(t,a) = x*(1-x)*(a-L*t/(1-x))^2 >= 0.
Its null direction is n=(1,L/(1-x)). Two such local blocks coupled by
2*eps*t1*t2 restrict to [[0,eps],[eps,0]] on their null vectors;
hence one negative direction for every eps != 0.

If a proposed completed global form also supplies diagonal null-sector
terms d1*t1^2+d2*t2^2, a necessary PSD condition is
    d1 >= 0, d2 >= 0, d1*d2 >= eps^2.
"""

from fractions import Fraction as F


def local_block(x, L, t, a):
    assert F(0) < x < F(1)
    return (L * L * x / (1 - x) * t * t
            - 2 * L * x * t * a
            + x * (1 - x) * a * a)


def local_square(x, L, t, a):
    return x * (1 - x) * (a - L * t / (1 - x)) ** 2


def coupled(x1, L1, t1, a1, x2, L2, t2, a2, eps, d1=F(0), d2=F(0)):
    return (local_block(x1, L1, t1, a1)
            + local_block(x2, L2, t2, a2)
            + 2 * eps * t1 * t2
            + d1 * t1 * t1 + d2 * t2 * t2)


def run():
    x1, L1 = F(1, 2), F(1)
    x2, L2 = F(1, 3), F(2)
    n1, n2 = L1 / (1 - x1), L2 / (1 - x2)
    assert (n1, n2) == (F(2), F(3))

    for x, L in ((x1, L1), (x2, L2)):
        for t in (F(-3), F(-1), F(0), F(1), F(4)):
            for a in (F(-5), F(-1), F(0), F(1), F(8)):
                assert local_block(x, L, t, a) == local_square(x, L, t, a)
                assert local_block(x, L, t, a) >= 0
        assert local_block(x, L, F(1), L / (1 - x)) == 0

    for eps in (F(1), F(1, 100), F(1, 10**9), F(-1, 7)):
        t1, t2 = F(1), -F(1) if eps > 0 else F(1)
        val = coupled(x1, L1, t1, n1 * t1,
                      x2, L2, t2, n2 * t2, eps)
        assert val == -2 * abs(eps)
        assert val < 0

    # On the two-dimensional null plane, test the exact determinant test.
    for eps in (F(1, 10), F(-2, 7)):
        for d1, d2 in ((F(0), F(0)), (F(1), F(1)),
                       (F(1, 10), F(1, 10)), (F(1, 10), F(1, 100))):
            determinant = d1 * d2 - eps * eps
            if determinant < 0:
                # t1=1, t2=-eps/d2 gives a negative witness when d2>0;
                # d2=0 uses a larger finite t2.
                if d2:
                    t1, t2 = F(1), -eps / d2
                else:
                    t1, t2 = F(1), -F(10**4) if eps > 0 else F(10**4)
                quadratic = d1*t1*t1 + d2*t2*t2 + 2*eps*t1*t2
                assert quadratic < 0
            else:
                for t1 in range(-5, 6):
                    for t2 in range(-5, 6):
                        quadratic = d1*t1*t1 + d2*t2*t2 + 2*eps*t1*t2
                        assert quadratic >= 0

    # Independent support windows can each be strictly positive, yet the
    # global form is negative (no truncation or tail error at all).
    def support_toy(a, b):
        return a*a + b*b - F(3, 4) * (a+b)**2
    for a in range(-10, 11):
        assert support_toy(F(a), F(0)) == F(a*a, 4)
        assert support_toy(F(0), F(a)) == F(a*a, 4)
    assert support_toy(F(1), F(1)) == -1

    print("PASS: 50 exact local prime Schur squares, with sharp null directions")
    print("PASS: arbitrarily small cross-prime coupling defeats local PSD")
    print("PASS: necessary null-mode completion inequality d1*d2 >= eps^2")
    print("PASS: strict positivity on each separate support window does not extend")


if __name__ == "__main__":
    run()
