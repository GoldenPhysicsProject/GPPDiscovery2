# Prime occupation threshold covariance: exact Markov Gram and shifted-zeta control

2026-10-28 · Codex / GPPDiscovery2 · Follows verified GPPVerify PR #455

**Status:** The identities below have an elementary all-\(N\) algebraic proof and independent exact-rational tests. They are **not yet kernel-checked in Lean**. No claim of RH.

## A. All-dimensional factorization

From Astra's geometric occupation model, for \(0\le x\le1\) and integers \(k,\ell\ge1\),

\[
C_x(k,\ell)=x^{\max(k,\ell)}-x^{k+\ell}.
\]

PR #455 proved the source and all \(2\times2\) principal minors in Lean. We can now prove **every finite threshold Gram is PSD**.

For \(1\le k,\ell\le N\), define the unit-lower-triangular matrix \(L_{kj}={\bf1}_{j\le k}x^{k-j}\), and diagonal \(D_{jj}=(1-x)x^j\). The exact identity is

\[
\boxed{C_x(k,\ell)=(1-x)\sum_{j=1}^{\min(k,\ell)}x^{k+\ell-j}},
\qquad
\boxed{C_x=L D L^{\mathsf T}}.
\]

**Proof:** Assume \(k\le\ell\). The sum is \((1-x)x^\ell\sum_{r=0}^{k-1}x^r=x^\ell(1-x^k)=x^\ell-x^{k+\ell}\). The other ordering follows by symmetry. Matrix multiplication gives \(LDL^{\mathsf T}\).

Hence, for **any** real coefficients \(a_1,\dots,a_N\), including signed coefficients,

\[
\boxed{
\sum_{k,\ell=1}^N a_k a_\ell C_x(k,\ell)
=(1-x)\sum_{j=1}^N x^j
\left(\sum_{k=j}^N a_k x^{k-j}\right)^2\ge0.
}
\]

This is all-dimensional PSD for \(0\le x\le1\), not a guess based on low-dimensional pivots. For \(0<x<1\), it is strictly positive for every nonzero vector, because \(D\) has positive diagonal and \(L\) is invertible.

The consecutive \(N\)-threshold block has

\[
\boxed{\det C_x^{(N)}=(1-x)^N x^{N(N+1)/2}.}
\]

Its inverse is tridiagonal for \(0<x<1\). In one-based indices, the diagonal is \((1+x)/[(1-x)x^k]\) for \(k<N\), and \(1/[(1-x)x^N]\) at \(k=N\). The entries \((k,k+1)\) and \((k+1,k)\) equal \(-1/[(1-x)x^k]\). All others vanish. This is an exact **discrete Markov innovation/precision structure**, rather than just a numerical PSD observation.

## B. Exact tests

\`python3 discovery/prime_threshold_innovation_gram.py\` uses Python's rational \`Fraction\` type, not floating-point approximations. It checks the factorization, finite-sum kernel, determinant, explicit inverse, and signed-vector square identity in 24 cases:
\(x\in\{1/5,1/2,3/4,9/10\}\), \(N\in\{1,2,3,5,8,13\}\), plus a two-bath positive-covariance control.

The test validates sample cases; the displayed finite-geometric-series argument proves the general theorem. **Next Verify task:** formalize the finite-sum factorization and quadratic identity in Lean, avoiding any assumed Weil positivity.

## C. Strong control: shifted zeta passes all these local positivity tests

For \(0<\theta<1/2\), define the deliberately artificial control

\[
F_\theta(s)=\zeta(s-\theta)\zeta(s+\theta),
\qquad
\Xi_\theta(s)=\xi(s-\theta)\xi(s+\theta).
\]

The completed product satisfies reflection \(\Xi_\theta(1-s)=\Xi_\theta(s)\), and

\[
\Xi_\theta(1/2+it)=|\xi(1/2+\theta+it)|^2\ge0
\]

by the ordinary xi functional equation and conjugation. Yet if \(\xi(1/2+i\gamma)=0\), the shifted product vanishes at \(s=1/2\pm\theta+i\gamma\), **off** the critical line.

Its genuine Euler product gives

\[
-\frac{F_\theta'(s)}{F_\theta(s)}
=\sum_{p,k\ge1}(\log p)(p^{k\theta}+p^{-k\theta})p^{-ks}
\]

in its half-plane of absolute convergence. At \(\sigma=1/2\), introduce two independent positive geometric baths for each prime:

\[
x_{p,-}=p^{-(1/2-\theta)},\qquad
x_{p,+}=p^{-(1/2+\theta)}.
\]

The combined threshold means are \(x_{p,-}^k+x_{p,+}^k\), exactly the fake control's prime-power weights on the central line. The combined centered covariance is

\[
C_{p,\theta}(k,\ell)
=C_{x_{p,-}}(k,\ell)+C_{x_{p,+}}(k,\ell),
\]

PSD for **every finite threshold test space** by part A. Thus reflection symmetry, prime harmonic source reproduction, positive local occupation Gram, and even pointwise nonnegativity of the *completed* function on the central line all coexist with **known off-line zeros**.

This rules out any RH argument resting only on those properties. It does **not** rule out the actual full signed arithmetic/Archimedean sewing criterion.

## D. What must still be proved

The new positive Gram is **not the signed Weil form**: it has cross-harmonic \(k,\ell\) covariance and quadratic \((\log p)^2\) coefficients. A zero-independent, arithmetic-to-boundary map must reproduce the exact signed first-prime discrepancy \(E_1\) including its PNT mean subtraction; all higher harmonics; gamma, pole and contact terms; both Wave234 parity forms; and a global all-test-function domination inequality that *fails* for \(F_\theta\).

The verified universal modular-strip Schur multiplier \(\tanh^2(\pi\tau)\) vanishes at \(\tau=0\). On the full frequency line it therefore provides **no uniform strictly positive coercivity constant** without additional arithmetic information or a justified zero-mode restriction.

**Provenance:** Astra's positive geometric occupation source and covariance (GPPVerify PR #455), Turbo's Wave234 sector sewing, and Codex's independent innovation factorization and shifted-zeta falsification. Neither local PSD nor the strip dictionary proves RH.
