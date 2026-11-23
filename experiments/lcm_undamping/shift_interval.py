"""Certify both normalized parity energies on the entire quarter-shift interval."""
from flint import arb, acb, ctx
from null_interference import values

ctx.prec = 128
N = 44
T = 128
mesh = 16
pi = arb.pi()
angles = [pi*(2*j+1)/(2*N) for j in range(N)]
nodes = [(1+a.cos())/8 for a in angles]


def samples():
    totals = [[arb(0), arb(0), arb(0)] for _ in nodes]
    for i in range(T*mesh+1):
        s = acb(arb(5)/2, arb(i)/mesh)
        base, m = values(s)
        weight = 1 if i else arb(1)/2
        for theta, accum in zip(nodes, totals):
            a, ma = values(s+theta)
            d, md = values(s-theta)
            v = (a-d)/(2*theta)
            w = ((a+d)/2-base)/theta**2
            accum[0] += weight*(-2*(ma+md)*v**2).real
            accum[1] += weight*(2*m*w**2).real
            accum[2] += weight*(-2*m*v**2).real
    strip_error = 2*arb(10)**16/((2*pi*mesh*arb(3)/4).exp()-1)
    tail = arb(10)**12*(1+T)**5*(-pi*T/4).exp()/(pi/4-arb(5)/(1+T))
    error = arb(0, (strip_error+tail).upper())
    return [[v/(mesh*pi)+error for v in row] for row in totals]


def enclose(data):
    # Absolute sum bounds the variation of the interpolant on [-1,1].
    mean = sum(data)/N
    variation = arb(0)
    for k in range(1,N):
        coefficient = 2*sum(v*(k*a).cos() for v,a in zip(data,angles))/N
        variation += abs(coefficient)
    remainder = arb(8)/3 * arb(10)**20 / arb(6)**N
    return mean + arb(0, (variation+remainder).upper())


if __name__ == '__main__':
    odd, even, zeta_odd = map(enclose, zip(*samples()))
    print('bounds for -Q_F(S)/theta^2', odd.lower(), odd.upper())
    print('bounds for Q_H(S)/theta^4', even.lower(), even.upper())
    print('bounds for Q_H(V)', zeta_odd.lower(), zeta_odd.upper())
    assert odd > arb(65)/10**7 and odd < arb(80)/10**7
    assert zeta_odd > arb(375)/10**8 and zeta_odd < arb(385)/10**8
    assert even > arb(128)/10**8 and even < arb(129)/10**8
