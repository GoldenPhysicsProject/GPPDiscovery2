"""Certified arithmetic-contour test for a shifted xi filter; python-flint 0.9.0."""
from flint import arb, acb, acb_series, ctx

ctx.prec = 112
theta = arb(1)/4
b = acb(2, 14)
eps = arb(1)/10000
T = 180
order = 30


def values(s):
    jet = acb_series([s, 1], prec=2).zeta()
    xi = s*(s-1)/2 * (-s*arb.pi().log()/2).exp() * (s/2).gamma() * jet[0]
    logder = 1/s + 1/(s-1) + ((s/2).digamma()-arb.pi().log())/2 + jet[1]/jet[0]
    return xi, logder


def cosine(z):
    return (1/(b+z) + 1/(b.conjugate()+z))/2


def cosine_energy(shifted):
    z = b+arb(1)/2
    m = values(z+theta)[1]+values(z-theta)[1] if shifted else values(z)[1]
    return (m.real/b.real + (m/b).real)/2


def calculate():
    nodes = [arb.legendre_p_root(order,k,weight=True) for k in range(order)]
    sums = [arb(0) for _ in range(3)]
    for panel in range(8*T):
        for node, weight in nodes:
            t = (2*panel+1+node)/16
            z = acb(arb(5)/4,t)
            a, ma = values(z+arb(1)/2+theta)
            d, md = values(z+arb(1)/2-theta)
            _, m = values(z+arb(1)/2)
            cross = a*cosine(-z)+d*cosine(z)
            terms = ((ma+md)*cross, m*cross, 2*m*a*d)
            for k, term in enumerate(terms):
                sums[k] += weight*term.real
    # Common conservative bounds from null_interference.md.
    quadrature = 2*T*arb(10)**18*(arb(1)/4)**(2*order)/(1-arb(1)/4)
    k = arb.pi()/8-arb(5)/(1+T)
    tail = arb(10)**5*(1+T)**5*(-arb.pi()*T/8).exp()/k
    error = arb(0,(quadrature+tail).upper())
    js,jz,zz = [(v/16 + error)/arb.pi() for v in sums]
    shifted = 2*eps*js + eps**2*cosine_energy(True)
    zeta = zz + 2*eps*jz + eps**2*cosine_energy(False)
    print('mixed shifted pairing',js)
    print('shifted energy',shifted)
    print('zeta energy',zeta)
    assert js < 0 and shifted < 0 and zeta > 0


if __name__ == '__main__':
    calculate()
