#!/usr/bin/env python3
"""Exact off-support gamma Toeplitz identity and rational Laplace-tail cap.

Let b(u)=sin(pi*u)^2 1_[0,1](u), S(z)=int b(u) exp(z*u)du, and
G(t)=int b(u)b(u+t)du.  For distance x>=1 between two translated bumps,
the real digamma spectral Toeplitz entry is EXACTLY

  A(x) = - sum_(n>=0) exp(-lambda_n*(x-1)) * S(-lambda_n)^2,
  lambda_n=2*n+1/2                (zeta),
  lambda_n=2*n+1/2 +/- 1/4      (the F_theta control).

Derivation: use psi(z)=-EulerGamma+int_0^infty
(exp(-u)-exp(-zu))/(1-exp(-u))du and Fourier inversion of |bhat|^2:
(1/pi)int_0^infty |bhat(t)|^2 cos(xt)dt=G(x).
For x>=1, G(x)=G(x+u/2)=0, so the Euler/log/pi terms vanish and

 A(x)=-int_0^infty exp(-a*u)/(2*(1-exp(-u)))G(x-u/2)du
     =-int_{x-1}^{x+1} exp(-2*a*v)/(1-exp(-2*v))G(x-v)dv,

where a=1/4 in zeta, a=1/4+/-1/8 for the F_theta control.  Expanding
the geometric denominator gives lambda_n=2*(n+a).  Since the bump is
symmetric around 1/2, S(lambda)=exp(lambda)S(-lambda), proving the sum.

This removes oscillatory digamma quadrature from EVERY gamma Toeplitz
entry at lattice separation d>=2 when delta=7/10.  Diagonals d=0,1
remain untouched and require a separate source-integral certificate.

After N terms, a completely rational bound follows from
S(-lambda)<20/lambda^3 (pi^2<10),
exp(-T)<=1/sum_{j=0}^J T^j/j!, and
1/(1-exp(-2L))<=(1+2L)/(2L) for L=x-1>0.

All identities are paper-level derivations; this executable checks the
specified normalization numerically and gives exact-rational tail caps.
It does not certify finite transcendental terms or prove RH.
"""

import argparse
from fractions import Fraction
import json
import math
import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parent))
from arch_annihilator_full_s1_probe import sine2_laplace


def rational_taylor_exp(t: Fraction, degree: int) -> Fraction:
    if t < 0 or degree < 0:
        raise ValueError("positive t and nonnegative degree required")
    total=Fraction(1)
    term=Fraction(1)
    for j in range(1,degree+1):
        term*=t/j
        total+=term
    return total


def rational_tail_cap(d: int, theta: Fraction, n_modes: int = 80,
                      taylor_degree: int = 36) -> Fraction:
    """Strict all-Arch-mode remainder bound from index N, no floats."""
    if d<2 or theta not in (Fraction(0),Fraction(1,4)) or n_modes<1:
        raise ValueError("d>=2; theta 0 or 1/4; n_modes>=1 required")
    L=Fraction(7*d,10)-1
    offsets=([Fraction(1,2)] if theta==0 else
             [Fraction(1,2)-theta,Fraction(1,2)+theta])
    geometric_upper=(1+2*L)/(2*L)
    return sum((Fraction(400)*geometric_upper/
                (2*n_modes+offset)**6/
                rational_taylor_exp((2*n_modes+offset)*L,taylor_degree))
               for offset in offsets)


def laplace_offsupport(d: int, theta: float, n_modes: int = 80) -> float:
    if d<2 or theta not in (0.,.25) or n_modes<1:
        raise ValueError("d>=2; theta 0 or 1/4; n_modes>=1 required")
    L=.7*d-1
    shifts=(0.,) if theta==0 else (-theta,theta)
    return -math.fsum(math.exp(-(2*n+.5+shift)*L)*
                      sine2_laplace(-(2*n+.5+shift))**2
                      for shift in shifts for n in range(n_modes))


def direct_digamma_offsupport(d: int, theta: float, cutoff: float = 800.) -> float:
    """Independent oscillatory source gamma integral; not a certified tail."""
    from scipy.integrate import quad
    from scipy.special import digamma

    def envelope(t):
        if abs(t)<1e-10:
            return .5
        if abs(t-2*math.pi)<1e-8:
            return -.25
        return 4*math.pi**2*math.sin(t/2)/(t*(4*math.pi**2-t*t))

    def integrand(t):
        if theta==0.:
            gamma=digamma(.25+.5j*t).real-math.log(math.pi)
        else:
            gamma=(digamma(.25-theta/2+.5j*t).real+
                   digamma(.25+theta/2+.5j*t).real-2*math.log(math.pi))
        return gamma*envelope(t)**2*math.cos(.7*d*t)/math.pi

    cuts=sorted(set(x for x in (0.,2*math.pi,20.,60.,200.,cutoff)
                    if x<=cutoff))
    return math.fsum(quad(integrand,lo,hi,epsabs=1e-12,limit=500)[0]
                     for lo,hi in zip(cuts,cuts[1:]))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--n-modes',type=int,default=80)
    p.add_argument('--taylor-degree',type=int,default=36)
    p.add_argument('--cutoff',type=float,default=800.)
    p.add_argument('--compare-digamma',action='store_true')
    args=p.parse_args()
    rows=[]
    for theta in (0.,.25):
        for d in range(2,6):
            cap=rational_tail_cap(d,Fraction(0) if theta==0. else Fraction(1,4),
                                  args.n_modes,args.taylor_degree)
            entry={'theta':theta,'d':d,'x':.7*d,
                   'laplace_partial':laplace_offsupport(d,theta,args.n_modes),
                   'rational_tail_upper':str(cap),
                   'tail_upper_float':float(cap)}
            if args.compare_digamma:
                direct=direct_digamma_offsupport(d,theta,args.cutoff)
                entry['direct_digamma_numeric']=direct
                entry['independent_discrepancy']=entry['laplace_partial']-direct
                # The direct cutoff is not rigorously enclosed; this is
                # a regression/normalization diagnostic only.
                assert abs(entry['independent_discrepancy'])<2e-10
            rows.append(entry)
    print(json.dumps({'status':'Exact identity and rational mode-tail; finite terms not interval certified',
                      'rows':rows},indent=2))


if __name__=='__main__':
    main()
