"""Damped interval check adapted from the preceding translated-bump certificate."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'positivity'))
from certify import iv, I, psi


L=3
def enclose(name,j,p,n,damping,unit_shift=False):
    damping=iv.mpf(damping)
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
    if name=='zeta':
        const=psi(half/2).real-logpi
        kernels=[(half,2)]
        poles=[half]
    else:
        theta=iv.mpf('.25')
        kernels=[(half-theta,2),(half+theta,2)]
        const=sum(psi(b/2).real-logpi for b,_ in kernels)
        poles=[half-theta,half+theta]
    value=const*c0
    cutoff=220
    for start,step in kernels:
        for i in range(cutoff):
            lam=start+i*step
            value+=2*(c0/lam-lap(-lam-damping))
        lam=start+cutoff*step
        # C(0)-C(t) = ||f-f(.+t)||^2/2 <= t^2 ||f'||^2/2.
        err=2*((1+abs(r))*k)**2*(1/lam**3+1/(2*step*lam**2))
        err+=2*c0*damping*(1/lam**2+1/(step*lam))
        value+=iv.mpf([0,1])*err
    for a in poles: value+=2*(lap(a-damping)+lap(-a-damping))
    maxn=int(float((p*iv.exp(L)).b))+1
    a=[1]*(maxn+1)
    coeff=[0]*(maxn+1)
    for d in range(2,maxn+1):
        coeff[d]=a[d]*iv.log(d)-sum(coeff[e]*a[d//e] for e in range(2,d) if d%e==0)
        if name=='FTH': c=(d**theta+d**(-theta))*coeff[d]
        else: c=coeff[d]
        value-=2*c*C(iv.log(d))*iv.exp(-damping*iv.log(d))/iv.sqrt(d)
    return value

if __name__=='__main__':
    for model in ('zeta','FTH'):
        for damping in ('0','.05','.10'):
            bound=enclose(model,20,7,1,damping,unit_shift=True)/2
            print(model,damping,bound)
            if model=='FTH' and damping!='.10': assert bound.b<0
            else: assert bound.a>0
