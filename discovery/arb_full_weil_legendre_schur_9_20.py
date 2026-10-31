"""Rigorous scalar Arb certification of an all-complex-function completed Weil
positivity theorem on any log support length L <= 9/20.

ANALYTIC proof: full_weil_legendre_low_tail_schur_9_20.md. This verifies
the explicit even two-mode/INFINITE tail and odd one-mode/INFINITE tail
Schur inequalities at the prime-free endpoint, not RH.
"""
from flint import arb,ctx,fmpq
ctx.prec=256
q=lambda p,d=1:arb(fmpq(p,d))
L=q(9,20);eta=q(1,100000);kap=q(1,2000)
assert L<arb(2).log() and L<1
e=(4*arb.pi()).log()+arb.const_euler()
beta=-(L/4).tanh().log()-((L/4).exp()-1)-e
K=L*L/2*(L/2).cosh()/((L/2).sinh()**2)
def a(n):
    return q(n)/((q(2*n-1)*q(2*n+1)).sqrt())
def T(n):
    if n==0:return q(1,12)
    return (a(n)**2+a(n+1)**2)/4
T02=a(1)*a(2)/4
T24=a(3)*a(4)/4
T13=a(2)*a(3)/4
c0=4*(L/4).sinh()/L.sqrt()
c2=(5*L).sqrt()*(4*(L/4).sinh()/L-48*(L/4).cosh()/L**2+192*(L/4).sinh()/L**3)
Uc=L*(((L/4)**4*(L/4).cosh())/24)**2
h_e=beta+q(25,12)-2*(1/eta-1)*Uc
A=beta+K*T(0)+2*(1-eta)*c0**2
B=beta+q(3,2)+K*T(2)+2*(1-eta)*c2**2
C=K*T02+2*(1-eta)*c0*c2
B_eff=B-kap-(K*T24)**2/(h_e-kap)
even_det=(A-kap)*B_eff-C**2
s2=(L/2).sinh()-L/2
h_o=beta+q(11,6)-2*s2
A_o=beta+1+K*T(1)-2*s2
odd_res=A_o-kap-(K*T13)**2/(h_o-kap)
print('Endpoint L=',L,'eta=',eta,'kappa=',kap)
print('Even h_e=',h_e)
print('Even A=',A,'B=',B,'C=',C)
print('Even effective B after high Schur=',B_eff)
print('Even strict determinant=',even_det)
print('Odd h_o=',h_o)
print('Odd strict Schur residual=',odd_res)
assert h_e>kap and A>kap and B_eff>kap/4
assert even_det>q(3,10000)
assert h_o>kap and odd_res>q(1,5)
print('CERTIFIED: for every admissible f supported on ANY log window <=9/20,')
print('full completed Weil Q[f] >= 1/2000 * ||f||², no prime atoms.')
print('This does not establish completed arithmetic positivity past log2 or RH.')
