#!/usr/bin/env python3
"""Outward Arb certificate: prime-omitted completed Weil background is
INDEFINITE at L=3/4, while actual p=2 term repairs this specific test.

The explicit smooth polynomial f = e1 - (2/5)e3 uses normalized shifted
Legendre e1, e3 on [0,L] (zero outside). The boundary zero extension is
in the finite logarithmic form domain; smooth compactly supported cores
approximate it in that domain. Not a global RH proof.
"""
from flint import arb, acb, ctx, fmpq
ctx.prec=256
qrat=lambda a,b=1:arb(fmpq(a,b))
I=acb(0,1)
L=qrat(3,4)
a=arb(2).log()
rt=arb(21).sqrt()
norm=qrat(29,25)
c=[
    qrat(58,25),
    -qrat(206,25)+8*rt/5,
    -8*rt,
    qrat(324,25)+48*rt/5,
    qrat(0),
    -qrat(336,25)-16*rt/5,
    qrat(0),
    qrat(32,5),
]
assert abs(c[0]-2*norm)<arb('1e-65')
TOL=1e-57
def qpoly(z):
    t=z/L
    s=acb(0)
    for v in c[::-1]:
        s=s*t+v
    return s

def kinetic_integrand(z):
    # q(0)-q(y) is divisible by y, so the singularity is REMOVED:
    # (q(0)-q(y))/(2 sinh y) =
    # -(sum_{k>=1} c_k (y/L)^(k-1))/(2 L sinh(y)/y)
    t=z/L
    s=acb(0)
    for v in c[:0:-1]:
        s=s*t+v
    return -s/(2*L*(I*z).sinc())

def tilt_integrand(z):
    # (e^(y/2)-1)/(2sinh(y)) = 1F1(1;2;y/2)/(4*sinh(y)/y)
    return qpoly(z)*(z/2).hypgeom_1f1(1,2)/(4*(I*z).sinc())

def integrate(f):
    val=acb.integral(lambda z,analytical:f(z),
                     acb(0),acb(L),rel_tol=TOL,abs_tol=TOL,
                     eval_limit=100000)
    return val.real
E=integrate(kinetic_integrand)-norm*(L/2).tanh().log()
P=integrate(lambda z:qpoly(z)*((z/2).exp()+(-z/2).exp()))
A=integrate(tilt_integrand)
c_infty=(4*arb.pi()).log()+arb.const_euler()
Q0=E+P-c_infty*norm-A
q_at_a=qpoly(acb(a)).real
S2=a/arb(2).sqrt()*q_at_a
Q=Q0-S2
print('L=3/4, f=e1-(2/5)e3, ||f||^2=29/25')
print('E gamma kinetic=',E)
print('P exact rank-two pole=',P)
print('A gamma tilt=',A)
print('Q0 prime-omitted COMPLETE Weil background=',Q0)
print('q_f(log2)=',q_at_a)
print('S2 actual first prime source=',S2)
print('Q=Q0-S2, actual first-prime completed form=',Q)
assert a<L and L<arb(3).log()
assert Q0 < -qrat(9,1000)
assert S2 < -qrat(67,1000)
assert Q > qrat(57,1000)
print('CERTIFIED: Q0[f]<-0.009 but Q[f]>0.057 on the SAME test.')
print('Scope: one explicit form-domain test, not an all-f sign or RH proof.')

# Locate a rigorous sign change of Q0 along the SAME rescaled odd Legendre
# family f_L=e1,L-(2/5)e3,L. The shape q(L*t) is independent of L.
# Rational endpoints only; this certifies EXISTENCE of a zero by continuity,
# not its uniqueness or a universal spectral crossing.
def background_at(LL):
    def shape(z):
        t=z/LL
        result=acb(0)
        for v in c[::-1]:
            result=result*t+v
        return result
    def regular_kinetic(z):
        t=z/LL
        s=acb(0)
        for v in c[:0:-1]:
            s=s*t+v
        return -s/(2*LL*(I*z).sinc())
    def integr(f):
        return acb.integral(lambda z, analytical:f(z),
                           acb(0),acb(LL),rel_tol=TOL,abs_tol=TOL,
                           eval_limit=100000).real
    EE=integr(regular_kinetic)-norm*(LL/2).tanh().log()
    PP=integr(lambda z:shape(z)*((z/2).exp()+(-z/2).exp()))
    AA=integr(lambda z:shape(z)*(z/2).hypgeom_1f1(1,2)/
             (4*(I*z).sinc()))
    return EE+PP-c_infty*norm-AA
left=background_at(qrat(7439,10000))
right=background_at(qrat(93,125))  # 93/125=0.744
print('Q0 at L=0.7439:',left)
print('Q0 at L=0.744:',right)
assert left>0 and right<0
print('CERTIFIED: the rescaled mirror-odd Legendre test Q0 changes sign')
print('between rational log support lengths 0.7439 and 0.744.')

# EXACT secondary strip-reflection decomposition, not generic positivity.
# The global mirror-odd test has f_B(s)=-f_A(epsilon-s).
# Let local strip reflection Rg(s)=g(epsilon-s); then
# q(log2)=-2(<g+,g+>-<g-,g->), g+/-=(g+/-Rg)/2.
# Polynomial antiderivatives for M=||g||² and J=<g,Rg>.
h=(L-a)/L
def evaluate_coeffs(coeffs,h):
    v=arb(0)
    for ck in coeffs[::-1]:
        v=v*h+ck
    return v
m_strip=evaluate_coeffs([
    qrat(0),
    qrat(103,25)-4*rt/5,
    -qrat(486,25)+28*rt/5,
    qrat(2004,25)-72*rt/5,
    -qrat(1064,5)+16*rt,
    qrat(7728,25)-32*rt/5,
    -qrat(224),qrat(64)],h)
j_strip=evaluate_coeffs([
    qrat(0),
    qrat(103,25)-4*rt/5,
    -qrat(486,25)+28*rt/5,
    qrat(1282,25)-56*rt/5,
    -qrat(392,5)+8*rt,
    qrat(1512,25)-8*rt/5,
    -qrat(112,5),qrat(16,5)],h)
g_even=(m_strip+j_strip)/2
g_odd=(m_strip-j_strip)/2
print('LOCAL R-even strip norm²=',g_even)
print('LOCAL R-odd strip norm²=',g_odd)
assert g_even>qrat(70,1000)
assert qrat(0)<g_odd<qrat(2,1000)
assert abs(q_at_a+2*(g_even-g_odd))<arb('1e-60')
assert abs((-S2)-2*(a/arb(2).sqrt())*(g_even-g_odd))<arb('1e-60')
print('CERTIFIED p2 repair is dominated by the local-strip-even subchannel')
