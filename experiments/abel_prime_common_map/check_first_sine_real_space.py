"""Independent x-space check of the first Dirichlet sine Weil diagonal.

Areal = C_inf ||f||² + positive translation energy, prime n=2 only,
pole = 2(C²-S²). This is a numerical normalization test, not a proof.
Requires mpmath. Cross-check against scan_first_prime_sine.py.
"""
import mpmath as mp
mp.mp.dps=50
L=mp.mpf("0.72")
a=mp.pi/L
ell=mp.log(2)
def autocorr(t):
    if t >= L:
        return mp.mpf(0)
    return (1-t/L)*mp.cos(a*t)+mp.sin(a*t)/(a*L)
def weight(t):
    return mp.exp(-t/2)/(-mp.expm1(-2*t))

E=2*mp.quad(lambda t:weight(t)*(1-autocorr(t)), [0,mp.mpf("0.01"),L])
E+=2*mp.quad(weight, [L,mp.inf])
C=mp.quad(lambda x:mp.sqrt(2/L)*mp.cos(a*x)*mp.cosh(x/2), [-L/2,L/2])
S=mp.mpf(0)
Cinf=-mp.euler-mp.log(mp.pi)-mp.pi/2-3*mp.log(2)
pole=2*(C*C-S*S)
prime=2*ell/mp.sqrt(2)*autocorr(ell)
W=E+Cinf+pole-prime
assert mp.mpf("0.003598")<W<mp.mpf("0.003601")
print("E=",mp.nstr(E,25))
print("archimedean scalar=",mp.nstr(Cinf,25))
print("pole=",mp.nstr(pole,25))
print("prime2=",mp.nstr(prime,25))
print("Weil first sine diagonal=",mp.nstr(W,25))
print("Numerical reproduction only, no interval certification.")
