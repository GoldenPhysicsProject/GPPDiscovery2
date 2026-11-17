# Exact Weil box / Suzuki potential, first gamma-rung cancellation and plastic prime-kick dynamics

**GPPDiscovery2, November 16, 2026.** New-to-program cross-checks and exact unconditional identities. **RH remains unproved.** Suzuki's equivalence of full screw-potential nonnegativity and RH is a published theorem (JLMS 108, 2023, Theorem 1.7, https://doi.org/10.1112/jlms.12785), NOT original to GPP. The plastic curvature threshold and prime-power interval methodology have been examined in Mittermeier's 2026 unrefereed certificates. Distinguish source identities, established criteria, and new proposals.

## 1. A ONE-PARAMETER COMPLETE WEIL TEST

For real compactly supported f, denote A_f(t)=integral f(x)f(x-t) dx; set
w(t)=e^(-t/2)/(1-e^(-2t)), v_n=Lambda(n)/sqrt(n),
Cinf=-gamma-log(pi)-pi/2-3log2=digamma(1/4)-log(pi).
GPPVerify source Weil quadratic form:
\[
 W(f)=\int_0^\infty w(t)\|f-T_tf\|^2dt+C_\infty\|f\|^2
    +2\left(\int fe^{x/2}\right)\left(\int fe^{-x/2}\right)
    -2\sum_{n\ge2}v_n A_f(\log n).
\]
Take the box b_L=1_[-L/2,L/2]. Despite endpoint jumps it belongs to the completed *logarithmic* Weil form domain: A_b(t)=(L-|t|)_+, ||b-T_t b||²=2min(t,L), and its gamma energy is finite.

Set C=pi²+8 Catalan. Exponential expansion of w gives
\[
 E_\infty(b_L)=2\int_0^\infty w(t)\min(t,L)dt
  =\frac12\left[C-e^{-L/2}\Phi(e^{-2L},2,1/4)\right].
\]
The box pole is 16(cosh(L/2)-1). Substitute into the full 2023 Suzuki potential
\[
 \Psi_\zeta(L)=4(e^{L/2}+e^{-L/2}-2)
  -\sum_{\log n\le L}v_n(L-\log n)
  +\frac{C_\infty L}{2}
  +\frac14[C-e^{-L/2}\Phi(e^{-2L},2,1/4)].
\]
It follows by EXACT algebra that
\[
 \boxed{W(b_L)=2\Psi_\zeta(L).}\tag{A}
\]
Suzuki Theorem 1.7 then yields
\[
 \boxed{\mathrm{RH}\ \Longleftrightarrow\
          W(1_{[-L/2,L/2]})\ge0\quad\forall L>0.}\tag{B}
\]
This is an exact recognition of his established one-variable criterion, NOT a new proof. It shows a single nested family of triangular autocorrelations already detects every off-line zero.

Do not confuse the 2023 FULL Psi_zeta with the 2025 gamma-free H=-g0. Suzuki *Ramanujan J.* 68 (2025), Corollary 1, separately proves RH iff H(L)>=0 for all sufficiently large L, where H=4(e^{L/2}+e^{-L/2}-2)-sum v_n(L-log n). Our earlier Chebyshev reserve implication invokes THAT gamma-free theorem and is correctly normalized.

## 2. CANCEL THE CONTINUOUS PRIME MEAN AGAINST THE FIRST GAMMA RUNG

Define the true prime atomic measure mu(dt)=sum_{n>=2} v_n delta_(log n)(dt), the continuous PNT reference mu0(dt)=e^{t/2}dt, and signed error measure nu=mu-mu0. These act only on compactly supported autocorrelation tests, so no divergent unrestricted integral is asserted.

For real f, let Y(f)=int int f(x)f(y)e^(-|x-y|/2) dx dy=2int_0^infty e^(-t/2)A_f(t)dt. This is a genuine PSD Yukawa/OU covariance, with Fourier multiplier 1/(lambda²+1/4).

