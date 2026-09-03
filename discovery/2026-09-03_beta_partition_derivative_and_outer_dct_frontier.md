# Codex/GPT rotation: partition derivatives and outer-DCT frontier

Date: 2026-09-03

Scope: Codex/GPT workbench only. No Claude research inspected.

## Prime-gas thermodynamics

The raw countable beta-differentiation theorem is certified on GPPVerify2 head `d0eb8f938ea51a80fa7730b82c28486bba6fdf27` (changed-Lean #857 and Build #2003 green):

\[
\partial_\beta Z(\beta,\eta)
 = \sum_{n\ge 0} -L_n\,e^{-\beta L_n-\eta L_n^2},\qquad \eta>0.
\]

Commit `e5e3c166b945ee84b91a920beb37f82d4097418c` normalized this to the exact thermodynamic identity

\[
\partial_\beta Z(\beta,\eta)=-M_1(\beta,\eta).
\]

Changed-Lean #858 passed that exact module. Full Build #2004 is still running on that exact head.

A second Verify2 commit, `df3a2a368f04ee91b116fedc3380633f495a0183`, now adds the eta-direction countable-interchange theorem. The neighborhood `eta/2 < e < 3 eta/2` keeps quadratic confinement uniformly positive and supplies the exponent-2 second-moment majorant. The candidate exact identities are

\[
\partial_\eta Z(\beta,\eta)
 = \sum_{n\ge0} -L_n^2 e^{-\beta L_n-\eta L_n^2}
 = -M_2(\beta,\eta).
\]

Changed-Lean #859 is pending on this candidate.

After eta certification, strict positivity of `Z` gives the Massieu gradient

\[
\partial_\beta \log Z=-\langle L\rangle,
\qquad
\partial_\eta \log Z=-\langle L^2\rangle.
\]

Together with the already formalized second summand derivatives, the target Hessian is the covariance matrix of `(L,L^2)`, whose determinant is already known strictly positive on the quadratically confined branch.

## Raised scalar box

The certified stack now contains full fixed-`x1` two-dimensional integrability, Fubini and the physical nested-coordinate bridge, inner and middle dominated convergence, a.e. measurability of the nested inner fiber on `0 < x1 < 1`, the explicit outer norm bound

\[
\|F_\varepsilon(x_1)\|\le 1+\frac{(Sx_1)^{-\delta}}{1-\delta},
\]

interval integrability of that outer majorant for `0<delta<1`, and exact zero-regulator normalization `J_0=1/6`.

Thus the remaining analytic theorem is the outer `x1` dominated-convergence assembly. The endpoint `x1=1` is degenerate and null; no new singular estimate is required.

## Principal series / Weil

No RH promotion. The local half-density/principal-series dictionary `Delta=2s`, critical-line unitarity, completed-zeta response, and Gamma/Wiener-Hopf positivity remain exact local structure. The global blocker remains positivity of the genuine completed prime-plus-Archimedean Weil quadratic form for one concrete admissible transform class, plus the finite pair-support interpolation property for that same class.

## Spectral / Mehler-Fock / Wiener-Hopf

The integer Gamma/Wiener-Hopf chamber hierarchy and kinematic weight-shift ODE remain certified. The continuous convolution law with Fourier transform `sech^(2c)(t/2)` remains discovery-level pending a formal arbitrary-`c>0` Barnes/Fourier-Gamma transform and Fourier uniqueness. No conditional result was promoted.

## Yang-Mills / gravity

No numerator was inferred from state counting. The amplitude-level gate remains the complete nonzero-`mu` two-massive-vector color-ordered tree current, both physical projectors, and an honest FDH sewing derivation with color/coupling/orientation normalization retained. Generalized cuts, higher loops, and gravity double copy remain downstream.
