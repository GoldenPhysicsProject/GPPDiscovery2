"""Interval bounds for the three canonical translated-bump witnesses."""
from certify import iv, I, psi
from math import isqrt

L=3
def enclose(name,j,p,n,unit_shift=False):
    k=j*iv.pi/L
    h=iv.log(p)
    r=n if unit_shift else n/iv.sqrt(p)
    def A(t):
        x=abs(t)
        if x.a>=L: return 0
        return (1-x/L)*iv.cos(k*x)+iv.sin(k*x)/(k*L)
    def C(t):
        return (1+r*r)*A(t)+r*(A(t+h)+A(t-h))
    c0=C(iv.mpf(0))
    # Each overlap on the positive half-line has |t-d| affine.
    segments=[]
    for d,weight in [(0,1+r*r),(h,r),(-h,r)]:
        for sign,left,right in [(-1,max(0,d-L),d),(1,max(0,d),d+L)]:
            if right<=left: continue
            x=sign*(left-d)
            phase=weight*iv.exp(I*k*x)
            segments.append((left,right-left,sign,phase,1-x/L-I/(k*L)))
    def lap(b):
        total=0
        for left,length,sign,phase,c in segments:
            v=b+I*k*sign
            e=iv.exp(v*length)
            J=(e-1)/v
            J1=(length*e-J)/v
            total+=(phase*iv.exp(b*left)*(c*J-sign*J1/L)).real
        return total
    half=iv.mpf('.5')
    logpi=iv.log(iv.pi)
    if name=='EPS':
        const=2*(iv.log(iv.sqrt(5)/iv.pi)+psi(half).real)
        kernels=[(half,1)]
        poles=[half]
    elif name=='DH':
        const=psi(iv.mpf('.75')).real+iv.log(5/iv.pi)
        kernels=[(iv.mpf('1.5'),2)]
        poles=[]
    elif name in ('zeta','beta','BEUR2'):
        odd=int(name=='beta')
        b=half+odd
        const=psi(b/2).real+iv.log((4 if odd else 1)/iv.pi)
        kernels=[(b,2)]
        poles=[] if odd else [half]
    else:
        theta=iv.mpf('.2')
        kernels=[(half-theta,2),(half+theta,2)]
        const=sum(psi(b/2).real-logpi for b,_ in kernels)
        poles=[half-theta,half+theta]
    value=const*c0
    cutoff=160
    for start,step in kernels:
        for i in range(cutoff):
            lam=start+i*step
            value+=2*(c0/lam-lap(-lam))
        lam=start+cutoff*step
        # C(0)-C(t) = ||f-f(.+t)||^2/2 <= t^2 ||f'||^2/2.
        err=2*((1+abs(r))*k)**2*(1/lam**3+1/(2*step*lam**2))
        value+=iv.mpf([0,1])*err
    for a in poles: value+=2*(lap(a)+lap(-a))
    maxn=int(float((p*iv.exp(L)).b))+1
    if name=='BEUR2':
        from translates import models
        model=models.beur2()
        for point,weight in zip(model['n'],model['c']):
            if point>maxn: break
            value-=2*iv.mpf(float(weight))*C(iv.log(iv.mpf(float(point))))/iv.sqrt(iv.mpf(float(point)))
        return value
    a=[0]*(maxn+1)
    if name=='EPS':
        for y in range(-isqrt(maxn//5),isqrt(maxn//5)+1):
            u=isqrt(maxn-5*y*y)
            for x in range(-u,u+1):
                a[x*x+5*y*y]+=1
        a=[v//2 for v in a]
    elif name=='DH':
        kap=(iv.sqrt(10-2*iv.sqrt(5))-2)/(iv.sqrt(5)-1)
        a=[[0,1,kap,-kap,-1][i%5] for i in range(maxn+1)]
    elif name=="beta": a=[[0,1,0,-1][i%4] for i in range(maxn+1)]
    else: a=[1]*(maxn+1)
    coeff=[0]*(maxn+1)
    for d in range(2,maxn+1):
        coeff[d]=a[d]*iv.log(d)-sum(coeff[e]*a[d//e] for e in range(2,d) if d%e==0)
        if name=='FTH': c=(d**theta+d**(-theta))*coeff[d]
        else: c=coeff[d]
        value-=2*c*C(iv.log(d))/iv.sqrt(d)
    return value
if __name__=='__main__':
    for row in [('EPS',15,5,-2),('DH',82,7,3),('FTH',20,7,3),('BEUR2',60,7,3)]:
        val=enclose(*row)
        print(row,val,flush=True)
        assert val.b<0

    for name in ('zeta','beta'):
        for j,p in [(15,5),(82,7),(60,7),(20,7)]:
            vals=[enclose(name,j,p,sign,unit_shift=True)/2 for sign in (-1,1)]
            print(name,j,p,[str(x) for x in vals],flush=True)
            assert all(x.a>0 for x in vals)
