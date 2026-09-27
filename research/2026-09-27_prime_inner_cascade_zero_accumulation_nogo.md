# No-go: the raw infinite cascade of prime inner channels cannot exist as a nonzero analytic inner function

Date: 2026-09-27
Status: exact local-zero geometry plus an elementary analytic no-go. No RH claim.

For each prime p let

L_p=log p,
a_p=p^(-1/2),

and take the causal prime channel

Theta_p(z)=B_{a_p}(e^(i L_p z)),

where

B_a(w)=(w-a)/(1-aw).

Each Theta_p is inner on the upper half-plane.

## 1. Exact zero lattice

Zeros satisfy

e^(i L_p z)=a_p=e^(-L_p/2).

Hence

boxed:
z_{p,k}
=
2 pi k/L_p + i/2,
qquad k in Z.

Thus every prime has its entire zero lattice on Im z=1/2.

In particular,

boxed:
z_{p,0}=i/2

for every prime p.

So all prime channels share one identical interior zero.

## 2. Immediate infinite-product obstruction

Suppose an infinite product of the Theta_p, multiplied only by nonvanishing analytic renormalization factors, converged locally uniformly in the upper half-plane to a nonzero analytic function.

Every finite partial product has a zero at z=i/2 whose multiplicity equals the number of included primes.

A locally uniform nonzero analytic limit cannot have unbounded zero multiplicity at a fixed interior point.

Equivalently, after dividing by any zero-free counterterm, the Taylor coefficients through arbitrarily high order at i/2 vanish as the prime cutoff grows.

Therefore

boxed:
the raw infinite cascade of the local prime inner factors cannot converge to a nonzero analytic inner transfer.

A determinant/phase counterterm which is everywhere nonzero cannot repair this, because it does not alter the zero divisor.

## 3. Cancelling only the common k=0 zero is still insufficient

One might divide each local channel by the elementary Blaschke factor associated with z=i/2 before taking the product.

But for each fixed nonzero integer k,

z_{p,k}
=
2 pi k/log p + i/2
longrightarrow
i/2

as p->infinity.

Thus after removing k=0, the k=1 zeros alone form an infinite sequence of distinct zeros accumulating at the interior point i/2.

By the identity theorem, no nonzero analytic function on the upper half-plane can possess such an interior accumulation of zeros.

Hence

boxed:
no finite-order endpoint cancellation can make the prime zero lattices into the zero set of a nonzero analytic global inner function.

The local zero lattices must be cancelled/reorganized nonlocally before the infinite analytic limit is formed.

## 4. Blaschke-condition version

The same conclusion follows from the upper-half-plane Blaschke condition.

A bounded nonzero analytic function with zero set {z_j} must satisfy

sum_j Im(z_j)/(1+|z_j|^2) < infinity.

For the prime zeros z_{p,k}, even the single k=0 contribution is

(1/2)/(1+1/4)=2/5

for every prime.

Therefore the sum over primes diverges immediately.

Even after deleting k=0, any fixed k contributes a term tending to 2/5 as p grows, so that subseries still diverges.

Thus the full local-prime zero divisor is far outside the Blaschke class.

## 5. Consequence for the RH construction

This proves that the correct global object cannot be

"take every prime inner channel, multiply them, then renormalize its magnitude."

The problem is not merely a divergent scalar normalization. The local analytic zero divisor itself is non-globalizable.

This explains why:
- local prime unitarity is true but insufficient;
- scalar det_3 renormalization controls the Euler logarithm but does not by itself produce the global causal transfer;
- the rational/Archimedean/co-Poisson step must act **before or during** the infinite-channel limit and cancel the local boundary spectra at operator level.

The nontrivial Riemann zeros can then emerge as collective resonances of the quotient rather than inherited local zeros.

## 6. Sharpened construction order

The viable order is now constrained:

1. build the finite positive prime colligation / Hodge--Koszul system;
2. attach the real-place Poisson/shadow boundary map;
3. take the physical quotient/minimal realization so the local prime zero lattices cancel;
4. only then take the infinite-prime limit;
5. prove the resulting completed transfer is causal/inner.

Any construction which takes the raw infinite product of the individual prime inner functions before the global quotient is analytically impossible.

This is a useful no-go because it eliminates a large class of otherwise tempting "infinite product of local unitary scatterers" proofs.
