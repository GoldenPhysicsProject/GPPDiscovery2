"""Finite Davenport–Heilbronn −D'/D current: exact divisor algebra, no Euler product.

For the symmetric real DH combination of primitive quartic mod-5 characters,
a(n) is 5-periodic: {0:0, 1:1, 2:alpha, 3:-alpha, 4:-1}.
-D'(s)/D(s) = sum_{n>=2} c(n)n^{-s} in Re s >= 2.
All integers n below exp(2h), not only prime powers, enter the Weil window.

The gamma/conductor kernel is recorded in the bridge note
work/codex/2026-10-13_dh_dirichlet_current_odd_gamma_explicit_formula.md.
"""
import mpmath as mp
mp.mp.dps = 80
alpha = (mp.sqrt(10-2*mp.sqrt(5))-2)/(mp.sqrt(5)-1)
def a(n):
    return (mp.mpf(0), mp.mpf(1), alpha, -alpha, mp.mpf(-1))[n % 5]
def divisors(n):
    return [d for d in range(1, n+1) if n%d==0]
def coefficients(N):
    c=[mp.mpf(0) for _ in range(N+1)]
    b=[mp.mpf(0) for _ in range(N+1)]; b[1]=1
    for n in range(2,N+1):
        c[n]=a(n)*mp.log(n)-sum(a(d)*c[n//d] for d in divisors(n) if d>1)
        b[n]=-sum(a(d)*b[n//d] for d in divisors(n) if d>1)
        # Independent Dirichlet-inverse check.
        assert mp.almosteq(c[n],sum(a(d)*mp.log(d)*b[n//d] for d in divisors(n)),abs_eps=mp.mpf('1e-70'))
    return c
def Weil_arch_DH_even(F,h):
    """Real even F supported on [-2h,2h]. High-precision value, NOT Arb certificate."""
    R=2*h; F0=F(mp.mpf(0))
    def integrand(t):
        if t==0: return F0/2
        return (2*mp.exp(-3*t/2)*F(t)-2*mp.exp(-2*t)*F0)/(-mp.expm1(-2*t))
    return (mp.euler+mp.log(mp.pi/5)+mp.log1p(-mp.exp(-2*R)))*F0 + mp.quad(integrand,[mp.mpf('1e-15'),R])
def Weil_zero_sum_DH_even(F,h):
    """Exact finite arithmetic sum plus numerical Arch integral, NO poles for DH."""
    R=2*h
    N=int(mp.floor(mp.exp(R)))
    c=coefficients(N)
    arithmetic=sum(2*c[n]*F(mp.log(n))/mp.sqrt(n) for n in range(2,N+1) if mp.log(n)<R)
    return -Weil_arch_DH_even(F,h)-arithmetic
if __name__ == '__main__':
    c=coefficients(24)
    assert mp.almosteq(c[2],alpha*mp.log(2))
    assert mp.almosteq(c[3],-alpha*mp.log(3))
    assert mp.almosteq(c[4],-(2+alpha**2)*mp.log(2))
    assert c[5]==0
    for n in range(2,21): print(n,mp.nstr(c[n],18))
    print('PASS: c2>0, c3<0; DH arithmetic record is NOT monotone')
