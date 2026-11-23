"""Independent check of the a=2 undamping identity, using exact integer LCMs."""
from math import cos, exp, lcm, log, pi, sin
from scipy.integrate import quad


def check(L, mode, shift):
    width = L + shift
    endpoint = exp(width)
    frequency = mode * pi / L

    def overlap(x):
        x = abs(x)
        if x >= L:
            return 0.
        return (1-x/L)*cos(frequency*x) + sin(frequency*x)/(frequency*L)

    def derivative(x):
        if abs(x) >= L:
            return 0.
        return -(1-abs(x)/L)*frequency*sin(frequency*x)

    def pair(fn, t):
        return fn(t) + (fn(t-shift) + fn(t+shift))/2

    def C(t):
        return pair(overlap, t)

    def wprime(x):
        t = log(x)
        return x**-1.5*((2.5*x**-2-.5)*C(t)
                        + (1-x**-2)*pair(derivative, t))

    def integral(fn, a, b, knots):
        return quad(fn, a, b, points=sorted({u for u in knots if a<u<b}),
                    epsabs=1e-12, epsrel=1e-12, limit=200)[0]

    breaks = [shift, L, abs(shift-L)]
    continuous = 2*integral(lambda t: (exp(t/2)-exp(-1.5*t)-exp(-2.5*t))*C(t),
                            0, width, breaks)
    residual = -2*integral(lambda t: exp(-2.5*t)*C(t), 0, width, breaks)
    integer = 1
    jumps = work = 0.
    for n in range(1, int(endpoint)+1):
        updated = lcm(integer, n)
        jumps += 2*log(updated//integer)*(1-n**-2)*C(log(n))/n**.5
        integer = updated
        work += 2*integral(lambda x: (log(integer)-x+1)*wprime(x),
                           n, min(n+1, endpoint), [exp(t) for t in breaks])
    assert abs(continuous-jumps-residual-work) < 1e-10
    return continuous-jumps, residual, work


if __name__ == '__main__':
    for case in [(.72, 1, 0.), (3., 20, log(7)), (3., 1, 0.), (2., 3, log(3))]:
        print(case, check(*case))
