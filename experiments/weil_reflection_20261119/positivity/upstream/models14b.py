"""Round 14B models (integer / own-gamma-factor data only; zeros never used).
ZETA, EPS (x^2+5y^2, own r_Q, Gamma(s)), BEUR2 (spliced Beurling: real prime powers < 55 + DMV-type Beurling primes >= 55,
zeta's arch borrowed: it has none), DH (Davenport-Heilbronn, own coefficients, Gamma_R(s+1), conductor 5, no pole),
FTH (control F_theta = Lambda(s-theta)Lambda(s+theta): Euler product with positive weights 2cosh(theta log n)Lambda(n),
degree-2 FE, every zero off the line)."""
import sys, os, math, numpy as np
from scipy.special import digamma
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..'))
import harness as h
from akg_kg import vonmangoldt_table
NX = int(math.exp(8.6)) + 2
h.NMAX = NX
wz = lambda t: np.exp(-t/2)/(-np.expm1(-2*t))

def zeta():
    NS, LAM = vonmangoldt_table(NX)
    return dict(name='ZETA', n=NS.astype(float), c=LAM, C=digamma(0.25)-math.log(math.pi), w=wz, poles=[(0.5, 1.0)])

def eps():
    E = h.epstein_model()
    return dict(name='EPS', n=E['n'], c=E['c'], C=E['C'], w=E['w'], poles=[(0.5, 1.0)])

def beur2():
    Z = zeta(); B = h.beurling_model(x0=55.0); m = Z['n'] < 55
    n = np.concatenate([Z['n'][m], B['n']]); c = np.concatenate([Z['c'][m], B['c']]); o = np.argsort(n)
    return dict(Z, name='BEUR2', n=n[o], c=c[o])

KAP = (math.sqrt(10-2*math.sqrt(5))-2)/(math.sqrt(5)-1)
def dh_coeff():
    chi = {0: 0, 1: 1, 2: 1j, 3: -1j, 4: -1}
    return {r: ((1-1j*KAP)/2*chi[r] + (1+1j*KAP)/2*np.conj(chi[r])).real for r in range(5)}
def dh():
    cf = dh_coeff(); N = NX
    a = np.array([cf[k % 5] for k in range(N+1)]); a[0] = 0
    # -f'/f = sum Lf(n) n^-s :  a(n) log n = sum_{d|n} Lf(d) a(n/d), a(1)=1
    Lf = np.zeros(N+1); acc = np.zeros(N+1)
    for n in range(2, N+1):
        Lf[n] = a[n]*math.log(n) - acc[n]
        if Lf[n] != 0:
            k = np.arange(1, N//n + 1); acc[n*k] += Lf[n]*a[k]
    idx = np.nonzero(np.abs(Lf) > 1e-13)[0]
    return dict(name='DH', n=idx.astype(float), c=Lf[idx], C=digamma(0.75)-math.log(math.pi)+math.log(5),
                w=lambda t: np.exp(-1.5*t)/(-np.expm1(-2*t)), poles=[], a=a)

def fth(theta=0.2):
    Z = zeta()
    return dict(name=f'FTH{theta}', n=Z['n'], c=Z['c']*2*np.cosh(theta*np.log(Z['n'])),
                C=digamma(0.25+theta/2)+digamma(0.25-theta/2)-2*math.log(math.pi),
                w=lambda t: (np.exp(-(0.5-theta)*t)+np.exp(-(0.5+theta)*t))/(-np.expm1(-2*t)), poles=[(0.5+theta, 1.0), (0.5-theta, 1.0)], theta=theta)
