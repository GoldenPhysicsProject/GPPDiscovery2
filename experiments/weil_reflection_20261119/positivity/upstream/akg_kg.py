"""Round 13: AKG via the Pasterski-Shao KG construction -- numerics for C-B2, C-Abel, C-Window, toy off-line, C-Pair.
Construction side uses ONLY primes, the pole and the archimedean kernel (no zeros).
Zeros (Platt table zeros_14.dat from GPP Drive "Zeros", cross-checked with mpmath) are used ONLY as a comparison
(test data), in zero_side().  Labels: NUMERICAL for everything printed here.
Normalisation (D2/Verify kernel form):
  W(g) = C_inf A(0) + 2 int_0^inf w(t)[A(0)-A(t)]dt + 2 int A(t)cosh(t/2)dt - 2 sum_n Lambda(n) n^-1/2 A(log n)
  A(t)=int g(x)g(x+t)dx, w(t)=e^{-t/2}/(1-e^{-2t}), C_inf = psi(1/4) - log pi; zero side sum_rho |gv(gamma)|^2, gv(r)=int g e^{iry}
Bulk (smeared) field, u > L/2, from primes/pole/arch only:
  Phi_g(u) = e^{-u/2} gv(i/2) + e^{u/2} gv(-i/2) - sum_n Lambda(n) n^-1/2 g(log n - u) - int w(x) g(x-u) dx
which equals sum_rho gv(gamma_rho) e^{i gamma_rho u} by the explicit formula applied to g(.-u).
"""
import numpy as np, json, struct, math, sys
from scipy.integrate import quad
from scipy.special import digamma
import mpmath as mp

C_INF = digamma(0.25) - math.log(math.pi)
w = lambda t: math.exp(-t/2)/(-math.expm1(-2*t))
XG, WG = np.polynomial.legendre.leggauss(80)

P = np.polynomial.Polynomial
def make_g(L, kind):
    a = L/2
    base = (1 - P([0, 1/a])**2)**4
    poly = base if kind == 'even' else base*P([1, 0.6/a, -0.3/a**2])
    g = lambda x: np.where(np.abs(x) <= a, poly(x), 0.0)
    g.poly = poly; g.a = a
    return g

def integ(f, lo, hi):  # Gauss-Legendre on [lo,hi] (exact for polynomials of degree < 160)
    if hi <= lo: return 0.0
    x = 0.5*(hi-lo)*XG + 0.5*(hi+lo)
    return 0.5*(hi-lo)*np.sum(WG*f(x))

def A(g, L, t):
    t = abs(t)
    return integ(lambda x: g(x)*g(x+t), -L/2, L/2-t) if t < L else 0.0

def vonmangoldt_table(N):
    sieve = np.ones(N+1, bool); sieve[:2] = False
    for p in range(2, int(N**.5)+1):
        if sieve[p]: sieve[p*p::p] = False
    ns, lam = [], []
    for p in np.nonzero(sieve)[0]:
        q = int(p)
        while q <= N:
            ns.append(q); lam.append(math.log(p)); q *= int(p)
    o = np.argsort(ns)
    return np.array(ns, float)[o], np.array(lam)[o]

def W_parts(g, L, NS, LAM):
    A0 = A(g, L, 0)
    arch = C_INF*A0 + 2*quad(lambda t: w(t)*(A0-A(g, L, t)), 0, L, limit=200, epsabs=1e-14)[0] \
           + 2*A0*quad(w, L, np.inf)[0]
    pole = 4*quad(lambda t: A(g, L, t)*math.cosh(t/2), 0, L, limit=200, epsabs=1e-14)[0]
    m = np.log(NS) < L
    prime = 2*sum(lam/math.sqrt(n)*A(g, L, math.log(n)) for n, lam in zip(NS[m], LAM[m]))
    return dict(arch=arch, pole=pole, prime=prime, W=arch+pole-prime)

def platt(fn, maxz):
    out = []
    with open(fn, 'rb') as f:
        nb = struct.unpack('Q', f.read(8))[0]
        for b in range(nb):
            hdr = f.read(32)
            if len(hdr) < 32: break
            t0, t1, N0, N1 = struct.unpack('ddQQ', hdr)
            Z = 0
            for k in range(N1-N0):
                z1, z2, z3 = struct.unpack('QIB', f.read(13))
                Z += (z3 << 96)+(z2 << 64)+z1
                out.append(t0 + float(Z)*2.0**-101)
                if len(out) >= maxz: return np.array(out)
    return np.array(out)

def gv(g, L, r):
    """int g(y) e^{i r y} dy. |r|>=5: exact integration by parts for the polynomial g (vanishes to order 4 at +-a);
    small |r|: Gauss quadrature."""
    r = np.atleast_1d(r).astype(complex)
    big = np.abs(r) >= 5
    out = np.zeros(r.shape, complex)
    if big.any():
        rb = r[big]; a = g.a; d = g.poly; k = 0; acc = np.zeros(rb.shape, complex)
        while d.degree() >= 0 and np.any(d.coef != 0):
            acc += (-1)**k*(np.exp(1j*rb*a)*d(a) - np.exp(-1j*rb*a)*d(-a))/(1j*rb)**(k+1)
            d = d.deriv(); k += 1
            if k > 60: break
        out[big] = acc
    if (~big).any():
        out[~big] = gv_quad(g, L, r[~big])
    return out

def gv_quad(g, L, r):
    r = np.atleast_1d(r).astype(complex)
    K = max(8, int(np.max(np.abs(r))*L/20)+1)
    edges = np.linspace(-L/2, L/2, K+1)
    out = np.zeros(r.shape, complex)
    for lo, hi in zip(edges[:-1], edges[1:]):
        x = 0.5*(hi-lo)*XG + 0.5*(hi+lo); wt = 0.5*(hi-lo)*WG*g(x)
        for i0 in range(0, len(r), 2000):
            out[i0:i0+2000] += np.exp(1j*np.outer(r[i0:i0+2000], x)) @ wt
    return out

