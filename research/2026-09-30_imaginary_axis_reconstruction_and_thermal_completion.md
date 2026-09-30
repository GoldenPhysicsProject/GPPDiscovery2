# Reconstructed imaginary-axis argument: one arithmetic Gaussian orbit suffices

Date: 2026-09-30. Author: Codex Work Mode.

Status: rigorous zero retention, exact principal-series Gram kernel, and a complete conditional imaginary-axis forcing argument. Explicit zero-independent Poisson trial functions have been constructed and tested. The necessary bound for all scale times is not proved; this document is not a proof of RH. No novelty or Lean-certification claim is made.

Daniel asked to recover the interrupted imaginary-axis work and complete the argument, rather than audit manuscripts. The earlier derivation was recovered from Discovery2 commit `902687229c62568782fcd7c7c7d1daa9a8dd7530` and preserved in full. The new result here is that its obstruction to a uniform operator bound does **not** dispose of the construction: one explicitly specified cyclic Gaussian orbit is sufficient. The operator can grow exponentially while that particular orbit has much smaller growth.

## 1. The coordinates and the conclusion we need

Write a nontrivial zero as

\[
\rho=\beta+i\gamma,\qquad z=\rho-\tfrac12,
\qquad \nu=-iz,\qquad \Delta=2\rho.
\]

Then

\[
z\in i\mathbb R
\quad\Longleftrightarrow\quad
\nu\in\mathbb R
\quad\Longleftrightarrow\quad
\beta=\tfrac12
\quad\Longleftrightarrow\quad
\operatorname{Re}\Delta=1.
\]

Thus the imaginary-axis statement is the critical-line statement in the centered coordinate. The calculation below retains the full complex number z. It never replaces a zero by its ordinate before making the spectral argument.

## 2. An arithmetic domain that retains every zero

Use Fourier transformation with kernel exp(-2 pi i u v), and set

\[
\mathcal S_0=\{f\in\mathcal S(\mathbb R): f\text{ even},\ f(0)=\widehat f(0)=0\},
\qquad
k_f(x)=e^{x/2}\sum_{n\ge1}f(ne^x).
\]

Poisson summation gives k_f(x)=k_fhat(-x). Consequently k_f and all its derivatives decay faster than every exponential at both ends. For Re(s)>1, absolute convergence gives

\[
\int_{\mathbb R}k_f(x)e^{(s-1/2)x}\,dx
=\zeta(s)\int_0^\infty f(u)u^{s-1}\,du.
\]

The left side is entire. The right Mellin factor is holomorphic for Re(s)>-2 because f(u)=O(u^2), and its value at s=1 is zero because fhat(0)=0. Continuation therefore establishes the identity throughout the critical strip, with the zeta pole cancelled. Every nontrivial zero annihilates every k_f.

Use the logistic density supplied by the principal-series papers,

\[
p(x)=\frac1{4\cosh^2(x/2)},\qquad
\mathcal H=L^2(\mathbb R,p(x)^{-1}\,dx),\qquad
\mathcal R=\overline{\{k_f:f\in\mathcal S_0\}}^{\mathcal H},\qquad
\mathcal Q=\mathcal H/\mathcal R.
\]

This construction uses the integer lattice and a fixed explicit weight, without any zero list.

For |Re(z)|<1/2, let

\[
\ell_z(h)=\int h(x)e^{zx}\,dx,
\qquad h_z(x)=p(x)e^{\bar z x}.
\]

The logistic bilateral Laplace transform is

\[
M(c):=\int_{\mathbb R}p(x)e^{cx}\,dx
=\int_0^\infty\frac{u^c}{(1+u)^2}\,du
=\Gamma(1+c)\Gamma(1-c)
=\frac{\pi c}{\sin\pi c},\qquad |\operatorname{Re}c|<1,
\]

with M(0)=1. The beta integral proves the formula, including its domain.

For a zero parameter z=rho-1/2, h_z lies in R-perp and is nonzero, so ell_z descends to Q with the exact norm

\[
\boxed{\|\ell_z\|_{\mathcal Q^*}^2=M(2\operatorname{Re}z).}
\]

