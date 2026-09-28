# Critical prime KMS state: the half-density boundary exists naturally in a new GNS representation

Date: 2026-09-27
Status: exact finite-local and quasi-local operator-algebra construction; global factor classification and RH connection remain open.

This note addresses the critical weak-escape phenomenon physically rather than trying to force the beta=1 state into the beta>1 Fock representation.

## 1. Local prime thermal states remain perfectly regular at beta=1

For each prime p, let

h_p = ell2(N0),
N_p|k>=k|k>.

At inverse temperature beta>0 define

rho_{p,beta}
=
(1-p^(-beta))
sum_{k>=0} p^(-beta k)|k><k|.

This is a faithful trace-one density matrix for every beta>0.

At the critical arithmetic value beta=1,

boxed:
rho_p
=
(1-p^(-1))
sum_{k>=0} p^(-k)|k><k|.

Nothing singular happens at any fixed prime.

Its canonical thermofield purification is

boxed:
|Omega_p>
=
sqrt(1-p^(-1))
sum_{k>=0} p^(-k/2)|k,k>.

Thus the arithmetic half-density p^(-k/2) is literally the square root rho_p^(1/2) appearing in the standard purification.

## 2. The critical global state exists quasi-locally although the naive partition function diverges

For every finite prime set P define the product state

phi_P
=
tensor_{p in P} rho_p

on

A_P=tensor_{p in P} B(h_p).

If P subset Q, restriction of phi_Q to A_P is phi_P.

Therefore the family defines a consistent state phi_crit on the quasi-local inductive-limit algebra

A_ar = closure union_P A_P.

By the GNS construction there exists a Hilbert space H_crit, a representation pi_crit, and a cyclic vector Omega_crit such that

boxed:
phi_crit(A)
=
<Omega_crit,pi_crit(A)Omega_crit>.

So the beta=1 arithmetic state DOES exist as a normalized vacuum state in its natural thermodynamic-limit representation.

What fails is representation by one trace-class global density matrix in the beta>1 Fock Hilbert space.

## 3. Why the naive Fock vector escapes

For finite P the product TFD vector is

Omega_P=tensor_{p in P}Omega_p.

Its overlap with the bare product vacuum is

<0|Omega_P>
=
product_{p in P} sqrt(1-p^(-1)).

As P exhausts the primes,

product_p (1-p^(-1))
=
0

in the Euler-product sense associated with the zeta pole at 1.

Equivalently, the deviation from the vacuum reference is not summable.

Thus the critical product state belongs to a representation disjoint from the naive finite-particle vacuum representation.

This gives a precise thermodynamic-limit interpretation of the previously proved weak escape:
the state did not disappear; the Hilbert representation changed.

## 4. Local modular operator

For a faithful density matrix rho_p on B(h_p), the standard Hilbert-Schmidt representation has modular operator

Delta_p=L_{rho_p} R_{rho_p}^{-1}.

On the matrix unit |k><l|,

Delta_p |k><l|
=
[rho_p(k)/rho_p(l)] |k><l|
=
p^{-(k-l)} |k><l|.

Therefore

boxed:
spec_point(Delta_p)
=
{p^m:m in Z}

(up to the sign convention m=l-k).

The local modular Hamiltonian

K_p=-log Delta_p

has frequencies

boxed:
m log p,  m in Z.

These are exactly the signed prime occupation differences.

## 5. Global modular frequencies are logarithms of positive rationals

For a finite tensor product, modular eigenvalues multiply. Hence the finite-support global modular spectrum contains

product_p p^{m_p},

with m_p in Z and only finitely many nonzero.

By unique factorization this set is exactly

boxed:
Q_+,

the positive rationals.

Thus the modular Hamiltonian frequencies are

boxed:
log Q_+.

Since Q_+ is dense in R_+, log Q_+ is dense in R.

So the thermodynamic-limit critical arithmetic vacuum naturally converts the discrete prime data into a dense real modular spectrum.

This is an exact operator-algebraic version of the earlier Peter-Weyl / dense Kronecker-flow picture.

## 6. The doubled sheets and the half-density are built into Tomita standard form

Finite-locally, the TFD standard form has:
- a left algebra;
- a commuting right algebra;
- modular operator Delta;
- modular conjugation J exchanging the two sides;
- the Tomita operator S=J Delta^(1/2).

Thus the two-sheet structure is not an optional pictorial doubling. It is the canonical standard-form doubling of a faithful thermal state.

And the exponent 1/2 is structurally distinguished because the square root Delta^(1/2) is the modular midpoint.

This gives a mathematically precise version of:
- two equivalent sheets;
- sheet exchange;
- half-density weighting;
- a common boundary vacuum.

It does NOT by itself identify the modular half power with the conformal weight Delta=1/2+i lambda; the exact intertwiner between modular standard form and the PSL(2,R) principal series remains to be constructed.

## 7. Why this is a better home for the critical number universe

The previous ell2(N) coherent vector

sum_n n^(-1/2)|n>

is nonnormalizable.

But every finite prime cylinder of the beta=1 KMS state is normalized, and the compatible infinite product state has a GNS vacuum.

So the correct boundary theory is likely not an ordinary vector in the same Hilbert space as the beta>1 bulk coherent states.

It is a thermodynamic-limit / GNS boundary representation.

This is exactly what one expects of a holographic conformal boundary: the boundary Hilbert representation can be inequivalent to the normalizable bulk representation.

## 8. Candidate bridge to the principal series

The modular flow acts on a local matrix unit by

sigma_t(|k><l|)
=
p^{-it(k-l)} |k><l|.

Globally the characters are q^{-it}, q in Q_+.

This is the same real modular-time character appearing in the arithmetic boundary flow.

A promising next theorem is therefore to construct a half-sided modular inclusion or another standard modular-covariance structure from the divisibility/decimation semigroup. Such structures canonically generate PSL(2,R)-type Möbius actions in operator algebra.

If that succeeds, the CFT1 principal series would emerge from the critical prime KMS algebra rather than being imposed externally.

This is a target, not yet proved.

## 9. Relative modular operator as a new RH target

The modular operator of the raw prime KMS vacuum is NOT the Riemann-zero operator: its spectrum is generated by rational prime ratios.

The zero spectrum must still be collective.

However the operator-algebraic setting suggests a more natural positive object than a global density matrix:

boxed:
relative modular operator
Delta_{completed | prime}.

Relative modular operators are positive self-adjoint by construction.

If the prime-plus-Archimedean completed vacuum can be represented as a second faithful state/weight on the same standard form, then the physical scattering/Weyl operator may be obtainable from their relative modular data.

A decisive target is:

construct two zero-independent states/weights,
phi_ar and phi_completed,
such that a renormalized relative-modular Fredholm determinant or Weyl function equals

xi(1/2+z)/xi(1/2).

If achieved, positivity/self-adjointness would supply exactly the missing spectral reality mechanism.

This is currently a hypothesis, but it is more compatible with the critical thermodynamic limit than demanding an ordinary trace-class global density matrix at the boundary.