Directly from the two exponential pole factors:
\[
 \mathrm{Pole}(f)-2\int A_f(t)\mu_0(dt)
 =4\int_0^\infty A_f(t)\cosh(t/2)dt
   -2\int_0^\infty A_f(t)e^{t/2}dt=Y(f).
\]
The lowest (k=0) archimedean gamma exponential rung is
\[
 E_0(f)=\int_0^\infty e^{-t/2}\|f-T_tf\|^2dt
       =4\|f\|^2-Y(f).
\]
Therefore
\[
 \boxed{E_0(f)+\mathrm{Pole}(f)-2\int A_f(t)\mu_0(dt)
              =4\|f\|^2.}\tag{C}
\]
The first gamma rung, continuous-prime reference and pole CANCEL EXACTLY, leaving
\[
 \boxed{
 W(f)=(C_\infty+4)\|f\|^2
  +\int_0^\infty \frac{e^{-5t/2}}{1-e^{-2t}}\|f-T_tf\|^2dt
  -2\int_0^\infty A_f(t)\nu(dt).
 }\tag{D}
\]
The middle term is positive; the last is the actual signed arithmetic prime discrepancy. The remaining scalar constant Cinf+4 = -1.37218341922566558... is NEGATIVE: the formula is a sharper reduction, not an unconditional sign theorem.

