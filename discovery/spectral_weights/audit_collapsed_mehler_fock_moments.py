import mpmath as mp

mp.mp.dps = 60


def q(x):
    return mp.pi*x*x/mp.cosh(mp.pi*x)


def beta_dirichlet(s):
    return mp.nsum(lambda n: (-1)**n/(2*n+1)**s, [0, mp.inf])


def exact_even_moment(m):
    return 4*mp.factorial(2*m+2)*beta_dirichlet(2*m+3)/mp.pi**(2*m+2)

mass = mp.quad(lambda x: q(x), [-mp.inf, 0, mp.inf])
print('mass numeric =', mp.nstr(mass, 50))
print('mass exact   =', mp.nstr(mp.pi/4, 50))
print('mass error   =', mp.nstr(abs(mass-mp.pi/4), 8))

for m in range(5):
    num = mp.quad(lambda x: x**(2*m)*q(x), [-mp.inf, 0, mp.inf])
    ex = exact_even_moment(m)
    normalized = num/(mp.pi/4)
    print('m=', m)
    print('  moment numeric =', mp.nstr(num, 50))
    print('  moment exact   =', mp.nstr(ex, 50))
    print('  abs error      =', mp.nstr(abs(num-ex), 8))
    print('  normalized     =', mp.nstr(normalized, 50))
