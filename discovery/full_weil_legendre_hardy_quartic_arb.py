"""Full completed (prime-free) Weil Arb certificate to L=43/100 via quartic Hardy curvature.

Exact analytic proof:
H(t)=log coth(t/2) = 2 sum_(j odd>=1) exp(-j t)/j for t>0.
Set a=L/2, u=x-a. Then V_L(a+u)=2 Σodd exp(-j a)*cosh(j u)/j.
cosh z>=1+z²/2+z⁴/24, hence
V>=H(a)+H''(a)u²/2+H''''(a)u⁴/24.

Gamma tilt potential Γ<=exp(L/4)-1.
Let t=(x-L/2)/L, k2=L²H''(L/2)/2,
k4=L⁴H''''(L/2)/24, W(t)=k2 t²+k4 t⁴.
For uniformly distributed t∈[-1/2,1/2]:
E(t²)=1/12, E(t⁴)=1/80, Var(t²)=1/180,
Cov(t²,t⁴)=1/840, Var(t⁴)=1/3600.

On reflection-even f=alpha e0+g, mean(g)=0:
∫W|f|²>=E(W)|alpha|²-2 sqrt(Var(W)) |alpha| ||g||.
Legendre log jump J>=3/2||g||².
Cosh pole Young gives positive mean and small negative fluct bound.
Thus Q_even>= A |alpha|² + B ||g||² -2 b |alpha| ||g||,
where A=beta+EW+2(1-eta)C0²/L,
B=beta+3/2-2(eta^-1-1)dc²,
b²=k2²/180+k2*k4/420+k4²/3600.
Odd sector lower O=beta+1-2(sinh(L/2)-L/2).
If A-d>0,B-d>0,(A-d)(B-d)>b²,O>d, full Q>=d||f||².

Arb verifies ONLY these scalar inequalities; exact analytic proof in
discovery/full_weil_legendre_hardy_quartic.md. RH OPEN.
"""
from flint import arb,ctx,fmpq
ctx.prec=256
q=lambda n,d=1:arb(fmpq(n,d))
L=q(43,100)
eta=q(1,1000)
delta=q(1,1000)
a=L/2
c=(4*arb.pi()).log()+arb.const_euler()
beta=-(L/4).tanh().log()-((L/4).exp()-1)-c
h2=a.cosh()/(a.sinh()**2)
h4=(a.cosh()**2+5)*a.cosh()/(a.sinh()**4)
k2=(L**2/2)*h2
k4=(L**4/24)*h4
Wmean=k2/12+k4/80
Wvar=k2*k2/180+k2*k4/420+k4*k4/3600
C0=4*(L/4).sinh()
dc2=L/2+(L/2).sinh()-C0*C0/L
s2=(L/2).sinh()-L/2
A=beta+Wmean+2*(1-eta)*C0*C0/L
B=beta+q(3,2)-2*(1/eta-1)*dc2
Odd=beta+1-2*s2
det=(A-delta)*(B-delta)-Wvar
assert L<arb(2).log() and L<1
assert dc2>0 and s2>0
assert A>delta and B>delta
assert Odd>delta
assert det>0
print('FULL completed Weil all functions with support <= L=43/100 (prime-free)')
print('beta=',beta)
print('k2=',k2,' k4=',k4)
print('mean W=',Wmean,' Var(W)=b²=',Wvar)
print('even A=',A,' B=',B)
print('even determinant after delta I=',det)
print('odd lower=',Odd)
print('CERTIFIED: Q_L[f] >= (1/1000)||f||² for ALL complex admitted f; '
      'shorter supports by centered zero extension. This is not RH.')
