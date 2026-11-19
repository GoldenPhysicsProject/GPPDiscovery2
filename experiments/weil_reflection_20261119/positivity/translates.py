"""Weil matrices on translated Dirichlet sines, using the pinned model data."""
import math
import sys
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.linalg import toeplitz
from numpy.polynomial.legendre import leggauss
sys.path.insert(0,str(Path(__file__).resolve().parent/'upstream'))
import models14b as models

def gram_column(model,L,j,d,order):
    k=j[:,None]*np.pi/L
    def autocorr(t):
        x=np.abs(np.atleast_1d(t))
        return np.where(x<L,(1-x/L)*np.cos(k*x)+np.sin(k*x)/(k*L),0.)
    def corr(t):
        return (autocorr(t+d)+autocorr(t-d))/2
    end=L+d
    cuts=np.unique(np.r_[np.linspace(0,end,math.ceil(end/.2)+1), d, abs(L-d), end])
    a,b=cuts[:-1],cuts[1:]
    x,w=leggauss(order)
    t=((b-a)[:,None]*x/2+(b+a)[:,None]/2).ravel()
    w=((b-a)[:,None]*w/2).ravel()
    A=corr(t)
    A0=corr(0).ravel()
    tail=quad(model['w'],end,np.inf,epsabs=1e-13)[0]
    arch=(model['C']+2*tail)*A0+2*((A0[:,None]-A)@(w*model['w'](t)))
    poles=sum(4*wt*(A@(w*np.cosh(alpha*t))) for alpha,wt in model['poles'])
    n=model['n']
    sel=np.log(n)<end
    prime=2*corr(np.log(n[sel]))@(model['c'][sel]/np.sqrt(n[sel]))
    return arch+poles-prime

def scan(order):
    z=models.zeta()
    char=np.array([0,1,0,-1])
    beta=dict(z,name='beta',C=models.digamma(.75)+np.log(4/np.pi),
              w=lambda t:np.exp(-1.5*t)/(-np.expm1(-2*t)),poles=[],
              c=z['c']*char[z['n'].astype(int)%4])
    for model in [z,beta,models.eps(),models.dh(),models.beur2(),models.fth()]:
        best=[(np.inf,)]*3
        for L in (1,2,3):
            js=np.arange(1,1+math.floor(100*L/np.pi))
            diag=gram_column(model,L,js,0.,order)
            for p in (2,3,5,7):
                h=np.log(p)
                last=math.floor((8-L)/h)
                cols=[diag]+[gram_column(model,L,js,i*h,order) for i in range(1,last+1)]
                for i in range(1,last+1):
                    # Congruence by positive diagonal removes the shift weights.
                    v=diag-np.abs(cols[i])
                    ix=np.argmin(v)
                    row=(float(v[ix]),L,p,int(js[ix]),i)
                    if i==1: best[0]=min(best[0],row)
                    best[1]=min(best[1],row)
                for ix,j in enumerate(js):
                    v=np.linalg.eigvalsh(toeplitz(np.array(cols)[:,ix]))[0]
                    best[2]=min(best[2],(float(v),L,p,int(j),last))
        print(model['name'],best,flush=True)
if __name__=='__main__':scan(int(sys.argv[1]) if len(sys.argv)>1 else 20)
