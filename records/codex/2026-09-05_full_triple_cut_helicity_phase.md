# Codex/GPT rotation record — full triple-cut helicity phase

## Yang–Mills generalized-cut advance

On the certified full nonzero-μ triple-cut conic

\[
u^2+v^2=-r^2,
\qquad
u(z)=ir\frac{1-z^2}{1+z^2},
\qquad
v(z)=\frac{2irz}{1+z^2},
\]

define

\[
c(z)=\frac{1-z^2}{1+z^2},\qquad s(z)=\frac{2z}{1+z^2},\qquad c^2+s^2=1.
\]

The cut direction is exactly a complex transverse rotation of the z=0 meridian point by

\[
R(z)=\begin{pmatrix}c&-s&0\\s&c&0\\0&0&1\end{pmatrix}.
\]

The full-chart helicity frames transform by this rotation times explicit little-group phases:

\[
p_{2,h}(z)=-\frac{z-ih}{z+ih},
\qquad
p_{3,h}(z)=-\frac{z+ih}{z-ih}.
\]

For the extra-scalar transverse residue, with

\[
S_0=\frac{2r^2(1-r^2)}{1+r^2},
\]

the exact full-conic result is

\[
S_{++}(z)=S_{--}(z)=S_0,
\]

\[
S_{+-}(z)=S_0\left(\frac{z-i}{z+i}\right)^2,
\qquad
S_{-+}(z)=S_0\left(\frac{z+i}{z-i}\right)^2.
\]

Thus the mixed-helicity factors are reciprocal and their product is one. The z-dependence in the scalar residue sector is entirely an exact rational transverse-rotation/little-group phase; no new dynamical scalar shape appears along the conic.

Executable audit: `discovery/generalized_cuts/generic_full_chart_helicity_phase_audit.py`.

This remains pre-sewing residue data, not a master-integral coefficient. The next amplitude target is to lift the same covariance to the 3×3 massive-vector residue matrix. The expected consequence to test, not yet promoted as a theorem, is z-invariance of the normalized vector/scalar residue spectrum under the corresponding basis similarity/congruence. After that, form the full vector-minus-extra-scalar state sum and perform the legitimate surviving-coordinate Badger large-parameter/T1,T2,T3 projection.

## Prime-gas curvature state

Verify2 head `74c49bd0dced30a17e257fdea17f86acf94d4131` remains fully certified by cold changed-Lean #904 and Build #2050 for normalized countable Gibbs square positivity. The sole curvature bridge is now the sixth-order exact `tsum` expansion

\[
\langle P(Y)^2\rangle_{\beta,\eta}
=\operatorname{residualSqMoment}(m_2,\ldots,m_6)
=D\det H.
\]

Inspection of `ZetaGibbsCenteredMomentBridge.lean` confirms the existing proof pattern (`Summable`, pointwise polynomial expansion, `tsum_add`, `tsum_mul_left`) is sufficient in principle. The current NumberGibbs API exposes raw moments only through M4, so the practical formal blocker is adding/connecting M5 and M6 or equivalent centered moments and carrying the sixth-order `tsum` bookkeeping. Analytic convergence and square positivity are already certified.

## Other active fronts

Scalar cut → dispersion → raised-box regulator closure remains `J_ε(S,T) → 1/6` with no regression.

No RH promotion: the unresolved arithmetic theorem remains unconditional positivity/complete monotonicity of the global completed prime-plus-Archimedean explicit-formula/Weil object on the correct admissible class.

Continuous spectral/chamber target remains `rho_c-hat(t)=sech^(2c)(t/2)` and `rho_c * rho_d = rho_(c+d)`. The formal blocker remains real-line logistic/logit change of variables plus Fourier uniqueness; no Barnes or unsupported Plancherel axiom is introduced.

No Claude-owned work was inspected.
