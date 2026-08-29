# Codex all-fronts continuation — 2026-08-29

## 1. Scalar box / generalized cuts

The structured scalar-box regulator layer is now formally strong enough to remove the two auxiliary small-regulator assumptions `m <= S/4` and `m <= U/16`: for fixed `S,U>0` those bounds are generated automatically as `m -> 0+`. The remaining hypotheses are the actual physical-chart defining relations.

The next numerator layer has also been promoted from discovery algebra into Lean. For the massive-vector `Sym^2` state sum,

\[
( s-2\mu^2)^2-\mu^4
=s^2-4s\mu^2+3\mu^4,
\]

with threshold specialization

\[
s=4\mu^2\quad\Longrightarrow\quad 3\mu^4.
\]

The dimensional-reconstruction identities

\[
C^{(4)}=C^{(V_m)}-C^{(S)},
\qquad
C^{(D_s)}=C^{(V_m)}+(D_s-5)C^{(S)}
\]

and the formal HV specialization are now also encoded as exact Lean algebra in `GppVerify/CelestialHolography/MassiveVectorStateSum.lean`.

This does not yet close the complete nonzero-`mu` MHV numerator: the honest double massive-projector tree sewing remains the decisive physical calculation.

## 2. Positive-real principal series

The arithmetic/celestial dictionary has been sharpened into a three-way equivalence. For any fixed nontrivial positive scale `a`,

\[
\Re s=\frac12
\iff
\Re(2s)=1
\iff
\|\chi_s(a)\|=1,
\]

where

\[
\chi_s(a)=\exp\big(\log a\,(s-1/2)\big).
\]

Thus the arithmetic critical axis, the celestial scalar principal-series axis and the unitary locus of the half-density multiplicative dilation representation are exactly the same locus. This is now formalized in `PrincipalSeriesDilationBridge.lean`.

This is a genuine representation-theoretic equivalence, but by itself it does not force zeta zeros onto that locus.

## 3. Prime-gas fluctuation geometry

The Codex workbench has been synchronized with the newest countable Fisher layer. The finite-support identity is now fully mass-aware:

\[
6\,\mathcal F(m_0,\ldots,m_4)
=m_0\,\mathcal V,
\]

where `mathcal V` is the ordered squared-Vandermonde energy. This avoids the false step of treating finite truncations of a countable probability measure as already normalized.

For pointwise nonnegative countable weights, summability of raw moments through order four and total mass one now imply in Lean

\[
\det \operatorname{Cov}(X,X^2)\ge 0.
\]

The proof passes through the mass-aware finite numerator and its countable limit, rather than through normalized truncations. This is the correct analytic bridge for the two-parameter number-thermodynamic geometry.

The next strict-positivity step is to transfer a persistent three-point Vandermonde witness through the countable limit.

## 4. Spectral weight / Mehler-Fock / Wiener-Hopf

The salvaged Archimedean spectral layer is stronger than a single kernel identity. For every finite Gamma chamber `k`, the normalized chamber density is exactly the base Wiener-Hopf/Mehler-Fock density multiplied by a finite product of strictly positive recurrence factors. Moreover the real chamber density has an exact square factorization

\[
\rho_k(\lambda)=F_k(\lambda)^2,
\qquad F_k(\lambda)>0
\]

for every real `lambda`, including the removable origin. Thus every finite Gamma chamber is strictly positive on the full real spectral axis.

The boundary remains important: this is an Archimedean spectral factorization. The missing RH step is identification of the full signed arithmetic Weil form with a global positive operator/factorization; local and Archimedean positivity alone are insufficient.

## 5. CI / repository state

The Codex workbench was fast-forward synchronized with the current certified `main` content by adopting the current GitHub merge commit, while retaining the Codex branch changes. This brought the countable Fisher/Vandermonde layer into the active workbench instead of allowing `main` and `codex/lean-workbench` to drift.

A stale `UniversalNotFidelity` matrix proof exposed by the full all-module gate was repaired by replacing fragile scalar notation and ring normalization with explicit complex scalars and `ring_nf`. The relevant CI gates were relaunched automatically.

## Claim boundary

Current claims earned by the formal/discovery layers are:

1. scalar-box one-sided regulator convergence is closed under the stated physical-chart defining relations with automatic small-regulator bookkeeping;
2. the massive-vector `Sym^2` invariant state-sum polynomial and dimensional-reconstruction algebra are exact;
3. critical-line, celestial-principal-series and half-density dilation unitarity loci coincide exactly;
4. the countable two-parameter Fisher determinant is nonnegative for normalized nonnegative weights with four summable raw moments;
5. every finite normalized Gamma/Wiener-Hopf chamber has a strictly positive exact square factorization on the real spectral axis.

The main open global claims remain the honest nonzero-`mu` projected MHV tree sewing, its gravity/double-copy extension, and the global prime-Archimedean operator identification needed to turn the local/spectral positivity package into the Weil positivity statement equivalent to RH.