def zero_side(g, L, gam):
    v = gv(g, L, gam); v2 = gv(g, L, -gam)
    return float(np.sum(np.abs(v)**2 + np.abs(v2)**2))

def Phi(g, L, us, NS, LAM):
    """bulk field from primes/pole/arch only (u > L/2)"""
    lg = np.log(NS); c = LAM/np.sqrt(NS)
    gm = gv(g, L, np.array([0.5j, -0.5j]))  # gv(i/2)=int g e^{-y/2}, gv(-i/2)=int g e^{y/2}
    out = np.empty(len(us)); diag = np.empty(len(us))
    for k, u in enumerate(us):
        i0, i1 = np.searchsorted(lg, [u-L/2, u+L/2])
        gg = g(lg[i0:i1]-u)
        ps = np.sum(c[i0:i1]*gg)
        diag[k] = np.sum((c[i0:i1]*gg)**2)
        ar = integ(lambda x: np.array([w(t) for t in x])*g(x-u), u-L/2, u+L/2)
        out[k] = (math.exp(-u/2)*gm[0] + math.exp(u/2)*gm[1]).real - ps - ar
    return out, diag

def hann_mean(us, F, u0, U):
    m = (us >= u0) & (us <= U)
    s = np.sin(np.pi*(us[m]-u0)/(U-u0))**2
    return float(np.trapezoid(s*F[m], us[m])/np.trapezoid(s, us[m]))

if __name__ == '__main__':
    U = float(sys.argv[1]) if len(sys.argv) > 1 else 13.0
    NS, LAM = vonmangoldt_table(int(math.exp(U+1.05))+1)
    gam = platt('/workspace/zeros/zeros_14.dat', 6000)
    chk = [abs(gam[k]-float(mp.zetazero(k+1).imag)) for k in (0, 1, 99)]
    res = dict(U=U, zero_check_vs_mpmath=chk, n_zeros=len(gam), gamma_max=float(gam[-1]), runs=[])
    du = 0.004
    for L in (0.5, 1.0, 2.0):
        for kind in ('even', 'asym'):
            g = make_g(L, kind)
            wp = W_parts(g, L, NS, LAM)
            Z = zero_side(g, L, gam)
            us = np.arange(L/2+0.5, U+du/2, du)
            F, D = Phi(g, L, us, NS, LAM)
            F2 = F**2
            u0 = 2.0
            cb2 = hann_mean(us, F2, u0, U)
            diag = hann_mean(us, D, u0, U)
            # C-Abel: one-sided exponential regulator from u0
            m = us >= u0
            abel = {}
            for eps in (0.5, 0.25, 0.1):
                wt = np.exp(-2*eps*(us[m]-u0))
                abel[str(eps)] = float(np.trapezoid(wt*F2[m], us[m])/np.trapezoid(wt, us[m]))
            # C-Window: finite windows of length 1,2,4 at several positions: leakage Q - W
            win = []
            for Lw in (1.0, 2.0, 4.0):
                for a in np.arange(u0, U-Lw+1e-9, Lw/2):
                    win.append((Lw, float(a), hann_mean(us, F2, a, a+Lw) - wp['W']))
            # explicit-formula pointwise check of Phi vs zero sum at a few u (test data)
            uc = np.array([3.0, 7.0, 11.0]); Fc, _ = Phi(g, L, uc, NS, LAM)
            v = gv(g, L, gam); v2 = gv(g, L, -gam)
            Zc = [float(np.sum(v*np.exp(1j*gam*u) + v2*np.exp(-1j*gam*u)).real) for u in uc]
            run = dict(L=L, g=kind, **wp, zero_side=Z, W_minus_Z=wp['W']-Z,
                       CB2_hann=cb2, CB2_rel_err=(cb2-wp['W'])/wp['W'], abel=abel,
                       window_leak_min=min(x[2] for x in win)/wp['W'], window_leak_max=max(x[2] for x in win)/wp['W'],
                       window_leak_by_length={str(Lw): [min(x[2] for x in win if x[0] == Lw)/wp['W'], max(x[2] for x in win if x[0] == Lw)/wp['W']] for Lw in (1.0, 2.0, 4.0)},
                       pair_diag_mean=diag, pair_offdiag_needed=cb2-diag,
                       Phi_pointwise=[float(x) for x in Fc], zero_sum_pointwise=Zc)
            # toy off-line quartet (HYPOTHETICAL, diagnostic): rho = 1/2 +- beta + i gamma0 (and conjugates)
            if kind == 'even':
                beta, g0 = 0.1, 28.0
                gt = gv(g, L, np.array([g0-1j*beta, g0+1j*beta]))
                toy = F + 2*np.real(gt[0]*np.exp(1j*g0*us)*np.exp(beta*us)) + 2*np.real(gt[1]*np.exp(1j*g0*us)*np.exp(-beta*us))
                run['toy_offline_beta0.1_g28'] = {str(Uc): hann_mean(us, toy**2, u0, Uc)/wp['W'] for Uc in (5.0, 7.0, 9.0, 11.0, 13.0) if Uc <= U}
            res['runs'].append(run)
            print(json.dumps({k: run[k] for k in ('L', 'g', 'W', 'zero_side', 'CB2_hann', 'CB2_rel_err', 'abel', 'window_leak_min', 'window_leak_max', 'pair_diag_mean')}), flush=True)
    json.dump(res, open('akg_kg_results.json', 'w'), indent=1, default=float)
