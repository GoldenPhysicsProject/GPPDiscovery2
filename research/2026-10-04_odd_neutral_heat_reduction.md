# Odd-core positivity suffices: connecting pole neutralization to Gaussian deflation

Date: 2026-10-04. Author: Codex. Status: analytic reduction with proof below; no RH proof and no Lean certification of the analytic argument.

## Source connections, rather than a new start

Read the live GPPVerify main files RankOneThresholdControls.lean, PrimeEdgeDtn.lean, SchurGapTransfer.lean, ThreadWeilParity/HodgeIndexBoundary.lean, ThreadS/SignatureInertia.lean, and RiemannHypothesis/WeilPositivityCriterion.lean. Read the Discovery2 workbench notes 2026-09-30_neutralization_preserves_zero_signature.md and 2026-09-30_pole_calibrated_neutral_loewner_reduction.md. Read v34's unconditional heat expansion and semigroup-deflation proof (uploaded source lines 3014 onward and 3183 onward).

The source ingredients are already present. This note connects them to the odd-only experiment. It does not claim a new general Weil criterion or priority for a parity restriction.

Important formal boundary: WeilPositivityCriterion.lean proves positivity of arbitrary finite zero-coordinate assignments equivalent to RH. It does not formalize the explicit formula or the density/approximation connecting arithmetic test functions to those assignments. SignatureInertia.lean proves an inertia-count identity, not the needed arithmetic index bound. HodgeIndexBoundary.lean states its primitive-positivity/lower-bound hypotheses explicitly. Do not count any of these hypotheses as discharged.

## 1. Fix the normalization and the test class

For real f in C_c^infinity(R), put

    F(z) = integral f(u) exp(z u) du,
    f_tilde(u) = f(-u),
    Q(f) = sum_rho m_rho F(rho-1/2) F(1/2-rho).

Use the full nontrivial zero multiset, with multiplicity. The sum is absolutely convergent by rapid vertical decay and the standard zero-counting bound. Define the pole form and its removal by

    P(f) = 2 F(1/2) F(-1/2),
    A(f) = Q(f) - P(f).

Through the classical explicit formula, A is the prime-plus-Archimedean core denoted -W_R-W_P in the project. Put c(f)=F(1/2)+F(-1/2), s(f)=F(1/2)-F(-1/2). Then P=(c^2-s^2)/2, exactly the project's rank-two sign convention. A common positive overall normalization changes none of the sign claims.

In this note K(t) is the FULL zero heat sum. The v34 heat trace indexed modulo +/- has K(t)/2. Keep that factor of two when transferring numerical formulas; do not mix the conventions.

The standard explicit formula and admissible holomorphic-strip tests can be found at https://www.aimath.org/WWN/rh/articles/html/75a/ . The steps below spell out the additional parity, pole, and tail arguments instead of inferring them from a finite interpolation slogan.

## 2. An odd, pole-neutral differential range

Write D=d/du, L0=D^2-1/4, T=D L0. If h is real even and compactly supported smooth, f=T h is real odd. Integration by parts gives

    F_f(z) = -z(z^2-1/4) F_h(z).

The overall minus is from the bilateral Laplace convention; it cancels in the quadratic pairing. At z=+/-1/2 the multiplier vanishes, so P(f)=0 and A(f)=Q(f).

At a nontrivial zero, z=rho-1/2 is neither +/-1/2 nor zero. The endpoint exclusion follows from 0<Re(rho)<1; z=0 is excluded by zeta(1/2) != 0 (indeed there are no real nontrivial zeros, by the alternating eta series on 0<s<1). Thus T retains every nontrivial zero channel. It is not merely a pole-killer that loses inconvenient zeros.

## 3. Exact heat identity and signs

