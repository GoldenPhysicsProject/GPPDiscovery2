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


## E. Infinite local operator: positive trace class, but no uniform gap

The same factorization has an **exact infinite-dimensional meaning** for each fixed \(0<x<1\). On \(\ell^2(\{1,2,\ldots\})\), define \(v_j(k)={\bf1}_{k\ge j}x^{k-j}\). Then

\[
C_x=\sum_{j=1}^{\infty}(1-x)x^j\,|v_j\rangle\langle v_j|,
\qquad
\|v_j\|_{\ell^2}^2=\frac1{1-x^2}.
\]

The nonnegative rank-one series converges in trace norm, since

\[
\boxed{\operatorname{Tr} C_x=
\sum_{j\ge1}(1-x)x^j\|v_j\|^2
=\frac{x}{1-x^2}.}
\]

Equivalently, if \(S\) is the unilateral right shift, then \(L=(I-xS)^{-1}\), \(D=(1-x)\operatorname{diag}(x,x^2,\ldots)\), and \(C_x=LDL^*\). This exhibits the covariance as a causal discrete Green/innovation kernel, but **not** a boundedly invertible global norm.

Indeed, for the \(N\times N\) leading block,
\[
0<\lambda_{\min}(C_x^{(N)})
\le \langle e_N,C_x^{(N)}e_N\rangle
=x^N(1-x^N)\longrightarrow0.
\]
Thus no positive lower coercivity constant independent of the occupation cutoff \(N\) follows from the local covariance, even at a single fixed prime. The infinite operator is compact, positive and infinite rank, with eigenvalues accumulating at zero. Finite positive definiteness and infinite-dimensional uniform coercivity are distinct claims.

At the physical midpoint \(x_p=p^{-1/2}\), the local trace is
\[
\operatorname{Tr}C_{x_p}=\frac{p^{-1/2}}{1-p^{-1}}.
\]
Its sum over all primes diverges. Consequently the unsmeared direct sum over prime sites is not trace class, despite every local site being positive trace class. Compact log-support tests still involve finitely many prime powers and have well-defined quasi-local covariance. This is another reason a global bulk/boundary sewing estimate cannot be obtained merely by assembling local PSD blocks.
