# Orientation boundary anomaly and the discrete Casimir-Dirac bridge

Date: 2026-09-18

Status: exact operator identities plus a new project-internal synthesis. No RH proof is claimed.

## 1. Motivation from Which Way Is Forward v13

The orientation paper has an exact doubled first-order factorization

D_- D_+ = -(Q_K + |q|^2) I_8,

with q=0 giving decoupled four-component incidence equations and q!=0 locking them. Mass is interpreted there as a transverse norm.

The current RH attack independently produced the unilateral discrete Casimir Laplacian

L = 2I - S - S*

on l2(N), with every strictly positive mass killing the dual ghost and only the zero-mass threshold remaining.

The two structures admit an exact common first-order form.

## 2. Massive causal factor

Let S be the unilateral shift, S* S = I and S S* = I - P_0. For 0<r<1 define

A_r = r^{-1/2}(I-rS).

Then

A_r* A_r
= r^{-1}(I-rS*)(I-rS)
= L + m_r^2 I,

where

m_r^2 = r + r^{-1} - 2 = (1-r)^2/r.

The reverse ordering gives

A_r A_r*
= r^{-1}(I-rS)(I-rS*)
= L + m_r^2 I - r P_0.

Therefore

A_r* A_r - A_r A_r* = r P_0.

The entire causal/adjoint asymmetry is a rank-one boundary projection.

## 3. Doubled discrete Dirac operator

Define the self-adjoint doubled first-order operator

D_r = [[0, A_r*], [A_r, 0]].

Then

D_r^2
= diag(A_r* A_r, A_r A_r*)
= diag(L+m_r^2 I, L+m_r^2 I-rP_0).

This is the exact discrete counterpart of a first-order doubled factorization whose square is kinetic plus mass-squared. The two partner sectors agree in the bulk and differ only by the boundary anomaly rP_0.

At r<1, A_r is boundedly invertible:
A_r^{-1} = sqrt(r) sum_{n>=0} r^n S^n,
with exact norm ||A_r^{-1}|| = sqrt(r)/(1-r) = 1/m_r.
Thus positive mass is exactly bounded invertibility/coercivity of the first-order causal factor.

At r->1, m_r->0, A_r->I-S and the inverse becomes unbounded. This is the zero-mass threshold where the RH ghost can escape.

## 4. Golden self-consistent point

The unit-mass condition m_r^2=1 is

(1-r)^2/r = 1,

equivalently

r=(1-r)^2,

so

r=phi^{-2}, 1-r=phi^{-1}.

At this point

||A_r^{-1}||=1.

Thus the golden contraction is the unique causal factor for which the normalized discrete Dirac mass is one and the inverse first-order factor has unit norm.

This is the same r=phi^{-2} independently obtained from:
- the minimal trace-3 hyperbolic SL2(Z) sector;
- the q=5 finite-place shadow kernel;
- the unit-mass Casimir transfer recurrence.

## 5. Orientation reversal = causal/adjoint dualization

On the bilateral spectral variable z=e^{i theta}, the causal symbol is

a_r(z)=r^{-1/2}(1-rz).

Orientation reversal theta -> -theta, equivalently z -> z^{-1}=conj(z) on |z|=1, sends

a_r(z) -> a_r(z^{-1}) = conjugate(a_r(z)),

which is the adjoint first-order factor.

The orientation-even bulk product is

a_r(z^{-1}) a_r(z)
= m_r^2 + 2 - z - z^{-1}.

This realizes, inside the RH operator model, the orientation paper's exact principle that reversal of a one-dimensional unitary character sends it to its dual/adjoint.

## 6. Bulk orientation blindness versus boundary witness

On the bilateral shift U on l2(Z), U*U=UU*=I, hence causal and adjoint orderings coincide:

A_r* A_r = A_r A_r*.

On the unilateral/casual Hardy shift S on l2(N), the compression creates

S*S - SS* = P_0,

and consequently

A_r* A_r - A_r A_r* = rP_0.

Thus orientation order is invisible in the translation-invariant bulk and becomes detectable only after imposing a causal boundary. The boundary vacuum P_0 is the complete witness of the ordering/orientation choice.

This is a precise operator model for the paper's question "Which way is forward?": without a boundary the two factor orderings are equivalent; after causal half-space compression, forward/backward factorization differs by a rank-one boundary index.

