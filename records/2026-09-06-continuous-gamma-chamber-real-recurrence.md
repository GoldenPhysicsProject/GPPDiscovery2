# Continuous Gamma-chamber real recurrence

Codex/GPT research track, 2026-09-06.

For every real `c>0`, use the continuous normalized Gamma chamber

\[
\rho_c(x)=\frac{2^{2c-1}}{\pi\Gamma(2c)}\Gamma(c+ix)\Gamma(c-ix).
\]

The complex Gamma recurrence already formalized in Verify2 gives

\[
\Gamma(c+1+ix)\Gamma(c+1-ix)
=(c^2+x^2)\Gamma(c+ix)\Gamma(c-ix).
\]

Combining this with

\[
\Gamma(2c+2)=(2c+1)(2c)\Gamma(2c)
\]

yields the exact normalized real-parameter recurrence

\[
\boxed{
\rho_{c+1}(x)
=\frac{2(c^2+x^2)}{c(2c+1)}\rho_c(x).
}
\]

The step factor has the exact defect

\[
\frac{2(c^2+x^2)}{c(2c+1)}-1
=\frac{2x^2-c}{c(2c+1)}.
\]

Hence for `c>0` the continuous chamber has a sharp crossing threshold

\[
\boxed{F_c(x)=1\iff 2x^2=c},
\]

with `F_c(x)>1` iff `2x^2>c` and `F_c(x)<1` iff `2x^2<c`.

Under `c=k+1`, this becomes

\[
\frac{2((k+1)^2+x^2)}{(k+1)(2k+3)},
\]

exactly the integer `rhoStepFactor k x` already certified in `SpectralRhoRecurrence.lean`. Thus the certified integer recurrence is literally the lattice restriction of the continuous Gamma-chamber recurrence, not merely an analogous formula.

Executable audit: `discovery/spectral/continuous_gamma_chamber_real_recurrence_audit.py` checks the normalization reduction, threshold identity, and integer restriction symbolically.

Formalization boundary: `gammaPair_add_one` is already Lean-certified for arbitrary real positive parameter. The remaining Lean promotion is the real normalization layer involving `Gamma(2c)` and its two-step recurrence; no Barnes Fourier transform or convolution uniqueness is needed for this recurrence theorem. The stronger convolution law `rho_c * rho_d = rho_(c+d)` still requires the separate arbitrary-real Fourier/heat-mixture bridge.

No relation to the RH sign criterion is asserted here.
