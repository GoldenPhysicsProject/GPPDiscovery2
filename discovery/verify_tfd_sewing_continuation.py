#!/usr/bin/env python3
"""Numerical controls for the 2026-09-27 TFD sewing continuation.

Proofs are in the companion research notes. Floating-point controls do not
certify RH, infinite-dimensional positivity, or tiny eigenvalue signs.
Uses NumPy/SciPy; no external data, network, or zero ordinates.
"""
import json
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import digamma


def primes_to(limit):
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for n in range(2, int(limit ** 0.5) + 1):
        if sieve[n]:
            sieve[n*n::n] = False
    return np.flatnonzero(sieve).astype(float)


def synthesis_controls(primes):
    rows = []
    for cutoff in (100, 1000, 10000, 100000, 1000000):
        p = primes[primes <= cutoff]
        r = p ** -0.5
        n = np.arange(2, 43)[:, None]
        v2 = np.sqrt(1 - 1/p)[None, :] * r[None, :] ** n
        # Stable singular values from a small Gram matrix; no sign claims for
        # near-zero eigenvalues. Full SVD directly avoids squaring conditioning.
        if cutoff <= 10000:
            nuclear = float(np.linalg.svd(v2, compute_uv=False).sum())
        else:
            nuclear = None
        row_bound = float(np.linalg.norm(v2, axis=1).sum())
        a1norm = float(np.sqrt(np.sum((1-1/p)/p)))
        first_row_l1 = float(np.sum(np.sqrt(1-1/p)/p))
        rows.append(dict(cutoff=cutoff, primes=len(p),
                         V1_first_row_l2=a1norm,
                         V2_nuclear_41_rows=nuclear,
                         V2_row_nuclear_bound_41_rows=row_bound,
                         V2_first_row_l1=first_row_l1,
                         V3_column_sum=float(np.sum(p**-1.5))))
    # Entire prime sum bounded by the sum over every integer >=2:
    # sum_n>=2 sqrt(sum_p(1-1/p)p^-n)
    # <= sqrt(sum_p(p^-2-p^-3))/(1-1/sqrt(2))
    # <= sqrt(zeta(2)-zeta(3))/(1-1/sqrt(2)); use the elementary
    # coarser sum_{n>=2} n^-2 <= 1 for a data-free bound.
    return dict(rows=rows, universal_V2_nuclear_bound=1/(1-2**-0.5))


def jprime(s, p):
    lp = np.log(p)
    return np.sum(lp / np.expm1(s * lp))


def bernstein_controls(p):
    q = 1.5
    pp = p[p <= 97]
    rows = []
    for z in (0.1, 0.7, 2.0, 5.0):
        gamma_closed = 0.5 * (digamma(1+(q+z)/2)-digamma(1+q/2))
        gamma_integral = quad(
            lambda x: (-np.expm1(-z*x))*np.exp(-(q+2)*x)
            / (-np.expm1(-2*x)), 0, 40,
            epsabs=2e-13, epsrel=2e-13)[0]
        prime_closed = jprime(q, pp) - jprime(q+z, pp)
        # Independently sum the prime-power Levy atoms.
        atom_sum = 0.0
        for prime in pp:
            ell = np.log(prime)
            for m in range(1, 161):
                atom_sum += ell*np.exp(-q*m*ell)*(-np.expm1(-z*m*ell))
        rows.append(dict(z=z, gamma_closed=float(gamma_closed),
                         gamma_quadrature=float(gamma_integral),
                         prime_closed=float(prime_closed),
                         prime_atoms=float(atom_sum),
                         total=float(gamma_closed+prime_closed),
                         max_error=float(max(abs(gamma_closed-gamma_integral),
                                             abs(prime_closed-atom_sum)))))
    assert max(x['max_error'] for x in rows) < 2e-11
    return dict(base_q=q, prime_cutoff=97, values=rows)


