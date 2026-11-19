"""Round 13e: falsifier harness. Same KG field, signed bound and two-space decomposition for
  ZETA  : Riemann zeta (reference)
  EPS   : Epstein zeta of Q = x^2+5y^2 (disc -20, class number 2): FE with Gamma(s), NO Euler product; coefficients of
          -Z'/Z computed from its own representation numbers r_Q(n) (Dirichlet log-derivative recursion), own gamma factor.
  BEUR  : discrete Beurling primes (DMV-type proxy): primes chosen so Pi_B(x) (powers weighted 1/m) tracks the continuous
          Pi_C with dPsi_C = 1_{x>=20}(1 - sum_q x^{rho_q-1})dx, rho_q = 1/2 +- 0.1 +- 28i. Euler product + Lambda_B >= 0,
          NO functional equation, NO gamma factor; zeta_B zeros in Re s > 0 = the quartet (Pi_B - Pi_C bounded).
Explicit-formula data (general Weil formula for Lambda_F(s) = A^s Gamma_F(s) F(s) = Lambda_F(1-s), poles at 0,1):
  W_F(g) = C_F A(0) + 2 int_0^inf w_F(t)[A(0)-A(t)]dt + 2 int A(t)cosh(t/2)dt - 2 sum_n c_F(n) n^-1/2 A(log n)
  ZETA: C = psi(1/4) - log pi, w = e^{-t/2}/(1-e^{-2t});  EPS: C = 2 log(sqrt20/2pi) + 2 psi(1/2), w = e^{-t/2}/(1-e^{-t}).
Field (u > L/2):  Phi_g(u) = [e^{-u/2} gv(i/2)] + e^{u/2} gv(-i/2) - sum c(n) n^-1/2 g(log n - u) - int w_F(x) g(x-u)dx
  (BEUR: no e^{-u/2} pole-at-0 term, no arch term).
"""
import numpy as np, math, json, sys
from scipy.special import digamma
from scipy.integrate import quad
sys.path.insert(0, '.')
from akg_kg import vonmangoldt_table, make_g, gv, hann_mean
from defect_kappa import basis, Amat, XG, WG
NMAX = int(math.exp(13.0 + 2.05)) + 1

def zeta_model():
    NS, LAM = vonmangoldt_table(NMAX)
    return dict(name='ZETA', n=NS, c=LAM, C=digamma(0.25) - math.log(math.pi),
                w=lambda t: np.exp(-t/2)/(-np.expm1(-2*t)), pole0=True)