The signed measure is the weighted Chebyshev error:
\[
 \nu(dt)=e^{-t/2}d[\psi(e^t)-e^t],\quad
 R(x)=\psi(x)-x.
\]
Stieltjes integration by parts for smooth f with A(L)=0 and R(1)=-1 gives
\[
 \int_0^L A_f(t)\nu(dt)
 =\|f\|^2-\int_0^L e^{-t/2}R(e^t)
                [A_f'(t)-A_f(t)/2]dt,
\]
and thus an equivalent completed source identity
\[
 \boxed{W(f)=(C_\infty+2)\|f\|^2+E_{\ge1}(f)
        +2\int_0^L e^{-t/2}R(e^t)[A_f'(t)-A_f(t)/2]dt.}\tag{E}
\]
This precisely connects the completed operator to the Chebyshev/Cesaro memory program. The last integral has NO known unconditional favorable sign.

## 3. PLASTIC CONSTANT: CURVATURE AFTER THE SAME EXACT CANCELLATION

For L>0 away from t=log(p^k), differentiate the full Suzuki potential:
\[
 \boxed{\Psi_\zeta''(t)
 =e^{t/2}+e^{-t/2}-w(t)
 =e^{t/2}-\frac{e^{-5t/2}}{1-e^{-2t}}.}\tag{F}
\]
Distributionally on (0,infty), subtract the prime atomic kicks:
\[
 \Psi_\zeta''(t)=e^{t/2}-\frac{e^{-5t/2}}{1-e^{-2t}}
                -\sum_{n\ge2}v_n\delta(t-\log n).
\]
The smooth curvature changes sign exactly at e^(3t)-e^t-1=0. The unique positive root r=e^t solves
\[
 \boxed{r^3-r-1=0,\quad
 r=1.324717957244746\ldots,\quad\log r=0.281199574322962\ldots}
\]
This is the **plastic constant**. Its analytic origin is the residual gamma ladder competing against the completed pole, not the golden ratio. Since log2>log r, every prime-free gap between consecutive prime powers is STRICTLY CONVEX, with increasing curvature k(t)=e^(t/2)-e^(-5t/2)/(1-e^(-2t)).

## 4. EXACT FINITE-EVENT CONVEX DUALITY AND AN ELEMENTARY INTERVAL CERTIFICATE

Define the smooth universal completed baseline
\[
 F(t)=4(e^{t/2}+e^{-t/2}-2)+C_\infty t/2+E_\infty(b_t)/2.
\]
Then Psi_zeta(t)=F(t)-sum_{log n<=t}v_n(t-log n).
Its first derivative is explicitly ELEMENTARY:
\[
 \boxed{F'(t)=2(e^{t/2}-e^{-t/2})+C_\infty/2
 +\mathrm{arctanh}(e^{-t/2})+\arctan(e^{-t/2}).}\tag{G}
\]
Indeed E_box'(t)/2=int_t^infty w(u)du=atanh(e^-t/2)+atan(e^-t/2).
For consecutive prime powers q_j,q_(j+1) set a=log q_j,b=log q_(j+1),
A_j=sum_{log n<=a}v_n, B_j=sum_{log n<=a}v_n log n.
The exact event formula is
\[
 \Psi_\zeta(t)=F(t)-A_j t+B_j,\qquad t\in[a,b].
\]
Its derivative is strictly increasing, so minimum is at an endpoint or the UNIQUE interior solution F'(t)=A_j. Equivalently, the FULL Suzuki sign condition on this event gap is the ONE-SCALAR inequality
\[
 \boxed{B_j\ge\sup_{t\in[a,b]}[A_jt-F(t)].}\tag{H}
\]
This is a convex-conjugate scalar check with actual prime coefficients, no zeros, and no previous-rung smallest eigenvalue. Requiring it for every event (and the known initial prime-free window) is equivalent to Suzuki's RH criterion, not a proof.

An explicit sufficient error-safe certification avoids even solving the derivative equation. Let y=Psi(a), d=F'(a)-A_j, c=F''(a)>0, h=b-a and u0=clamp(-d/c,0,h). Since F'' increases on the interval,
\[
 \Psi(a+u)\ge y+du+\tfrac12cu^2,\quad0\le u\le h.
\]
Therefore
\[
 \boxed{y+du_0+\tfrac12cu_0^2\ge0
        \ \Longrightarrow\ \Psi(t)\ge0\text{ on }[a,b].}\tag{I}
\]
This is a rigorous FORMULA, not a verified ALL-EVENT condition. It does not pay any tiny eigenvalue. At the first three prime intervals 2-3,3-4,4-5 the high-precision parabola lower bounds are .0337270205775, .0365377733276, .0430342990749, respectively; NUMERICAL checks only and not improvements over existing published interval certificates.

## 5. Independently executed verification and upstream tasks

Reproducible: experiments/abel_prime_common_map/verify_suzuki_box_gamma_rung.py. Run with mpmath 60 digits; independently checked (A), (D) specialized to box, and plastic threshold for L=.12,.3,.69,.7,1,1.4,2.5,5,8, agreement to better than 50 decimal places. Its numerical positivity samples DO NOT imply RH.

Lean units: (1) interval indicator autocorrelation and translation energy; (2) generic source pole/OU/gamma first-rung algebra (C); (3) signed Chebyshev Stieltjes identity (E); (4) plastic polynomial equivalence and strict convexity; (5) prime event kick, convex-conjugate and parabola sufficient test; (6) extend Suzuki's published analytic equivalence to formal objects ONLY when the required explicit-formula theorem is in-tree.

## 6. Exact open obligation

The completed positivity required for RH is now a countable event-by-event SOURCE inequality B_j≥sup(A_jt-F(t)). The prime-event finite data contain real arithmetic information, but no all-event estimate is proved. Neither PNT reference cancellation, gamma-rung removal, convexity, plastic constant nor finite numerics closes this. Preserve the shifted F_theta off-line falsifier.


## 7. STRONGER SPECTRAL COROLLARY: exact 1/4 -> 5/4 digamma shift and fixed negative band

Let D=-i d/dx on the full real line and put
\[
m_{\rm ref}(\lambda)=\Re\psi(5/4+i\lambda/2)-\log\pi,
\]
where psi here is DIGAMMA, not Chebyshev psi. The original gamma+constant multiplier is
\[
m_{\rm arch}(\lambda)
  =\Re\psi(1/4+i\lambda/2)-\log\pi.
\]
The positive Yukawa covariance Y in section 2 has Fourier multiplier
\[
\widehat{e^{-|\cdot|/2}}(\lambda)
  =\frac1{\lambda^2+1/4}
  =\Re\frac{1}{1/4+i\lambda/2}.
\]
Digamma recurrence psi(z+1)=psi(z)+1/z now gives the **exact all-frequency identity**
\[
 \boxed{m_{\rm arch}(\lambda)+\frac1{\lambda^2+1/4}
       =m_{\rm ref}(\lambda).}\tag{R1}
\]
Therefore the exact source completed Weil form is
\[
 \boxed{
 W(f)=\frac1{2\pi}\int_{\mathbb R}m_{\rm ref}(\lambda)
                      |\hat f(\lambda)|^2 d\lambda
   -2\int_0^\infty A_f(t)[\mu(dt)-e^{t/2}dt].
 }\tag{R2}
\]
This is the same first-gamma-rung cancellation (D) in spectral language, and is an **exact source-dependent separation of archimedean geometry from the signed Chebyshev discrepancy**.

More explicitly, define a_k=2k+1/2. The reference multiplier has an elementary positive-gamma representation
\[
 \boxed{m_{\rm ref}(\lambda)
     =C_\infty+4+
         2\sum_{k=1}^\infty
          \frac{\lambda^2}{a_k(a_k^2+\lambda^2)}.}\tag{R3}
\]
Every summand is strictly increasing in |\lambda|>0; their sum diverges as |\lambda|->infty. Since m_ref(0)=Cinf+4=-1.372183419225...<0, **there exists exactly ONE positive frequency lambda_* where m_ref=0.** The 60-digit root is
\[
\boxed{\lambda_*=6.1258715695008534784643951123522789194247560\ldots.}\tag{R4}
\]
Thus m_ref is negative exactly on |\lambda|<lambda_* and positive exactly on |\lambda|>lambda_*. A sign computation at finite precision gives the value; the uniqueness theorem is exact, from (R3).

### A genuinely improved finite-index theorem for the REFERENCE PART ALONE

Fix any R>lambda_* and let m_R=m_ref(R)>0 and m_0=m_ref(0)<0. For f supported on an interval of length L with its first N moments zero, the Fourier low-band concentration estimate from the earlier all-width note gives
\[
 \alpha_N(L,R)=\frac{LR}{\pi}
     \left(\frac{(RL/2)^N}{N!}\right)^2.
\]
Then
\[
 \boxed{\langle f,m_{\rm ref}(D)f\rangle
  \ge[m_R-(m_R+|m_0|)\alpha_N(L,R)]\|f\|^2.}\tag{R5}
\]
Choose N such that alpha_N<=m_R/[2(m_R+|m_0|)]. Such N grows **only O(L+log L)** for any fixed R>lambda_*: Stirling's inequality N!>=(N/e)^N implies alpha_N<=(LR/pi)4^(-N) whenever N>=e R L. The REFERENCE operator's negative index on each support interval is therefore O(L), and its fixed-band geometry is completely controlled without a doubly-exponential eigenvalue penalty.

**DO NOT misstate this as an O(L) index bound for the full Weil form.** The residual signed prime error in (R2) has an exponentially growing worst-case norm bound with L. Its true arithmetic cancellations, which might remove that cost, are precisely the open RH-strength part. The earlier full-Weil all-width finite-index theorem remains valid but has an enormous conservative N(L).

### How this answers the F_theta discrimination question

For shifted nonnegative prime weights \(\Lambda(n)\cosh(\theta\log n)/\sqrt n\), the old superadditivity survived by monotone weighting. The NEW signed discrepancy with respect to the **fixed zeta pole reference** does not:
\[
 (\cosh\theta t)\mu-e^{t/2}dt
 =(\cosh\theta t)(\mu-e^{t/2}dt)
  +(\cosh\theta t-1)e^{t/2}dt.
\]
The second summand is a positive deterministic exponential drift for theta>0, absent at theta=0. Thus this source pairing is NOT generically invariant under the off-critical deformation. However a genuine completed shifted F_theta model also shifts its gamma and pole data, so this observation alone is NOT a completed F_theta positivity falsifier. One must compare ALL local factors, not freeze the zeta gamma/pole silently.

The exact new target is a norm/form bound on the signed **Chebyshev remainder** in (R2) relative to the fixed-band reference operator, taking full shifted gamma/pole controls into account. Only such an arithmetic-specific inequality could turn this reconstruction into RH.


## 8. EXACT CAUSAL LAPLACE TRANSFER OF THE SIGNED PRIME DISCREPANCY

The signed measure nu=mu-e^{t/2}dt is more than an informal remainder. In the half-plane Re z>1/2 its Laplace transform is absolutely meaningful and satisfies
\[
 \boxed{
 \mathcal L\nu(z)
   =\int_{0}^{\infty}e^{-zt}\nu(dt)
   =-\frac{\zeta'}{\zeta}\left(z+\tfrac12\right)
        -\frac1{z-\tfrac12}.}\tag{T1}
\]
The subtraction cancels exactly the simple zeta pole at z=1/2, leaving the finite value
\[
 \boxed{\mathcal L\nu(1/2)=-\gamma,}\tag{T2}
\]
where the value is the CONTINUATION LIMIT, not a claim of absolute convergence at the boundary.

The right side of (T1) has an unambiguous meromorphic continuation. Its right-half-plane poles lie at z=rho-1/2 for nontrivial zeros rho with Re rho>1/2; their residues are -multiplicities. No other pole can cancel those residues. The completed functional equation reflects any off-critical nontrivial zero to another with Re rho>1/2. Therefore
\[
 \boxed{
 \mathrm{RH}\iff\mathcal L\nu(z)\text{ extends holomorphically throughout Re z>0}.}\tag{T3}
\]
This is the usual zero-free-half-plane criterion rewritten as a **causal prime-error transfer function**. It is an EXACT analytic restatement, not a positive Hilbert-space realization nor proof. Poles with Re z>0 would correspond formally to exponentially growing response modes; on RH the only nontrivial spectral singularities lie on the imaginary boundary. A holomorphic half-plane transfer function need not be positive real or a reflection-positive covariance, so this should NOT be conflated with Osterwalder–Schrader or Weil positivity.

For theta>0, the shifted-prime weights can be represented as cosh(theta t) mu. The fixed-zeta-reference discrepancy then decomposes algebraically as cosh(theta t) nu + (cosh(theta t)-1)e^{t/2}dt, which has a new smooth exponential drift. But a full shifted completed F_theta test must shift the archimedean and pole factors as well; freezing them is NOT a valid completed-model comparison.

Numerical regression: experiments/abel_prime_common_map/verify_weil_reference_digamma_transfer.py checks the exact recurrence (R1) to ~60 digits, the reference root to 50 digits, and the limit of the pole-subtracted transform at z=1/2 against -gamma. This is not a zero-location computation.

**Final separation of obligations:** The universal spectral reference has fixed O(1) negative-frequency bandwidth and O(L) negative index on length-L support. All RH sensitivity resides in the signed arithmetic remainder nu and its actual completed action on autocorrelations. Proving its sign relative to the reference, or positivity of every Suzuki prime-event minimum, remains unsolved.


## 9. COMPLETED FINITE CONTINUUM CERTIFICATE: first interval plus 665,134 exact prime-event barriers

The companion note research/suzuki_exact_integer_event_parabola_2026_11_16.md and executables
- experiments/abel_prime_common_map/certify_suzuki_initial_interval.py
- experiments/abel_prime_common_map/certify_suzuki_event_parabola.py
give a fully outward-rational proof of **strict** positivity of the full completed Suzuki potential for *every* real \(0<t\le\log(10^7)\). The initial prime-free interval is certified with the single exact q=3/2 checkpoint; the prime-free event gaps are certified by \(2F''(\log q)\Psi(\log q)-\min(\Psi'(\log q^+),0)^2>0\), using strict integer comparisons at every 665,134 prime-power q≤10^7. This has been independently rerun in the current research session, including all event arithmetic and the initial interval.

THIS IS A FINITE-RANGE NECESSARY CHECK ON THE PUBLISHED SUZUKI RH CRITERION, not a proof of its positivity for arbitrarily large t, not positivity on all Weil test functions, and not more extensive than Mittermeier's 2026 checkpoints extending to 10^10. No Lean compilation was attempted. Do not conflate the 2023 completed Psi with the separate 2025 gamma-free eventual-sign criterion.
