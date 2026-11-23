"""Centered even/odd xi-filter test. Requires python-flint 0.9.0."""
from flint import arb, acb, acb_series, ctx
from null_interference import values

ctx.prec = 112
T = 110
order = 32


def terms(t):
    s = acb(arb(7)/4, t)
    x = acb_series([s, 1], prec=5)
    jet = x*(x-1)/2 * (-x*arb.pi().log()/2).exp() * (x/2).gamma() * x.zeta()
    m = jet[1]/jet[0]
    theta = arb(1)/4
    a, ma = values(s+theta)
    d, md = values(s-theta)
    v = (a-d)/(2*theta)
    w = ((a+d)/2-jet[0])/theta**2
    # Fold even products onto the right vertical contour.
    return (-4*m*jet[1]**2, 2*m*jet[2]**2, -2*(ma+md)*v**2, 2*m*w**2,
            -2*m*jet[1]*jet[3], -2*m*jet[3]**2,
            2*m*jet[2]*jet[4], 2*m*jet[4]**2)


def calculate():
    nodes = [arb.legendre_p_root(order,k,weight=True) for k in range(order)]
    sums = [arb(0) for _ in range(8)]
    for panel in range(8*T):
        for node, weight in nodes:
            for k, val in enumerate(terms((2*panel+1+node)/16)):
                sums[k] += weight*val.real
    quad = 2*T*arb(10)**21*(arb(1)/4)**(2*order)/(1-arb(1)/4)
    k = arb.pi()/4-arb(5)/(1+T)
    tail = arb(10)**12*(1+T)**5*(-arb.pi()*T/4).exp()/k
    error = arb(0,(quad+tail).upper())
    results = [(v/16+error)/arb.pi() for v in sums]
    print(*results, sep='\n')
    a2,b,v,w,c,d,e,f = results
    determinants = [a2*d/2-c**2, b*f-e**2]
    print('odd and even block determinants', *determinants)
    assert all(v > 0 for v in results[:4] + determinants)


if __name__ == '__main__':
    calculate()
