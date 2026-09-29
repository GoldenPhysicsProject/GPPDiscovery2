#!/usr/bin/env python3
"""Finite controls for two exact graph-domain derivations; not an RH test.

No Riemann-zero ordinates are input. Random matrices use a fixed seed.
Run from any directory; outputs a JSON record under ../research/.
"""
from pathlib import Path
import json
import math
import numpy as np
import scipy
from scipy.linalg import eigh, lstsq, solve
from scipy.integrate import quad


def trace_controls():
    kappa = 0.5
    points = np.array([-2.0, -0.3, 0.0, 0.4, 1.8, 3.05])
    n = len(points)
    K = np.exp(-kappa * np.abs(points[:, None] - points)) / (2*kappa)
    G = solve(K, np.eye(n), assume_a="pos")
    assembled = np.zeros_like(G)
    assembled[0, 0] += kappa
    assembled[-1, -1] += kappa
    block_errors = []
    block_determinants = []
    for j, ell in enumerate(np.diff(points)):
        r = np.exp(-kappa*ell)
        C, A = r*r/(1-r*r), r/(1-r*r)
        tfd = 2*kappa*np.array([[C+0.5, -A], [-A, C+0.5]])
        dtn = kappa*np.array([[1/np.tanh(kappa*ell), -1/np.sinh(kappa*ell)],
                              [-1/np.sinh(kappa*ell), 1/np.tanh(kappa*ell)]])
        block_errors.append(float(np.max(np.abs(tfd-dtn))))
        block_determinants.append(float(np.linalg.det(dtn)))
        assembled[j:j+2, j:j+2] += dtn
    growth = []
    for t in [0., 0.1, 1., 3., 10.]:
        D = np.diag(np.exp(-1j*t*points))
        norm = math.sqrt(float(eigh(D.conj().T @ G @ D, G, eigvals_only=True)[-1]))
        bound = (math.sqrt(t*t+4*kappa*kappa)+abs(t))/(2*kappa)
        assert norm <= bound+2e-12
        growth.append(dict(time=t, quotient_norm=norm, ambient_exact_norm=bound))
    assert np.max(np.abs(assembled-G)) < 1e-12
    assert max(block_errors) < 1e-12
    return dict(kappa=kappa, points=points.tolist(),
                precision_max_error=float(np.max(np.abs(assembled-G))),
                tfd_max_error=max(block_errors), block_determinants=block_determinants,
                growth=growth)


def schur_controls():
    rng = np.random.default_rng(29092026)
    n, k = 12, 17
    C = (rng.normal(size=(k,n))+1j*rng.normal(size=(k,n))) / np.sqrt(2*k)
    c = (rng.normal(size=n)+1j*rng.normal(size=n))/np.sqrt(2*n)
    G = np.eye(n)+C.conj().T@C
    samples = []
    for cutoff in [1, 5, 12]:
        u = np.zeros(n)
        u[:cutoff] = 1
        q = float(np.vdot(u, solve(G, u, assume_a="pos")).real)
        for a in [0j, 0.001+0.002j, 0.3-0.7j]:
            A = 0.8+0.2j
            b = A-a*np.dot(u,c)
            formula = abs(b)**2/(1+abs(a)**2*q)
            # Independent distance to the graph, not minimization of the reduced formula.
            matrix = np.vstack([np.eye(n), C, (a*u)[None,:]])
            target = np.r_[c, C@c, A]
            v = lstsq(matrix,target)[0]
            actual = float(np.linalg.norm(matrix@v-target)**2)
            samples.append(dict(cutoff=cutoff, a=[a.real,a.imag],
                                q=q, formula=formula, least_squares=actual,
                                error=abs(actual-formula)))
    assert max(row["error"] for row in samples) < 2e-12
    return dict(seed=29092026, arithmetic_dimension=n, connected_dimension=k,
                max_error=max(row["error"] for row in samples), samples=samples)


def concentration_controls():
    # Synthetic model ONLY: C=I, c=e_1, A=1, a(z)=z^m at a manufactured zero z=0.
    # Hence q_N=N/2 and b_N=1-z^m. No zeta-zero claim is involved.
    rows=[]
    for multiplicity in [1,2,3]:
        for cutoff in [100,10000,1000000]:
            for scaled_offset in [0.,1.,2.]:
                z=scaled_offset*cutoff**(-1/(2*multiplicity))
                a=z**multiplicity
                distance=abs(1-a)/math.sqrt(1+cutoff*a*a/2)
                limit=1/math.sqrt(1+scaled_offset**(2*multiplicity)/2)
                rows.append(dict(multiplicity=multiplicity, cutoff=cutoff,
                                 scaled_offset=scaled_offset, z=z,
                                 distance=distance, scaled_limit=limit))
    return dict(model="synthetic C=I, c=e1, A=1, a(z)=z^m", rows=rows)


def off_real_controls():
    kappa, a = 0.5, 0.2
    rows=[]
    for n in [5,20,100,300]:
        d2=math.sqrt(math.pi/2)*(n*n+kappa*kappa+1)
        energy=quad(lambda x:(4*x*x+n*n+kappa*kappa)*math.exp(-2*x*x)/d2,
                    -np.inf,np.inf,epsabs=1e-12)[0]
        log_value=a*a+n*a-0.5*math.log(d2)
        rows.append(dict(n=n, real_H1_norm_squared=energy,
                         off_real_abs=math.exp(log_value), off_real_log_abs=log_value))
    assert max(abs(x["real_H1_norm_squared"]-1) for x in rows)<2e-12
    # Nonreal factors are positive on the real line; polynomial roots are explicit.
    b=2.3
    roots=[complex(sign_b*b,sign_a*a) for sign_b in [-1,1] for sign_a in [-1,1]]
    q=lambda z:((z-b)**2+a*a)*((z+b)**2+a*a)
    assert max(abs(q(z)) for z in roots)<1e-12
    return dict(kappa=kappa, imaginary_offset=a, rows=rows,
                invisible_factor_roots=[[z.real,z.imag] for z in roots],
                invisible_factor_root_error=max(abs(q(z)) for z in roots))


def main():
    result=dict(status="floating-point identity controls; not RH evidence",
                numpy_version=np.__version__, scipy_version=scipy.__version__,
                trace_tfd=trace_controls(), schur=schur_controls(),
                concentration=concentration_controls(), off_real=off_real_controls())
    path=Path(__file__).resolve().parents[1]/"research/2026-09-29_scale_graph_controls.json"
    path.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(dict(output=str(path),
                          precision_error=result["trace_tfd"]["precision_max_error"],
                          tfd_error=result["trace_tfd"]["tfd_max_error"],
                          schur_error=result["schur"]["max_error"],
                          gaussian_norm_error=max(abs(r["real_H1_norm_squared"]-1)
                                                  for r in result["off_real"]["rows"])),indent=2))


if __name__=="__main__":
    main()
