# A Sobolev completion with polynomial scale growth: exact construction and its missing complex zeros

Date: 2026-09-29, America/Toronto.
Status: exact elementary functional analysis; explicit failed RH closure. No RH proof and no Lean certification.

Daniel asked us to attempt the missing arithmetic growth theorem, not merely restate it. This note constructs a concrete domain with the desired growth bound, identifies exactly which zeros it retains, and proves that it cannot retain off-line zeros. A companion note computes the arithmetic BPY graph defect directly.

## 1. Provenance and scope

Live Discovery2 workbench read: be2cc539e89c84d93f51616514b74d4f92a9f842. Independent working branch starts at 5cc33a940105e54c32507ddb69c1c0a2aeefdeaa. Bridge bootstrap was read at main; the inspected main head was ba7d2091cc8a12ca10c9d0394d8668b5650c3314. GPPVerify/main was 1c703dff212a0809dc31952df5d96161aaf5346a; no new CI result is asserted.

Read supplied v34's periodization nonclosability and Nyman--Burnol sections, the three supplied celestial thermal/spectral/block papers, and the latest BPY connected-synthesis, first-chaos coercivity, TFD whitening, survival-amplitude, and graph notes. No external mathematical search or zero list was used.

The v34 obstruction says a weighted L2 norm does not control a pointwise Fourier trace. Simply completing the graph of a nonclosable trace introduces independent boundary degrees of freedom. The following derivative norm instead makes the real trace genuinely continuous.

## 2. The space and exact scale bound

Fix kappa>0. On H^1(R), use

    ||f||_kappa^2 = integral_R (|f'(lambda)|^2 + kappa^2 |f(lambda)|^2) dlambda.

Let U_t f(lambda)=exp(-it lambda) f(lambda). This is the centered Mellin scale action on the critical-frequency line, in the convention of the preceding zero-survival note.

Since (U_t f)'=exp(-it lambda)(f'-itf),

    ||U_t|| <= 1+|t|/kappa.

Thus this honest trace-retaining completion has two-sided polynomial, hence subexponential, scale growth. The group is strongly continuous by density and the locally uniform bound.

In fact its exact operator norm is

    R_kappa(t) = (sqrt(t^2+4 kappa^2)+|t|)/(2 kappa).

Proof: Fourier transform in lambda turns the squared H^1 norm into the weighted L2 norm with weight kappa^2+x^2. Modulation translates x, so the squared operator norm is the essential supremum of

    [kappa^2+(x-t)^2]/[kappa^2+x^2].

Elementary maximization gives R_kappa(t)^2. Frequency packets near a maximizing point approach the bound. QED.

## 3. A zero-independent multiplier quotient

Let F be a nonzero entire function. Define, from its real restriction alone,

    N_F = closure in H^1 of {F g : g in C_c^infinity(R)},
    X_F = H^1 / N_F.

The product Fg is smooth and compactly supported; no global multiplier bound is needed. The subspace is invariant under U_t in both time directions because multiplication by exp(-it lambda) preserves C_c^infinity. The quotient therefore carries a strongly continuous group V_t satisfying

    ||V_t|| <= R_kappa(t) <= 1+|t|/kappa.

For F(lambda)=xi(1/2+i lambda), this definition uses the completed xi function, not a list of its zeros.

Write Z_R={gamma in R:F(gamma)=0}. Then exactly

    N_F = {f in H^1 : f(gamma)=0 for every gamma in Z_R}.

Proof of the forward inclusion: point evaluation is continuous in one-dimensional H^1, and all Fg vanish at every real zero.

For the reverse inclusion first approximate f by compactly supported H^1 functions without changing its vanishing at the relevant zeros, using smooth cutoff multiplication. There are finitely many zeros on each compact set. Near one zero gamma, f(gamma)=0 gives

    |f(x)|^2 <= |x-gamma| integral_between_gamma_and_x |f'(y)|^2 dy.

Cutting f off on an epsilon-neighborhood of gamma changes its H^1 norm by a quantity tending to zero. In particular the derivative-of-cutoff term is bounded by a constant times the integral of |f'|^2 on a shrinking neighborhood. Repeat at the finitely many zeros. The resulting compactly supported function is supported away from Z_R, where division by F is smooth and locally bounded with its derivative. Approximate the quotient there by compactly supported smooth functions. Multiplication by F returns the required approximation. QED.

Consequently X_F retains exactly the value traces at the real zeros. It is insensitive to their multiplicity at this H^1 regularity: higher jets would require a stronger topology. This is not a claim that the actual zeros are simple.

For each gamma in Z_R the nonzero bounded quotient functional ell_gamma([f])=f(gamma) obeys

    ell_gamma(V_t[f])=exp(-it gamma) ell_gamma([f]).

This supplies an actual polynomial-growth realization for the retained real-zero data. It does not establish that every complex zero is retained.

## 4. Exact trace metric and the TFD matrix

The reproducing kernel for this norm is the one-dimensional massive Green function

    K_kappa(x,y)=exp(-kappa|x-y|)/(2 kappa).

