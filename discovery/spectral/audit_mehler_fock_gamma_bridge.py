import mpmath as mp

mp.mp.dps = 80


def P(lam):
    return mp.pi * lam / mp.sinh(mp.pi * lam)


def mehler(lam):
    return lam * mp.tanh(mp.pi * lam)


def audit(lam):
    p_gamma = abs(mp.gamma(1 + 1j * lam)) ** 2
    m_gamma = abs(mp.gamma(mp.mpf('0.5') + 1j * lam)) ** 2 / abs(mp.gamma(1j * lam)) ** 2
    product_gamma = lam**2 * abs(mp.gamma(mp.mpf('0.5') + 1j * lam)) ** 2
    return (
        abs(P(lam) - p_gamma),
        abs(mehler(lam) - m_gamma),
        abs(P(lam) * mehler(lam) - product_gamma),
    )


if __name__ == '__main__':
    for lam in [mp.mpf('0.1'), mp.mpf('0.7'), mp.mpf('1.3'), mp.mpf('3.0')]:
        eP, eM, eProd = audit(lam)
        print(lam)
        print('  P error      =', mp.nstr(eP, 12))
        print('  Mehler error =', mp.nstr(eM, 12))
        print('  product error=', mp.nstr(eProd, 12))