## 7. Relation to the RH ghost

Previous results in this research cycle show:
- every m_r^2>0 graph kills the dual Nyman ghost;
- a nonzero obstruction can only be a zero-mass threshold resonance;
- normalized arithmetic decimation drives finite Casimir bulk energy to zero while a hypothetical ghost must retain its boundary charge.

The present factorization explains that geometry: the zero-mass limit destroys bounded invertibility of the causal first-order operator while the rank-one boundary witness survives. Therefore the RH obstruction is naturally interpreted as a boundary/threshold defect of an otherwise orientation-dual bulk factorization.

This is not yet a proof. The required theorem remains: show that the full multiplicative dilation constraints cannot support a nonzero threshold boundary charge.

## 8. Direct relation to the doubled Lorentzian/transverse-mass paper

The structural dictionary is now:

Which Way Is Forward:
  first-order doubled Klein/Clifford maps D_±
  square -> Q_K + |q|^2
  q=0 decouples half-spin sectors
  q!=0 locks them
  mass = transverse norm

RH/Casimir:
  first-order causal factors A_r, A_r*
  square -> L + m_r^2
  m=0 loses coercivity and admits threshold escape
  m>0 locks/inverts the causal channel
  causal vs adjoint order differs only by boundary P_0

This is an exact operator-level correspondence of architecture. No identification of the physical mass |q| with the arithmetic regulator m_r is claimed yet. A genuine unification would require an intertwiner between the finite-dimensional doubled Klein carrier and the Hardy/Casimir boundary representation.

## 9. Next attack

1. Build the quarter-turn on the doubled Hardy carrier:
   J(f,g)=(-g,f), J^2=-I, J^4=I.
2. Compute how J and the sector-swap conjugate D_r, A_r and A_r*.
3. Identify the boundary projection P_0 as the obstruction to exact orientation/deck symmetry after unilateral compression.
4. Combine with multiplicative decimation U_m and the ghost constraints.
5. Seek a theorem that all-m dilation covariance annihilates the surviving P_0 threshold charge.

## 10. Order-four doubled Hardy lift

Define

J = [[0,-I],[I,0]].

Then J^2=-I and J^4=I. Direct block multiplication gives

J D_r J^{-1} = -[[0,A_r],[A_r*,0]].

Therefore J exchanges the causal and adjoint first-order factors up to the central sign. Since

D_r^2 = diag(H_+,H_-),
H_+=A_r*A_r,
H_-=A_rA_r*,

one has

J D_r^2 J^{-1}=diag(H_-,H_+).

The mismatch of the two even sectors is exactly

H_+-H_-=rP_0.

Thus the order-four lift exchanges the two partner sectors and the sole obstruction to their equality after causal compression is the boundary vacuum projection.

## 11. Rapidity parametrization and correction of the finite-place parameter

Important distinction: the local finite-place Poisson radius and the Cayley/impedance contraction are not the same parameter.

Write

a_q = q^{-1/2}.

On the unitary line s=1/2+it, with theta=t log q,

K_{q,1}(s)
= (1-a_q^2)/(1+a_q^2-2a_q cos theta).

Thus a_q is the genuine Poisson radius of the finite-place kernel.

Define the Cayley/impedance contraction

r_q=(1-a_q)/(1+a_q)=(sqrt(q)-1)/(sqrt(q)+1).

Introduce the hyperbolic parameter

kappa_q = artanh(a_q).

Then exactly

a_q = tanh(kappa_q),
r_q = exp(-2 kappa_q),
mu_q = 2 sinh(kappa_q) = 2/sqrt(q-1),

and

mu_q^2=(1-r_q)^2/r_q.

So the earlier use of r_q as the finite-place "contraction" must be read specifically as the Cayley/impedance contraction derived from the finite-place Poisson radius, not as the Poisson radius itself.

At q=5,

a_5=1/sqrt(5),
kappa_5=artanh(1/sqrt(5))=asinh(1/2)=log(phi),
mu_5=1,
r_5=exp(-2 log phi)=phi^{-2}.

This makes the q=5/golden coincidence a single hyperbolic coordinate identity.

## 12. Finite-place extrema recover the modular eigenvalue pair

With a=tanh(kappa),

