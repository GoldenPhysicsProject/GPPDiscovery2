#!/usr/bin/env python3
"""Dataset checks and finite controls for the logistic Poisson quotient.

Inputs are user-provided ordinates, not independently certified zeros.
No dense matrix of the full dataset is formed. Only selected small windows
are used for generalized eigenvalues; every window reports conditioning.
"""
import argparse
import hashlib
import json
import math
from decimal import Decimal
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh


def p_density(x):
    e=math.exp(-abs(x))
    return e/(1+e)**2


def P(d):
    d=np.asarray(d,dtype=float)
    y=np.pi*np.abs(d)
    result=np.ones_like(y)
    nz=y>1e-8
    result[nz]=2*y[nz]*np.exp(-y[nz])/(-np.expm1(-2*y[nz]))
    result[~nz]=1-y[~nz]**2/6+7*y[~nz]**4/360
    return result


def pair_norm(r,d,t):
    q=abs(r*math.sin(d*t/2))/math.sqrt((1-r)*(1+r))
    return math.hypot(1,q)+q


def window_result(z,j,k,t,T=0):
    freq=z[j:j+k]-z[j]
    delta=freq[:,None]-freq[None,:]
    g=P(delta)*np.sinc(delta*T/np.pi)
    eig=np.linalg.eigvalsh(g)
    cond=float(eig[-1]/eig[0]) if eig[0]>0 else None
    result={'first_row':j+1,'count':k,'height':float(z[j]),'width':float(freq[-1]),
            'averaging_T':T,'gram_min_eigenvalue':float(eig[0]),'condition_number':cond}
    if eig[0]<=0 or cond>1e11:
        result['norm_status']='not reported: double-precision Gram is ill-conditioned'
        return result
    phase=np.diag(np.exp(1j*freq*t))
    numerator=phase.conj().T@g@phase
    numerator=(numerator+numerator.conj().T)/2
    vals,vec=eigh(numerator,g)
    v=vec[:,-1]
    residual=np.linalg.norm(numerator@v-vals[-1]*g@v)/(np.linalg.norm(numerator)*np.linalg.norm(v))
    value=math.sqrt(float(vals[-1]))
    assert 1-1e-8 <= value <= math.exp(abs(t)/2)+1e-5,(result,value)
    result.update(operator_norm=value,generalized_eigen_residual=float(residual),norm_status='finite numerical control')
    if k==2:
        result['pair_formula']=pair_norm(float(g[0,1]),freq[-1],t)
        assert abs(value-result['pair_formula'])<2e-7
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--data-dir',type=Path,required=True)
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1]/'research/2026-09-30_thermal_zero_controls.json')
    args=parser.parse_args()
    high=args.data_dir/'zeta_zeros_100k.txt'; large=args.data_dir/'zeros6.txt'
    h=np.loadtxt(high); z=np.loadtxt(large)
    assert np.array_equal(h[:,0],np.arange(1,len(h)+1))
    assert np.all(np.diff(h[:,1])>0) and np.all(np.diff(z)>0)
    # Compare retained decimal strings, so comparison error is not float rounding.
    highlines=high.read_text().splitlines(); largelines=large.read_text().splitlines()
    diffs=[abs(Decimal(a.split()[1])-Decimal(b.strip())) for a,b in zip(highlines,largelines)]
    worst=max(range(len(diffs)),key=diffs.__getitem__)
    provenance=[]
    for path,arr in [(high,h[:,1]),(large,z)]:
        provenance.append({'name':path.name,'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                           'rows':len(arr),'first_ordinate':float(arr[0]),'last_ordinate':float(arr[-1]),'strictly_increasing':True})
    t=math.log(2)
    clusters=[]; selected=[]
    for k in [2,3,4,8,12]:
        widths=z[k-1:]-z[:1-k]
        j=int(np.argmin(widths))
        clusters.append({'count':k,'first_row':j+1,'last_row':j+k,'first_ordinate':float(z[j]),'last_ordinate':float(z[j+k-1]),'width':float(widths[j])})
        selected.append(window_result(z,j,k,t))
    for j in [0,len(h)-12,len(z)-12]:
        selected.append(window_result(z,j,12,t))
    closej=clusters[0]['first_row']-1
    time_averages=[window_result(z,closej,2,t,T) for T in [0,1,10,100,1000,10000]]
    quadrature=[]
    for d in [0,.002958654,.2,1,2.3]:
        q=2*quad(lambda x:p_density(x)*math.cos(d*x),0,np.inf,epsabs=2e-12)[0]
        exact=float(P(d))
        quadrature.append({'difference':d,'abs_error':abs(q-exact)})
    laplace=[]
    for c in [0,.2,.7]:
        q=quad(lambda x:math.exp(c*x)*p_density(x) if abs(x)<700 else 0,-np.inf,np.inf,epsabs=1e-11)[0]
        exact=1 if c==0 else math.pi*c/math.sin(math.pi*c)
        laplace.append({'c':c,'abs_error':abs(q-exact)})
    assert max(x['abs_error'] for x in quadrature+laplace)<2e-10
    moment_output=[]
    from scipy.special import digamma
    for n in [0,1,2,3]:
        val=quad(lambda x:float(P(x))*(float(digamma(.5+.5j*x).real-digamma(.5)))**n/np.pi,0,35,epsabs=2e-12)[0]
        target=[.25,.125,.125,.5*math.log(2)-3/16][n]
        moment_output.append({'power':n,'integral':val,'comparison':target,'abs_error':abs(val-target),
                              'comparison_status':'proved in supplied source' if n<3 else 'conjectural supplied closed form; numerical only'})
    out={'status':'finite diagnostics, no independent certification of zeros or proof of RH',
         'data':provenance,'shared_decimal_comparison':{'rows':len(h),'max_difference':str(diffs[worst]),'worst_row':worst+1,
             'larger_than_half_last_decimal_count':sum(x>Decimal('0.0000000005') for x in diffs)},
         'time':t,'ambient_and_quotient_exact_norm_from_proof':math.sqrt(2),
         'minimum_width_clusters':clusters,'selected_windows':selected,'closest_pair_time_averages':time_averages,
         'kernel_quadrature':quadrature,'laplace_quadrature':laplace,'supplied_moment_controls':moment_output}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
