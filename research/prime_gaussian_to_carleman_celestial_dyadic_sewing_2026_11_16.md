# From the positive prime Gaussian field to the Carleman principal series: exact dyadic sewing into the celestial thermal weight

**GPPDiscovery2; 2026-11-16.** Source-derived, unconditional mathematical identities and a new-to-this-program cross-comparison. Carleman's Mellin spectral theorem and the gamma duplication product are **classical prior mathematics**, not discoveries of a zeta-zero theorem. The connections to Daniel Toupin's August 2026 spectral paper and the precise UV no-go are the research contribution here. **Nothing in this note proves RH, ARP, OB-6, a full celestial CFT or an identification of the Weil form with a positive physical correlator.**

## 1. Sources and context

- Prior GPPDiscovery2 notes: research/prime_plancherel_OS_wall_2026_11_16.md and research/prime_OS_positive_RG_fixed_point_2026_11_16.md. These derive a positive prime power Gaussian field for sigma>1, a normalizability boundary at critical half density and a positive pole-scaling limit. Both use the actual von Mangoldt coefficients but the scaling limit is also obtained for shifted off-line controls.
- User's original August 2026 TeX sources: Modular_Thermality_of_the_Celestial_Spectral_Weight.tex and Spectral_Weight_from_Principal_Series.tex. Their celestial two-particle phase-space spectral factor on Delta_2=1+i lambda_2 is
  \[
  P(\lambda_2)=|\Gamma(1+i\lambda_2)|^2
               =\frac{\pi\lambda_2}{\sinh(\pi\lambda_2)}.
  \]
  The former also proves its Fourier transform is the logistic density.
- Standard literature: Carleman operator, Mellin spectral multiplier pi/cosh(pi lambda), e.g. Pushnitski–Yafaev, "Diagonalizations of two classes of unbounded Hankel operators" (2013), https://link.springer.com/article/10.1007/s13373-013-0044-0 ; standard beta/gamma integration DLMF 1.14 https://dlmf.nist.gov/1.14 .
- GPPVerify ArithmeticReflectionPositivity.lean / ArchimedeanFloor.lean / ShiftPresentation.lean provide the ACTUAL arithmetic Weil-form coefficients.

## 2. TWO sequential positive RG limits, and their distinct topologies

Let h(s)=-zeta'(s)/zeta(s). At sigma>1 the stationary arithmetic Gaussian covariance is
\[
 C_\sigma(\tau)=h(\sigma+|\tau|)
 =\sum_{n\ge2}\Lambda(n)n^{-\sigma}e^{-|\tau|\log n}.
\]
The positive-time reflected covariance C_sigma(t+u) is an explicit Gram sum. At sigma=1+eps, rescale tau->eps tau and normalize by the positive h(1+eps):
\[
 C_\epsilon^{(1)}(\tau)
  =\frac{h(1+\epsilon(1+|\tau|))}{h(1+\epsilon)}
  \xrightarrow[\epsilon\downarrow0]{}
  \frac1{1+|\tau|}.
\]
This is a positive Gaussian limit and its positive-time reflected kernel is (1+t+u)^(-1).

Now introduce a *separate* large-distance zoom R->infinity with field-strength renormalization R:
\[
 K_R(t,u)=\frac{R}{1+R(t+u)}=\frac1{t+u+R^{-1}}.
\]
For fixed t,u>0, K_R->K_C(t,u)=(t+u)^(-1), the **Carleman kernel**. All K_R are PSD because
\[
 K_R(t,u)=\int_0^\infty e^{-r/R}e^{-rt}e^{-ru}\,dr.
\]
For f∈L²(R_+), these bounded positive quadratic forms increase to the Carleman form:
\[
 \langle f,K_R f\rangle
  =\int_0^\infty e^{-r/R}\left|\int_0^\infty e^{-rt}f(t)dt\right|^2 dr
  \uparrow
  \int_0^\infty\left|\int_0^\infty e^{-rt}f(t)dt\right|^2 dr.
\]
(For complex f use Tonelli on modulus squares and the standard bounded Laplace transform.) Since 0≤K_R≤K_C≤pi I, **K_R converges strongly, not in operator norm**. Indeed the dilation t↦Rt unitarily conjugates K_R to K_1 while leaving K_C invariant, so ||K_C-K_R||=||K_C-K_1|| for every R. More quantitatively, the normalized indicator on (0,1) gives
\[
 \|K_C-K_R\|\ge 3\log(4/3)>0
\]
by conjugated testing (the integral over [0,1]^2 of 1/(t+u)-1/(1+t+u) equals 3 log(4/3)). This avoids a false claim of uniform positivity convergence near the origin.

