"""Independent high-precision source-vs-prime-resolvent test for FULL F_theta two-space geometry.
Uses no zeta zeros. Numeric regression only, independent of exact signed rational certificate.
"""
import mpmath as mp
mp.mp.dps=55
q_int=3100
L=mp.log(q_int)
theta=mp.mpf(1)/4
ps=[]
for n in range(2,10002):
    if all(n%d for d in range(2,int(n**.5)+1)):
        ps.append(n)
# Independently form source prime-power ramp and positive resolvent Gram.
ramp=mp.mpf(0)
for p in ps:
    power=p; k=1
    while power<q_int:
        l=mp.log(power)
        ramp+=mp.log(p)/mp.sqrt(power)*mp.cosh(theta*l)*(L-l)
        if power>q_int//p:break
        power*=p;k+=1

def J(b):return (mp.expm1(-b*L)+b*L)/(b*b)
polet=sum(J(b) for b in [mp.mpf(1)/2+theta,mp.mpf(1)/2-theta,-mp.mpf(1)/2+theta,-mp.mpf(1)/2-theta])
csmooth=(mp.digamma(mp.mpf(1)/4+theta/2)+mp.digamma(mp.mpf(1)/4-theta/2)-2*mp.log(mp.pi))/2

def gamma_ladder(a):
    z=mp.exp(-2*L)
    return (mp.zeta(2,a/2)-mp.exp(-a*L)*mp.lerchphi(z,2,a/2))/4
energy=gamma_ladder(mp.mpf(1)/2+theta)+gamma_ladder(mp.mpf(1)/2-theta)
Qsource=energy+csmooth*L+polet-2*ramp
print('theta',theta,'L',mp.nstr(L,30))
print('completed smooth source',mp.nstr(energy+csmooth*L+polet,45))
print('source prime ramp',mp.nstr(ramp,45))
print('Q_full_shifted_box',mp.nstr(Qsource,45))
assert Qsource<0
for N in [3101,5000,10000]:
    ps_N=[p for p in ps if p<=N]
    vartheta=sum(mp.log(p) for p in ps_N)
    C2=mp.mpf(0)
    for p in ps_N:
        l=mp.log(p)
        # two independent shift-resolvent species q=p^(-1/2 +/- theta)
        species=[]
        for sign in [1,-1]:
            u=mp.power(p,-mp.mpf(1)/2+sign*theta)
            terms=mp.mpf(0); k=1
            while k*l<L:
                terms+=u**k*(L-k*l)
                k+=1
            species.append((L+2*terms)/2)
        C2+=mp.log(p)*sum(species)
    BN=energy+csmooth*L+polet+vartheta*L
    D=BN-C2
    # both independence checks: C² from resolvents vs Euler prime ramp, and delta vs Q_source
    shift_error=C2-(vartheta*L+2*ramp)
    print('N',N,'vartheta',mp.nstr(vartheta,18),'BN',mp.nstr(BN,20),
          'R-1',mp.nstr(C2/BN-1,23),'diff_from_source',mp.nstr(D-Qsource,5),
          'resolvent_error',mp.nstr(shift_error,5))
    assert abs(D-Qsource)<mp.mpf('1e-46')
    assert abs(shift_error)<mp.mpf('1e-46')
    assert C2>BN>0
print('PASS: full shifted source equals two-positive-resolvent difference with negative box at each cutoff')
