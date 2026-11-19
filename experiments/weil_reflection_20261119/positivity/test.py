"""Fixed-grid test of the two-point Pick form. Run with Python, NumPy and SciPy."""
import numpy as np
from scipy.special import digamma, bernoulli
from math import factorial

# Heights 0 through 100 by tenths, depths 0.05, 0.2, 0.5.
# Pair each point with its right neighbor. Test every primitive integer
# direction in [-4,4]^2 up to sign. The unit direction tests the diagonal.
heights = np.arange(1002)/10
depths = (.05,.2,.5)
directions = [(m,n) for m in range(5) for n in range(-4,5)
              if (m or n>0) and np.gcd(m,abs(n))==1]
characters = {
    'Z': [1], 'B':[0,1,0,-1], 'C':[0,1,1j,-1j,-1],
    'D':[0,1,-1j,1j,-1], 'R':[0,1,-1,-1,1],
    'T':[]}
characters['T']=[characters['B'][j%4]*characters['R'][j%5] for j in range(20)]
k=(np.sqrt(10-2*np.sqrt(5))-2)/(np.sqrt(5)-1)
def series(s,ch):
    # Sum each residue class using Euler-Maclaurin at a common cutoff.
    q=len(ch)
    N=40*q
    j=np.arange(1,N+1)
    v=np.exp(-s[:,None]*np.log(j)) @ np.array([ch[i%q] for i in j])
    for a in range(1,q+1):
        c=ch[a%q]
        if not c: continue
        x=N+a
        tail=x/q/(s-1)+.5
        rising=np.ones_like(s)
        for r,b in enumerate(BER,1):
            rising *= s if r==1 else (s+2*r-3)*(s+2*r-2)
            tail += b*rising*(q/x)**(2*r-1)
        v+=c*np.exp(-s*np.log(x))*tail
    return v
BER=[float(bernoulli(2*r)[-1])/factorial(2*r) for r in range(1,11)]
def values(s):
    v={key:series(s,ch) for key,ch in characters.items()}
    return dict(zeta=v['Z'],beta=v['B'],
                DH=((1-1j*k)*v['C']+(1+1j*k)*v['D'])/2,
                Epstein=v['Z']*v['T']+v['B']*v['R'])
def slopes(z):
    s=.5-1j*z
    step=1e-5
    v=values(s)
    vp=values(s+step)
    vm=values(s-step)
    out={}
    for name,q in [('zeta',1),('beta',4),('DH',5),('Epstein',20)]:
        a=int(name in ('beta','DH'))
        g=(np.log(q/np.pi)+digamma((s+a)/2))/2
        if name=='Epstein': g=np.log(np.sqrt(5)/np.pi)+digamma(s)
        if name in ('zeta','Epstein'): g+=1/s+1/(s-1)
        out[name]=1j*(g+(vp[name]-vm[name])/(2*step*v[name]))
    return out

def main():
    best={}
    for y in depths:
        # At height zero and depth .5 the pole-removal formula needs a limit.
        mask=(heights[:-1]>0) | (y!=.5)
        z=heights+1j*y
        if y==.5: z[0]=z[1]
        for name,h in slopes(z).items():
            A=h[:-1].imag/y
            B=h[1:].imag/y
            C=((h[:-1]-h[1:].conj())/(-.1+2j*y)).real
            for m,n in directions:
                val=(m*m*A+2*m*n*C+n*n*B)/(m*m+n*n)
                i=np.argmin(np.where(mask,val,np.inf))
                row=(float(val[i]),heights[i],y,m,n)
                if name not in best or row<best[name]: best[name]=row
    print(best)
if __name__=='__main__': main()