The Carleman covariance is scale-homogeneous: K_C(at,au)=a^(-1)K_C(t,u), a formal 1d correlator power 2Delta=1, so Delta=1/2. At t=u=0 it is singular and must be handled as a positive-time quadratic form/distribution, not an ordinary stationary Gaussian covariance with finite variance.

## 3. Exact principal-series Mellin diagonalization

Let C:L²(0,infty,dt)->L²(0,infty,dt) be
\[
 (Cf)(t)=\int_0^\infty\frac{f(u)}{t+u}\,du.
\]
Set \(Uf(x)=e^{x/2}f(e^x)\), a unitary map to L²(R,dx). Directly:
\[
 (UCU^{-1}g)(x)
 =\int_\mathbb R\frac{g(y)}{2\cosh((x-y)/2)}\,dy.
\]
The Fourier transform on x (equivalently the unitary Mellin transform on t) makes C multiplication by
\[
 \boxed{c(\lambda)=\int_\mathbb R\frac{e^{-i\lambda x}}{2\cosh(x/2)}\,dx
 =\Gamma(\tfrac12+i\lambda)\Gamma(\tfrac12-i\lambda)
 =\frac{\pi}{\cosh(\pi\lambda)}.}
\]
Thus C is a bounded, injective, positive operator with ||C||=pi, spectrum [0,pi], and **no strictly positive L² coercivity constant** (c(lambda)->0 at infinity). The generalized Mellin eigenfunctions are t^(-1/2+i lambda); precisely the d=1 principal-series line. This is classical Carleman harmonic analysis. The line is selected by a unitary L²(dt) representation, not by the zeros of xi.

## 4. The EXACT gamma duplication bridge to the GPP celestial thermal factor

Toupin's 2d principal-series weight is \(P(\lambda_2)=|\Gamma(1+i\lambda_2)|^2=\pi\lambda_2/\sinh(\pi\lambda_2)\). Under the PROJECT'S proposed weight dictionary Delta_2=2s, the spectral parameters satisfy lambda_2=2lambda_1, not lambda_2=lambda_1. The duplication formula
\[
 \Gamma(1+2i\lambda)
 =\frac{2^{2i\lambda}}{\sqrt\pi}
     \Gamma(\tfrac12+i\lambda)\Gamma(1+i\lambda)
\]
therefore yields
\[
 \boxed{P(2\lambda)=\frac{c(\lambda)}{\pi}\,P(\lambda)
  =\operatorname{sech}(\pi\lambda)P(\lambda).}\tag{A}
\]
This is a POSITIVE SPECTRAL TRANSFER. Since P(lambda)∈(0,1], it implies
\[
 \boxed{0<P(2\lambda)\le c(\lambda)/\pi.}\tag{B}
\]
Define on L²(R,dx) the Fourier multiplier \(\mathcal S\) by
\[
 \widehat{\mathcal Sf}(\lambda)
    =\sqrt{P(\lambda)/\pi}\,\widehat f(\lambda).
\]
It is bounded with ||S||=1/sqrt(pi), and because it commutes with the Carleman convolution C,
\[
 \boxed{\mathcal S C\mathcal S=P(2D),\quad D=-i\,d/dx,}\tag{C}
\]
where P(2D) denotes the multiplier P(2lambda). Hence every finite Gram matrix of the celestial phase-space **weight operator** is positive. If one transports a spectral measure d(lambda_2) through lambda_2=2lambda_1, the Jacobian 2 must be included; (C) is an identity of multipliers with respect to a COMMON d(lambda_1), not a claim that unnormalized physical measures are identical.

