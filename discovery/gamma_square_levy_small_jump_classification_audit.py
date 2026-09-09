"""
Gamma-square / celestial chamber Levy small-jump classification.

For a>0 the corrected symmetric Levy density is

    nu_a(x) = a / (|x| sinh(pi |x|)).

This audit records and numerically checks the exact endpoint structure:

  x^2 nu_a(x) -> a/pi                         (x -> 0),
  x exp(pi x) nu_a(x) -> 2a                  (x -> +infty).

Hence near zero nu_a(x) ~ a/(pi |x|^2). Consequences:

* the Levy condition int min(1,x^2) nu_a(x) dx < infinity holds;
* jump activity is infinite: int_{|x|<1} nu_a(x) dx = infinity;
* total variation is infinite: int_{|x|<1} |x| nu_a(x) dx = infinity;
* for p>0, int_{|x|<1} |x|^p nu_a(x) dx is finite iff p>1;
  therefore the Blumenthal--Getoor index is exactly 1.

This is a structural classification of the continuous chamber convolution
semigroup with characteristic function sech(t/2)^(2a).  It is Discovery-level
until the endpoint/integrability statements are formalized in Lean.
"""

from mpmath import mp

mp.dps = 80


def nu(a, x):
    x = mp.mpf(x)
    return mp.mpf(a) / (abs(x) * mp.sinh(mp.pi * abs(x)))


def two_sided_p_moment_cutoff(a, p, eps):
    """2 int_eps^1 x^p nu_a(x) dx."""
    a, p, eps = mp.mpf(a), mp.mpf(p), mp.mpf(eps)
    return 2 * mp.quad(lambda x: x**p * nu(a, x), [eps, 1])


def levy_condition(a):
    """int_R min(1,x^2) nu_a(x) dx, evaluated symmetrically."""
    a = mp.mpf(a)
    near = 2 * mp.quad(lambda x: x**2 * nu(a, x), [0, 1])
    far = 2 * mp.quad(lambda x: nu(a, x), [1, mp.inf])
    return near + far


def check_close(label, got, target, tol=mp.mpf("1e-50")):
    err = abs(got - target)
    print(f"{label}:\n  got    = {mp.nstr(got, 60)}\n  target = {mp.nstr(target, 60)}\n  error  = {mp.nstr(err, 8)}")
    if err > tol:
        raise AssertionError(f"{label}: error {err} exceeds {tol}")


def main():
    a = mp.mpf("1.7")

    # Endpoint constants.
    for x in [mp.mpf("1e-10"), mp.mpf("1e-20"), mp.mpf("1e-30")]:
        val = x**2 * nu(a, x)
        print("small-x", mp.nstr(x, 4), mp.nstr(val, 50),
              "target", mp.nstr(a / mp.pi, 50))
    check_close("small-x endpoint at 1e-30", mp.mpf("1e-30")**2 * nu(a, mp.mpf("1e-30")),
                a / mp.pi, mp.mpf("1e-50"))

    for x in [20, 40, 80]:
        val = mp.mpf(x) * mp.e**(mp.pi * x) * nu(a, x)
        print("large-x", x, mp.nstr(val, 50), "target", mp.nstr(2*a, 50))
    check_close("large-x endpoint at 80", mp.mpf(80) * mp.e**(80*mp.pi) * nu(a, 80),
                2*a, mp.mpf("1e-50"))

    # The Levy condition is finite.
    lc = levy_condition(a)
    print("Levy condition integral (finite) =", mp.nstr(lc, 60))
    if not mp.isfinite(lc):
        raise AssertionError("Levy condition integral should be finite")

    # Cutoff behavior for p moments.  Theory from nu ~ a/(pi x^2):
    # p=1: 2a/pi log(1/eps) + O(1)
    # p<1: 2a/[pi(1-p)] eps^(p-1) + O(1)
    # p>1: finite as eps -> 0.
    print("\nTwo-sided small-jump p-moment cutoffs")
    for p in [mp.mpf("0.5"), mp.mpf("1.0"), mp.mpf("1.5"), mp.mpf("2.0")]:
        vals = []
        for eps in [mp.mpf("1e-3"), mp.mpf("1e-5"), mp.mpf("1e-7")]:
            vals.append(two_sided_p_moment_cutoff(a, p, eps))
        print("p =", p, "values =", [mp.nstr(v, 30) for v in vals])

    # p=1 logarithmic coefficient.
    eps1, eps2 = mp.mpf("1e-7"), mp.mpf("1e-10")
    m1, m2 = two_sided_p_moment_cutoff(a, 1, eps1), two_sided_p_moment_cutoff(a, 1, eps2)
    slope = (m2 - m1) / mp.log(eps1 / eps2)
    check_close("p=1 logarithmic divergence coefficient", slope, 2*a/mp.pi,
                mp.mpf("1e-6"))

    # p=1/2 power-law coefficient after multiplying by eps^(1-p).
    p = mp.mpf("0.5")
    eps = mp.mpf("1e-12")
    moment = two_sided_p_moment_cutoff(a, p, eps)
    scaled = moment * eps**(1-p)
    target = 2*a / (mp.pi * (1-p))
    check_close("p<1 power divergence coefficient", scaled, target, mp.mpf("1e-5"))

    # p>1 Cauchy convergence under shrinking cutoff.
    p = mp.mpf("1.5")
    m_a = two_sided_p_moment_cutoff(a, p, mp.mpf("1e-8"))
    m_b = two_sided_p_moment_cutoff(a, p, mp.mpf("1e-12"))
    print("p=1.5 cutoff difference =", mp.nstr(abs(m_b-m_a), 30), "(tends to 0)")

    print("\nPASS: corrected Gamma-square chamber Levy law has BG index 1,"
          " infinite activity, infinite variation, and finite quadratic Levy mass.")


if __name__ == "__main__":
    main()