def edge_controls():
    rows = []
    for prime in (2, 3, 5, 11, 101):
        ell = 0.5*np.log(prime)
        for q in (0.5, 1.0, 1.7):
            z = q*ell
            precision = np.array([[1/np.tanh(z), -1/np.sinh(z)],
                                  [-1/np.sinh(z), 1/np.tanh(z)]])
            identity = np.eye(2)
            cayley = (precision-identity) @ np.linalg.inv(precision+identity)
            expected = -np.exp(-z)*np.array([[0., 1.], [1., 0.]])
            transfer = -cayley
            # Full determinant retains even traversals; the symmetric
            # restriction retains the original Euler factor.
            x = np.exp(-z)
            determinant_error = abs(np.linalg.det(identity-transfer)-(1-x*x))
            plus = np.array([1., 1.])/np.sqrt(2)
            symmetric_error = abs(plus@transfer@plus-x)
            assert determinant_error < 2e-13 and symmetric_error < 2e-13
            gamma = np.linalg.inv(precision)/(2*q)
            schur = gamma[0,0]-gamma[0,1]**2/gamma[1,1]
            # Independent positive mixed-boundary spectral expansion. The
            # omitted tail is bounded by ell/(pi^2*(N-1/2)).
            count = 50000
            n = np.arange(count)
            poles = ((n+0.5)*np.pi/ell)**2
            spectral = np.sum(1/(q*q+poles))/ell
            tail_bound = ell/(np.pi**2*(count-0.5))
            err = abs(schur - np.tanh(q*ell)/(2*q))
            assert abs(schur-spectral) <= tail_bound*(1+1e-6)
            assert err < 2e-13
            assert np.max(np.abs(cayley-expected)) < 2e-13
            rows.append(dict(prime=prime,q=q,cayley_error=float(np.max(np.abs(cayley-expected))),
                             paired_determinant_error=float(determinant_error),
                             symmetric_transfer_error=float(symmetric_error),
                             conditional_covariance=float(schur),
                             spectral_sum=float(spectral),tail_bound=float(tail_bound)))
    return rows


def odd_even_controls(primes):
    rows=[]
    p=primes[primes<=97]
    for s in (0.5, 0.8, 1.4):
        x=p**(-s)
        log_zeta_finite=-np.log1p(-x).sum()
        even=-0.5*np.log1p(-x*x).sum()
        odd=np.arctanh(x).sum()
        error=abs(log_zeta_finite-even-odd)
        assert error<3e-13
        rows.append(dict(s=s,finite_prime_log_euler=float(log_zeta_finite),
                         even_channel=float(even),odd_squeeze=float(odd),
                         identity_error=float(error)))
    return rows


def finite_cutoff_controls(p):
    # Every naive finite-prime m_P has a negative cut density near lambda=1.
    # rho_P(1+k^2) = Re(B_P(1/2+ik))/(2*pi*k).
    rows=[]
    k=0.1
    for cutoff in (0, 2, 7, 31, 97):
        pp=p[p<=cutoff]
        s=0.5+1j*k
        b=1/(s-1)-0.5*np.log(np.pi)+0.5*digamma(1+s/2)-jprime(s,pp)
        density=b.real/(2*np.pi*k)
        # Real-axis value u=1; prime truncation still yields a positive value.
        r=np.sqrt(2)
        ss=0.5+r
        bb=1/(ss-1)-0.5*np.log(np.pi)+0.5*digamma(1+ss/2)-jprime(ss,pp)
        value=bb/(2*r)
        assert density < 0 and value > 0
        eps=1e-7
        u=-0.75+eps
        rr=np.sqrt(1+u)
        sc=0.5+rr
        bc=1/(sc-1)-0.5*np.log(np.pi)+0.5*digamma(1+sc/2)-jprime(sc,pp)
        residue=eps*bc/(2*rr)
        rows.append(dict(prime_cutoff=cutoff,rho_at_lambda_1_01=float(density),
                         m_at_u_1=float(value),residue_at_minus_3_quarters=float(residue)))
    return rows


def weyl_packet_controls():
    # chi(y)=sqrt(630)*y^2(1-y)^2 has unit L2(0,1) norm and chi=chi'=0
    # at endpoints. These H^2_0 packets satisfy every endpoint extension.
    # ||chi'||^2=12, ||chi''||^2=504, hence exact residual below.
    rows=[]
    for k in (0., 1., 3.):
        for length in (10., 100., 1000.):
            residual=np.sqrt(48*k*k/length**2+504/length**4)
            rows.append(dict(wavenumber=k,length=length,
                             residual_norm=float(residual)))
    return rows


def main():
    p=primes_to(1000000)
    result=dict(
        status="floating-point controls; analytic proofs are in companion notes; RH open",
        synthesis=synthesis_controls(p),
        bernstein=bernstein_controls(p),
        edge=edge_controls(),
        odd_even=odd_even_controls(p),
        finite_cutoffs=finite_cutoff_controls(p),
        weyl_packets=weyl_packet_controls())
    path=Path(__file__).resolve().parents[1]/'research'/'2026-09-27_tfd_sewing_numerical_controls.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({"output":str(path),"synthesis":result['synthesis']['rows'],
                      "bernstein_max_error":max(x['max_error'] for x in result['bernstein']['values']),
                      "edge_max_cayley_error":max(x['cayley_error'] for x in result['edge']),
                      "finite_cutoffs":result['finite_cutoffs']},indent=2))


if __name__=='__main__':
    main()