The unconditional strip 0<beta<1 places **every** nontrivial zero inside this domain, including a hypothetical off-line zero. No zero is discarded in forming this quotient.

Let (V_t[h])(x)=[h(x+t)]. It is well-defined because, with f_t(u)=e^{t/2}f(e^t u), k_f_t(x)=k_f(x+t). It satisfies

\[
\ell_z(V_tq)=e^{-zt}\ell_z(q),\qquad
\|V_t\|\le e^{|t|/2}.
\]

Reflection J[h](x)=[h(-x)] is an isometry, preserves the arithmetic relations by Poisson summation, and obeys JV_tJ=V_-t.

## 3. A single Gaussian couples to every zero

Fix **any** tau>0, without reference to the zeros, and define

\[
g_\tau(x)=\frac1{\sqrt{4\pi\tau}}e^{-x^2/(4\tau)},\qquad
q_\tau=[g_\tau]\in\mathcal Q.
\]

Completing the square gives the entire identity

\[
\boxed{\ell_z(q_\tau)=e^{\tau z^2}\ne0\quad\text{for every }z\in\mathbb C.}
\]

In particular, this one state sees every retained zero. Its evenness gives Jq_tau=q_tau and hence

\[
d_\tau(t):=\|V_tq_\tau\|_{\mathcal Q}=d_\tau(-t).
\]

There is also a genuine cyclicity statement: the translates of g_tau span a dense subspace of H, so the translates of q_tau span a dense subspace of Q. To prove it, suppose h in H is orthogonal to every translated Gaussian. The function

\[
F(x)=\overline{h(x)}p(x)^{-1}e^{-x^2/(4\tau)}
\]

is integrable after multiplication by e^(c x) for every real c, by Cauchy--Schwarz and Gaussian decay. Orthogonality says that its entire bilateral Laplace transform vanishes on the real axis. Analytic continuation and Fourier uniqueness imply F=0 and then h=0. Passing through the quotient proves the second density claim.

This cyclicity does not assert that a bound for this orbit is a uniform operator bound. The constants for different finite combinations of translates can depend on the combination.

### The completed imaginary-axis implication

**Theorem.** Suppose that for every epsilon>0 there is C_(epsilon,tau)<infinity such that

\[
\boxed{d_\tau(t)\le C_{\epsilon,\tau}e^{\epsilon t}\qquad(t\ge0).}\tag{G}
\]

Then every nontrivial zero satisfies Re(rho)=1/2. It suffices to prove the analogous subexponential bound on t=n t_0 for any one fixed t_0>0.

**Proof.** Write z=delta+i gamma for an arbitrary zero parameter. Boundedness of ell_z and the nonzero Gaussian transform imply

\[
d_\tau(t)\ge
\frac{|\ell_z(V_tq_\tau)|}{\|\ell_z\|}
=\frac{\exp\{\tau(\delta^2-\gamma^2)-\delta t\}}
{\sqrt{M(2\delta)}}.
\]

If delta<0, choose epsilon with 0<epsilon<-delta. The displayed lower bound contradicts (G) as t tends to infinity. Thus every zero has delta>=0. The functional equation supplies the reflected zero 1-conjugate(rho), whose centered real part is -delta; applying the same argument gives delta<=0. Therefore delta=0. Alternatively use d_tau(-t)=d_tau(t) in the same lower bound. The proof on integer multiples of t_0 is identical. QED.

This proves the entire implication from the one-orbit estimate to the imaginary-axis conclusion. It does **not** prove estimate (G). The exact remaining mathematical assertion is stated next in terms of actual arithmetic trial functions.

## 4. Constructing the arithmetic approximants

By the quotient definition,

\[
\boxed{
d_\tau(t)=\inf_{f\in\mathcal S_0}
\left(\int_{\mathbb R}\frac{|g_\tau(x+t)-k_f(x)|^2}{p(x)}\,dx\right)^{1/2}.
}\tag{A}
\]

There is no spectral input in this formula. Therefore it would suffice to construct f_(t,epsilon) in S_0 for which the displayed norm is at most C_(epsilon,tau) exp(epsilon t).

The recovered self-dual seed is

