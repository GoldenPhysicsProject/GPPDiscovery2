"""Rigorous 256-bit Arb scalar check for completed Weil all-tests to L=209/500.

ANALYTIC proof (adjacent .md):
1. Exact full completed gamma/contact/pole decomposition, prime-free.
2. H(t)=log coth(t/2) has H''''(t)>0, hence V_L''(x)>=H''(L/2),
   so V_L(x)>=H(L/2)+H''(L/2)*(x-L/2)^2/2.
3. Gamma potential <=exp(L/4)-1, giving local beta+K*t²,
   t=(x-L/2)/L and K=(L²/2)*H''(L/2).
4. Positive interior jump J_gamma >= logarithmic Legendre form;
   reflection-odd J>=||f||²; reflection-even mean-zero J>=3/2||g||².
5. Reflection-even f=a*e0+g. The only constant/fluctuation cross
   coupling in the curvature square is e2:
   <e0,t² e0>=1/12, <e0,t² e2>=1/(6sqrt5).
   Drop the positive term K||t*g||².
6. Pole even cosh moment: Young with eta=1/100.
   Odd pole sinh moment: Cauchy upper, cosh=0.
   Then even form >= A|a|²+B||g||²-2 b|a|||g||,
   odd form >= O||f_odd||².
7. Assert A-d>0, B-d>0, (A-d)(B-d)>b² and O>d
   with outward Arb. This proves Q>=d||f||² for ALL complex f.

This only proves prime-free short-support positivity, not RH.
"""
from flint import arb,ctx,fmpq
ctx.prec=256
q=lambda n,d=1:arb(fmpq(n,d))
L=q(209,500)
eta=q(1,100)
delta=q(1,2000)
c=(4*arb.pi()).log()+arb.const_euler()
beta=-(L/4).tanh().log()-((L/4).exp()-1)-c
Hpp=(L/2).cosh()/((L/2).sinh()**2)
K=(L**2/2)*Hpp
C0=4*(L/4).sinh()
dcosh=L/2+(L/2).sinh()-C0*C0/L
dsinh=(L/2).sinh()-L/2
A=beta+K/12+2*(1-eta)*C0*C0/L
B=beta+q(3,2)-2*(1/eta-1)*dcosh
cross=K/(6*arb(5).sqrt())
O=beta+1-2*dsinh
det=(A-delta)*(B-delta)-cross**2
assert 0<L<arb(2).log()
assert dcosh>0 and dsinh>0
assert A>delta and B>delta
assert O>delta
assert det>0
print('Full Q all-complex-f, support L <= 209/500 prime-free')
print('beta =', beta)
print('Hpp =', Hpp)
print('K =', K)
print('even A =', A, '; even B =', B, '; cross =', cross)
print('even determinant after -delta identity =', det)
print('odd lower =', O)
print('CERTIFIED Q[f] >= 1/2000 ||f||² for every admissible f '
      'supported inside the interval, via positive curvature + '
      'logarithmic Legendre jump + two-channel pole inequality.')
print('Not a global Weil positivity or RH proof; formalization in Lean open.')
