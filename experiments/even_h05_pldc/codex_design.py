#!/usr/bin/env python3
"""Untrusted continuum-design experiment for the h=1/2 EVEN zeta sector.

Uses Grok S26 rational PL-DC multiplier, **unchanged**, as an input.
Minimizes beta_X(lambda, PL exterior)+lambda^2/2 on an explicit frequency
grid. The truncated objective is a LOWER bound on the required infinite
integral, so a positive optimistic margin is ONLY a candidate worth
developing, never a positivity proof. A negative optimistic margin is
a basis-dependent obstruction, not a counterexample to Weil positivity.

Source: Astra positive-pole Hilbert lemma (private bridge 2026-10-15);
Grok S26 multiplier (GPPDiscovery5/s26). Codex workbench continuation.
"""
import argparse
import json
import math
import numpy as np
from scipy.special import digamma
from scipy.linalg import solve


def frequency_grid(xmax):
    spans = [(0.0, 115.0, .025), (115.0, 135.0, .0025),
             (135.0, xmax, .025)]
    edges = []
    for lo, hi, dx in spans:
        if hi <= lo:
            continue
        e = np.linspace(lo, hi, int(round((hi-lo)/dx))+1)
        if edges:
            e = e[1:]
        edges.extend(e)
    e = np.asarray(edges)
    return (e[:-1]+e[1:])/2, np.diff(e)


def cosine_cosh_integral(h, x):
    return (.5*np.sinh(h/2)*np.cos(h*x) +
            x*np.cosh(h/2)*np.sin(h*x))/(x*x+.25)


def make_multiplier(data):
    den = int(data['den'])
    h = data['h_q'][0]/data['h_q'][1]
    D = data['D_q'][0]/data['D_q'][1]
    a = np.array(data['a_num'], dtype=float)/den
    uy = 2*h + D*np.arange(len(a))
    y = np.array(data['y_num']+[0], dtype=float)/den
    z = np.array([num/d for num,d in data['z_q']], dtype=float)
    slope = np.r_[0.0, np.diff(y)/np.diff(z), 0.0]
    jump = np.diff(slope)
    kap = math.log(2)/math.sqrt(2)
    def compute(x):
        zeta = digamma(.25+.5j*x).real
        # Trig polynomial uses the same a_num, frequencies and sign as S26.
        trigon = np.cos(np.outer(x,uy))@a
        what = -2*(np.cos(np.outer(x,z))@jump)/(x*x)
        return zeta-math.log(math.pi)-2*kap*np.cos(x*math.log(2)) +what-trigon
    return h, float(y[0]), compute


def run(args):
    with open(args.input) as f:
        data=json.load(f)
    h,C,mfun=make_multiplier(data)
    assert abs(h-.5)<1e-14
    z=h+(args.H-h)*np.linspace(0,1,args.N+1)**args.grade
    # N unknown ordinates at z[0]...z[N-1], terminal value fixed 0.
    n=args.N+1
    M=np.zeros((n,n)); v=np.zeros(n); ss=0.0
    gmin=(float('inf'),0.0)
    xgrid,weights=frequency_grid(args.X)
    for start in range(0,len(xgrid),args.chunk):
        x=xgrid[start:start+args.chunk]; dx=weights[start:start+args.chunk]
        m=mfun(x)
        ix=int(np.argmin(m))
        if m[ix]<gmin[0]:gmin=(float(m[ix]),float(x[ix]))
        if np.min(m)<=0:
            raise RuntimeError('Multiplier nonpositive on float grid: '+str(gmin))
        base=np.sin(h*x)/x
        cw=cosine_cosh_integral(h,x)
        co=np.cos(np.outer(x,z))
        dz=np.diff(z)
        phi=np.empty((len(x),args.N))
        phi[:,0]=(co[:,0]-co[:,1])/(dz[0]*x*x)-np.sin(h*x)/x
        for j in range(1,args.N):
            phi[:,j]=((co[:,j]-co[:,j-1])/dz[j-1]+
                      (co[:,j]-co[:,j+1])/dz[j])/(x*x)
        R=np.column_stack((-cw,phi))
        W=(4/math.pi)*dx/m
        M+=R.T@(W[:,None]*R)
        v+=R.T@(W*base)
        ss+=float(np.dot(base,W*base))
    # Positive-pole cost in the direct sum; no Parseval tail assumption here.
    M[0,0]+=.5
    eigmin=float(np.linalg.eigvalsh(M)[0])
    sol=solve(M,-v,assume_a='pos',check_finite=True)
    lam=float(sol[0]); y=np.r_[sol[1:],0.0]
    optimistic=float(ss+v@sol)
    margin=1-C*optimistic
    cap=math.sqrt(2/C)
    interior=(h-4*lam*math.sinh(h/2)+
              lam*lam*(h+math.sinh(h))/2)
    outside=sum((z[j+1]-z[j])*
                (y[j]*y[j]+y[j]*y[j+1]+y[j+1]*y[j+1])/3
                for j in range(args.N))
    # Independent coarse L2 mass, not a verified integral-tail bound.
    out={
        'status':'FLOAT OPTIMISTIC LOWER-OBJECTIVE ONLY; NOT ARB/LEAN CERTIFIED',
        'source':'Grok S26 h=1/2 exact rational PL-DC multiplier',
        'h':h,'C':C,'lambda':lam,'lambda_cap':cap,
        'N':args.N,'H':args.H,'grade':args.grade,'X':args.X,
        'grid_points':len(xgrid),'min_m_grid':gmin,
        'gram_min_eigenvalue':eigmin,
        'truncated_cost_plus_pole':optimistic,
        'optimistic_margin':margin,
        'residual_L2_halfline':interior+outside,
        'tail_not_included':True,
        'knots':z.tolist(),'exterior_ordinates':y.tolist(),
    }
    with open(args.output,'w') as f:json.dump(out,f,indent=2)
    print(json.dumps({k:vv for k,vv in out.items()
                      if k not in ('knots','exterior_ordinates')},indent=2))
    if not np.isfinite(optimistic) or not np.isfinite(margin):
        raise RuntimeError('Nonfinite diagnostic')


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--input',default='s26_mult_h05_pl16L6.json')
    p.add_argument('--output',default='even_h05_float_design.json')
    p.add_argument('--N',type=int,default=96)
    p.add_argument('--H',type=float,default=15.0)
    p.add_argument('--X',type=float,default=500.0)
    p.add_argument('--grade',type=float,default=1.5)
    p.add_argument('--chunk',type=int,default=1200)
    run(p.parse_args())