\[
\phi(u)=(4\pi^2u^4-6\pi u^2)e^{-\pi u^2}.
\]

It belongs to S_0: if D=u d/du and a(u)=exp(-pi u^2), then phi=D(D+1)a, Fourier transformation sends D to -(D+1), and a is self-dual. Thus phi is self-dual and phi(0)=phihat(0)=0. Its exact completed Mellin identity is

\[
\int k_\phi(x)e^{(s-1/2)x}\,dx=\xi(s).
\]

For finitely many real centers c_j and coefficients a_j, set

\[
f(u)=\sum_j a_j e^{-c_j/2}\phi(e^{-c_j}u).
\]

This is an actual element of S_0, with

\[
k_f(x)=\sum_j a_j k_\phi(x-c_j).
\]

The code `scripts/construct_gaussian_poisson_orbit.py` constructs such coefficients by weighted least squares. It uses tau=0.01 and equally spaced centers from -t-6 to 6, at spacing 1/12. All coefficient vectors are saved, so every trial f can be reconstructed. No zero table is read until **after** every coefficient vector has been constructed.

The exact trial-residual norm is an upper bound in (A). The numbers below are numerical estimates of those norms, not interval-certified upper bounds. Residuals were re-evaluated without refitting on a twice-finer grid using extended precision.

| t | Ambient Gaussian norm | Poisson residual norm, numerical | Finite zero-dual lower norm, numerical |
|---:|---:|---:|---:|
| 0 | 2.828223 | 0.1927910911 | 0.1925683643 |
| 4 | 10.652680 | 0.1926862142 | 0.1925684079 |
| 8 | 77.330112 | 0.1926800920 | 0.1925683673 |
| 12 | 571.209363 | 0.1926812609 | 0.1925684023 |
| 16 | 4220.672699 | 0.1926893143 | 0.1925683749 |
| 20 | 31186.783917 | 0.1930253391 | 0.1925683932 |

The analytic ambient norm used here is

\[
\|g_\tau(\cdot+t)\|_{\mathcal H}^2
=\frac{2+2e^{\tau/2}\cosh t}{\sqrt{8\pi\tau}}.
\]

The finite lower norms use the first 30 positive tabulated ordinates and their negatives only as an independent comparison. For their retained vectors let G_ij=<h_i,h_j> and b_j=ell_j(g_tau(.+t)); then b*G^-1 b is the squared norm of the orthogonal projection onto that finite dual span and is at most d_tau(t)^2, assuming the tabulated points are exact zeros. The numerical table does not independently certify that assumption or its error propagation.

The fitting matrices had numerical condition numbers from 3.09e9 to 3.84e9 after column normalization. This prevents interpreting the computed coefficients as optimally determined. It does not invalidate evaluating a specified finite trial function. The largest discrepancy between the two residual evaluations was 2.55e-11; the largest coefficient magnitude was about 6445. These are finite consistency checks, not a bound uniform in time.

The theta sum was evaluated after using its exact evenness, with n=1,...,5. For |x|<3 the omitted n>=6 tail is below 1e-43 uniformly; for |x|>=3 the seed's decay is below exp(-1200), up to explicit polynomial prefactors. These errors are far smaller than the floating-point cancellation error at the tested coefficients and times. The integration window extends three units beyond all basis centers. Quadrature error was checked by refinement, not rigorously enclosed.

The recorded coarse pilot at spacing 1/4 grew strongly, while refining to 1/12 removed that growth over the tested interval. Thus a coarse finite basis cannot be used to declare failure of the one-state route. Conversely, six successful times do not establish (G).

For an off-line zero at large height, the Gaussian coupling remains mathematically nonzero but has size exp(-tau gamma^2+tau delta^2). Its exponential-in-time effect can take a very long time to dominate. Underflowed numerical coefficients must never be treated as absent zero channels in the proof.

## 5. The principal-series factor is exactly the retained Gram kernel

In the thermal completion, the exact Gram kernel is

\[
K(z,w)=\langle h_z,h_w\rangle=M(z+\bar w)
=\frac{\pi(z+\bar w)}{\sin\pi(z+\bar w)}.
\]

For critical parameters z=i gamma and w=i eta it becomes

