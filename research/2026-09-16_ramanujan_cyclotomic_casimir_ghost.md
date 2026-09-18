# Ramanujan–cyclotomic diagonalization of the Casimir–Nyman ghost

## Setup

For m>=2 define the centered divisibility observable

c_m(n)=1/m-1_{m|n}.

The reciprocal Nyman source in the Casimir graph is

QF_{1/m}=sum_{n>=1} c_m(n)n^{-1/2} delta_{log n}.

The Casimir Green kernel is

G_C(log i,log j)=exp(-|log i-log j|/2),

so after including the half-density coefficients the source Gram kernel is

1/max(i,j)=min(1/i,1/j).

Equivalently, if A_m(n)=sum_{j<=n}c_m(j)=(n mod m)/m, then

G_{m,k}=sum_{n>=1} A_m(n)A_k(n)/(n(n+1)).

The target correlation is

<delta_0,QF_{1/m}>=(log m)/m.

## Profinite additive characters

The exact Fourier expansion is

c_m(n)=-(1/m) sum_{a=1}^{m-1} exp(2 pi i a n/m).

Grouping characters by exact order gives Ramanujan sums r_d(n):

c_m(n)=-(1/m) sum_{d|m,d>1} r_d(n).

Möbius inversion gives

r_m(n)=-sum_{d|m} mu(m/d) d c_d(n),   m>1.

Thus the reciprocal Nyman source span is exactly the finite Ramanujan-sum span.

Under Haar measure on the profinite integers,

<r_d,r_e>_Haar=delta_{d,e} phi(d).

The arithmetic side is therefore diagonal in exact conductor.

## Von Mangoldt target vector

Since <delta_0,QF_{1/m}>=(log m)/m,

<delta_0,R_d>
 =-sum_{m|d} mu(d/m) log m
 =-Lambda(d),

where R_d is the Casimir source associated with r_d.

Hence in the Ramanujan basis the Nyman target vector is exactly -Lambda(d). In particular it is supported only on prime powers.

For the finite conductor set D_N={2,...,N}, let B_N be the Casimir Gram matrix of the Ramanujan sources and Lambda_N=(Lambda(d))_{d in D_N}. Then

d_N^2=1-Lambda_N^T B_N^{-1} Lambda_N.

This agrees numerically with the reciprocal Nyman projection, e.g. d_8^2 ~= 0.0242445253 and d_20^2 ~= 0.0165382521.

## Prime-power / composite Schur quotient

Partition conductors into prime powers P and non-prime-powers C. Because Lambda vanishes on C,

B=[[B_PP,B_PC],[B_CP,B_CC]]

and

d_N^2
=1-Lambda_P^T (B_PP-B_PC B_CC^{-1} B_CP)^{-1} Lambda_P.

Thus mixed-prime conductors are internal auxiliary states. They do not couple directly to the target; they renormalize the effective prime-power metric by a Schur complement.

## Cyclotomic logarithmic derivative

For the Ramanujan sum r_m,

sum_{n>=1} r_m(n) z^n = - z Phi_m'(z)/Phi_m(z),   |z|<1.

Also

Lambda(m)=log Phi_m(1),   m>1,

because Phi_m(1)=p for m=p^k and 1 otherwise.

Therefore the target is the cyclotomic boundary functional

r_m -> -log Phi_m(1).

## Weighted Bergman realization

For a mean-zero periodic source a_n define cumulative sums

A_n=sum_{j<=n} a_j

and

F_a(z)=sum_{n>=1} A_n z^n.

Then the Casimir norm is

||a||_C^2
=sum_{n>=1}|A_n|^2/(n(n+1))
=(1/pi) int_D |F_a(z)|^2 (1-|z|^2)/|z|^2 dA(z).

Thus the Casimir graph is a weighted Bergman space.

The target is

F_0(z)=z/(1-z),   ||F_0||=1.

For conductor m,

F_m(z)=-[z/(1-z)] Phi_m'(z)/Phi_m(z),

and

<F_0,F_m>=-log Phi_m(1)=-Lambda(m).

Hence RH is equivalent to F_0 belonging to the closure of the span of these cyclotomic logarithmic derivatives in the displayed weighted Bergman norm. Weighted Bergman formulations of Nyman-Beurling are known in the literature; the additional structure here is the Casimir origin of the norm, the Ramanujan exact-conductor diagonalization, and the sparse von-Mangoldt/cyclotomic target vector.

## Discrete finite-energy ghost equation — corrected summation form

Let f(z)=sum b_n z^n lie in the Casimir/Bergman space and define

h_j=sum_{n>=j} b_n/[n(n+1)].

Then

<f,F_m>=sum_{j>=1} r_m(j) h_j.

