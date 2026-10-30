# Corrected Weil mirror parity = two arithmetic Loewner divided-difference operators

2026-10-30. Exact identity from Toupin v34 one-sided Weil form and the previously verified rank-two displacement structure. New algebraic decomposition and Arb sign test. RH NOT proved.

## 1. Arithmetic sine transform and rank-two displacement

Let L=2log λ, Fourier modes U_m(x)=L^(-1/2)e^(2πimx/L) for integer m, and let Q_mn be the CORRECTED tail-complete prime+Archimedean+pole Weil matrix. Put a_(p,r)=r log p and w_(p,r)=(log p)p^(−r/2). Define the smooth-in-m real odd sine transform

\[
g(z)=\int_0^L \left[2\cosh(y/2)-\frac{e^{y/2}}{2\sinh y}\right]\sin(2\pi zy/L)\,dy
-\sum_{p^r\le e^L}w_{p,r}\sin(2\pi za_{p,r}/L).
\]

The apparent y=0 singularity is removable after multiplying by sin(2πzy/L). Its derivative g'(z) is obtained by differentiating under the integral. For all DISTINCT integer m,n,

\[
\boxed{Q_{mn}=\frac{g(m)-g(n)}{\pi(n-m)}.}
\]

This identity follows by inserting q_mn(y)=[sin(2πmy/L)−sin(2πny/L)]/[π(n−m)] into the exact Weil distribution. The contact and gamma tail have q_mn(0)=0 for m≠n, so they contribute only to the diagonal. Consequently g(−m)=−g(m), and Q commutes with Fourier reversal. This recovers the team's rank-two displacement relation without a zero hypothesis.

## 2. Exact EVEN and ODD Loewner reduction

On a centered 2N+1 mode set, use normalized even basis e0 and (e_m+e_−m)/sqrt2 (m≥1); odd basis (e_m−e_−m)/sqrt2 (m≥1). Set t_m=m²; define H(t)=sqrt(t)g(sqrt(t)) and J(t)=g(sqrt(t))/sqrt(t) (t>0), extending H differentiably to t=0 by H'(0)=g'(0). Let b0=1/sqrt2 and b_m=1 for m≥1. Define the common arithmetic diagonal

\[
\boxed{d_m=Q_{mm}+\frac{g'(m)}{\pi}.}
\]

For all m,n≥0 the EVEN block is exactly

\[
\boxed{
Q^+_{mn}=d_m\delta_{mn}
-\frac2\pi b_m b_n
\begin{cases}
\frac{H(t_m)-H(t_n)}{t_m-t_n},&m\ne n,\\
H'(t_m),&m=n.
\end{cases}
}
\]

For all m,n≥1 the ODD block is exactly

\[
\boxed{
Q^-_{mn}=d_m\delta_{mn}
-\frac{2mn}{\pi}
\begin{cases}
\frac{J(t_m)-J(t_n)}{t_m-t_n},&m\ne n,\\
J'(t_m),&m=n.
\end{cases}
}
\]

The diagonal identities are exact: for m≥1, Q^+_{mm}=Q_{mm}−g(m)/(πm) and Q^-_{mm}=Q_{mm}+g(m)/(πm), while
2H'(m²)=(g(m)/m)+g'(m) and 2m²J'(m²)=g'(m)−g(m)/m. For m=0, b0²=1/2 makes the even formula reproduce Q00 exactly.

Thus the arithmetic mirror sectors are two **rescaled Loewner matrices of functions linked by H(t)=t J(t)** plus the SAME diagonal d. This is a potentially valuable operator-valued Pick/Herglotz formulation of the missing one-sided sign, not yet a positivity proof.

## 3. A crucial falsifier: common diagonal is NOT positive

For λ=5/2, Arb 512-bit exact integrals of the nonsingular g and g' formulas verify the offdiagonal identity at seven mixed-sign index pairs and both parity formulas at three positive-index pairs. The signed common diagonal has certified values

d0=+0.25462863905544636614;
d1=+0.27099289955038953931;
d4=+3.53831423752695641486;
d5=−0.040068512530856487535;
d8=−1.928494844902931409137.

These are strict ball-enclosed signs, not double-precision guesses; d5 error radius ~5.61e−86, d8 error radius ~3.46e−96. Thus a proposed proof that both Loewner pieces are positive **and** d≥0 is flatly impossible in this naive decomposition. Correct positivity must use a signed cancellation between d and the matrix-valued Loewner terms. This also explains why local entrywise and Gershgorin criteria are too crude.

Source GPPDiscovery2 discovery/arb_parity_loewner_decomposition.py; workflow arb-parity-loewner.yml, Actions run 41044462683 SUCCESS.

## 4. Relation to certified near-null direction

At λ=5/2,N=20, an independent 512-bit Arb certificate proves 1.08226835e−23 < λ_min(Q) < 1.08226836e−23. Mirror odd block lower >1e−20, so the minimum is strictly in the EVEN block. Its rational trial packet has >1−3.30e−17 coefficient mass in modes |m|≤10. Thus the immediate target is the *mirror-even H-Loewner matrix plus signed d*, and the low/high Schur coupling in that same parity; odd is exactly decoupled.

## 5. Open all-support tasks

Either show the exact signed Loewner+diagonal combination is PSD for ALL integer modes at every cofinal support without using RH, or construct a source-side boundary factorization that forces it and fails on shifted-zeta Fθ. The operator monotonicity of H or J is not established, and even if it were, signed d means this naive sufficient condition is not enough. Exact finite matrices, rank-two displacement, and small support gamma positivity do not solve RH.
