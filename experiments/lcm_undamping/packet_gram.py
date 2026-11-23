"""Certified real exponential packet test. Requires python-flint 0.9.0."""
from flint import arb, arb_series, ctx

ctx.prec = 384
rates = [arb(14) + arb(k)/8 for k in range(10)]
coefficients = [
    -866125540820550560, 7919388442715279585, -32183844607633877015,
    76298932223867782841, -116286799540165664627, 118159202864763944483,
    -80044106631510924792, 34859494583414463665, -8856141794630453582,
    1000000000000000000,
]


def response(b):
    s = b + arb(1)/2
    series = arb_series([s, 1], prec=2).zeta()
    return 1/s + 1/(s-1) + ((s/2).digamma()-arb.pi().log())/2 + series[1]/series[0]


def certify(shifted):
    theta = arb(1)/4
    values = [response(b+theta)+response(b-theta) if shifted else response(b)
              for b in rates]
    # Multipoint Schur recursion for the right half-plane Pick kernel.
    w = [(v-1)/(v+1) for v in values]
    for i, b in enumerate(rates):
        pivot = w[i]
        if i == 9 and shifted:
            assert pivot > 1
        else:
            assert abs(pivot) < 1
        for j in range(i+1, len(rates)):
            w[j] = (w[j]-pivot)/(1-pivot*w[j])*(rates[j]+b)/(rates[j]-b)
    energy = sum(c*d*(x+y)/(a+b)
                 for c,x,a in zip(coefficients,values,rates)
                 for d,y,b in zip(coefficients,values,rates))
    assert (energy < 0) if shifted else (energy > 0)
    return pivot, energy


if __name__ == '__main__':
    for shifted in (False, True):
        pivot, energy = certify(shifted)
        print('shifted', shifted, 'last Schur parameter', pivot.str(20),
              'explicit packet energy', energy.str(20))