K_q(theta)
=1/(cosh(2kappa)-sinh(2kappa) cos theta).

Hence

K_q(0)=exp(2kappa)=r_q^{-1},
K_q(pi)=exp(-2kappa)=r_q.

At q=5 this gives

K_5(0)=phi^2,
K_5(pi)=phi^{-2}.

Thus the same q=5 finite-place kernel contains both the expanding and contracting eigenvalues of the minimal trace-3 hyperbolic SL2(Z) sector as its two extremal phase values. In the original spectral variable, the second point is t=pi/log 5.

This is stronger than the previously formalized center identity K_{5,1}(1/2)=phi^2. It should be formalized separately.

## 13. Causal Green kernel and intrinsic stochastic normalization

With r=exp(-2kappa) and mu=2sinh(kappa),

A_kappa = exp(kappa)I-exp(-kappa)S,

A_kappa^{-1}
= exp(-kappa) sum_{n>=0} exp(-2nkappa) S^n.

Multiplying by mu gives

mu A_kappa^{-1}
= sum_{n>=0}(1-r)r^n S^n.

The coefficients form a normalized geometric probability law. Therefore mu A_kappa^{-1} is a one-sided Markov/unital averaging kernel on constants (formally, and boundedly on the Hardy space).

At unit mass mu=1, no external normalization is needed:

A_{log phi}^{-1}
= sum_{n>=0} phi^{-(2n+1)} S^n,

and sum_{n>=0}phi^{-(2n+1)}=1.

Thus q=5 is uniquely the finite place in this family for which the causal inverse itself is already normalized as a Markov/unital kernel. This gives a more intrinsic unit-mass characterization than the earlier unit-variance observation.

## 14. Direct finite-place Poisson factorization

The finite-place kernel itself factors as the modulus square of the normalized outer function

B_a(z)=sqrt(1-a^2)/(1-a z),

namely

K_q(theta)=|B_{a_q}(e^{i theta})|^2.

Equivalently its precision is

K_q^{-1} = (1-a_q^2)^{-1}(I-a_q S)^*(I-a_q S)

at the Toeplitz-symbol level.

The squared Taylor amplitudes of B_a form the local prime Gibbs law

P_q(N=n)=(1-q^{-1})q^{-n}.

Thus the finite-place shadow kernel, the local prime-gas occupation law, and the one-sided Hardy outer factor are three forms of the same local object. The Cayley transform of its radius then produces the golden Casimir transfer parameter at q=5.

## 15. Updated boundary of claim

There are now two exact first-order structures:
- the physical finite-dimensional doubled Klein/Clifford factorization with transverse norm |q|;
- the infinite-dimensional Hardy/Casimir factorization with dimensionless mass mu.

The map mu=2sinh(kappa), a=tanh(kappa), r=e^{-2kappa} is exact internally on the Hardy/local-kernel side, but no theorem yet identifies physical |q| with arithmetic mu. That remains an intertwiner target.

The strongest current project-internal target is to prove that the orientation/deck symmetry of the doubled causal/adjoint system descends to the arithmetic Hardy realization in a way that annihilates the rank-one zero-mass boundary charge. Boundary self-adjointness alone is known to be insufficient.


## 16. Finite shadow endpoint and the boundary-dipole anomaly

The finite prime occupation shift makes the origin of the unilateral boundary anomaly exact.

Let S_N act on e_0,...,e_N by S_N e_j=e_{j+1} for j<N and S_N e_N=0. Let R_N e_j=e_{N-j}. Then

R_N S_N R_N = S_N*,

S_N* S_N = I-P_N,
S_N S_N* = I-P_0,

hence

S_N* S_N - S_N S_N* = P_0-P_N.

For

A_{r,N}=r^{-1/2}(I-rS_N),

one gets

A_{r,N}*A_{r,N}-A_{r,N}A_{r,N}*=r(P_0-P_N).

Moreover R_N(P_0-P_N)R_N=-(P_0-P_N). Thus the finite ordering anomaly is an orientation-odd boundary dipole exchanged by exact occupation reversal.

If x is R_N-even, then |x_0|=|x_N| and the expectation of the anomaly vanishes exactly.

