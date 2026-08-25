import mpmath as mp

mp.mp.dps = 80


def Lambda(s):
    return mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def Lambda_prime(s):
    return mp.diff(Lambda, s)


if __name__ == '__main__':
    for t in [mp.mpf('0.3'), mp.mpf('3.0'), mp.mpf('10.0'), mp.mpf('20.0')]:
        s = mp.mpf('0.5') + 1j * t
        val = Lambda(s)
        der = Lambda_prime(s)
        print('t =', t)
        print('  Im Lambda       =', mp.nstr(mp.im(val), 14))
        print('  Re Lambda_prime =', mp.nstr(mp.re(der), 14))
        if abs(val) > mp.mpf('1e-60'):
            print('  Re logderiv     =', mp.nstr(mp.re(der / val), 14))