def epstein_model():
    N = NMAX; r = np.zeros(N+1)
    ymax = int(math.sqrt(N/5))+1
    for y in range(-ymax, ymax+1):
        rem = N - 5*y*y
        if rem < 0: continue
        xm = int(math.isqrt(rem)); xs = np.arange(-xm, xm+1); v = xs*xs + 5*y*y
        np.add.at(r, v[v <= N], 1)
    a = r/2.0; a[0] = 0  # Z_Q = 2 * sum a(n) n^-s, a(1) = 1
    assert a[1] == 1
    logn = np.log(np.arange(N+1, dtype=float)); logn[0] = 0
    acc = np.zeros(N+1); c = np.zeros(N+1)
    nz = np.nonzero(a)[0]; nz = nz[nz >= 2]
    for d in range(1, N+1):
        c[d] = a[d]*logn[d] - acc[d]
        if c[d] != 0:
            k = nz[:np.searchsorted(nz, N//d, side='right')]
            if len(k): acc[d*k] += c[d]*a[k]
    idx = np.nonzero(np.abs(c) > 1e-14)[0]; idx = idx[idx >= 2]
    return dict(name='EPS', n=idx.astype(float), c=c[idx], C=2*math.log(math.sqrt(20)/(2*math.pi)) + 2*digamma(0.5),
                w=lambda t: np.exp(-t/2)/(-np.expm1(-t)), pole0=True, r=r)

def beurling_model(x0=20.0):
    q = [0.6+28j, 0.6-28j, 0.4+28j, 0.4-28j]
    lx = np.linspace(math.log(x0), math.log(NMAX)+0.01, 2_000_000)
    x = np.exp(lx)
    dens = 1 - sum((x**complex(r-1)).real for r in q)       # dPsi_C/dx
    assert dens.min() > 0
    dPi = dens/lx*x                                          # dPi_C/dlx
    Pi = np.concatenate([[0], np.cumsum(0.5*(dPi[1:]+dPi[:-1])*np.diff(lx))])
    # fixed point: pi_B(x) = Pi_C(x) - sum_{m>=2} round(pi_B(x^{1/m}))/m ; primes where round(pi_B) increments
    pb = Pi.copy()
    for it in range(8):
        corr = np.zeros_like(Pi); m = 2
        while lx[-1]/m >= lx[0]:
            corr += np.floor(np.interp(lx/m, lx, pb, left=0.0)+0.5)/m; m += 1
        pb = Pi - corr
    cnt = np.floor(pb+0.5); cnt = np.maximum.accumulate(np.maximum(cnt, 0))
    jumps = np.nonzero(np.diff(cnt) > 0)[0]+1
    # place each prime at the linearly interpolated crossing of pb through (level - 1/2) inside the grid cell,
    # not at the grid point (grid snapping biases psi_B by ~ -x * dlx/2 and fakes e^{u/2} growth in the field)
    primes = []
    for j in jumps:
        for lev in np.arange(cnt[j-1]+1, cnt[j]+1):
            a, b = pb[j-1], pb[j]; th = 0.5 if b == a else min(max((lev-0.5-a)/(b-a), 0.0), 1.0)
            primes.append(math.exp(lx[j-1] + th*(lx[j]-lx[j-1])))
    P = np.array(primes); ns, cs = [], []
    for p in P:
        m = p
        while m <= NMAX:
            ns.append(m); cs.append(math.log(p)); m *= p
    o = np.argsort(ns)
    return dict(name='BEUR', n=np.array(ns)[o], c=np.array(cs)[o], C=None, w=None, pole0=False, nprimes=len(P), quartet=q)

def powers(primes, X):
    s = 0.0; m = 2
    while 2**m <= X*4 and m < 40:
        lim = X**(1.0/m)
        if primes and primes[0] <= lim:
            s += np.searchsorted(primes, lim, side='right')/m
        else:
            break
        m += 1
    return s

def operators(model, L, M):
    nseg = max(4, int(M/4)+2); I = np.eye(M)
    e = np.linspace(-L/2, L/2, nseg+1)
    xq = np.concatenate([0.5*(b-a)*XG+0.5*(b+a) for a, b in zip(e[:-1], e[1:])]); wq = np.concatenate([0.5*(b-a)*WG for a, b in zip(e[:-1], e[1:])])
    P = basis(L, M, xq); c = (P*wq) @ np.cosh(xq/2); s = (P*wq) @ np.sinh(xq/2)
    pole = 2*(np.outer(c, c) - np.outer(s, s))
    arch = np.zeros((M, M))
    if model['C'] is not None:
        w = model['w']; arch = model['C']*I + 2*I*quad(lambda t: float(w(t)), L, np.inf)[0]
        edges = np.concatenate([[0], L*np.geomspace(1e-6, 1, 60)])
        for a, b in zip(edges[:-1], edges[1:]):
            for xg, wg in zip(0.5*(b-a)*XG+0.5*(b+a), 0.5*(b-a)*WG):
                A = Amat(L, M, xg, nseg); arch += 2*wg*float(w(xg))*(I - 0.5*(A+A.T))
    prime = np.zeros((M, M)); absprime = np.zeros((M, M))
    m = np.log(model['n']) < L
    for n, cc in zip(model['n'][m], model['c'][m]):
        A = Amat(L, M, math.log(n), nseg); prime += cc/math.sqrt(n)*(A+A.T); absprime += abs(cc)/math.sqrt(n)*(A+A.T)
    return arch, pole, prime, absprime

def W_scalar(model, g, L):
    from akg_kg import A as Af
    A0 = Af(g, L, 0); W = 0.0
    if model['C'] is not None:
        w = model['w']
        W += model['C']*A0 + 2*quad(lambda t: float(w(t))*(A0-Af(g, L, t)), 0, L, limit=200)[0] + 2*A0*quad(lambda t: float(w(t)), L, np.inf)[0]
    W += 4*quad(lambda t: Af(g, L, t)*math.cosh(t/2), 0, L, limit=200)[0]
    m = np.log(model['n']) < L
    W -= 2*sum(cc/math.sqrt(n)*Af(g, L, math.log(n)) for n, cc in zip(model['n'][m], model['c'][m]))
    return W

def field(model, g, L, us):
    lg = np.log(model['n']); cw = model['c']/np.sqrt(model['n'])
    gm = gv(g, L, np.array([0.5j, -0.5j])); out = np.empty(len(us))
    for k, u in enumerate(us):
        i0, i1 = np.searchsorted(lg, [u-L/2, u+L/2])
        v = math.exp(u/2)*gm[1].real - np.sum(cw[i0:i1]*g(lg[i0:i1]-u))
        if model['pole0']: v += math.exp(-u/2)*gm[0].real
        if model['w'] is not None:
            xs = np.linspace(u-L/2, u+L/2, 801); v -= np.trapezoid(model['w'](xs)*g(xs-u), xs)
        out[k] = v
    return out

if __name__ == '__main__':
    models = [zeta_model(), epstein_model(), beurling_model()]
    info = {mo['name']: dict(n_atoms=int(len(mo['n']))) for mo in models}
    info['BEUR']['nprimes'] = models[2]['nprimes']
    eps = models[1]
    info['EPS']['c_first'] = {int(n): float(c) for n, c in zip(eps['n'][:25], eps['c'][:25])}
    info['EPS']['frac_atoms_not_prime_power'] = None
    NSz, _ = vonmangoldt_table(NMAX); pp = set(NSz.astype(int).tolist())
    info['EPS']['frac_atoms_not_prime_power'] = float(np.mean([int(n) not in pp for n in eps['n']]))
    info['EPS']['frac_negative_c'] = float(np.mean(eps['c'] < 0))
    # growth of the coefficient sums vs zeta: sum_{n<X} c(n) n^-1/2 and sum |c(n)| n^-1/2 against 2 sqrt(X)
    for mo in models:
        for X in (1e2, 1e4, 1e6):
            m = mo['n'] < X
            info[mo['name']][f'signed_sum_minus_main_X{X:.0e}'] = float(np.sum(mo['c'][m]/np.sqrt(mo['n'][m])) - 2*math.sqrt(X))
            info[mo['name']][f'abs_sum_over_2sqrtX_X{X:.0e}'] = float(np.sum(np.abs(mo['c'][m])/np.sqrt(mo['n'][m]))/(2*math.sqrt(X)))
    print(json.dumps(info), flush=True)
    rows = []
    for L in (0.5, 1.0, 2.0, 3.0, 4.0):
        M = int(max(24, 10*L))
        for mo in models:
            arch, pole, prime, absprime = operators(mo, L, M)
            W = arch + pole - prime
            row = dict(model=mo['name'], L=L, lam_min_W=float(np.linalg.eigvalsh(W)[0]),
                       lam_min_arch=float(np.linalg.eigvalsh(arch)[0]) if mo['C'] is not None else None,
                       lam_max_prime_signed=float(np.linalg.eigvalsh(prime)[-1]) if np.any(prime) else 0.0,
                       lam_max_prime_abs=float(np.linalg.eigvalsh(absprime)[-1]) if np.any(absprime) else 0.0,
                       lam_max_prime_minus_pole=float(np.linalg.eigvalsh(prime-pole)[-1]),
                       lam_min_prime=float(np.linalg.eigvalsh(prime)[0]) if np.any(prime) else 0.0)
            # field: Cesaro (Hann) mean of Phi^2 on [u0, U] for U = 9, 11, 13, and flux
            g = make_g(L, 'even'); u0 = max(2.0, math.log(20)+L/2+0.1) if mo['name'] == 'BEUR' else max(2.0, L/2+0.1)
            du = 0.004; us = np.arange(u0, 13.0+du/2, du); F = field(mo, g, L, us)
            row['hann_mean'] = {str(U): hann_mean(us, F**2, u0, U) for U in (7.0, 9.0, 11.0, 13.0)}
            row['max_abs_Phi_by_quarter'] = [float(np.max(np.abs(F[(us >= a) & (us < a+(13-u0)/4)]))) for a in np.linspace(u0, 13, 5)[:-1]]
            if mo['C'] is not None:
                Ws = W_scalar(mo, g, L); row['W_g'] = Ws
                row['hann_over_W'] = {k: v/Ws for k, v in row['hann_mean'].items()}
            rows.append(row); print(json.dumps(row), flush=True)
    json.dump(dict(info=info, rows=rows), open('harness_results.json', 'w'), indent=1, default=float)
