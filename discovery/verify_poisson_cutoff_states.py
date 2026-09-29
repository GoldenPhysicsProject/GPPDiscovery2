#!/usr/bin/env python3
"""Poisson/Gamma/cutoff-state controls, without any Riemann-zero data.

The inverse-Gram example is a single-prime toy, not the BPY operator.
The normal-word expansion has an explicit analytic norm-tail estimate.
"""
import json
import math
from pathlib import Path
from collections import defaultdict
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.special import loggamma


def theta_positive(t):
    """sum_{k>=1} exp(-pi*t*k*k), truncated past exponent 50.

    Uses the direct positive series. The integral tail is bounded by
    exp(-pi*t*M*M)/(2*pi*t*M) after the last integer M.
    """
    last=max(1,int(math.ceil(math.sqrt(50/(math.pi*t)))))
    k=np.arange(1,last+1,dtype=float)
    value=float(np.exp(-math.pi*t*k*k).sum())
    bound=math.exp(-math.pi*t*last*last)/(2*math.pi*t*last)
    return value,bound


def poisson_controls():
    rows=[]
    for N in [3,10,40]:
        for c in [2,5,26,130]:
            direct,tail=theta_positive(c/(N*N))
            dual,dual_tail=theta_positive(N*N/c)
            poisson=N/(2*math.sqrt(c))-0.5+N/math.sqrt(c)*dual
            rows.append(dict(N=N,c=c,direct=direct,poisson=poisson,
                             abs_error=abs(direct-poisson),
                             analytic_series_tail_bound=tail+N/math.sqrt(c)*dual_tail))
    assert max(row['abs_error'] for row in rows)<2e-13
    return rows


def gamma_controls():
    def density(t):
        return math.exp(2*loggamma(0.25+0.5j*t).real)/(2*math.pi*math.sqrt(2*math.pi))
    rows=[]
    for h in [0.,math.log(2),math.log(5),2.3]:
        value,error=quad(lambda t:2*math.cos(t*h)*density(t),0,np.inf,
                         epsabs=2e-12,epsrel=2e-12,limit=250)
        target=1/math.sqrt(math.cosh(h))
        rows.append(dict(h=h,gamma_integral=value,overlap=target,
                         abs_error=abs(value-target),quadrature_error_estimate=error))
    assert max(row['abs_error'] for row in rows)<2e-11
    return rows


def cutoff_controls():
    rows=[]
    for N in [20,100,1000]:
        denominator,_=theta_positive(2/(N*N))
        for a,b in [(1,1),(1,2),(2,3),(3,5),(4,4),(8,3)]:
            numerator,_=theta_positive((a*a+b*b)/(N*N))
            gaussian=numerator/denominator
            gaussian_limit=math.sqrt(2)/math.sqrt(a*a+b*b)
            sharp=(N//max(a,b))/N
            sharp_limit=1/max(a,b)
            factor=(a*b)**(-0.5)/math.sqrt(math.cosh(math.log(a/b)))
            assert abs(factor-gaussian_limit)<1e-14
            rows.append(dict(N=N,a=a,b=b,sharp=sharp,sharp_limit=sharp_limit,
                             gaussian=gaussian,gaussian_limit=gaussian_limit,
                             gaussian_error=abs(gaussian-gaussian_limit)))
    # Independently form actual finite shift vectors for the sharp formula.
    N=37
    shift_errors=[]
    for a,b in [(2,3),(5,7),(8,8)]:
        u=np.ones(N)/math.sqrt(N)
        out=np.zeros(max(a,b)*N)
        # S_a S_b* u, with unused coordinates represented explicitly.
        out[a-1:a*(N//b):a]=u[b-1:N:b]
        value=float(np.dot(u,out[:N]))
        shift_errors.append(abs(value-(N//max(a,b))/N))
    assert max(shift_errors)<1e-14
    return dict(rows=rows,sharp_vector_check_max_error=max(shift_errors))


def word_powers(last):
    """Exact integer coefficients of (S+S*)^j in S^a S*^b form."""
    current={(0,0):1}
    powers=[current]
    for _ in range(last):
        nxt=defaultdict(int)
        for (a,b),coefficient in current.items():
            nxt[(a+1,b)]+=coefficient
            if a:
                nxt[(a-1,b)]+=coefficient
            else:
                nxt[(0,b+1)]+=coefficient
        current=dict(nxt)
        powers.append(current)
    return powers


def inverse_gram_controls():
    # C=0.4 I+0.2 S_2. G=I+C*C=alpha I+beta(S_2+S_2*).
    alpha,beta,last=1.2,0.08,18
    powers=word_powers(last)
    ratio=2*abs(beta)/alpha
    remainder=ratio**(last+1)/(alpha*(1-ratio))
    def expectation(state):
        total=0.
        for j,terms in enumerate(powers):
            moment=sum(coefficient*state(a,b) for (a,b),coefficient in terms.items())
            total+=(-beta/alpha)**j*moment/alpha
        return total
    sharp_limit=expectation(lambda a,b:2.**(-max(a,b)))
    gaussian_limit=expectation(lambda a,b:math.sqrt(2)/math.sqrt(4.**a+4.**b))
    rows=[]
    for N in [20,100,1000,10000]:
        norm2,_=theta_positive(2/(N*N))
        sharp=expectation(lambda a,b:(N//(2**max(a,b)))/N)
        cache={}
        def gaussian_state(a,b):
            key=tuple(sorted((a,b)))
            if key not in cache:
                cache[key]=theta_positive((4.**a+4.**b)/(N*N))[0]/norm2
            return cache[key]
        gaussian=expectation(gaussian_state)
        rows.append(dict(N=N,sharp_q_over_N=sharp,sharp_limit=sharp_limit,
                         gaussian_q_over_Z=gaussian,gaussian_limit=gaussian_limit,
                         gaussian_error=abs(gaussian-gaussian_limit)))
    assert rows[-1]['gaussian_error']<rows[0]['gaussian_error']
    assert remainder<1e-15
    return dict(model='single-prime toy C=0.4I+0.2S_2, not BPY',
                alpha=alpha,beta=beta,Neumann_last_degree=last,
                analytic_operator_norm_remainder_bound=remainder,
                sharp_limit=sharp_limit,gaussian_limit=gaussian_limit,rows=rows)


def main():
    results=dict(status='floating-point identity controls, not RH evidence',
                 numpy_version=np.__version__,scipy_version=scipy.__version__,
                 poisson=poisson_controls(),gamma=gamma_controls(),
                 cutoffs=cutoff_controls(),inverse_gram=inverse_gram_controls())
    path=Path(__file__).resolve().parents[1]/'research/2026-09-29_poisson_cutoff_controls.json'
    path.write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(dict(output=str(path),
                         poisson_max_error=max(x['abs_error'] for x in results['poisson']),
                         gamma_max_error=max(x['abs_error'] for x in results['gamma']),
                         toy_q_sharp=results['inverse_gram']['sharp_limit'],
                         toy_q_gaussian=results['inverse_gram']['gaussian_limit'],
                         analytic_Neumann_tail=results['inverse_gram']['analytic_operator_norm_remainder_bound']),indent=2))


if __name__=='__main__':
    main()
