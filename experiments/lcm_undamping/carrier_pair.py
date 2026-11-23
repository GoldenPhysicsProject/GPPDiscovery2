"""Certified two-envelope sine witness. Run with python-flint 0.9.0."""
from flint import acb, acb_series, arb, ctx

ctx.prec = 256


def response(z):
    s = z + arb(1)/2
    jet = acb_series([s, 1], prec=2).zeta()
    return 1/s + 1/(s-1) + ((s/2).digamma()-arb.pi().log())/2 + jet[1]/jet[0]


def sine_gram(t, shifted):
    rates = [acb(arb(n)/16, t) for n in (13, 14)]
    theta = arb(1)/4
    h = [response(z+theta)+response(z-theta) if shifted else response(z) for z in rates]
    def entry(i, j):
        usual = (h[i]+h[j].conjugate())/(rates[i]+rates[j].conjugate())
        reflected = (h[i]+h[j])/(rates[i]+rates[j])
        return (usual-reflected).real/2
    return entry(0,0), entry(0,1), entry(1,1)


if __name__ == '__main__':
    for t in (13, 14, 15):
        for shifted in (False, True):
            a,b,c = sine_gram(t, shifted)
            energy = 169*a - 364*b + 196*c
            assert a > 0 and c > 0
            if t == 14 and shifted:
                assert energy < 0 and a*c-b*b < 0
            else:
                assert energy > 0
            print(t, shifted, energy.str(16))
