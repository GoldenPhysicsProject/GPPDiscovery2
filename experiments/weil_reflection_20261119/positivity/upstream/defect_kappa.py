"""Round 13b: Weil defect curve and the two-space exponent kappa, widths L' = 0.5..8.
Construction: primes, pole, arch only. Zeros (zeros_14.dat) only to cross-check the Galerkin matrix at small L.
Basis: orthonormal Dirichlet sines phi_j on I=[-L/2,L/2], j=1..M.  W_jk = arch_jk + pole_jk - prime_jk, with
 arch_jk = C_inf d_jk + 2 int_0^L w(t)[d_jk - S_jk(t)]dt + 2 d_jk int_L^inf w,  S(t) = (A(t)+A(t)^T)/2, A_jk(t)=int phi_j(x)phi_k(x+t)dx
 pole_jk = 2(c_j c_k - s_j s_k),  prime_jk = sum_{n<=e^L} Lambda(n) n^-1/2 (A_jk(log n)+A_kj(log n))
Two-space split (Verify weilForm_regrouped): B = arch + pole + theta(N) I, C*C = theta(N) I + prime, W = B - C*C.
"""
import numpy as np, math, json, sys
from scipy.special import digamma
from scipy.integrate import quad
sys.path.insert(0, '.')
from akg_kg import vonmangoldt_table, platt
C_INF = digamma(0.25) - math.log(math.pi)
w = lambda t: np.exp(-t/2)/(-np.expm1(-2*t))
XG, WG = np.polynomial.legendre.leggauss(64)

def basis(L, M, x):
    j = np.arange(1, M+1)[:, None]
    return np.where(np.abs(x) <= L/2 + 1e-15, math.sqrt(2/L)*np.sin(j*np.pi*(x+L/2)/L), 0.0)

def Amat(L, M, t, nseg):
    lo, hi = -L/2, L/2 - t
    if hi <= lo: return np.zeros((M, M))
    e = np.linspace(lo, hi, nseg+1); xs = []; ws = []
    for a, b in zip(e[:-1], e[1:]):
        xs.append(0.5*(b-a)*XG+0.5*(b+a)); ws.append(0.5*(b-a)*WG)
    x = np.concatenate(xs); wt = np.concatenate(ws)
    return (basis(L, M, x)*wt) @ basis(L, M, x+t).T

def galerkin(L, M):
    nseg = max(4, int(M/4)+2)
    NS, LAM = vonmangoldt_table(int(math.exp(L))+2)
    # arch: graded composite Gauss in t on (0, L)
    edges = np.concatenate([[0], L*np.geomspace(1e-6, 1, 60)])
    I = np.eye(M); arch = C_INF*I + 2*I*quad(lambda t: float(w(t)), L, np.inf)[0]
    for a, b in zip(edges[:-1], edges[1:]):
        for xg, wg in zip(0.5*(b-a)*XG+0.5*(b+a), 0.5*(b-a)*WG):
            A = Amat(L, M, xg, nseg); arch += 2*wg*w(xg)*(I - 0.5*(A+A.T))
    xq = np.concatenate([0.5*(b-a)*XG+0.5*(b+a) for a, b in zip(np.linspace(-L/2, L/2, nseg+1)[:-1], np.linspace(-L/2, L/2, nseg+1)[1:])])
    wq = np.concatenate([0.5*(b-a)*WG for a, b in zip(np.linspace(-L/2, L/2, nseg+1)[:-1], np.linspace(-L/2, L/2, nseg+1)[1:])])
    P = basis(L, M, xq)
    c = (P*wq) @ np.cosh(xq/2); s = (P*wq) @ np.sinh(xq/2)
    pole = 2*(np.outer(c, c) - np.outer(s, s))
    prime = np.zeros((M, M)); theta = 0.0
    for n, lam in zip(NS, LAM):
        if math.log(n) < L:
            A = Amat(L, M, math.log(n), nseg); prime += lam/math.sqrt(n)*(A+A.T)
    for n, lam in zip(NS, LAM):  # theta(N) for the minimal admissible N (L < log(N+1)), primes only
        if n < math.exp(L) and abs(lam - math.log(n)) < 1e-12: theta += lam
    return dict(arch=arch, pole=pole, prime=prime, theta=theta, c=c, s=s)

def zero_check(L, M, gam):
    # W_jk from zero side: sum over +-gamma of phiv_j(g) conj(phiv_k(g)), phiv(r)=int phi e^{iry}
    nseg = 60
    e = np.linspace(-L/2, L/2, nseg+1)
    xq = np.concatenate([0.5*(b-a)*XG+0.5*(b+a) for a, b in zip(e[:-1], e[1:])]); wq = np.concatenate([0.5*(b-a)*WG for a, b in zip(e[:-1], e[1:])])
    P = basis(L, M, xq)*wq
    g = gam[gam < 3000]
    F = P @ np.exp(1j*np.outer(xq, g))
    Z = F @ F.conj().T; return 2*Z.real

if __name__ == '__main__':
    gam = platt('/workspace/zeros/zeros_14.dat', 6000)
    out = []
    for L in (0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0):
        M = int(max(24, 10*L))
        d = galerkin(L, M)
        W = d['arch'] + d['pole'] - d['prime']
        ev = np.linalg.eigvalsh(W)
        archpole = np.linalg.eigvalsh(d['arch'] + d['pole'])
        pr = np.linalg.eigvalsh(d['prime'])
        crude_tN = sum(math.log(p)*(1-1/p)/(1-p**-0.5)**2 for p in range(2, int(math.exp(L))+1) if all(p % q for q in range(2, int(p**.5)+1)) and p < math.exp(L))
        m_LN = d['theta'] + C_INF + L - 2*math.sinh(L/2)
        row = dict(L=L, M=M, lam_min_W=float(ev[0]), lam_2_W=float(ev[1]), scale=float(np.abs(W).max()),
                   lam_min_archpole=float(archpole[0]), lam_max_prime=float(pr[-1]),
                   separate_bound=float(archpole[0]-pr[-1]),
                   crude_m_minus_tN=m_LN - crude_tN, pole_odd=-2*float(d['s'] @ d['s']),
                   two_sinh=2*math.sinh(L/2), sum_Lambda_n_half=float(sum(l/math.sqrt(n) for n, l in zip(*vonmangoldt_table(int(math.exp(L))+1)) if n < math.exp(L))))
        if L <= 2.0:
            Z = zero_check(L, M, gam); row['zero_check_maxabs'] = float(np.abs(Z - W).max())
        out.append(row); print(json.dumps(row), flush=True)
    json.dump(out, open('defect_kappa_results.json', 'w'), indent=1)