CAUTION: Without the factor-of-two physical rescaling, the ratio of weights is P(lambda)/c(lambda)=lambda*coth(pi lambda), which is UNBOUNDED. The physically relevant dimension-doubled dictionary makes the transfer bounded. This normalization point is critical.

## 5. AN EXACT ALL-SCALE SEWING THEOREM WITH AN OPERATOR-NORM ERROR

Repeatedly applying the gamma duplication/hyperbolic double-angle identity gives
\[
 \boxed{P(\lambda)=\prod_{j=1}^\infty \operatorname{sech}\left(\frac{\pi\lambda}{2^j}\right)
       =\prod_{j=1}^\infty\frac{c(\lambda/2^j)}{\pi}.}\tag{D}
\]
Let A_j be the positive selfadjoint Fourier multiplier sech(pi lambda/2^j) on L²(R). Its inverse Fourier kernel is a positive probability density:
\[
 k_j(x)=\frac{2^j}{2\pi}\operatorname{sech}(2^{j-1}x),
 \qquad\int_\mathbb R k_j(x)\,dx=1.
\]
Thus each A_j is simultaneously a Markov convolution operator (nonnegative normalized kernel) AND a positive contraction in the operator order. They commute. Put \(T_N=A_1\cdots A_N\); then \(0\le P(D)\le T_{N+1}\le T_N\le I\). Moreover the convergence is not merely pointwise or strong but IN OPERATOR NORM, with a specific geometric error:
\[
 \boxed{\|T_N-P(D)\|_{\rm op}\le\frac{16}{3e^2}\,4^{-N},\quad N\ge1.}\tag{E}
\]
Proof: use log(cosh x)≤x²/2, hence 0≤1−sech x≤x²/2. For p_N(lambda)=prod_{j≤N}sech(pi lambda/2^j),
\[
 0\le p_N-P\le p_N\sum_{j>N}(1-\sech(\pi\lambda/2^j))
 \le\frac{\pi²\lambda²}{6\,4^N}\sech(\pi|\lambda|/2).
\]
Since sech y≤2e^(-y) and sup_{r≥0} r²e^(-ar)=4/(a²e²),
sup_{lambda} lambda² sech(pi lambda/2)≤32/(pi² e²), yielding (E).

This explicitly sews a 2d celestial thermal weight from infinitely many **positive normalized 1d Carleman factors**, with a proven uniform spectral error. It is a mathematical construction of the WEIGHT, not of an interacting celestial CFT or RH.

An equivalent probabilistic check: sech(pi lambda) is the characteristic function of a hyperbolic-secant random variable Y with density sech(x/2)/(2pi), and Σ_{j≥1}2^(-j)Y_j converges almost surely (independent copies, summable variances) to the logistic distribution with density 1/[4cosh²(x/2)], whose characteristic function is P(lambda). This matches the Fourier pair already in Toupin's August source. These are classical Fourier and probability identities.

## 6. CRITICAL NO-GO: the Weil-form UV symbol cannot be reproduced by a bounded weight isometry

The TRUE source Weil form, for real smooth f supported in fixed I_L=[-L/2,L/2], is
\[
 W(f)=E(f)+C_\infty\|f\|²+2(\int f e^{x/2})(\int f e^{-x/2})
      -2\sum_{\log n<L}v_n A_f(\log n),\quad
 v_n=\Lambda(n)/\sqrt n,
\]
\[
 E(f)=\int_0^\infty\frac{e^{-t/2}}{1-e^{-2t}}\|f-T_tf\|²dt.
\]
The Fourier symbol of the positive archimedean kinetic energy is
\[
 \boxed{a(\lambda)
 =2\sum_{k\ge0}\frac{\lambda²}{(2k+1/2)((2k+1/2)^2+\lambda²)}
 =\Re[\psi(\tfrac14+\tfrac{i\lambda}{2})-\psi(\tfrac14)]\uparrow\infty
 \quad(|\lambda|\to\infty).}\tag{F}
\]
Indeed each summand increases in |lambda| and tends to 2/(2k+1/2), whose sum diverges. Thus on ANY fixed nonempty compact support interval there exist normalized smooth real modulated wave packets f_m=phi(x)cos(mx), with E(f_m)->infinity.

