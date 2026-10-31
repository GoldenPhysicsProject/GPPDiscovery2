"""Numerical diagnostics for exact unramified Eisenstein scattering identities.

The mathematical statements are proved from the meromorphic completed
zeta functional equation, not from these floating mpmath checks.
DO NOT interpret unitary scattering as a proof of RH.
"""
import mpmath as mp

mp.mp.dps = 65
q = mp.mpf


def completed(s):
    return mp.power(mp.pi, -s/2) * mp.gamma(s/2) * mp.zeta(s)


def scattering(w):
    return completed(2*w - 1) / completed(2*w)


def shifted_completed(s, theta):
    return completed(s + theta) * completed(s - theta)


def fake_scattering(w, theta):
    return shifted_completed(2*w - 1, theta) / shifted_completed(2*w, theta)


def lderiv(s):
    return (-mp.log(mp.pi)/2 + mp.digamma(s/2)/2
            + mp.diff(mp.zeta, s)/mp.zeta(s))


def main():
    one = q(1)
    half = one/2
    theta = q('0.1')
    for t in map(q, ('0.3', '1.0', '3.1', '8.7')):
        w = half + 1j*t
        value = scattering(w)
        mirror = mp.conj(completed(1+2j*t))/completed(1+2j*t)
        assert abs(value-mirror) < q('1e-50')
        assert abs(abs(value)-1) < q('1e-50')
        phase_deriv = mp.im(mp.diff(
            lambda u: mp.log(scattering(half + 1j*u)), t))
        analytic = -4 * mp.re(lderiv(1+2j*t))
        assert abs(phase_deriv-analytic) < q('1e-45')
        fake = fake_scattering(w, theta)
        assert abs(abs(fake)-1) < q('1e-49')
        print('t=',mp.nstr(t,4),' |phi|=',mp.nstr(abs(value),9),
              ' phase slope=',mp.nstr(analytic,13),
              ' |phi_theta|=',mp.nstr(abs(fake),9))
    rho = mp.zetazero(1)
    wzero = (rho+1)/2
    wpole = rho/2
    assert abs(scattering(wzero)) < q('1e-48')
    assert abs(1/scattering(wpole)) < q('1e-48')
    assert abs(mp.re(wzero)-q('0.75')) < q('1e-50')
    assert abs(mp.re(wpole)-q('0.25')) < q('1e-50')
    fakezero = (rho + theta + 1)/2
    assert abs(fake_scattering(fakezero, theta)) < q('1e-47')
    assert abs(mp.re(fakezero)-q('0.8')) < q('1e-50')
    print('zero -> scattering w=(rho+1)/2 Re(w)=3/4; '
          'pole -> w=rho/2 Re(w)=1/4')
    print('shifted fake zero -> Re(w)=0.8, despite FE and '
          '|phi_theta(1/2+it)|=1')
    print('All scattering identity checks PASS. RH OPEN.')


if __name__ == '__main__':
    main()
