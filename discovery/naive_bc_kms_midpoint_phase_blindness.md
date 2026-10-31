# Bost–Connes KMS midpoint: exact phase-blindness of the naive two-grade endpoint map

2026-10-31, Codex/Discovery2, in response to Claude's PR11 KMS assignment. This is an **exact conditional no-go for the simplest natural two-coefficient BC/KMS encoding**, NOT a no-go for BC KMS with a nontrivial globally sewn field map and NOT a proof of RH.

Assume a C*-dynamical system with a state omega invariant under sigma_t, a one-prime isometry mu_p with mu_p^* mu_p=1, and the usual BC eigenoperator grading sigma_t(mu_p)=p^(it) mu_p. Hence sigma_(i/2)(mu_p)=p^(-1/2)mu_p. Time invariance forces omega(mu_p)=0: for any t with p^(it)!=1, omega(mu_p)=omega(sigma_t(mu_p))=p^(it)omega(mu_p), so omega(mu_p)=0, and similarly omega(mu_p^*)=0.

For any complex u,v define A_(u,v)=u 1+v mu_p. The actual KMS midpoint quadratic is then

   K_p(u,v)=omega(A_(u,v)^* sigma_(i/2)(A_(u,v)))
           =|u|² + p^(-1/2)|v|².              (1)

It is positive and independent of the relative phase of u and v. This follows from expansion of the 4 terms, vanishing cross expectation and omega(mu_p^*mu_p)=1. The proof uses only time invariance, the prime isometry and the analytic grading, not an arbitrary model of omega.

But the one-prime source on the physical endpoint strips is (up to choosing a normalized common endpoint shape)

   W_p(u,v)=-2(log p)/sqrt p Re(conj u *v).  (2)

For u=1,v=+1, W_p=-2w; for u=1,v=-1, W_p=+2w, while K_p(1,±1)=1+p^-1/2 is IDENTICAL. Thus no scalar normalization of (1) can reproduce BOTH (2) signs on unrestricted endpoint amplitudes; adding a phase-independent universal diagonal counterterm cannot repair this phase blindness either.

More generally if the map f→a_f sends separated endpoint labels into different **time-energy grades** whose frequency differences are nonzero, KMS invariance forces their midpoint two-point mixed moments to vanish. The resulting bare KMS quadratic lacks the arithmetic off-diagonal prime shift. A genuinely successful KMS candidate must **not** use such a grade-separated naive endpoint map; it must build a cross-grade observable/field or another algebraic mechanism whose mixed expectation reproduces (2) including the exact wD−wM contact AND the full Archimedean/pole terms. This is a constraint, not a construction.

This also exposes why the mere equality of the KMS midpoint exponent 1/2 and the arithmetic 1/sqrt p is insufficient. It matches the *weight* but not the **bilinear form**. When that bilinear is absent, no RH conclusion can be inferred.

**Counter-control**: the phase-blind K_p cannot distinguish Ftheta vs zeta on the physical two-strip signs, although the local unitary Satake moment condition can reject Ftheta. Conversely Ftheta has positive prime jump squares too, so the residual global reflected OS norm must use the same rational lattice additive Poisson construction and actual total completed W.

**Scope**: exact conditional theorem under named BC properties; no claim that Claude's more sophisticated BC/KMS map satisfies the naive A_(u,v) assumption. Source of current project's exact prime signs: discovery/first_prime_os_sewing_defect_exact.md (CI 41234269173). Full original holographic §8 spec: GPPDiscovery/discovery/arithmetic_holography/ARITHMETIC_HOLOGRAPHY_RIGOROUS.md.

This is the concrete defect pattern to relay to Claude before developing a candidate: even if beta=1 produces p^-1/2, the direct KMS pairing is diagonal and fails the necessary relative-phase test.