On the other hand the prime term is bounded by \(2V(L)\|f_m\|²\) via translation Cauchy–Schwarz, and the rank-two pole term is bounded by \(2Le^{L/2}\|f_m\|²\) by Cauchy–Schwarz on I_L. Therefore
\[
 \boxed{W(f_m)\to+\infty\quad\text{with }\sup_m\|f_m\|_{L²}<\infty.}\tag{G}
\]
The celestial spectral weight multiplier P(D) is bounded by 1, and for these highly modulated wave packets its quadratic tends to ZERO, since P(lambda)->0 as |lambda|->infinity:
\[
 \langle f_m,P(D)f_m\rangle\to0.
\]
Therefore NO bounded linear map \(J:L²(I_L)\to L²(\mathbb R)\), or into any Hilbert space carrying a bounded positive covariance operator, can satisfy \(W(f)=\langle Jf,P(D)Jf\rangle\) for all smooth supported f: the RHS is uniformly bounded on bounded L² sets, but W is not.

This is a rigorous **domain/ultraviolet obstruction to naive identification**, NOT a negative statement about RH. A compatible map would need an UNBOUNDED energy-domain operator (or unbounded completed covariance), and must reproduce prime+gamma+pole arithmetic. The correct form domain is logarithmically stronger than L², consistent with a(lambda)~log|lambda|. Matching just the Mellin labels and spectral phase-space weights is insufficient.

## 7. Shifted F_theta control and exact remaining problem

The earlier shifted model a_theta(n)=Lambda(n)cosh(theta log n) has the SAME normalized prime RG pole fixed point (only its rightmost pole shifts), hence the SAME long-distance Carleman operator and every factor of the SAME dyadic P-weight ladder. Yet its completed zeros may be displaced off the critical line. Thus the entire positive universal construction (sections 2–5) is **NOT RH-DISCRIMINATORY**. It proves a real shared kinematic/scale structure and pinpoints that Euler-product-sensitive, gamma/pole-completed data must supply the missing independent positivity.

GPPVerify's source exact Weil regrouping already yields the genuine remaining condition OB-6: positivity of B_N(f)−||C_N f||² / contractivity of C_N in the B_N seminorm for every support width L. The universal Carleman/P operator does NOT establish that contractivity.

The mathematically actionable new target is: construct an **unbounded, form-domain** intertwiner carrying the actual completed arithmetic Weil form into a positive Hilbert form, with an independent justification of its sign and an explicit failure of the F_theta off-line control. Do not replace that goal with the already-proved universal dyadic positivity.

## 8. Reproducibility and Lean formalization targets

- High-precision script: experiments/abel_prime_common_map/verify_carleman_celestial_scale_ladder.py (Mellin beta integral, gamma modulus, duplication, product to 60 scales, logistic Fourier pair, contractivity).
- UV mismatch script: experiments/abel_prime_common_map/verify_weil_vs_celestial_uv.py (symbol a from digamma, P decay on Gaussian modulations; numerical illustration only).
- Upstreamable Lean: (i) Hilbert-space Laplace Gram; (ii) Carleman Mellin beta integral; (iii) Fourier of sech; (iv) generic strongly-monotone positive bounded operator convergence versus nonconvergence in norm; (v) 1−sech x≤x²/2 and the explicit dyadic O(4^-N) bound; (vi) gamma duplication gives P(2λ)=P(λ)sech(pi λ); (vii) general unbounded-form/no-bounded-representation lemma. Verify Lean source under GppVerify/ only after independent mathematical audit.

**Conclusions:** There IS a fully explicit positive-scale → Carleman → principal-series → celestial thermal-weight ladder. Its spectral completion is fast and controlled. There is ALSO a rigorous mismatch with the full Weil energy, so this is not the missing ARP/RH proof and cannot be promoted into one by identification of conformal labels.
