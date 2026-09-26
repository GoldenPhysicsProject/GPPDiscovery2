# One modular seed for zeta, finite-place mass, and the RH boundary

Date: 2026-09-26
Status: exact finite-place operator identities; RH not proved.

Let h_p = l^2(primes) and define
L e_p = (log p)e_p,  delta = exp(-L),  R = delta^(1/2).
Thus delta_p = 1/p and R_p = 1/sqrt(p).

## Exact modular identities

On s = 1/2 + it,
D(s)=exp(-sL)=delta^(1/2) delta^(it)=R exp(-itL).
So the critical Euler amplitude is exactly modular half-density times unitary modular flow.

For Re(s)>1,
zeta(s)=det(I-delta^s)^(-1),
and
-zeta'(s)/zeta(s)=Tr[L delta^s (I-delta^s)^(-1)]
=sum_{p,m>=1}(log p)p^(-ms)
=sum_{n>=2} Lambda(n)n^(-s).

At beta=1 define the Bose covariance
C=delta(I-delta)^(-1)=(exp L-I)^(-1).
Then
C_p=1/(p-1),
mu_p^2=4C_p=4/(p-1).

Hence the previously introduced profinite mass-square operator is exactly
M_f^2 = 4 M_*^2 dGamma(C)
      = 4 M_*^2 sum_p N_p/(p-1).
The one-particle mass is m_f=2M_* C^(1/2).

The old constants are Schatten moments:
C1 = 2 Tr(C^(3/2)) = 2 sum_p (p-1)^(-3/2),
C2 = 4 Tr(C^2) = 4 sum_p (p-1)^(-2).

Since C_p~1/p, C is Hilbert-Schmidt but not trace class. Thus total critical occupation diverges while the quadratic covariance is finite. Also R_p~p^(-1/2), so R is in S_q iff q>2; on the critical line D(1/2+it) is in S_3 but not S_2, matching the previously derived det_3 threshold.

The covariance determines the whole finite Euler dynamics:
L=log(I+C^(-1)),
delta=C(I+C)^(-1),
D(s)=(C(I+C)^(-1))^s.

## Two boundary channels

For x=e^(-sE),
x/(1-x) = x/(1-x^2) + x^2/(1-x^2).
These are the odd- and even-repetition channels.

At real half-density s=1/2, r=e^(-E/2) and
C=r^2/(1-r^2),
A=r/(1-r^2)=sqrt(C(1+C)).
So the primitive m=1 and double m=2 channels seed respectively the anomalous/pairing and normal/occupation covariances of a two-mode TFD state. Higher odd/even repetitions are their trace-controlled descendants.

## Archimedean match

Let E_infty=2 pi lambda and
C_infty=1/(exp(E_infty)-1).
Then
sqrt(C_infty(1+C_infty))=1/(2 sinh(pi lambda)),
hence
P(lambda)=pi lambda/sinh(pi lambda)
         =E_infty sqrt(C_infty(1+C_infty)).
Thus the celestial principal-series spectral weight is modular energy times the same anomalous TFD covariance function.

## Exact RH bridge

For r=sqrt(1+u)>1, the finite-prime part of the shifted RH Stieltjes target is
J_C(r)=Tr[
 log(I+C^(-1))
 ((I+C^(-1))^(r+1/2)-I)^(-1)
].
Therefore
m_*(u)=a_infty(u) - J_C(r)/(2r),
where a_infty is the explicit rational/digamma Archimedean impedance already isolated in the RH program.

So the same positive covariance C that defines the finite-place mass-square operator also determines the finite-place term in the RH-equivalent Stieltjes criterion.

## Remaining theorem

The missing step is still global: construct the Archimedean/rational sewing map, independently of the zeros, so that the Schur-complement Weyl function of the doubled adelic modular standard form is exactly m_*(u) with positive spectral support. That positivity is equivalent to RH.

The finite-place side has now collapsed to one modular seed rather than an ad hoc collection of operators.
