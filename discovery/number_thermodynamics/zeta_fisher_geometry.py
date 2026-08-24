"""Zeta Gibbs ensemble: canonical cumulants and Fisher metric.

For beta>1, p_beta(n)=n^{-beta}/zeta(beta), n>=1, with energy E_n=log n.
Writing K(beta)=log zeta(beta), standard exponential-family differentiation gives

  <E> = -K'(beta) = -zeta'/zeta,
  Var(E) = K''(beta) >= 0,
  kappa_3(E) = -K'''(beta),

and generally the r-th energy cumulant is (-1)^r K^(r)(beta).
Thus g(beta)=K''(beta) is simultaneously the energy susceptibility and the
one-parameter Fisher information metric. The script verifies the first three
identities by high-precision moment evaluation against derivatives of log zeta.

A plain ``mp.nsum`` is not reliable here when beta is close to 1: the
log-weighted Dirichlet series converges too slowly.  We therefore sum an
initial segment directly and evaluate the infinite tail as a derivative of
the Hurwitz zeta function,

  sum_{n=N}^infinity (log n)^r n^{-beta}
      = (-1)^r d^r/d beta^r zeta(beta, N).

This is an exact decomposition, not a truncation approximation.
"""
import mpmath as mp
mp.mp.dps = 60


def log_moment_sum(beta, order, cutoff=64):
    """Return sum (log n)^order / n^beta using an exact analytic tail."""
    head = mp.fsum(
        mp.log(n) ** order * mp.power(n, -beta)
        for n in range(1, cutoff)
    )
    tail = (-1) ** order * mp.diff(
        lambda s: mp.zeta(s, cutoff), beta, order
    )
    return head + tail


def moments(beta):
    Z = mp.zeta(beta)
    m1 = log_moment_sum(beta, 1) / Z
    m2 = log_moment_sum(beta, 2) / Z
    m3 = log_moment_sum(beta, 3) / Z
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
