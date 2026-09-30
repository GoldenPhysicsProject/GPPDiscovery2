# Global representation theory as a zero-survival architecture

Date: 2026-09-29
Status: exact categorical reduction using Barrero--Barthel--Pol--Strickland--Williamson (2025), plus a precise compatibility obstruction. No RH claim.

## 1. Why this paper matches the prime-square-root construction

For a finite prime set P={p_1,...,p_r}, the square-root extension
Q(sqrt(p_1),...,sqrt(p_r)) has Galois group (Z/2)^r.
Abstractly this is the elementary abelian 2-group C_2^r.

Barrero et al. define global representations over a family U of finite groups as
contravariant functors on the category whose morphisms are conjugacy classes of
surjective homomorphisms. For U the elementary abelian p-groups, their global
representation system is a compatible diagram across C_p^r with Out(C_p^r)=GL_r(F_p);
they identify this with VI-module representation stability via Pontryagin duality.

Thus for p=2 their finite group tower is exactly the abstract group tower underlying
our squareclass hypercubes.

## 2. Their torsion-free theorem is structurally the no-escape statement we need

For a global representation X and x in X(G), their definition says x is torsion-free
iff for every morphism alpha:H->G in U,
alpha^*(x) != 0.

Because X is contravariant, a projection
C_2^{r+k} -> C_2^r
induces
X(C_2^r) -> X(C_2^{r+k}).

Therefore a torsion-free class at rank r survives every enlargement of the finite
squareclass system.

Their Theorem 7.7 says:

If U is a multiplicative global family and X is a nonzero compact object of D(U),
then some homology H_n(X) contains a torsion-free element.

Since the elementary abelian 2-groups are closed under subgroups, quotients, and
finite products, they form the relevant kind of multiplicative global family.

This is not merely analogous to our missing condition: it is literally a theorem
ensuring nonvanishing under all larger-rank pullbacks, provided the arithmetic
zero is encoded as nonzero compact derived data in the required global category.

## 3. Conditional RH closure theorem suggested by the paper

Suppose one constructs, zero-independently, a holomorphic family of morphisms
F_s : P_s -> Q_s
between perfect/global projective objects over U_2={C_2^r}_{r>=0}, natural in the
global-representation sense, with the following properties.

(A) Spectral detection:
for each nontrivial zeta zero rho,
C_rho := cofib(F_rho)
is a nonzero compact object of D(U_2).

(B) Scale covariance:
the completed Mellin scale evolution V_t acts naturally on H_*(C_rho), and every
nonzero class in the rho spectral sector transforms by
V_t x = exp((1/2-rho)t) x
(or dually the corresponding bounded functional has this character).

(C) Physical growth:
on the relevant completed norm, V_t and V_{-t} have subexponential growth:
for every epsilon>0,
||V_t|| <= C_epsilon exp(epsilon |t|).

Then RH follows.

Proof:
- By Theorem 7.7, nonzero compact C_rho has a torsion-free homology class x.
- Hence x cannot disappear under any higher prime/squareclass cutoff.
- By (B), it carries the rho scaling character.
- By (C), applying the two-sided growth estimate to x forces
  |Re(rho)-1/2| <= epsilon for every epsilon>0.
- Therefore Re(rho)=1/2.

Only one surviving class per zero is needed. This avoids any simplicity assumption
and is compatible with multiple zeros/Jordan polynomial growth.

## 4. Stronger retract statement

Their Lemma 7.10 and Corollary 7.11 say a torsion-free class produces a split
monomorphism e_G -> e_G tensor X, and every nonzero compact X in a multiplicative
global family generates some standard projective e_G in its thick tensor ideal.

For our purposes this means that if a zero is detected by a compact cofiber, its
surviving class is not merely nonzero: it has a retract/generator witness in the
tensor-triangular category. This could provide a robust finite certificate of
'zero data survives the cutoff system'.

## 5. Important obstruction: the arithmetic prime basis breaks full GL_r(F_2)

Direct application is NOT yet justified.

The abstract squareclass group C_2^r has full automorphism group GL_r(F_2).
Our physical prime state remembers the distinguished basis labelled by
p_1,...,p_r and the unequal weights log p_j or p_j^{-s}.

An arbitrary GL_r(F_2) automorphism mixes the prime generators and does not preserve
these weights. Even the particular 'flip all square roots' Möbius parity character
depends on the chosen prime basis.

Therefore the weighted zeta state is not automatically an object of the full global
representation category used by Barrero et al.

There are two possible repairs:

1. Enlarge X(C_2^r) to contain the full GL_r orbit of all prime-labelled weight data,
   so the physical prime labeling is a vector inside a genuine Out(C_2^r)-representation;
   then define the cutoff maps equivariantly.

2. Extract an unweighted topological/squareclass survival object carrying the full
   global symmetry, while the log-prime/Mellin weights live in a separate natural
   operator or coefficient system. One must prove the weighted zero class maps into
   the torsion-free global sector.

A weaker category of based/labeled F_2-vector spaces would fit the prime basis more
directly, but Barrero et al.'s theorem does not automatically transfer to that category;
its torsion-free theorem relies on the multiplicative global-family structure.

## 6. Why the compact/dualizable distinction is also useful

Barrero et al. prove that for infinite/non-groupoid global families compact and
dualizable objects generally differ; the category is rigidly-compactly generated only
for finite groupoids.

