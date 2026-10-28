# Exact arithmetic boundary source price in the centered prime-threshold Hilbert space

2026-10-28 · Codex · Extension of the geometric Fock state and Markov covariance

Let \(0<x<1\) and index thresholds \(k\ge1\). The true source/mean vector for the prime is \(m_k=x^k\). The centered covariance is

\[
C_{k\ell}=x^{\max(k,\ell)}-x^{k+\ell}.
\]

The **first column** has the exact identity \(C_{k1}=x^k(1-x)=(1-x)m_k\). Thus **at every finite cutoff \(N\)**,

\[
\boxed{C_N^{-1}m_N=(1-x)^{-1}e_1}
\]

and the optimal squared reproducing-kernel/Schur norm of the linear mean functional with respect to this physical covariance is

\[
\boxed{m_N^T C_N^{-1}m_N=\frac{x}{1-x}.}
\]

This result is independent of \(N\): the entire prime-power mean is represented by a source pointing along the **first** innovation / threshold, even though the covariance contains all higher \(k\).

For the actual midpoint prime bath \(x_p=p^{-1/2}\), the source includes the von Mangoldt factor \(\log p\). Therefore the natural direct-sum squared source cost is

\[
\boxed{\sum_p \frac{(\log p)^2\,p^{-1/2}}{1-p^{-1/2}}=\infty.}
\]

The divergence is elementary: the summand is at least \((\log p)^2p^{-1/2}\), larger than \(1/p\) for all \(p\ge2\), and the reciprocal-prime series diverges. A globally **normal bounded** source vector on the naive orthogonal direct sum of centered prime covariances therefore does not exist at the critical line. Compact log-support smearings still select finitely many prime sites and have well-defined finite covariance/source costs.

**New qualitative distinction:** the missing global prime–Archimedean intertwiner cannot be obtained simply by declaring the unrenormalized prime mean a single finite-energy source vector in the direct sum of local physical fluctuation Hilbert spaces. One must provide a nonlocal subtraction, relative/renormalized pairing, a domain restriction, or a different representation. This is not an impossibility theorem for a renormalized nonlocal bulk/boundary construction; it is a quantitative obstruction to the *naive bounded-source map*. It also clarifies what “(SPACE) price” would have to absorb in a genuine sewing argument.

For the two-species \(F_\theta(s)=\zeta(s-\theta)\zeta(s+\theta)\) control, each species has the same positive local source price \(x_{p,\pm}/(1-x_{p,\pm})\), so the direct-sum cost diverges there as well. A criterion depending only on source normalizability would not distinguish zeta from the shifted fake.

Independent exact-rational tests \`python3 discovery/prime_source_price.py\` (to be committed alongside the note) verify the inverse identity for four rational \(x\) and five cutoff sizes. The proof is simply the first-column identity above. No RH proof or zero localization follows.
