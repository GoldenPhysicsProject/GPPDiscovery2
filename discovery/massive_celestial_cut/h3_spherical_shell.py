"""Equal-mass celestial cut: fixed-energy H3 spherical transform.

For a two-particle cut with equal effective four-dimensional mass mu and total
COM energy M>2mu, set beta=sqrt(1-4mu^2/M^2)=tanh(eta), gamma=cosh(eta)=M/(2mu).
The massive scalar conformal-primary kernel restricted to the fixed-energy shell
is proportional to [gamma(1-beta x)]^{-Delta}. Its normalized angular average is

  A_Delta(eta) = 1/2 int_{-1}^1 [cosh eta - sinh eta x]^{-Delta} dx
               = sinh((1-Delta) eta)/((1-Delta) sinh eta).

On Delta=1+i lambda this is the H3 zonal spherical function

  phi_lambda(eta) = sin(lambda eta)/(lambda sinh eta),

with lambda=0 limit eta/sinh eta.

Multiplying by the equal-mass two-body phase-space total beta/(8 pi) gives

  beta phi_lambda/(8 pi)
    = sin(lambda eta)/(8 pi lambda cosh eta)
    = mu sin(lambda eta)/(4 pi M lambda).

This is a numerical/symbolic verification companion, not a formal proof.
"""
import mpmath as mp

mp.mp.dps = 60


def avg_numeric(eta, Delta):
    sh, ch = mp.sinh(eta), mp.cosh(eta)
    return mp.quad(lambda x: (ch - sh*x)**(-Delta), [-1, 1]) / 2


def avg_closed(eta, Delta):
    if abs(1-Delta) < mp.mpf('1e-50'):
        return eta/mp.sinh(eta)
    return mp.sinh((1-Delta)*eta)/((1-Delta)*mp.sinh(eta))


def phi(eta, lam):
    if abs(lam) < mp.mpf('1e-50'):
        return eta/mp.sinh(eta)
    return mp.sin(lam*eta)/(lam*mp.sinh(eta))


def phase_shell(eta, lam):
    beta = mp.tanh(eta)
    return beta*phi(eta, lam)/(8*mp.pi)


def phase_shell_mass(M, mu, lam):
    eta = mp.acosh(M/(2*mu))
    if abs(lam) < mp.mpf('1e-50'):
        return mp.tanh(eta)*eta/mp.sinh(eta)/(8*mp.pi)
    return mu*mp.sin(lam*eta)/(4*mp.pi*M*lam)


if __name__ == '__main__':
    worst = mp.mpf('0')
    for eta in map(mp.mpf, ['0.3','1.2','3.0']):
        for lam in map(mp.mpf, ['0.4','1.7','4.1']):
            Delta = 1 + 1j*lam
            e1 = abs(avg_numeric(eta,Delta)-avg_closed(eta,Delta))
            e2 = abs(avg_closed(eta,Delta)-phi(eta,lam))
            M = mp.mpf('7.3')
            mu = M/(2*mp.cosh(eta))
            e3 = abs(phase_shell(eta,lam)-phase_shell_mass(M,mu,lam))
            worst=max(worst,e1,e2,e3)
    assert worst < mp.mpf('1e-50')
    print('PASS: angular H3 kernel average = sinh((1-Delta)eta)/((1-Delta)sinh eta)')
    print('PASS: principal series gives sin(lambda eta)/(lambda sinh eta)')
    print('PASS: phase-space weighted shell = mu*sin(lambda eta)/(4*pi*M*lambda)')
    print('worst residual:', mp.nstr(worst,8))
