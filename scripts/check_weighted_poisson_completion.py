#!/usr/bin/env python3
"""Finite float64 controls for the analytic Poisson quotient; not a proof.

Reconstructed after the interrupted Work Mode workspace was replaced.
Run from any directory; output defaults to the companion research JSON.
"""
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh
from scipy.special import gamma


def cq(f, lo, hi):
    return quad(lambda x: complex(f(x)).real, lo, hi, epsabs=2e-12)[0] + 1j * quad(
        lambda x: complex(f(x)).imag, lo, hi, epsabs=2e-12)[0]


def phi(u):
    if abs(u) > 16:
        return 0.0
    return (4 * np.pi**2 * u**4 - 6 * np.pi * u**2) * np.exp(-np.pi * u*u)


def kernel(x):
    u = math.exp(x)
    return math.sqrt(u) * sum(phi(n*u) for n in range(1, max(2, int(10/u)+2)))


def zeta_em(s, n=40):
    # Euler--Maclaurin with eight Bernoulli coefficients.
    coeff = [1/12, -1/720, 1/30240, -1/1209600, 1/47900160,
             -691/1307674368000, 1/74724249600, -3617/10670622842880000]
    val = sum(k**(-s) for k in range(1, n)) + n**(1-s)/(s-1) + .5*n**(-s)
    for j, b in enumerate(coeff, 1):
        rising = np.prod([s+k for k in range(2*j-1)])
        val += b * rising * n**(-s-2*j+1)
    return val


def poly_norm(degree, t):
    # Gram of factorial-normalized monomials in exp(-|x|) dx.
    scales = np.array([math.sqrt(math.factorial(2*j)) for j in range(degree+1)])
    gram = np.array([[2*math.factorial(i+j)/(scales[i]*scales[j]) if (i+j)%2 == 0 else 0
                      for j in range(degree+1)] for i in range(degree+1)])
    shift = np.array([[math.comb(j,i)*(-t)**(j-i)*scales[i]/scales[j] if i<=j else 0
                       for j in range(degree+1)] for i in range(degree+1)])
    lam = eigh(shift.T @ gram @ shift, gram, eigvals_only=True)[-1]
    return float(math.sqrt(lam))


def main():
    errors = {}
    errors['poisson_reflection'] = max(abs(kernel(x)-kernel(-x)) for x in [.1,.4,1,1.8])
    errors['zeta_2'] = abs(zeta_em(2)-math.pi**2/6)
    errors['zeta_4'] = abs(zeta_em(4)-math.pi**4/90)
    for s in [.7+1.2j, 1.3+.8j, 2+.3j]:
        integral = cq(lambda x: kernel(x)*(np.exp((s-.5)*x)+np.exp(-(s-.5)*x)),0,3)
        xi = .5*s*(s-1)*np.pi**(-s/2)*gamma(s/2)*zeta_em(s)
        errors['theta_mellin_'+str(s)] = abs(integral-xi)
    a=.5; z=.12+.9j; w=-.2+.3j
    gram = 4*a/(4*a*a-(z+w.conjugate())**2)
    integ = cq(lambda x: np.exp((z+w.conjugate())*x-2*a*abs(x)), -np.inf, np.inf)
    errors['gram_integral'] = abs(gram-integ)
    exact = a/(a*a-z.real**2)
    norm = quad(lambda x: math.exp(2*z.real*x-2*a*abs(x)), -np.inf,np.inf)[0]
    errors['evaluation_norm'] = abs(exact-norm)
    gammas=np.array([14.134725141734694,21.022039638771555]); t=math.log(2)
    d=gammas[:,None]-gammas[None,:]; g=1/(1+d*d)
    phase=np.diag(np.exp(1j*(gammas-gammas[0])*t))
    numerical=math.sqrt(eigh(phase.conj().T@g@phase,g,eigvals_only=True)[-1])
    r=g[0,1]; q=r*abs(math.sin((gammas[0]-gammas[1])*t/2))/math.sqrt(1-r*r)
    explicit=math.hypot(1,q)+q
    errors['two_mode_norm'] = abs(numerical-explicit)
    assert max(errors.values()) < 2e-10, errors
    out={'status':'finite float64 controls; not infinite-dimensional proof checks',
         'reconstructed_after_workspace_replacement':True, 'errors':errors,
         'max_control_error':max(errors.values()), 'two_mode_norm':numerical,
         'polynomial_norms':{str(n):poly_norm(n,t) for n in [1,2,4,8,12]},
         'ambient_norm':math.sqrt(2)}
    path=Path(__file__).resolve().parents[1]/'research/2026-09-30_weighted_poisson_controls.json'
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
