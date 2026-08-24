"""Zeta Gibbs ensemble: canonical cumulants and Fisher metric.

For beta>1, p_beta(n)=n^{-beta}/zeta(beta), n>=1, with energy E_n=log n.
Writing K(beta)=log zeta(beta), standard exponential-family differentiation gives

  <E> = -K'(beta) = -zeta'/zeta,
  Var(E) = K''(beta) >= 0,
  kappa_3(E) = -K'''(beta),

and generally the r-th energy cumulant is (-1)^r K^(r)(beta).
Thus g(beta)=K''(beta) is simultaneously the energy susceptibility and the
one-parameter Fisher information metric. The script verifies the first three
identities by direct high-precision summation against derivatives of log zeta.
"""
import mpmath as mp
mp.mp.dps = 60


def moments(beta):
    Z = mp.zeta(beta)
    m1 = mp.nsum(lambda k: mp.log(k)*k**(-beta), [1, mp.inf])/Z
    m2 = mp.nsum(lambda k: mp.log(k)**2*k**(-beta), [1, mp.inf])/Z
    m3 = mp.nsum(lambda k: mp.log(k)**3*k**(-beta), [1, mp.inf])/Z
    var = m2-m1*m1
    mu3 = m3-3*m1*m2+2*m1**3
    return m1,var,mu3


def K(beta): return mp.log(mp.zeta(beta))


if __name__ == '__main__':
    worst=mp.mpf('0')
    for beta in map(mp.mpf,['1.2','1.7','2.5','5.0']):
        mean,var,mu3=moments(beta)
        d1=mp.diff(K,beta,1); d2=mp.diff(K,beta,2); d3=mp.diff(K,beta,3)
        worst=max(worst,abs(mean+d1),abs(var-d2),abs(mu3+d3))
        assert var >= 0
    assert worst < mp.mpf('1e-45')
    print('PASS: <log n> = -d log(zeta)/d beta')
    print('PASS: Var(log n) = d^2 log(zeta)/d beta^2 >= 0')
    print('PASS: third central cumulant = -d^3 log(zeta)/d beta^3')
    print('worst residual:', mp.nstr(worst,8))