\[
\boxed{K(i\gamma,i\eta)=P(\gamma-\eta),\qquad
P(v)=\frac{\pi v}{\sinh\pi v}.}
\]

This gives an explicit use of the thermal and spectral-weight papers in the arithmetic quotient. These are arithmetic log-frequency coordinates. If the celestial convention is lambda=2 gamma, the same formula reads P((lambda-lambda')/2); the factor of two is not silently dropped.

The weight is equivalent to the earlier exponential one:

\[
e^{|x|}\le p(x)^{-1}=e^{|x|}+2+e^{-|x|}\le4e^{|x|}.
\]

It therefore retains the same underlying closed arithmetic relation space, though its exact Gram kernel differs.

### Exact operator growth and why it does not settle the Gaussian orbit

In fact

\[
\boxed{\|V_t\|_{\mathcal Q}=e^{|t|/2}.}
\]

Here is the full lower-bound mechanism, independent of RH. A positive proportion of simple critical zeros is known (Bui--Conrey--Young, Theorem 1.1). Their distinct ordinates have counting function at least c T log T. Pigeonholing yields arbitrarily tight clusters of any fixed finite size.

Identify a dual vector h with F=h/p, giving norm integral |F|^2 p and dual evolution F(x)->F(x-t). Critical zero vectors become exp(-i gamma x). Divided differences from a tight cluster, after removal of the common unit-modulus modulation, converge to each fixed monomial x^j, in both the original and translated weighted norms. The integral formula for divided differences bounds them by |x|^j, so dominated convergence applies. The modulation is only a norm comparison; it is not assumed to preserve the arithmetic subspace.

Polynomials are dense in L2(p dx): orthogonality to all polynomials makes the Laplace transform of F p analytic in |Re c|<1/2 with every derivative at zero equal to zero; Fourier uniqueness then gives F=0. Translation on L2(p dx) has exact norm exp(|t|/2), since |(log p)'|<=1 and its limiting tail ratios reach exp(|t|). Polynomial approximation therefore supplies the matching lower bound on the arithmetic dual. This proves the formula.

The maximizing vectors can change with t and arise from high, increasingly close spectral clusters. This does **not** supply a matching lower bound for the one fixed q_tau. Formula (G) must therefore be investigated directly. No equivalent renorming can make the whole group subexponential, but an operator-wide renorming is stronger than what the imaginary-axis implication needs.

### Finite averaging is explicit, but still not a uniform repair

For dual vectors define B_T(v,w)=(2T)^-1 integral_-T^T <V_s* v,V_s* w> ds. In the F realization its density is

\[
p_T(x)=\frac1{2T}\int_{-T}^T p(x+s)\,ds
=\frac{\sinh T}{2T(\cosh x+\cosh T)},\qquad T>0.
\]

Its Gram kernel is

\[
K_T(z,w)=M(z+\bar w)\,
\frac{\sinh((z+\bar w)T)}{(z+\bar w)T}.
\]

For critical zeros it is P(gamma-eta) sinc((gamma-eta)T). Every fixed finite set of distinct critical values becomes orthonormal as T tends to infinity. Nevertheless, for each finite T the density still has exponential tails, the same polynomial/cluster proof applies, and the full group norm is again exp(|t|/2).

For a hypothetical off-line zero, the diagonal is

\[
K_T(z,z)=M(2\delta)\frac{\sinh(2\delta T)}{2\delta T},
\]

which diverges when delta is nonzero. Thus the infinite-time averaging step cannot be declared finite for every retained zero without an additional argument. The one-Gaussian route avoids requiring that averaging step.

## 6. Both supplied zero datasets were used

| File | Number of rows | Last ordinate |
|---|---:|---:|
| zeta_zeros_100k.txt | 100,001 | 74921.9297939584143077464583248196660 |
| zeros6.txt | 2,001,052 | 1132490.658714411 |

Both lists are strictly increasing. The indices in the first file are sequential. Their shared 100,001 rows differ by at most 2.9931095287836783088299e-9 in decimal arithmetic; they are not simply identical values rounded to the last displayed decimal. The files were used as supplied, without claiming new certification of their ordinates or completeness.

SHA-256:

- zeta_zeros_100k.txt: `a29267118ca0cf08480dfef2f53a86b4e3724d9f632fb23e00d7f1d3a92a5dda`
- zeros6.txt: `2ef7b752c2f17405222e670a61098250c8e4e09047f823f41e2b41a7b378e7c6`

The minimum adjacent gap in the larger file is approximately 0.002958654, between rows 1,115,578 and 1,115,579, at ordinates 663318.508310486 and 663318.511269140. Their thermal two-mode dilation norm at t=log 2 is about 1.2091660644. Small windows with 3, 4, 8 and 12 zeros were also evaluated, with conditions and generalized-eigenvalue residuals recorded. No dense two-million-square matrix was formed.

On that closest pair the norm in the finite averaged metric was approximately 1.05890155 at T=10, 1.00596496 at T=100 and 1.00006317 at T=1000. These finite numbers illustrate the nonuniform averaging mechanism; the exact all-space statement is proved in Section 5.

Files:

- `scripts/check_weighted_poisson_completion.py` and `research/2026-09-30_weighted_poisson_controls.json`: reconstructed prior controls, including Mellin normalization and polynomial translation norms.
- `scripts/check_thermal_zero_completion.py` and `research/2026-09-30_thermal_zero_controls.json`: full-list scans, cross-list comparison, small Gram matrices and thermal identities.
- `scripts/construct_gaussian_poisson_orbit.py` and `research/2026-09-30_gaussian_poisson_orbit_controls.json`: every finite arithmetic trial coefficient and the independently evaluated residuals.

## 7. Relation to the newly supplied manuscripts and current parallel work

The thermal and spectral-weight manuscripts supply the exact logistic/P Fourier pair used here. The kinematic-block paper's first three digamma moments were numerically cross-checked; its proposed third-moment closed form was kept marked numerical/open, as in its final status section. Its phase-space and block interpretation is not needed for the Hilbert-quotient proof.

Versions 26 and 34 of the arithmetic-principal-series program were compared at their framing and heat-regularization sections; v34's detailed regularization section was read. It already gives the nonvanishing factor sec^2(z/2) in the arithmetic heat trace and explicitly leaves positivity of the completed prime--Archimedean form open. The present Gaussian-orbit construction is a different sufficient route inside the Poisson quotient, not a claim that this arithmetic heat positivity has been established.

The ONON manuscript was inspected at its dictionary and spectral-identification passages. Its asserted unitary all-zero identification is not used as a premise. Meyer's primary paper constructs a nuclear Frechet spectral realization; the positive Hilbert dynamics needed here must still be established. The uploaded loop verification script was read, not executed: it concerns the cut/dispersion identities and depends on an additional source directory. None of those loop calculations are premises of (G).

The current bridge ledger also records the other Codex's finite-Haar formalization and CCM neutral Poincare reduction. This turn preserves those records, does not change GPPVerify, and makes no new CI or merge claim.

## 8. The exact remaining completion step

The required estimate is now entirely explicit: construct the S_0 trial functions in (A) with a subexponential residual bound for every time, or on all integer multiples of one fixed positive time. All-zero retention, the nonvanishing coupling of one cyclic state, scale covariance, and the implication to the imaginary axis are proved above.

The computed trial functions demonstrate actual arithmetic cancellation over a substantial finite range. What is missing is a proof controlling the coefficients, approximation error and range for arbitrarily large time. Neither the operator-wide growth obstruction nor finite numerical success decides that assertion. No global positivity, subexponential orbit estimate, or RH proof is claimed.

## Primary references

- Ralf Meyer, *A spectral interpretation for the zeros of the Riemann zeta function*, arXiv:math/0412277v3: https://arxiv.org/abs/math/0412277 .
- H. M. Bui, Brian Conrey, Matthew P. Young, *More than 41% of the zeros of the zeta function are on the critical line*, arXiv:1002.4127v2, Theorem 1.1: https://arxiv.org/abs/1002.4127 . Only positive-density simple critical zeros are used in the cluster argument.
- Daniel Toupin, supplied principal-series, modular-thermality, kinematic-block, and arithmetic-principal-series manuscripts, read from their attached source files.
