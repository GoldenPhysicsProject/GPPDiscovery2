"""Damp the entire arithmetic Weil distribution and test a reflected wave."""
import math
from functools import partial
from pathlib import Path
import sys
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'positivity'))
from translates import models

L = 3
mode = 20
shift = math.log(7)
end = L + shift

def overlap(t):
    x = np.abs(t)
    k = mode * math.pi / L
    return np.where(x < L, (1-x/L)*np.cos(k*x)+np.sin(k*x)/(k*L), 0.)

def corr(t):
    return overlap(t) + (overlap(t+shift)+overlap(t-shift))/2

def energy(model, a):
    c0 = float(corr(0))
    def test(t):
        return np.exp(-a*t)*corr(t)
    def integrate(fn):
        return quad(fn, 0, end, points=[L-shift,shift,L],
                    epsabs=2e-12, epsrel=2e-12)[0]
    arch = model['C']*c0 + 2*integrate(lambda t: model['w'](t)*(c0-test(t)))
    arch += 2*c0*quad(model['w'],end,np.inf,epsabs=1e-13)[0]
    poles = sum(4*weight*integrate(lambda t: np.cosh(b*t)*test(t))
                for b,weight in model['poles'])
    n = model['n']
    sel = n < np.exp(end)
    prime = 2*np.dot(model['c'][sel]/np.sqrt(n[sel]),test(np.log(n[sel])))
    return arch+poles-prime

if __name__ == '__main__':
    z = partial(energy, models.zeta())
    f = partial(energy, models.fth(.25))
    print('damping       zeta          shifted product (theta=1/4)')
    for a in (0,.01,.025,.05,.1,.15,.2,.25,.5,1,2,10):
        print(f'{a:7.3f}  {z(a):12.8f}  {f(a):12.8f}')
    root=brentq(f,0,.25)
    print('sign crossing for this single wave',root)
    assert f(0)<0 and f(.25)>0 and z(0)>0
