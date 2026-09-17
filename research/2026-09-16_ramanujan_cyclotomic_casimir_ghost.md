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

## Discrete finite-energy ghost equation

Let f(z)=sum b_n z^n lie in the Casimir/Bergman space and define

h_j=sum_{n>=j} b_n/[n(n+1)].

Then

<f,F_m>=sum_{j>=1} r_m(j) h_j.

If f is orthogonal to every Ramanujan generator, use

r_m(j)=sum_{d|(m,j)} d mu(m/d)

to obtain

sum_{d|m} d mu(m/d) [sum_{k>=1} h_{dk}]=0,  m>=2.

Möbius inversion gives the exact scale equation

m sum_{k>=1} h_{mk}=h_1,   m>=1.

Moreover

b_n=n(n+1)(h_n-h_{n+1}),

so

||f||_C^2=sum_{n>=1} n(n+1)|h_n-h_{n+1}|^2.

Thus an RH-obstructing ghost is precisely a sequence h_n -> 0 with finite weighted Dirichlet energy, h_1 != 0, and

sum_{k>=1} h_{mk}=h_1/m

for every m.

The elementary Hardy bound is sharp:

|h_1|^2 <= sum n(n+1)|Delta h_n|^2,

with equality only for h_n=h_1/n. The arithmetic multiple-sum constraints are therefore the sole additional obstruction.

## Exact ultraviolet escape identity

Let

A_K=sum_{k<=K} mu(k)/k,

a_K(r)=sum_{k|r,k<=K} mu(k).

For a ghost with H_m=sum_j h_{mj}=h_1/m,

sum_{k<=K} mu(k) H_{nk}
=(h_1/n) A_K
=h_n + sum_{r>K} a_K(r) h_{nr}.

Since A_K -> 0 by the prime number theorem, any nonzero ghost must be carried entirely by the r>K tail. After centering a_K by its periodic mean A_K, the statement becomes an explicit no-ultraviolet-escape problem for the Casimir Dirichlet energy. This is the discrete version of the previously identified Nyman ghost / Gamma high-frequency escape mechanism.

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