In the strong N->infinity limit on the ordinary unilateral l2 sector, P_N->0 while P_0 remains. The anomaly becomes rP_0. Therefore the half-line rank-one anomaly is precisely the finite shadow dipole after the far/shadow endpoint has escaped to infinity.

This gives an exact operator interpretation of the project's UV/no-escape obstruction: a nonzero zero-mass ghost must carry boundary charge that is balanced only by a non-Hilbert shadow endpoint at infinity.

## 17. Dilation-covariant orientation annihilation theorem

Let P_vac denote the first-coordinate projection on the arithmetic half-line and U_m the decimation operator (U_m q)_k=q_{mk}. For the partner Hamiltonians

H_+=A_r*A_r,
H_-=A_rA_r*,

the boundary anomaly gives

< U_m q,(H_+-H_-)U_m q >
= r <U_m q,P_vac U_m q>
= r |q_m|^2.

Therefore:

If the causal/adjoint orientation quotient identifies the two partner quadratic forms on every arithmetic dilation U_m q, i.e.

< U_m q,H_+U_m q >
=
< U_m q,H_-U_m q >

for every m>=1, then q_m=0 for every m and q=0.

For the dual Nyman ghost q_m=m h_m this annihilates the ghost coefficientwise and avoids all infinite Möbius inversion.

This is a conditional closure theorem. The missing theorem is now extremely specific: derive dilation-covariant deck/orientation invariance from the actual arithmetic completion rather than postulating it.

The structure mirrors the many-body no-go in Which Way Is Forward v13: one global Z2 equality kills only one relative boundary bit; a sufficiently local/covariant quotient is required to remove all relative bits. Here the multiplicative dilation semigroup supplies the family of arithmetic views.

## 18. Total dilation-orbit anomaly

Because each local anomaly is positive,

sum_{m>=1} < U_m q,(H_+-H_-)U_m q >
= r sum_{m>=1}|q_m|^2

whenever either side is finite.

Thus q in l2 is exactly finiteness of the total orientation-boundary anomaly over the full arithmetic dilation orbit. A zero-mass ghost must have infinite total orientation anomaly. This gives a physical/operator interpretation of the known threshold statement q notin l2.

Any independent theorem showing finite total deck/orientation defect for an admissible physical state would therefore eliminate the ghost.

## 19. Divisibility marginals of a hypothetical ghost

Assume the dual ghost multiple sums converge and satisfy

H(m):=sum_{k>=1}h_{mk}=h_1/m.

For a prime p and a>=0, finite subtraction gives the exact p-adic valuation-shell total

sum_{v_p(n)=a} h_n
=H(p^a)-H(p^{a+1})
=h_1(1-p^{-1})p^{-a}.

More generally, for a finite prime set P and exponents a_p>=0, finite inclusion-exclusion gives

Cylinder(P,a)
=
h_1 product_{p in P}(1-p^{-1})p^{-a_p}.

Thus after normalization by h_1, every finite family of p-adic valuations has exactly the product geometric law of Haar measure on the profinite integers.

Equivalently, the local square-root amplitude vector is

Omega_p
=
sqrt(1-p^{-1}) sum_{a>=0}p^{-a/2}|a>,

which is normalized and obeys S_p* Omega_p=p^{-1/2}Omega_p.

Its phase spectral density is precisely the finite-place Poisson/shadow kernel

| sqrt(1-p^{-1})/(1-p^{-1/2}e^{i theta}) |^2
=
K_{p,1}(1/2+i theta/log p).

So any nonzero ghost is forced to carry, in its divisibility marginals, exactly the critical local prime coherent-state statistics.

The all-prime vacuum fidelity is

product_p (1-p^{-1})=0,

and the critical coherent product lies outside the ordinary vacuum Fock sector. This recovers the previously observed critical coherent-state boundary from the dual ghost equations themselves.

## 20. Finite-variation no-ghost corollary

Suppose h_1!=0 and the atomic coefficients h_n define a finite-total-variation complex measure on N, equivalently sum_n |h_n|<infinity.

Normalize by h_1. The cylinder formula above gives the Haar valuation masses. For any fixed integer n, take an increasing family of prime sets P and the exact-valuation cylinder containing n. Its mass equals a finite factor from primes dividing n times

product_{p in P, p not dividing n}(1-p^{-1}),

which tends to zero because the prime harmonic series diverges.

