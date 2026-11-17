"""Floating-point Galerkin scan of the actual first-prime Weil form.

Diagnostic only: NOT interval certification or a proof of positivity/RH.
Requires numpy and scipy. L2-normalized Dirichlet sine basis. Digamma symbol
is exactly the real-place multiplier Re(psi(1/4+i*t/2))-log(pi).
At width L=0.72 only von Mangoldt n=2 enters the prime side.
"""
import json
import numpy as np
from scipy.special import roots_legendre, digamma

L = .72
LOG2 = np.log(2.)
V = LOG2 / np.sqrt(2.)
INTERVALS = [(0,10,160), (10,50,250), (50,200,300),
             (200,500,400), (500,2000,1000), (2000,10000,2000)]

def weil_matrix(n):
    k = np.arange(1, n+1)
    a = k * np.pi / L
    G = np.zeros((n,n), dtype=np.complex128)
    for left,right,order in INTERVALS:
        z,w = roots_legendre(order)
        xi = (left+right)/2+(right-left)*z/2
        weight = (right-left)/2 * w
        x = xi[:,None]
        F = np.sqrt(L/np.pi)/(2j) * (
             np.exp(.5j*k*np.pi)[None,:]*np.sinc((x-a[None,:])*L/(2*np.pi))
             -np.exp(-.5j*k*np.pi)[None,:]*np.sinc((x+a[None,:])*L/(2*np.pi)))
        symbol = (np.real(digamma(.25+.5j*xi))-np.log(np.pi)
                  -2*V*np.cos(LOG2*xi))
        G += 2*(F.conj().T @ (F*(weight*symbol)[:,None]))
    z,w = roots_legendre(800)
    x = L*z/2
    values = np.sqrt(2/L)*np.sin((x[:,None]+L/2)*a[None,:])
    C = np.sum(values*np.cosh(x[:,None]/2)*(L*w/2)[:,None],axis=0)
    S = np.sum(values*np.sinh(x[:,None]/2)*(L*w/2)[:,None],axis=0)
    G = np.real(G)+2*np.outer(C,C)-2*np.outer(S,S)
    return (G+G.T)/2

if __name__ == "__main__":
    rows=[]
    for n in [30,50,80,120]:
        A=weil_matrix(n)
        lam=np.linalg.eigvalsh(A)
        odd_k=np.arange(0,n,2)  # sine n odd, even under x -> -x
        even_k=np.arange(1,n,2)
        rows.append(dict(n=n, lambda_min=float(lam[0]),
            next_eigenvalue=float(lam[1]),
            even_parity_min=float(np.linalg.eigvalsh(A[np.ix_(odd_k,odd_k)])[0]),
            odd_parity_min=float(np.linalg.eigvalsh(A[np.ix_(even_k,even_k)])[0]),
            off_parity_abs_max=float(np.max(np.abs(A[np.ix_(odd_k,even_k)])))))
    print(json.dumps(dict(scope="Floating Galerkin only: no interval certificate",
        L=L, prime_term="n=2", frequency_cutoff=10000,
        quadrature_intervals=INTERVALS, rows=rows),indent=2))
