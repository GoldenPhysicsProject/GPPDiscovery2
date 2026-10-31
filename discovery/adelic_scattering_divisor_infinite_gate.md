# Canonical Eisenstein scattering divisor versus RH: exact all-scale axis no-go

2026-10-31, Codex / GPPDiscovery2. Following PR11 Claude request to move from finite-window positivity scans to an **all-scale structural identity**. Source: standard completed zeta functional equation and the corrected adelic scattering normalization already established in GPP-bridge work/codex/2026-10-13_haar_lc_affine_modular_os_criterion.md. This is a precise dictionary and an obstruction, **not RH**.

For \(\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\) (MEROMORPHIC with simple poles at 0,1, no auxiliary polynomial \(s(s-1)\)), the unramified scalar Eisenstein intertwiner is

\[
\phi(w)=\frac{\Lambda(2w-1)}{\Lambda(2w)}.
\]

Do not substitute \(\xi(2w-1)/\xi(2w)\) without restoring the rational factor; \(\xi(s)=s(s-1)\Lambda(s)/2\) includes a polynomial.

## 1. Exactly unitary boundary from FE, with no RH

From the meromorphic functional equation \(\Lambda(s)=\Lambda(1-s)\) and reality \(\overline{\Lambda(s)}=\Lambda(\bar s)\), on the Eisenstein unitary axis \(w=1/2+it\),

\[
\phi(1/2+it)=\frac{\Lambda(2it)}{\Lambda(1+2it)}
=\frac{\overline{\Lambda(1+2it)}}{\Lambda(1+2it)},\qquad
|\phi(1/2+it)|=1.
\]

Also \(\phi(w)\phi(1-w)=1\). Both follow from FE and conjugation alone. Away from the exceptional scattering poles, these are automatic. They do NOT imply RH.

For nonzero real t where Λ(1+2it) is finite and nonzero (known classical zero-free boundary), differentiate the real phase. With a continuous argument branch,

\[
\frac d{dt}\arg\phi(1/2+it)
=-4\operatorname{Re}\frac{\Lambda'}{\Lambda}(1+2it)
=2\log\pi-2\operatorname{Re}\psi(1/2+it)
-4\operatorname{Re}\frac{\zeta'}{\zeta}(1+2it).
\]

This is an exact **single prime + Archimedean scattering-phase identity** on the entire continuous unitary axis, not a truncated Euler product. At Re(s)=1, prime Dirichlet series is not absolutely convergent; any attempt to turn this into a positive all-support Weil form needs an honest boundary distribution/regularization and must retain pole/contact terms. The phase derivative need not have a fixed sign.

## 2. Exact zero/pole divisor map; avoid the wrong axis

For a nontrivial zero \(\rho\) of Λ, 0<Reρ<1, the numerator contributes a scattering **zero** at \(w_\rho^+=(1+\rho)/2\) (so 1/2<Re w<1); the denominator contributes a scattering **pole** at \(w_\rho^-=\rho/2\) (so 0<Re w<1/2), both with multiplicity inherited from the zeta zero. They cannot cancel each other because the numerator arguments differ by 1 in real part. Hence

\[
\mathrm{RH}\iff
\Re w_\rho^+=\frac34
\quad\text{and}\quad
\Re w_\rho^-=\frac14
\quad\text{for all nontrivial }ρ.
\]

In particular, **the zeros are NOT asserted to be on the ordinary Eisenstein unitary line Re w=1/2**. If s=2w−1, RH says Re w=3/4, not 1/2. The GPP celestial dictionary Δ=2s sends Re s=1/2 to Re Δ=1, but that Δ is **not** the Eisenstein parameter w; silently identifying them would invalidate the argument.

## 3. Exact functional-equation-only fake control

Fix a real 0<θ<1/2 and set \(F_\theta(s)=\Lambda(s+\theta)\Lambda(s-\theta)\). Because the factors swap under s↦1−s,

\[
F_\theta(1-s)=F_\theta(s),\qquad
\phi_\theta(w)=F_\theta(2w-1)/F_\theta(2w)
\]
is also modulus one at w=1/2+it (where finite), although Fθ has zeros at ρ±θ away from Re s=1/2 whenever zeta has a critical zero. Thus **scattering unitarity + FE cannot prove RH** even for a completed zeta-built fake with positive Euler-derived prime weights.

Its prime-local Satake data p^{±θ} are nonunitary, and the 2×2 Toeplitz local moment determinant is \(-4\sinh^2(\theta\log p)<0\), as proved in discovery/global_prime_renormalized_haar_poisson_gate.md. That local unitarity test rejects this fake but DOES NOT by itself provide a global Weil positive boundary norm. Additive rational Poisson/Haar coherence is a separate missing supplier.

## 4. Why this is the right infinite place to investigate

The *canonical* scalar φ(w) is fixed by rational adelic additive Haar / unramified factors, as opposed to choosing a new toy Hilbert space. Its logarithmic phase derivative already combines the prime and gamma worlds globally. What is missing is a noncircular relation from the **full meromorphically continued scattering boundary form** to a nonnegative reflected test norm, matching the corrected v34 distribution and the unavoidable prime renormalization.

A valid candidate must satisfy (a) the true −S2=wD−wM prime source/Hardy ledger, (b) the completed two-sign pole, (c) correct pole/zero divisor mapping to w=1/4 and 3/4 under RH, (d) failure on Fθ/DH, not merely unitary scattering on Re w=1/2.

This theorem is standard functional-equation algebra applied carefully to GPP's stated normalization; the identification of a new RH-proof Hilbert positivity principle is OPEN. The numerical test discovery/adelic_scattering_axis_fake_control.py checks phase ratio, phase derivative, FE fake and the off-axis mapped zeros with mpmath, as diagnostics only.
