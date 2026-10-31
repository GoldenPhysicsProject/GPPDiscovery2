"""Independent Gauss-Legendre smoke test of the exact completed Weil SOS.
Floating-point regression only; analytic proof is in the adjacent .md file.
The prime degree potential is integrated piecewise to respect step jumps.
"""
import math
import numpy as np
from scipy.special import roots_legendre


def prime_atoms(L):
    atoms = []
    for n in range(2, int(math.exp(L)) + 1):
        factors = []
        t = n
        for p in range(2, int(math.sqrt(t)) + 2):
            if t % p == 0:
                factors.append(p)
                while t % p == 0:
                    t //= p
        if t > 1:
            factors.append(t)
        if len(factors) == 1 and math.log(n) < L:
            atoms.append((math.log(n), math.log(factors[0]) / math.sqrt(n)))
    return atoms


def check(L, h_slope, N=180):
    xs, ws = roots_legendre(N)
    def integrate(a, b, fn):
        if b <= a:
            return 0.0
        x = (a+b)/2 + (b-a)*xs/2
        return (b-a)/2 * np.dot(ws, fn(x))
    def f(x):
        return np.sin(np.pi*x/L)**2 * (
            1 + 0.31j*np.cos(2*np.pi*x/L) + 0.47*np.sin(3*np.pi*x/L))
    def normsq(x):
        return np.abs(f(x))**2
    def H(x):
        return -np.log(np.tanh(x/2))
    def V(x):
        return (H(x) + H(L-x))/2
    def r(y):
        t = np.exp(y/2)
        return t*t/((t+1)*(t*t+1))
    def gamma_pot(x):
        return np.array([
            integrate(0, xi, r) + integrate(0, L-xi, r) for xi in x])
    def difference(y):
        return integrate(0, L-y, lambda x: np.abs(f(x+y)-f(x))**2)
    def corr(y):
        return 2*integrate(
            0, L-y, lambda x: np.real(np.conjugate(f(x))*f(x+y)))
    def h(x):
        return np.exp(h_slope*x)
    atoms = prime_atoms(L)
    def degree(x):
        ans = np.zeros_like(x)
        for a, weight in atoms:
            plus, minus = (x+a < L), (x-a > 0)
            ans[plus] += weight*h(x[plus]+a)/h(x[plus])
            ans[minus] += weight*h(x[minus]-a)/h(x[minus])
        return ans

    n2 = integrate(0, L, normsq)
    # The y>L tail is integrated exactly as H(L)*||f||².
    E = integrate(
        0, L,
        lambda ys: np.array([
            (2*n2-corr(y))/(2*np.sinh(y)) for y in ys])) + H(L)*n2
    A = integrate(0, L, lambda ys: r(ys)*np.array([corr(y) for y in ys]))
    S = sum(weight*corr(a) for a, weight in atoms)
    even = integrate(0, L, lambda x:f(x)*np.cosh((x-L/2)/2))
    odd = integrate(0, L, lambda x:f(x)*np.sinh((x-L/2)/2))
    P = 2*(abs(even)**2-abs(odd)**2)
    c = math.log(4*math.pi)+np.euler_gamma
    direct = E+P-c*n2-A-S

    jump = integrate(
        0, L,
        lambda ys: np.array([
            np.exp(y/2)/(2*np.sinh(y))*difference(y) for y in ys]))
    prime_squares = sum(
        weight*integrate(
            0,L-a,lambda x:
                h(x)*h(x+a)*np.abs(f(x)/h(x)-f(x+a)/h(x+a))**2)
        for a,weight in atoms)
    boundaries = sorted(set([0.,L]+[a for a,_ in atoms]+[L-a for a,_ in atoms]))
    local = sum(integrate(
        u,v,lambda x:(V(x)-gamma_pot(x)-degree(x)-c)*normsq(x))
        for u,v in zip(boundaries[:-1],boundaries[1:]))
    sos = local+jump+prime_squares+P
    err = abs(direct-sos)
    print(f'L={L}, h_slope={h_slope}, direct={direct:.14g}, '
          f'SOS={sos:.14g}, error={err:.3e}')
    assert err < 5e-10, (L, h_slope, err)


if __name__ == '__main__':
    for L in (0.4,1.1,1.56,1.7):
        for slope in (0,0.3):
            check(L,slope)
    print('All 8 independent SOS-vs-original form regressions pass. '
          'This is NOT Arb nor a completed Weil/RH certificate.')
