import mpmath as mp

mp.mp.dps = 80


def P(lam):
    if lam == 0:
        return mp.mpf(1)
    return mp.pi * lam / mp.sinh(mp.pi * lam)


def rho(lam):
    return (mp.mpf(2) / mp.pi) * P(lam)


def characteristic_numeric(k):
    return 2 * mp.quad(lambda x: rho(x) * mp.cos(k * x), [0, mp.inf])


def characteristic_closed(k):
    return mp.sech(k / 2) ** 2


def even_moment_numeric(n):
    return 2 * mp.quad(lambda x: x ** (2 * n) * rho(x), [0, mp.inf])


def even_moment_closed(n):
    return (
        4
        * mp.factorial(2 * n + 1)
        / mp.pi ** (2 * n + 2)
        * (1 - mp.power(2, -(2 * n + 2)))
        * mp.zeta(2 * n + 2)
    )


print("normalization", mp.nstr(characteristic_numeric(0), 60))
for k in [mp.mpf("0.3"), mp.mpf("1"), mp.mpf("2"), mp.mpf("3.7")]:
    num = characteristic_numeric(k)
    exact = characteristic_closed(k)
    print("phi", k, mp.nstr(num, 60), mp.nstr(exact, 60), "err", mp.nstr(abs(num-exact), 8))

for n in range(1, 5):
    num = even_moment_numeric(n)
    exact = even_moment_closed(n)
    print("moment", 2*n, mp.nstr(num, 60), mp.nstr(exact, 60), "err", mp.nstr(abs(num-exact), 8))

# Low cumulants reconstructed from moments.
m2 = even_moment_numeric(1)
m4 = even_moment_numeric(2)
m6 = even_moment_numeric(3)
m8 = even_moment_numeric(4)
k2 = m2
k4 = m4 - 3*m2**2
k6 = m6 - 15*m4*m2 + 30*m2**3
k8 = m8 - 28*m6*m2 - 35*m4**2 + 420*m4*m2**2 - 630*m2**4
print("cumulants", *(mp.nstr(x, 60) for x in [k2, k4, k6, k8]))
print("targets", mp.mpf(1)/2, mp.mpf(1)/4, mp.mpf(1)/2, mp.mpf(17)/8)
