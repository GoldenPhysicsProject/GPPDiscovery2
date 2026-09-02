# Fisher determinant as a Vandermonde triple expectation

Status note: this identity was independently rederived in the 2026-09-02 Codex rotation, but the branch audit immediately found that the finite weighted identity and strict three-point witness were already formally proved in `GppVerify/RiemannHypothesis/FiniteFisherVandermondeIdentity.lean`, with countable nonnegativity already in `CountableFisherNonnegativity.lean`. This file is therefore a rediscovery/provenance note, not a claim of novelty. The genuinely open extension here is the quadratically confined `(beta,eta)` number gas for all real `beta`, `eta>0`, including countable differentiation/Hessian identification and strictness in that family.

For any real random variable `X` with finite fourth moment, let

\[
g=\operatorname{Cov}(X,X^2)
 =\begin{pmatrix}
 \operatorname{Var}(X) & \operatorname{Cov}(X,X^2)\\
 \operatorname{Cov}(X,X^2) & \operatorname{Var}(X^2)
 \end{pmatrix}.
\]

Let `X_1,X_2,X_3` be iid copies of `X`. Then

\[
\det g
=\frac16\,\mathbb E\!\left[
 (X_1-X_2)^2 (X_2-X_3)^2 (X_3-X_1)^2
\right].
\]

Equivalently, with

\[
V(X_1,X_2,X_3)
=\det\begin{pmatrix}
1 & X_1 & X_1^2\\
1 & X_2 & X_2^2\\
1 & X_3 & X_3^2
\end{pmatrix}
=(X_1-X_2)(X_2-X_3)(X_3-X_1),
\]

one has `3! det Cov(X,X^2)=E[V^2]`.

For the quadratically confined number gas

\[
p_n(\beta,\eta)=Z(\beta,\eta)^{-1}
\exp[-\beta\log n-\eta(\log n)^2],\qquad \eta>0,
\]

the three states `n=1,2,3` give the explicit positive witness

\[
\det g\ge
p_1p_2p_3
\,(\log2)^2(\log3-\log2)^2(\log3)^2>0,
\]

provided the covariance moments exist. Thus after the countable derivative/Hessian bridge is proved, strict convexity of `log Z` follows without a delicate determinant-limit argument.

Current target: reuse the already-certified finite Vandermonde theorem rather than reproving it, and formalize the quadratically confined countable summability/differentiation layer for every real `beta`, `eta>0`.