This is a warning against demanding too much. Our zero-survival argument needs a
compact nonzero cofiber plus a controlled scale action; it does not require every zero
object to be dualizable/rigid. This matches the earlier correction that exact unitarity
of full analytic jet data can accidentally impose simplicity, whereas two-sided
subexponential growth is sufficient for RH.

## 7. Smallest next theorem

The new load-bearing arithmetic/categorical target is:

Construct a finite-prime completed Poisson/Euler complex whose cofiber:
- is perfect/compact at every finite rank;
- is functorial under the squareclass cutoff maps;
- is nonzero exactly when the completed arithmetic response vanishes;
- carries the Mellin scale character exp((1/2-s)t).

If this construction can be promoted to a genuine global representation over the
elementary abelian 2-group family (or an exact theorem with the same torsion-free
survival conclusion in the naturally labelled category), the categorical no-escape
part is supplied by Theorem 7.7. The remaining analytic estimate is the already
isolated subexponential physical scale bound.


## 8. Major strengthening: the finite zeta gauge is the half-density normalization of standard global projective incidence

Barrero et al. define, for each finite group M, the standard projective
c_M=e_{M,k}. They show

c_M(T) = k[Epi(T,M)/Aut(M)] = k[s_M(T)],

where s_M(T) is the set of normal subgroups N of T with T/N isomorphic to M.

Take the full finite-abelian global family and restrict evaluations to cyclic groups.
For T=C_n and M=C_d, cyclicity gives exactly one subgroup with quotient C_d when
d divides n and none otherwise. Therefore

dim c_{C_d}(C_n) = 1_{d|n}.

More strongly, because that subgroup is unique, the nonzero one-dimensional
evaluation has a canonical quotient-kernel basis vector.

Hence the matrix

A_N(n,d)=1_{d|n}

is not an ad hoc arithmetic matrix: it is the evaluation/incidence matrix of the
standard projective generators c_{C_d} on cyclic test objects C_n.

Let D=diag(1,2,...,N). Then the project's finite half-density zeta gauge is exactly

Z_N = D^{-1/2} A_N D^{1/2},

because

Z_N(n,d)=sqrt(d/n) 1_{d|n}.

The inverse incidence matrix is the classical divisor Mobius matrix

A_N^{-1}(n,d)=mu(n/d)1_{d|n},

so automatically

Z_N^{-1}(n,d)=mu(n/d)sqrt(d/n)1_{d|n}.

Thus BOTH the zeta gauge and its Mobius inverse are the half-density normalized
projective-incidence transform of the global representation category.

This gives a representation-theoretic explanation of an exact structure that the
project had previously discovered independently.

## 9. The von Mangoldt gauge identity is projective evaluation of the divisor logarithm

The standard arithmetic identity

sum_{d|n} Lambda(d)=log n

now reads as evaluation of an incidence/projective coefficient vector on C_n.

After half-density normalization,

sum_{d|n} sqrt(d/n) [Lambda(d)/sqrt(d)]
= log n/sqrt(n),

which is exactly the previously formalized zeta-gauge current identity

Z_N (Lambda(d)/sqrt d) = log(n)/sqrt n

away from cutoff truncation.

So the tame primal logarithmic current is naturally the image, under standard
global-projective incidence, of the von Mangoldt coefficient state.

The raw dual Mobius obstruction found earlier is then the dual incidence inversion
inside this same category. This explains why the primal direction is simple and the
dual boundary observation recovers reciprocal-zeta/Mobius difficulty.

## 10. Better family: finite abelian groups encode the prime labels intrinsically

The earlier GL_r(F_2) basis-mixing obstruction can be avoided by not using
C_2^r as the primary global-family object.

Let U_ab be the full family of finite abelian groups, which is closed under subgroups,
quotients and finite products and is therefore multiplicative global.

For a finite set of distinct primes P define

G_P = product_{p in P} C_p.

Because the prime orders are distinct, this group is cyclic of squarefree order
n_P=product P, but its p-primary factors are characteristic. Therefore automorphisms
cannot mix different primes: the arithmetic label p is encoded intrinsically by the
order of the Sylow factor.

For P subset Q there is a canonical quotient G_Q -> G_P, exactly the desired
'forget added primes' map. A torsion-free global class at G_P therefore survives
under every larger-prime extension G_Q.

This is a much better categorical host for the physical prime-labeled data than an
unlabelled elementary-abelian C_2^r.

The square-root sign hypercube still appears as the independent sign/parity data
associated with the prime factors, but the global category itself now remembers
which factor is the prime 2,3,5,... through group order rather than through an
arbitrarily chosen F_2 basis.

## 11. Natural maps from projective sums implement Dirichlet coefficient systems

Yoneda gives

Hom(c_{C_d}, X) approximately X(C_d)

for the corresponding standard generators. In particular maps from finite direct sums

P_N = direct_sum_{d<=N} c_{C_d}

to a chosen global object are determined by coefficient data at the cyclic quotients.

This means finite Dirichlet coefficient vectors can be promoted to actual natural
morphisms of global representations rather than treated only as scalar matrices.

The next construction should therefore seek the completed Poisson/Euler map as a
morphism (or short complex) built from these c_{C_d}, with the half-density metric
inserted on cyclic evaluation. Restriction to cyclic groups must recover the already
verified Z_N/M_N arithmetic, while the ambient finite-abelian global family supplies
the multiplicative hypothesis needed for the torsion-free survival theorem.

This is now the preferred categorical implementation of the no-escape route.
