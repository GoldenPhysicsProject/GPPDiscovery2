# Codex/GPT run: strict covariance and continuous real-c semigroup

Date: 2026-09-07

## Verify2

Previous head `d26284f30196a41b5800e868f20cfdec4203816a` passed full Build #2091. Cold #945 remained in progress in the changed-module compilation and was not treated as a certification pass.

New head `b519913bd0519021c64273f777b6d92017fb9b7e` adds the exact strict bridge

\[
E_{\rm pair}>0,\quad W>0
\quad\Longrightarrow\quad
\operatorname{Cov}_{w,\rm norm}(g,y)>0,
\]

using the already formalized identity `pairwiseAlignmentEnergy = 2 * covarianceNumerator`.

Fresh cold #946 and Build #2092 were triggered on that head.

## Discovery2

Added `discovery/spectral/continuous_gamma_chamber_real_c_semigroup_audit.py` at `db125042bb9ac5a52dc5e346187485af1f5bc8f5`.

It extends the previous integer chamber audit to genuinely noninteger `c,d>0` for

\[
\rho_c(x)=\frac{2^{2c-1}}{\pi\Gamma(2c)}|\Gamma(c+ix)|^2,
\qquad
\widehat\rho_c(t)=\operatorname{sech}^{2c}(t/2),
\]

and numerically audits

\[
\rho_c*\rho_d=\rho_{c+d}.
\]

Independent high-precision execution during the run returned relative errors of order `1e-51` (or exact numerical zero at the working precision) across the chosen noninteger transform and convolution cases.

The heat-time semigroup target remains

\[
\mathbb E e^{-qS_c}=\operatorname{sech}^{2c}(\sqrt q/2),
\qquad
\mathbb E S_c=\frac c4,
\qquad
\operatorname{Var}(S_c)=\frac c{48},
\qquad
S_c+S_d\stackrel d=S_{c+d}.
\]

## Honest boundaries

The executable audit is not the exact analytic proof. Formal promotion still requires the Barnes/Gamma Fourier transform under the repository convention, Fourier/Laplace uniqueness, and the measure-theoretic normalized-Gamma product/Fubini layer.

No Yang--Mills/gravity coefficient was promoted. The missing physical amplitude object remains the factor-preserving opposite crossed full-conic tree with uncut denominator provenance retained through topology subtraction.

No RH promotion: unconditional completed prime-plus-Archimedean Weil positivity remains unresolved.

Prime-gas thermodynamic results are unchanged this run.

No Claude-owned work was inspected.
