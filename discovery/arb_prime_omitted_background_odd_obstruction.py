"""Outward Arb witness: prime-OMITTED completed real-place/pole Q0 is
NOT positive on L=3/4. The true Weil Q includes the n=2 prime term;
this test deliberately omits it to falsify a proposed background-only
support-uniform positive gap. The witness f=e1-(2/5)e3 is a real odd
shifted Legendre polynomial (norm²=29/25).

Direct definition, including entire gamma tail; no spectral eigensolver.
"""
from flint import arb, acb, ctx, fmpq
ctx.prec=192
I=acb(0,1)
q=lambda n,d=1:arb(fmpq(n,d))
L=q(3,4)
LC=acb(L)
root21=q(21).sqrt()
norm=q(29,25)
q0=2*norm
c=(4*arb.pi()).log()+arb.const_euler()

def autocorr(z):
    t=z/LC
    q11=2-6*t+4*t**3
    q13=root21*(-2*t+10*t**2-12*t**3+4*t**5)
    q33=2-14*t+56*t**3-84*t**5+40*t**7
    return q11-q(4,5)*q13+q(4,25)*q33

def missing_over_z(z):
    t=z/LC
    p11=6-4*t*t
    p13=root21*(2-10*t+12*t*t-4*t**4)
    p33=14-56*t*t+84*t**4-40*t**6
    return (p11-q(4,5)*p13+q(4,25)*p33)/LC

def real_integral(f):
    return acb.integral(lambda z, analytical:f(z),acb(0),LC,
        rel_tol=1e-55,abs_tol=1e-55,eval_limit=100000).real

def sinhc(z):
    return (I*z).sinc()

Einner=real_integral(lambda z:missing_over_z(z)/(2*sinhc(z)))
Etail=q0/2*((L/2).tanh().log()*(-1))
P=real_integral(lambda z:autocorr(z)*((z/2).exp()+(-z/2).exp()))
Tilt=real_integral(lambda z:autocorr(z)*(z/2).hypgeom_1f1(1,2)/(4*sinhc(z)))
Q0=Einner+Etail+P-c*norm-Tilt
print('L=3/4, witness e1-(2/5)e3, norm²=29/25')
print('positive kinetic interior:',Einner)
print('positive kinetic exterior:',Etail)
print('indefinite pole:',P)
print('regular gamma tilt:',Tilt)
print('prime-omitted completed Q0:',Q0)
assert Q0 < -q(9,1000), 'Need strict negative interval enclosure'
print('CERTIFIED Q0[e1-(2/5)e3] < -9/1000 < 0')
print('This forbids a global Q0>=delta ||f||² for delta>0 at L=3/4.')
print('Does NOT claim the real prime-inclusive Weil form is negative or RH false.')


# Independently accounted p=2 prime-edge resource ledger, NOT a second
# expense against an already counted Archimedean supplier.
a=q(2).log()
eps=L-a
w=a/q(2).sqrt()
assert eps>0 and 2*eps<a
t=eps/L
r3=q(3).sqrt()
r7=q(7).sqrt()
# f(x)=[sqrt(3)P1(2x/L-1)-(2/5)sqrt(7)P3(2x/L-1)]/sqrt(L).
h=[-r3+q(2,5)*r7,2*r3-q(24,5)*r7,
   q(12)*r7,-q(8)*r7]  # coefficients of polynomial in x/L
M=2*sum((h[i]*h[j]*t**(i+j+1)/q(i+j+1)
       for i in range(len(h)) for j in range(len(h))),arb(0))
qa=autocorr(acb(a)).real
D=M-qa
S=w*qa
H=-(eps/2).tanh().log()
E=Einner+Etail
kinetic_unspent=E-H*M/2
edge_surplus=(H/2-w)*M
edge_laplacian=w*D
actualQ=Q0-S
assert qa<0 and D>0 and M>0
assert kinetic_unspent>=0 and edge_surplus>0 and edge_laplacian>0
assert S<-q(67,1000) and actualQ>q(57,1000)
assert abs((E-S)-(kinetic_unspent+edge_surplus+edge_laplacian))<q(1,10**40)
print('actual p2 prime source S2:',S)
print('actual completed Q=Q0-S2:',actualQ)
print('boundary strip mass M:',M)
print('edge squared difference D:',D)
print('unspent kinetic E-H(eps)*M/2:',kinetic_unspent)
print('positive boundary supplier (H(eps)/2-w)*M:',edge_surplus)
print('positive signed-graph edge supplier w*D:',edge_laplacian)
print('CERTIFIED positive prime-edge RESOURCE LEDGER, no E double spending.')
print('Scope: exact p2 source and one explicit test; not all-function Q positivity.')
