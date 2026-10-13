"""Exact rational polynomial single-carrier DH witness + high precision NOT Arb.
Daniel Toupin RHpositive & Unification. One carrier: h=3, k=3, omega=857/10.
Q_DH/||g||² ~ -0.641365178743...; not a certified interval.
"""
import sympy as sp
import mpmath as mp
h=sp.Rational(3); w=sp.Rational(857,10); k=3
x,t,u=sp.symbols('x t u')
b=sp.expand((x/h)*(1-(x/h)**2)**k)
B=sp.factor(sp.integrate(sp.expand(b.subs(x,u+t)*b.subs(x,u)),(u,-h,h-t)))
expected=(t-6)**7*(7*t**8+294*t**7+5166*t**6+47628*t**5+227448*t**4+408240*t**3-23328*t**2-979776*t-839808)/sp.Integer(1723590708840)
assert sp.simplify(B-expected)==0
norm=sp.integrate(b*b,(x,-h,h))
assert norm==sp.Rational(2048,15015) and B.subs(t,0)==norm
mp.mp.dps=45
alpha=(mp.sqrt(10-2*mp.sqrt(5))-2)/(mp.sqrt(5)-1)
def a(n):return (mp.mpf(0),mp.mpf(1),alpha,-alpha,mp.mpf(-1))[n%5]
R=mp.mpf(6); W=mp.mpf(857)/10
c=[mp.mpf(0)]*(int(mp.floor(mp.exp(R)))+1)
for n in range(2,len(c)):
    c[n]=a(n)*mp.log(n)-sum(a(d)*c[n//d] for d in range(2,n+1) if n%d==0)
BB=sp.lambdify(t,B,'mpmath')
N0=mp.mpf(norm.p)/norm.q
def U(y):return BB(y)*mp.cos(W*y)
def integrand(y):
    if y==0:return N0/2
    return 2*(mp.exp(-mp.mpf('1.5')*y)*U(y)-mp.exp(-2*y)*N0)/(-mp.expm1(-2*y))
knots=[mp.mpf(0)]+[mp.pi*j/W for j in range(1,int(R*W/mp.pi))]+[R]
integral=sum(mp.quad(integrand,[a,b]) for a,b in zip(knots,knots[1:]))
arch=(mp.euler+mp.log(mp.pi/5)+mp.log1p(-mp.exp(-2*R)))*N0+integral
arith=sum(2*c[n]*U(mp.log(n))/mp.sqrt(n) for n in range(2,len(c)) if mp.log(n)<R)
value=-(arch+arith)/N0
assert -mp.mpf('.642')<value<-mp.mpf('.640')
print('EXACT B(t)=',B)
print('EXACT ||g||²=',norm)
print('NUMERICAL arch/norm=',mp.nstr(arch/N0,35))
print('NUMERICAL arithmetic/norm=',mp.nstr(arith/N0,35))
print('NUMERICAL DH Q/norm=',mp.nstr(value,35))
print('NOT AN INTERVAL CERTIFICATE')
