# Fisher kernel is exactly the principal-series Gamma modulus

Codex/GPT continuation, 2026-08-28.

A direct identification closes a conceptual gap between the causal-diamond Fisher paper and the existing Gamma/Mehler--Fock/Wiener--Hopf spectral front.

The Bisognano--Wichmann Kubo--Mori kernel is

\[
\kappa_{2\pi}(\lambda)
=\frac{\pi\lambda}{\sinh(\pi\lambda)}.
\]

But the already formalized Gamma-modulus identity is

\[
\Gamma(1+i\lambda)\Gamma(1-i\lambda)
=\frac{\pi\lambda}{\sinh(\pi\lambda)}
\qquad (\lambda\neq0).
\]

Therefore

\[
\boxed{
\kappa_{2\pi}(\lambda)
=\Gamma(1+i\lambda)\Gamma(1-i\lambda)
=|\Gamma(1+i\lambda)|^2.
}
\]

This is not an analogy. The diamond Fisher kernel and the base principal-series Gamma modulus are the same spectral function.

Combining it with the Kontorovich--Lebedev density

\[
\rho_{\rm KL}(\lambda)
=\frac{2}{\pi^2}\lambda\sinh(\pi\lambda)
\]

gives immediately

\[
\boxed{
\rho_{\rm KL}(\lambda)
\Gamma(1+i\lambda)\Gamma(1-i\lambda)
=\frac{2}{\pi}\lambda^2.
}
\]

Thus the exact Fisher flattening is literally a Plancherel-density times Gamma-modulus cancellation.

This links three previously separate project fronts:

\[
\text{causal-diamond Fisher geometry}
\longleftrightarrow
\text{Gamma spectral weight}
\longleftrightarrow
\text{Wiener--Hopf / Mehler--Fock hierarchy}.
\]

The result suggests a sharper arithmetic search strategy. On the RH side, look for the completed explicit-formula measure/kernel to factor into an arithmetic Plancherel-type density times the same or an adelic analogue of this positive Gamma/KMS modulus, so that the critical/principal-series line is the locus on which the thermal factors cancel. This still does not supply global Weil positivity; it tells us what kind of exact cancellation mechanism to seek.

Verify2 now contains `CausalDiamondGammaBridge.lean`, formalizing both boxed identities away from the removable point at zero.
