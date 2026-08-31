# Codex/GPT rotation: Fisher lower witness, scalar DCT boundary, spectral/source audit

Date: 2026-08-31

## 1. Two-parameter Fisher geometry: finite lower witness

Verify2 now contains the exact finite theorem

`four_point_covariance_det_ge_first_vandermonde`.

For normalized nonnegative weights `p,q,r,s` and support values `x,y,z,w`, the covariance determinant of the sufficient statistics `(X,X^2)` obeys

\[
pqr(x-y)^2(x-z)^2(y-z)^2\le
\det\operatorname{Cov}(X,X^2).
\]

This is immediate from the exact four-point Cauchy--Binet/Vandermonde expansion already formalized, because the other three minors are nonnegative.

This theorem is useful for the countable zeta-Gibbs program because it isolates the shape of the desired quantitative witness: after a valid finite-truncation/countable passage, retaining the states `n=1,2,3`, with `x_n=log n`, yields

\[
\det g\ge p_1p_2p_3\,[\log 2\,\log 3\,\log(3/2)]^2.
\]

For the two-parameter Gibbs weights

\[
p_n=Z(\beta,\eta)^{-1}e^{-\beta\log n-\eta(\log n)^2},
\]

this becomes

\[
\det g\ge
\frac{e^{-\beta\log6-\eta[(\log2)^2+(\log3)^2]}}{Z(\beta,\eta)^3}
[\log2\,\log3\,\log(3/2)]^2>0.
\]

The remaining formal issue is not the finite algebra: it is a countable/truncation theorem that preserves this lower witness while the moment sums converge.

## 2. Scalar raised-box regulator

The focused cut-to-loop paper was re-mined. Its scalar chain remains consistent with the formal target: the celestial cut gives the phase-space Gamma factor, the regulated scalar box gives the exact cut, and fixed-channel dispersion reconstructs the loop. The current Verify2 scalar moment already has the physical nested affine-simplex object, interior pointwise convergence, and one-channel domination.

The analytic DCT proof is complete in the Codex ledger. The only missing result is Lean measure packaging: nested interval `Integrable` certificates, almost-everywhere removal of the simplex boundary faces, and iterated dominated convergence proving

\[
J_\varepsilon(S,T)\to 1/6.
\]

No additional Beta/Gamma calculation is needed.

## 3. Spectral / principal-series source audit

The focused kinematic-block paper confirms the exact cross-front dictionary:

\[
P(\lambda)=\frac{\pi\lambda}{\sinh(\pi\lambda)}
=\Gamma(1+i\lambda)\Gamma(1-i\lambda)
=|\Gamma(2s)|^2,
\qquad s=\frac12+\frac{i\lambda}{2}.
\]

It also identifies the chiral block with a conical Legendre function and the shadow map with the degree symmetry `nu -> -nu-1`, placing the kinematic transform in the Mehler--Fock setting. The same paper explicitly labels the zeta Mellin bridge as a reformulation rather than an RH proof: the archimedean/additive kernel does not by itself supply the missing multiplicative prime interference.

This supports the current formal separation: local principal-series unitarity, completed-zeta response, Gamma/Mehler--Fock weights, and Wiener--Hopf identities are exact; the missing global theorem is still the identification of a prime-plus-archimedean construction with the genuine Weil quadratic form followed by unconditional positivity.

## 4. Yang--Mills / gravity boundary

No numerator was promoted. The scalar regulator theorem remains the immediate analytic predecessor. After it closes, the next honest amplitude object remains a fixed-loop-momentum, nonzero-`mu`, `D_s=4` Yang--Mills tree sewing numerator with correct polarization/state sum, color and normalization. Four-dimensional cut matching alone is insufficient for the rational sector.

## 5. CI state

Verify2 commit `b92d211749010c5889b68e19b0f44e483d4a60fd` was pushed with the finite Fisher lower-witness theorem. Fifteen workflows launched; Build and Gibbs differential thermodynamics were in progress at the last poll. Do not promote to `main` until the full required CI/gate set is terminal green.