The cylinders decrease to {n}, so continuity from above of a finite complex measure gives measure({n})=0 for every n. Countable additivity then gives total mass zero, contradicting H(1)/h_1=1.

Therefore every nonzero ghost necessarily satisfies

sum_n |h_n|=infinity.

In particular, if q_n=n h_n belongs to l2, then by Cauchy-Schwarz h belongs to l1, so no nonzero ghost exists. This is a new measure-theoretic proof of the l2 no-ghost implication and clarifies why the obstruction must live in the critical non-Fock/infinite-variation sector.


## 21. Cayley boundary generator: the finite-place center as a spectral shift

Let

C = (I+S)(I-S)^{-1}

on the natural domain of the unbounded inverse of I-S. Then

S=(C-I)(C+I)^{-1}.

For any 0<a<1,

I-aS
=
[(C+I)-a(C-I)](C+I)^{-1}
=
(1-a)(C+lambda I)(C+I)^{-1},

where

lambda=(1+a)/(1-a).

For the finite-place Poisson radius a_q=q^{-1/2},

lambda_q=(sqrt(q)+1)/(sqrt(q)-1)=K_{q,1}(1/2).

Thus the principal-series-center value of the local finite-place shadow kernel is exactly the additive spectral shift of the universal Cayley/Nyman boundary generator C. This embeds the independently formalized finite-place kernel directly into the singular boundary operator whose pole is z=1.

In terms of the Casimir rapidity kappa, a=tanh kappa and therefore lambda=e^{2kappa}=r^{-1}.

## 22. Conservative two-channel completion uniquely selects q=5

Consider the two rational transfer functions

alpha_lambda(z)=c(1-z)/(lambda-z),
beta_lambda(z)=c/(lambda-z),

so that

beta_lambda/alpha_lambda=1/(1-z),

the universal Nyman boundary inverse.

Demand the conservative boundary normalization

|alpha_lambda(e^{i theta})|^2+|beta_lambda(e^{i theta})|^2=1

for every theta. Since

|1-e^{i theta}|^2+1=3-2cos theta,

and

|lambda-e^{i theta}|^2=lambda^2+1-2lambda cos theta,

coefficient comparison gives

c^2=lambda,
3lambda=lambda^2+1,

hence

lambda^2-3lambda+1=0.

The analytic/stable branch lambda>1 is uniquely

lambda=phi^2,
c=phi.

Since lambda=K_{q,1}(1/2), this uniquely forces q=5.

Equivalently lambda+lambda^{-1}=3, so the corresponding Casimir mass is

mu^2=lambda+lambda^{-1}-2=1.

Therefore the following three normalizations are exactly equivalent:
- conservative two-channel normalization of the Nyman boundary inverse;
- unit Casimir mass;
- finite-place center q=5.

## 23. Golden de Branges pair equals the unit-mass Casimir Green system

At kappa=log phi,

A_phi = phi I - phi^{-1}S,

and

A_phi* A_phi=L+I.

Its inverse transfer function is

A_phi^{-1}(z)
=
1/(phi-phi^{-1}z)
=
phi/(phi^2-z)
=
beta_{phi^2}(z).

Also

alpha_{phi^2}(z)
=
(1-z)A_phi^{-1}(z).

Hence the conservative identity

|alpha|^2+|beta|^2=1

is exactly

(|1-z|^2+1)/|A_phi(z)|^2=1,

the boundary-symbol form of

A_phi* A_phi=L+I.

Thus the normalized golden two-channel Hardy/de Branges pair, the unit-mass discrete Casimir-Dirac factor, and the q=5 finite-place shadow center are not parallel analogies: they are the same transfer system written in three coordinate languages.

The coefficient expansion is

beta_{phi^2}(z)
=
sum_{n>=0} phi^{-(2n+1)} z^n,

so this same transfer is the unit-mass Markov kernel previously derived.

## 24. Domain warning

C=(I+S)(I-S)^{-1} is unbounded because 1 lies on the spectrum of S. The identities above are exact as rational transfer-function identities and on the natural domain of (I-S)^{-1}. They do not by themselves prove that a dual RH ghost lies in the domain of C or in the associated local Dirichlet/de Branges space. Establishing precisely that boundary regularity remains equivalent to killing the threshold defect and must not be assumed.