The tail h_j is well-defined because Cauchy--Schwarz gives absolute convergence of its
defining series.  Moreover

b_n=n(n+1)(h_n-h_{n+1})

and

||f||_C^2=sum_{n>=1} n(n+1)|h_n-h_{n+1}|^2.

Hence

sum_{n>=1}|h_n-h_{n+1}|<infinity

by Cauchy--Schwarz against sum 1/[n(n+1)].  Since h_n->0, summation by parts is legitimate.

For m>1 put

R_m(N)=sum_{j<=N} r_m(j).

Because r_m is periodic with mean zero, R_m is bounded and periodic.  Therefore the exact,
unconditionally convergent ghost equation is

0
=
sum_{j>=1} r_m(j) h_j
=
sum_{n>=1} R_m(n)(h_n-h_{n+1}),

and the last series is absolutely convergent.

Using the divisor formula for r_m,

R_m(N)
=
sum_{d|m} d mu(m/d) floor(N/d)
=
-sum_{d|m} d mu(m/d) {N/d},

where the N term cancels because sum_{d|m}mu(m/d)=0 for m>1.

### Correction of the earlier progression-sum claim

The previous version of this note replaced

sum_j r_m(j)h_j

by

sum_{d|m} d mu(m/d) sum_k h_{dk}

and then Möbius-inverted to obtain
m sum_k h_{mk}=h_1.

That splitting is NOT justified at the zero-mass boundary in general.  The finite
linear combination can converge by cancellation of the mean-zero Ramanujan factor even
when the individual arithmetic-progression sums diverge.  A threshold tail h_n~C/n is
the basic example.

The raw progression equation is therefore retained only under an additional hypothesis
ensuring convergence of every progression sum, for example h in l1.  It is not an
unconditional characterization of the Casimir/Bergman ghost.

For Abel regularization the exact safe identity is

lim_{r up 1}
sum_{d|m} d mu(m/d)
  sum_{k>=1} h_{dk} r^{dk}
=0.

For every fixed r<1 the inner sums converge absolutely; the divisor splitting is then
legitimate.  The limit must be taken only after the divisor combination is formed.

If, in addition, q_n:=n h_n has a limit C and the finite parts

G_d
:=
lim_{r up 1}
[
 d sum_{k>=1} h_{dk} r^{dk}
 + C log(1-r^d)
]

exist, then the Abel identity gives the renormalized Möbius law

sum_{d|m} mu(m/d) G_d = C Lambda(m),   m>1.

Equivalently,

G_m=G_1+C log m.

Thus a nonzero threshold coefficient does not produce the old constant scale law; it
produces a logarithmic anomaly whose Möbius derivative is exactly the von Mangoldt
function.

This correction invalidates any downstream argument that used the raw progression sums
without first proving the required summability or regularization.  In particular, the
previous 'finite-variation/profinite cylinder' and 'massive no-ghost from progression
Cauchy--Schwarz' arguments are conditional on that stronger topology and are not, by
themselves, universal statements about the whole discrete Nyman defect space.

The elementary Hardy bound remains valid:

|h_1|^2 <= sum n(n+1)|Delta h_n|^2,

with equality only for h_n=h_1/n.

The unconditional arithmetic obstruction is therefore the bounded-periodic Ramanujan
summation-by-parts family displayed above.

## Prime-power translation towers

For a prime p,

r_{p^k}(n)=0 unless p^{k-1}|n, and
nr_{p^k}(p^{k-1}j)=p^{k-1} r_p(j).

Consequently the half-density Casimir sources satisfy

R_{p^k}=p^{(k-1)/2} tau_{(k-1)log p} R_p,

where tau shifts logarithmic support to the right. Hence

B_{p^a,p^b}=p^{(a+b-2)/2} C_p((a-b)log p),

with C_p the autocorrelation of one prime seed. After removing the trivial scale factors, each prime-power block is Toeplitz in the exponent. The target coupling remains constant along the tower:

<delta_0,R_{p^k}>=-log p.

## Status

No RH proof is claimed. The main gain is an exact diagonal arithmetic coordinate system in which:

1. profinite Haar orthogonality is diagonal by conductor;
2. the target is the sparse von Mangoldt vector;
3. composite conductors are Schur-complement internal states;
4. the Casimir norm is a weighted Bergman / Brownian energy;
5. the ghost is an explicit finite-energy sequence satisfying scale-invariant multiple-sum equations;
6. prime powers form logarithmic Toeplitz translation towers.

The next target is a coercive/no-escape theorem for the multiple-sum equation in the Casimir Dirichlet energy, or equivalently a contraction estimate for the Schur-reduced prime-power Toeplitz network.