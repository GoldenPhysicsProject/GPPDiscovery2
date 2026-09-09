import mpmath as mp

mp.mp.dps = 60


def rho(a, x):
    """Gamma-square density extending the normalized celestial spectral law."""
    return (4 ** a / (2 * mp.pi * mp.gamma(2 * a))) * abs(mp.gamma(a + 1j * x)) ** 2


def phi(a, t):
    """Exact characteristic function predicted by the Barnes/Fourier identity."""
    return mp.sech(t / 2) ** (2 * a)


def even_integral(f):
    return 2 * mp.quad(f, [0, mp.inf])


def close(x, y, tol=mp.mpf("1e-45")):
    return abs(x - y) < tol


# Noninteger parameters are included deliberately: the result is a continuous
# convolution semigroup, not merely an integer convolution-power observation.
for a in [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("1.5"), mp.mpf("2.3")]:
    normalization = even_integral(lambda x: rho(a, x))
    assert close(normalization, 1)

    for t in [mp.mpf("0.3"), mp.mpf("1.2")]:
        fourier = even_integral(lambda x: mp.cos(t * x) * rho(a, x))
        assert close(fourier, phi(a, t), mp.mpf("1e-42"))

    second_moment = even_integral(lambda x: x * x * rho(a, x))
    fourth_moment = even_integral(lambda x: x ** 4 * rho(a, x))
    assert close(second_moment, a / 2)
    assert close(fourth_moment, a * (1 + 3 * a) / 4)

# At a=1 the Gamma-square family reduces exactly to the normalized celestial
# spectral density rho_1(x)=2x/sinh(pi x), using
# |Gamma(1+ix)|^2 = pi x / sinh(pi x).
for x in [mp.mpf("0.2"), mp.mpf("0.8"), mp.mpf("1.7")]:
    assert close(rho(1, x), 2 * x / mp.sinh(mp.pi * x))

# The convolution semigroup is exact at characteristic-function level:
# phi_{a+b}=phi_a phi_b.
for a, b, t in [
    (mp.mpf("0.7"), mp.mpf("1.1"), mp.mpf("0.9")),
    (mp.mpf("0.25"), mp.mpf("2.4"), mp.mpf("1.7")),
]:
    assert close(phi(a + b, t), phi(a, t) * phi(b, t))

print("PASS")
print("rho_a(x) = 4^a |Gamma(a+i x)|^2 / (2 pi Gamma(2a))")
print("hat rho_a(t) = sech(t/2)^(2a)")
print("Var = a/2")
print("E[X^4] = a(1+3a)/4")
print("a=1 gives rho_1(x)=2x/sinh(pi x)")
