# Archimedean Gamma / Mehler--Fock positive-factor closure

## Exact result

The all-real Wiener--Hopf extension and the base Gamma bridge now combine exactly.  Write

\[
W_{\rm ext}(\lambda)=
\begin{cases}
\dfrac{\pi\lambda}{\sinh(\pi\lambda)},&\lambda\neq0,\\[4pt]
1,&\lambda=0,
\end{cases}
\]

and let

\[
a(\lambda)=\sqrt{W_{\rm ext}(\lambda)}.
\]

The existing Lean results give `a(λ)>0`, `a(λ)^2=W_ext(λ)`, and

\[
\operatorname{Re}\rho_\Gamma(0,\lambda)=\frac{2}{\pi}W_{\rm ext}(\lambda)
\]

for every real \(\lambda\), including the removable origin.  Therefore define

\[
b(\lambda)=\sqrt{\frac{2}{\pi}}\,a(\lambda).
\]

Then, exactly and for all \(\lambda\in\mathbb R\),

\[
b(\lambda)>0,\qquad
b(\lambda)^2=\operatorname{Re}\rho_\Gamma(0,\lambda),\qquad
b(\lambda)\neq0.
\]

This is now formalized in
`GppVerify/CelestialHolography/WienerHopfGammaPositiveFactor.lean`
on `codex/lean-workbench` and explicitly CI-gated by the sech/Wiener--Hopf workflow.

## Interpretation and hard boundary

This closes the positive square-root factorization of the **Archimedean base Gamma / Mehler--Fock spectral weight**.  It is useful because the factor is canonical, strictly positive, all-real, and normalized through the removable \(\lambda=0\) point rather than only away from the origin.

It is not a global arithmetic factorization.  In the explicit-formula normalization currently under audit, the prime sector enters with the opposite overall sign from this positive Archimedean sector.  Consequently one cannot direct-sum the prime-local positive Gram factors with this Gamma factor and call the result Weil positivity.  A genuine zero-independent global bridge still requires a signed/compressed factorization, constraint cancellation, or an equivalent OS/no-ghost mechanism that reproduces the full completed arithmetic kernel.

No RH claim follows from this result alone.

## Adjacent active fronts retained

* Scalar-cut/regulator front: the exact regulated scalar cut and logarithmic \(\mu\to0^+\) asymptotic remain valid; the raised-box Beta majorant is exact.  The missing analytic closure is still nested simplex Fubini/dominated convergence, followed by an honest \(D_s=4\), \(\mu\neq0\) Yang--Mills sewing numerator and generalized cuts.
* Prime-gas thermodynamics: exact cumulant/differential identities remain valid.  One-dimensional Fisher scalar curvature is identically zero, so nontrivial fluctuation geometry must be built from a genuine two-parameter thermodynamic family.
* Chamber/convolution front: the exact chamber coefficients and recurrence remain valid.  The former all-loop rationality extrapolation is retired beyond \(L=2\); the \(L=3\) sector must be treated at the MZV/level-2 period level rather than forced into a rational ansatz.

## Next frontier

1. Promote the Archimedean factor into a global **signed/compressed explicit-formula factorization problem**, retaining the prime-sector sign rather than hiding it.
2. Finish the scalar raised-box nested measure-theoretic closure, then insert the first genuine four-dimensional gauge numerator.
3. Construct a two-parameter prime-gas family and compute its Hessian/Fisher curvature rather than using the trivial one-dimensional metric.
4. Resolve the \(L=3\) chamber convolution analytically in the appropriate MZV basis and formalize only identities that survive exact audit.
