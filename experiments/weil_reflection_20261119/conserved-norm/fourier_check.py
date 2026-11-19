"""Independent frequency-side computation in the absolutely convergent half-plane."""
import numpy as np
from scipy.integrate import simpson
from scipy.special import digamma
from check import energy, models, L, mode, shift

def density(sigma,t):
    s=sigma+1j*t
    # All prime powers through 37. At sigma>=10.25 the tail after this
    # cutoff is bounded by 2*sum_{n>37} log(n)/n**sigma for the density.
    primes=[2,3,5,7,11,13,17,19,23,29,31,37]
    d=2*(1/s+1/(s-1)).real + digamma(s/2).real-np.log(np.pi)
    for p in primes:
        n=p
        while n<=37:
            d-=2*np.log(p)*n**(-sigma)*np.cos(t*np.log(n))
            n*=p
    return d

def fourier_power(t):
    k=mode*np.pi/L
    # Stable evaluation of the integrals of the two plane waves in sin(ku).
    def plane(v):
        return L*np.exp(-1j*v*L/2)*np.sinc(v*L/(2*np.pi))
    base=(plane(t-k)-plane(t+k))/(2j)
    return (2/L)*np.abs(base)**2*(1+np.cos(t*shift))

for model,delta in [(models.zeta(),0),(models.fth(.25),.25)]:
    target=energy(model,10)
    for tmax in (600,1200,2400):
        t=np.linspace(0,tmax,int(tmax*20)+1)
        d=density(10.5,t) if delta==0 else density(10.5+delta,t)+density(10.5-delta,t)
        approx=simpson(fourier_power(t)*d,x=t)/np.pi
        print(model['name'],tmax,'spectral',approx,'arithmetic',target,'difference',approx-target)
    assert abs(approx-target)<1e-6
