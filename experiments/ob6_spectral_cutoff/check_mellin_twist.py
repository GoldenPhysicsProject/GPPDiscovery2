"""Direct zero-independent source verification of balanced Mellin tilt and box threshold.
Numerics only (for research), no RH assumption and no zeros as input.
"""
import mpmath as mp
mp.mp.dps=50
q=3100; L=mp.log(q)
ps=[]
for p in range(2,q):
    if all(p%d for d in range(2,int(p**.5)+1)):
        n=p
        while n<q:
            ps.append((mp.log(n),mp.log(p)/mp.sqrt(n)))
            n*=p

def phi(th):
    th=mp.mpf(th)
    J=lambda b: (mp.expm1(-b*L)+b*L)/(b*b)
    pole=mp.fsum(J(b) for b in [mp.mpf('.5')+th,mp.mpf('.5')-th,-mp.mpf('.5')+th,-mp.mpf('.5')-th])/2
    const=(mp.digamma(mp.mpf('.25')+th/2)+mp.digamma(mp.mpf('.25')-th/2)-2*mp.log(mp.pi))/4
    zz=mp.exp(-2*L)
    gamma=mp.fsum((mp.zeta(2,a/2)-mp.exp(-a*L)*mp.lerchphi(zz,2,a/2))/8 for a in [mp.mpf('.5')+th,mp.mpf('.5')-th])
    prime=mp.fsum(v*mp.cosh(th*l)*(L-l) for l,v in ps)
    return pole+const*L+gamma-prime

for t in ['0','.05','.10','.15','.20','.22','.24','.25']:
    print('theta',t,'Phi',mp.nstr(phi(t),26))
r=mp.findroot(phi,(mp.mpf('.20'),mp.mpf('.25')),solver='anderson')
print('BOX observed root theta~',mp.nstr(r,45),'Phi(root)',mp.nstr(phi(r),8),'events',len(ps))
theta=mp.mpf('0.25')
w=lambda t: mp.exp(-t/2)/(1-mp.exp(-2*t))
K=mp.quad(lambda t: 2*w(t)*(mp.cosh(theta*t)-1), [0,mp.mpf('.01'),1,10,50,mp.inf])
C0=mp.digamma(mp.mpf('.25'))-mp.log(mp.pi)
Ct=(mp.digamma(mp.mpf('.25')+theta/2)+mp.digamma(mp.mpf('.25')-theta/2)-2*mp.log(mp.pi))/2
print('contact K',mp.nstr(K,32),'C0-Ctheta',mp.nstr(C0-Ct,32),'error',mp.nstr(K-(C0-Ct),6))
assert abs(K-(C0-Ct))<mp.mpf('1e-35')
assert phi(0)>0 and phi(mp.mpf('.25'))<0
print('PASS: exact scalar source identity numerical validation')