Let g_t(u)=(4 pi t)^(-1/2) exp(-u^2/(4t)), with centered transform exp(t z^2). Put alpha_rho=-(rho-1/2)^2. The full heat trace and its odd-neutral version are

    K(t) = sum_rho m_rho exp(-alpha_rho t),
    H(t) = -K'''(t) + (1/2) K''(t) - (1/16) K'(t)
         = sum_rho m_rho w(alpha_rho) exp(-alpha_rho t),
    w(alpha) = alpha(alpha+1/4)^2.

All these series and their derivatives converge locally uniformly for t>0: |Re z|<1/2, Re(alpha)=(Im z)^2-(Re z)^2 tends to infinity with zero height, and N(R)=O(R log R).

For every real polynomial q,

    f_(q,t) = T q(-D^2) g_(t/2)

is real odd, rapidly Gaussian-decaying, and has both pole moments zero. Its quadratic form is exactly

    A(f_(q,t)) = Q(f_(q,t))
               = sum_rho m_rho w(alpha_rho) q(alpha_rho)^2 exp(-alpha_rho t).

One direct sign check is

    [-z(z^2-1/4)] [z(z^2-1/4)]
      = -z^2(z^2-1/4)^2
      = alpha(alpha+1/4)^2.

Equivalently T*=-T, and T*T=-D^2(D^2-1/4)^2. The heat equation D^2 g_t=partial_t g_t gives the displayed third-order time differential. This is a Hermitian Weil form, not the unjustified replacement of a complex square by an absolute square.

## 4. Deflation proof: the odd-neutral class still detects every off-line quartet

Suppose rho0=1/2+delta+i gamma is off line. There are no real nontrivial zeros, so delta*gamma != 0. Its exponent alpha0=a+i b has b != 0. The functional equation and conjugation give the full quartet, or a conjugate pair in the +/- quotient.

There are only finitely many DISTINCT alpha with Re(alpha)<=a. Choose a real polynomial q which vanishes at all of those except alpha0 and conjugate(alpha0), and is nonzero at both retained points. This is achieved by the product of factors for the other real nodes and conjugate pairs; the finite set is conjugation-stable.

The filtered heat sum then has leading term

    2 Re(C exp(-alpha0 t)) + o(exp(-a t)),

where C is a positive multiplicity factor times w(alpha0)q(alpha0)^2 and is NONZERO. The exact factor depends only on whether +/- pairs are counted separately. There is a strictly positive real-part gap to the next surviving exponent. Polynomial growth of q and w plus the zero-counting bound controls the entire remaining tail, not just a finite zero subset: for t>=1, factor out the next exponential rate and sum a Gaussian-damped polynomial majorant.

Since b != 0, choose a sequence t_j -> infinity for which Re(C exp(-i b t_j))=-|C|. Then Q(f_(q,t_j))<0 for all sufficiently large j. These are odd, pole-neutral witnesses. No inverse of A and no +/-2 calibration were used.

The deflation polynomial depends on a hypothetical off-line spectrum. It is a contradiction witness, not an arithmetic construction supplying positivity.

## 5. Compact support is not skipped

The preceding witnesses are derivatives of Gaussians, not compactly supported. Fix one negative witness f=T h, where h=q(-D^2)g_(t/2) is even and Gaussian-decaying. Choose real even smooth cutoffs chi_R equal to one on [-R,R], zero outside [-2R,2R], with their standard derivative bounds. Put

    f_R=T(chi_R h).

Each f_R is real odd, compactly supported, and EXACTLY pole-neutral. Cutting off f directly would not preserve the two moments; cutting off h before applying T does.

For each integer M, the Gaussian tails and integration by parts show

    sup_(|sigma|<=1/2, tau real)
       (1+|tau|)^M |F_(f_R-f)(sigma+i tau)| -> 0.

The same weighted seminorms of F_f and F_fR stay bounded. Cauchy estimates are unnecessary: derivatives of chi_R h converge in every exponentially weighted L1 norm needed for integration by parts. Choose M sufficiently large and use N(R)=O(R log R); the zero sums defining Q(f_R) converge to Q(f) by an absolutely summable majorant. The pole terms vanish throughout. Consequently A(f_R)<0 for some finite R. This supplies the test-space passage missing from finite-coordinate interpolation alone.

## 6. The resulting reduction

The following are equivalent:

1. RH.
2. A(f)>=0 for every real odd f in C_c^infinity(R).
3. A(T h)>=0 for every real even h in C_c^infinity(R).
4. The polynomially filtered odd-neutral heat sum in Section 3 is >=0 for every real q and t>0.

Proof: under RH, Q(f)=sum m |F(i gamma)|^2>=0. For odd real f, F(-1/2)=-F(1/2), hence A(f)=Q(f)+2 F(1/2)^2>=0. Thus 1=>2=>3. The cutoff argument extends 3 to the Gaussian-polynomial tests, giving 3=>4. The deflation proof gives 4=>1.

Therefore the odd core, ON ALL WINDOWS AND THE COMPLETE TEST CLASS, already suffices to force every zero to Re(rho)=1/2. The even inertia and two inverse thresholds are unnecessary for this particular global implication. This connects the existing neutralization and heat proofs rather than proving the arithmetic positivity premise.

This must NOT be mistaken for a finite-matrix implication A_odd>=0 => Q_odd>=0. That implication is false: take A_odd=I and s=(2,0), giving Q_odd=diag(-1,1). The reduction exploits the global arithmetic zero expansion and arbitrary support/resolution, not a rank-one theorem at a single cutoff.

To transfer a hypothetical theorem about every finite CCM odd matrix to item 2, the matrix-to-form identification and an appropriate form-core approximation must also be supplied. Mere L2 density does not justify an unbounded quadratic-form limit. Smooth compactly supported odd tests have rapidly convergent Fourier expansions on an interval with support headroom; their zero extensions and archimedean form bounds are the relevant approximation problem. This note proves the continuum criterion, not that separate implementation bridge.

## 7. What was tried against the remaining sign

The passive decomposition A=L_prime-W_R-2 S I does not by itself yield A_odd>=0: positive L_prime leaves a shifted Archimedean term with uncontrolled sign. Pole neutralization removes P, not the negative prime quadratic contribution. The nonnegative multiplier w on positive real alpha cannot be used before proving alpha real; at an off-line quartet the conjugate weights give the oscillation above. Thus neither termwise passive-network positivity nor a modulus-square substitution closes the sign.

The sharp next task is an arithmetic identity or bound for A(T h) on even h, using the actual joint prime/Archimedean form. Existing local DtN and Schur identities can be reused, but the global identification with a positive form must still be derived. This note does NOT claim that bound, an unconditional principal-series theorem, or a completed RH proof.

## 8. Reproducible control and current numerical evidence

scripts/check_odd_neutral_heat.py uses a SYNTHETIC quartet z=+/-0.2+/-2i and synthetic on-axis pairs +/-ki, k=1,...,100. It uses q(alpha)=1-alpha to deflate the first line pair. At 80 decimal digits and t=13.1595155706969659461281897349, the quartet energy is -6.51323859389980775279969330408e-20 and the positive on-axis sum is 1.79345452457539559549223617212e-20. The total is -4.71978406932441215730745713196e-20. Both pole values and the deflated line value are zero. The quartet identity residual is 1.1429874e-100 and the heat-derivative identity residual is 3.3735033e-80. This control verifies that the proposed restriction does NOT erase an off-line witness; it is not evidence of arithmetic positivity and uses no actual zeta zero table.

The earlier arithmetic lambda=2.5,N=12 run was independently repeated at 80 dps. It reproduced c^T Ae^-1 c+2=-6.5588781348443733142212864032103131e-21, s^T Ao^-1 s-2=-2.5592976171353585589166414543420637e-16, one even negative direction and none odd. Minimum Ao eigenvalue 1.8919221340338387585265959911676546e-13. These are numerical signs, not interval certificates or a uniform theorem.

## 9. Verification and provenance boundary

No new Lean module was added for these analytic claims. The current GPPVerify toolchain was read as leanprover/lean4:v4.33.1. Its Build workflow supports workflow_dispatch and PR builds and explicitly compiles changed modules for PR events. Local Lean/lake executables are absent. Existing finite modules were inspected directly; their current CI state was not inferred from their presence on main.

The continuum reduction is a written mathematical proof based on the classical explicit formula, unconditional zero-counting bound, Gaussian decay, and v34's deflation idea. Formalizing it requires the analytic apparatus which the existing ThreadHT survey marks as APPARATUS, not just the finite pairedForm theorem. This separation is essential for Claude's formalization handoff.
