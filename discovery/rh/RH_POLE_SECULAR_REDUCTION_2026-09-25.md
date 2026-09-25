# RH pole channel secular reduction
Date: 2026-09-25
Status: exact finite-dimensional reduction plus high-precision numerical evidence. No RH proof.

Let Q = W02 - WR - WP and A = -WR - WP. In the CCM Fourier basis n=-N,...,N with L=2 log(lambda),

W02 = (1/2) c c^T - (1/2) s s^T,

with
c_n = 8 sqrt(L) sinh(L/4) L / (L^2 + 16 pi^2 n^2),
s_n = 8 sqrt(L) sinh(L/4) (4 pi n) / (L^2 + 16 pi^2 n^2).

Thus c is even and s is odd. Since A preserves parity,

Q_even = A_even + (1/2) c c^T,
Q_odd  = A_odd  - (1/2) s s^T.

Exact rank-one secular criterion:
1. If A_even is invertible with exactly one negative eigenvalue and all remaining eigenvalues positive, then Q_even is positive definite iff
   c^T A_even^{-1} c < -2.
   Equality gives a zero mode.
2. If A_odd is positive definite, then Q_odd is positive definite iff
   s^T A_odd^{-1} s < 2.
   Equality gives a zero mode.

Proof: matrix determinant lemma / rank-one inertia. Define
F_even(mu)=1+(1/2)c^T(A_even-mu I)^{-1}c.
Between the unique negative eigenvalue of A_even and its first positive eigenvalue, F_even is strictly increasing. Its zero is the lowest eigenvalue of Q_even. Hence that zero is positive iff F_even(0)<0, i.e. c^T A_even^{-1}c<-2.
Similarly
F_odd(mu)=1-(1/2)s^T(A_odd-mu I)^{-1}s
decreases from F_odd(0) to -infinity before the first pole, so the lowest zero is positive iff F_odd(0)>0, i.e. s^T A_odd^{-1}s<2.

High-precision check at lambda=3:
N=2: ce+2=-4.112428581e-9, so-2=-7.837240566e-6
N=3: ce+2=-3.034030226e-11, so-2=-1.653853693e-7
N=4: ce+2=-1.707427024e-13, so-2=-1.435599350e-9
N=5: ce+2=-2.765341458e-15, so-2=-2.326820126e-11
N=6: ce+2=-2.759800568e-17, so-2=-4.154561113e-13

At every checked N, A_even has exactly one negative eigenvalue, A_odd is positive, and both scalar inequalities are on the safe side. The thresholds +/-2 are approached rapidly as N grows.

Interpretation:
The full finite positivity problem has collapsed to:
(A) prove inertia(A_even)=(1 negative, rest positive);
(B) prove A_odd>0;
(C) prove the two scalar boundary-response inequalities above.

The vectors c and s are the even/odd real combinations of the Cauchy evaluation vector at the artificial pole locations z=+/- i L/(4 pi), so the scalar responses should be attacked through the pole-healing / Pick-Weyl machinery rather than entrywise matrix estimates.

This is the current pole-lemma frontier.
