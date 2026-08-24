#!/usr/bin/env python3
"""
Exact thermodynamic stability identities for the zeta Gibbs ensemble.

For beta>1,
    p_beta(n) = n^(-beta)/zeta(beta),
    K(beta) = log zeta(beta),
    U(beta) = E_beta[log n] = -K'(beta),
    Var_beta(log n) = K''(beta)
by termwise differentiation of the absolutely convergent Dirichlet series.
With physical temperature T=1/beta,
    C = dU/dT = beta^2 K''(beta) = beta^2 Var(log n) >= 0.
For entropy S=K-beta*K',
    dS/dbeta = -beta*K''(beta) <= 0.
Thus K'' is simultaneously Fisher information, energy susceptibility,
and heat capacity divided by beta^2.
"""
import mpmath as mp
mp.mp.dps = 60

for beta in [mp.mpf('1.2'), mp.mpf('1.7'), mp.mpf('2.0'), mp.mpf('4.0')]:
    z = mp.zeta(beta)
    zp = mp.diff(mp.zeta, beta, 1)
    zpp = mp.diff(mp.zeta, beta, 2)
    K2 = mp.diff(lambda b: mp.log(mp.zeta(b)), beta, 2)
    variance = zpp/z - (zp/z)**2
    assert abs(K2-variance) < mp.mpf('1e-50')
    assert K2 > 0
    heat_capacity = beta**2*K2
    entropy_slope = -beta*K2
    assert heat_capacity > 0
    assert entropy_slope < 0

print('PASS: K\'\' = zeta\'\'/zeta - (zeta\'/zeta)^2 = Var_beta(log n)')
print('PASS: number-gas heat capacity beta^2 K\'\' is positive for tested beta>1')
print('PASS: entropy slope dS/dbeta = -beta K\'\' is negative')