Indeed (-d^2/dx^2+kappa^2)K_kappa(x,y)=delta_y, and integration by parts gives the point-evaluation identity. Hence |f(y)| <= ||f||_kappa/sqrt(2 kappa).

For finitely many distinct real trace points x_1<...<x_m and prescribed values v_j, the minimum interpolation energy is

    min ||f||_kappa^2 = v* K^{-1} v,
    K_ij=K_kappa(x_i,x_j).

This follows by orthogonal projection onto the span of the evaluation kernels. On each interval of length ell the minimizer solves -f''+kappa^2 f=0. For endpoint values a,b its energy is

    kappa coth(kappa ell)(|a|^2+|b|^2)
       -2 kappa csch(kappa ell) Re(conj(a)b).

Thus the interval Dirichlet-to-Neumann matrix is

    D_ell = kappa [[coth(kappa ell), -csch(kappa ell)],
                  [-csch(kappa ell), coth(kappa ell)]].

The two exterior half-lines contribute kappa|v_1|^2+kappa|v_m|^2. Summing the interval matrices and these exterior terms gives exactly K^{-1}, not an approximation.

Put r=exp(-kappa ell), C=r^2/(1-r^2), A=r/(1-r^2). Then

    D_ell = 2 kappa [[C+1/2, -A],[-A,C+1/2]],
    det D_ell = kappa^2,
    eigenvalues = kappa (1-r)/(1+r), kappa (1+r)/(1-r).

This is exactly the vacuum-completed TFD covariance, up to a sign change of one endpoint and the scale 2 kappa. At kappa=1/2 and an interval of length log p, r=p^(-1/2) and C=1/(p-1), recovering the prime-local formula.

Scope: this identifies a universal one-dimensional trace-energy mechanism behind the same TFD matrix. It does NOT identify distances between Riemann-zero frequencies with log p. The kernel calculation applies to arbitrary trace points and therefore cannot by itself select arithmetic zeros.

## 5. Decisive obstruction: complex zeros are invisible

If q is any smooth function nonzero on R, then multiplication by q maps C_c^infinity(R) bijectively to itself. Consequently

    {Fq g:g in C_c^infinity} = {F g:g in C_c^infinity},
    N_(Fq)=N_F,
    X_(Fq)=X_F.

Take the real-even polynomial

    q(z)=[(z-b)^2+a^2][(z+b)^2+a^2],
    0<a<1/2, b>0.

It is strictly positive on R, but has zeros at z=+/-b+/-ia. Under s=1/2+iz these become four off-critical zeros inside 0<Re s<1. Multiplication by q/q(0) preserves evenness, reality on the real axis, the central normalization, and (for xi) entire order one. Yet the quotient, scale group, trace metric and TFD blocks above remain EXACTLY unchanged.

Therefore this completion is intrinsically blind to inserted off-line zeros. A subexponential estimate in it cannot prove RH without a separate theorem identifying the full holomorphic arithmetic quotient with the real-trace quotient. That identification is the missing zero-survival/no-escape step, not an automatic consequence of the bound.

## 6. Why off-real evaluation is not continuous

Even restricting to entire functions with Schwartz real restrictions does not fix this with the same H^1 norm. Let

    f_n(z)=exp(-(z-b)^2) exp(-in(z-b)) / d_n,
    d_n^2=sqrt(pi/2)(n^2+kappa^2+1).

Direct Gaussian integration gives ||f_n||_kappa=1 on R. But at z=b+ia,

    |f_n(b+ia)|=exp(a^2+na)/d_n -> infinity.

Thus off-real evaluation is not bounded in this topology. Reversing the sign of n handles the other half-plane. The same exponential-growth obstruction reappears explicitly in the missing trace.

## 7. Why graph completion alone is not enough

For a single point trace T f=f(x_0) on C_c^infinity inside L2, shrinking bumps with fixed height converge to zero in L2 while keeping Tf fixed. The closure of the graph is the whole product L2 x C. For a discrete lattice of trace points the analogous closure is L2 direct-sum ell2 of the lattice, using finitely many disjoint shrinking bumps and density.

Modulation is unitary on this enlarged product, but the new boundary modes are independent of the bulk and occur at the chosen lattice frequencies. They have not been derived as arithmetic zero modes. The H^1 construction ties the real traces to the bulk; sections 5--6 show precisely what it still fails to tie in.

## 8. Status and next boundary

Proved: a real-trace completion with polynomial scale growth; its exact quotient; its TFD interpolation metric; and its exact blindness to nonreal zero factors.

Not proved: a topology retaining all complex arithmetic zero data while enjoying this bound. The positive result solves the growth problem only after selecting a topology that sees real traces. It cannot be promoted as an RH argument.

Numerical checks in discovery/verify_scale_graph_completions.py verify finite matrix identities and the graph-distance formula in the companion note. They are floating-point controls, not evidence for RH or for completeness of the real-line zero spectrum.
