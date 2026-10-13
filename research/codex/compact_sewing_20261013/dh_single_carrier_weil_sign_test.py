"""2026-10-13 — one-carrier DH-vs-zeta Weil sign test (NUMERICAL only).

Real explicit witness:
  h=7/2, omega=857/10,
  g(x)=u*(1-u*u)^4*cos(omega*x) for u=x/h, |x|<=h; 0 otherwise.
Convolution FFT & trapezoid are NOT rigorous Arb bounds.
Use the exact cosine/rational-polynomial autocorrelation identity to certify.
"""
import math
import numpy as np
from scipy.signal import fftconvolve
from sympy import factorint

EULER=0.5772156649015328606
alpha=(math.sqrt(10-2*math.sqrt(5))-2)/(math.sqrt(5)-1)

def a(n):
    return (0.,1.,alpha,-alpha,-1.)[n%5]

def c_dh(N):
    c=np.zeros(N+1)
    for n in range(2,N+1):
        v=a(n)*math.log(n)
        for d in range(2,math.isqrt(n)+1):
            if n%d==0:
                v-=a(d)*c[n//d]
                if d*d!=n: v-=a(n//d)*c[d]
        c[n]=v
    return c

def result(N=8001,h=3.5,omega=85.7,mode='cos'):
    x=np.linspace(-h,h,N); dx=x[1]-x[0];u=x/h
    b=u*(1-u*u)**4
    g=b*np.cos(omega*x) if mode=='cos' else b*np.sin(omega*x)
    F=fftconvolve(g,g[::-1],mode='full')*dx
    f=F[N-1:]; F0=float(np.trapezoid(g*g,x))
    t=np.arange(N)*dx;R=2*h
    D=int(math.exp(R))+2; cc=c_dh(D)
    v=np.empty(N);v[0]=F0/2
    v[1:]=2*(np.exp(-1.5*t[1:])*f[1:]-np.exp(-2*t[1:])*F0)/(-np.expm1(-2*t[1:]))
    wDH=(EULER+math.log(math.pi/5)+math.log1p(-math.exp(-2*R)))*F0+np.trapezoid(v,t)
    v[1:]=(2*np.exp(-.5*t[1:])*f[1:]-2*np.exp(-t[1:])*F0)/(-np.expm1(-2*t[1:]))
    v[0]=F0/2
    wZ=(math.log(4*math.pi)+EULER+math.log(math.tanh(h)))*F0+np.trapezoid(v,t)
    Pz=2*np.trapezoid((np.exp(t/2)+np.exp(-t/2))*f,t)
    pDH=pZ=0.
    for n in range(2,D+1):
        ln=math.log(n)
        if ln>=R: continue
        i=int(ln/dx); w=ln/dx-i
        fn=(1-w)*f[i]+w*f[i+1]
        pDH+=2*cc[n]/math.sqrt(n)*fn
        pp=factorint(n)
        if len(pp)==1:
            pr=next(iter(pp))
            pZ+=2*math.log(pr)/math.sqrt(n)*fn
    return (-(wDH+pDH)/F0,(Pz-wZ-pZ)/F0)

if __name__=='__main__':
    for N in (4001,8001,16001):
        for mode in ('cos','sin'):
            d,z=result(N=N,mode=mode)
            print('N',N,'mode',mode,'DH',round(d,8),'zeta',round(z,8))
    # Expected at N=16001: DH roughly -1.118686, zeta +3.747007
