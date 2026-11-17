"""Paritized rank-one pole healing, exact algebra and source-only finite Galerkin.
The result is an RH-relevant pilot; no infinite-width positivity certificate.
"""
import sympy as sp
import numpy as np
from scipy.linalg import eigh
from galerkin_two_pole_source import build, pole_moment

# Generalized rank-one Krein criterion tested over exact rationals:
# if H has inertia (one negative, all other positive, zero nullity),
# H+t u u^T is PSD iff (u^T H^-1 u <= -1/t).
for u in [sp.Matrix([1,sp.Rational(1,2)]),
          sp.Matrix([1,1]),
          sp.Matrix([2,sp.Rational(1,3)])]:
    H=sp.diag(-1,1)
    q=(u.T*H.inv()*u)[0]
    for t in [sp.Rational(1,2),sp.Rational(4,3),sp.Rational(2)]:
        M=H+t*u*u.T
        psd=(M[0,0]>=0 and M.det()>=0)
        claim=(1+t*q<=0)
        assert psd==claim,(u,q,t,psd,claim)
print('PASS exact rank-one inertia/scalar criterion over rational examples')

# True source at L=18/25, only prime event n=2:
M=48
B,V,W,E=build(M,True)
c=np.array([pole_moment(n+1,'c') for n in range(M)])
s=np.array([pole_moment(n+1,'s') for n in range(M)])
H=W-2*np.outer(c,c)+2*np.outer(s,s)  # pole-removed source
# Dirichlet sine n odd is even reflection parity: indices 0,2,4,...
for parity in [0,1]:
    ix=np.arange(parity,M,2)
    block=H[np.ix_(ix,ix)]
    full=W[np.ix_(ix,ix)]
    evals=np.linalg.eigvalsh(block)
    label='even' if parity==0 else 'odd'
    print(label,'no-pole bottom eigenvalues',evals[:4],
          'negative index numerical',int((evals<0).sum()),
          'full bottom',np.linalg.eigvalsh(full)[0],
          'largest normalized prime Gram',eigh(V[np.ix_(ix,ix)],B[np.ix_(ix,ix)],eigvals_only=True)[-1])
    if parity==0:
        ce=c[ix]
        q=float(ce@np.linalg.solve(block,ce))
        assert evals[0]<0 and evals[1]>0
        assert q<-.5
        print('even pole q=<c,H^-1 c> =',q,
              'critical pole coefficient t*=',-1/q,
              'actual pole coefficient=2',
              'scalar margin = ', -(1+2*q))
        # Numerically verify inverse pole healing, no small positive inverse needed
        cured=block+2*np.outer(ce,ce)
        assert np.linalg.eigvalsh(cured)[0]>0
    else:
        se=s[ix]
        odd_full=block-2*np.outer(se,se)
        assert np.linalg.eigvalsh(block)[0]>0
        tau=float(se@np.linalg.solve(block,se))
        assert 2*tau<1
        print('odd pole criterion 2<s,H_odd^-1 s>=',2*tau,'<1')
        assert np.linalg.eigvalsh(odd_full)[0]>0
print('PASS finite source-only parity-resolved rank-one test; NOT continuum positivity')
