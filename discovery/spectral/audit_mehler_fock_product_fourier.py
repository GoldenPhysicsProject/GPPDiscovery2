import mpmath as mp

mp.mp.dps = 70


def q(lam):
    return mp.pi * lam**2 / mp.cosh(mp.pi * lam)


def qhat_closed(k):
    s = 1 / mp.cosh(k / 2)
    return mp.pi / 4 * s * (2 * s**2 - 1)


def qhat_quad(k):
    f = lambda x: mp.cos(k * x) * q(x)
    return 2 * mp.quad(f, [0, 1, 3, 7, mp.inf])


if __name__ == '__main__':
    k0 = 2 * mp.acosh(mp.sqrt(2))
    print('zero =', mp.nstr(k0, 30))
    for k in [0, 0.5, 1.5, k0, 2.0, 4.0]:
        qc = qhat_closed(k)
        qn = qhat_quad(k)
        print('k =', mp.nstr(k, 20))
        print('  closed =', mp.nstr(qc, 25))
        print('  quad   =', mp.nstr(qn, 25))
        print('  error  =', mp.nstr(abs(qc-qn), 8))
