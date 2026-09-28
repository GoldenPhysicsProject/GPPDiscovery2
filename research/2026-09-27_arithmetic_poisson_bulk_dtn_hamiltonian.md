# Arithmetic Poisson bulk: the logarithmic Hamiltonian is an exact Dirichlet-to-Neumann operator

Date: 2026-09-27
Status: exact operator construction. No RH assumption and no zero data.

This note upgrades the arithmetic-holography picture from a transform analogy to an explicit free bulk/boundary field theory.

## 1. Boundary Hilbert space

Use the arithmetic Hardy/Fock boundary Hilbert space

H_ar = ell2(N)

with orthonormal basis |n>, equivalently the positive Hardy cone on the prime torus.

Define the self-adjoint logarithmic Hamiltonian

boxed:
H|n>=(log n)|n>.

H is nonnegative and has compact resolvent after separating the vacuum n=1: log n -> infinity with finite multiplicity.

Unique factorization identifies this same space with bosonic Fock space over prime modes:

ell2(N)
~= tensor_p ell2(N0),

and

boxed:
H=sum_p (log p) N_p

on the finite-occupation core.

Thus primes are elementary one-mode energies and integers are the exact multiparticle basis.

## 2. Exact harmonic bulk extension

For boundary data

f=sum_n a_n |n>

define its radial extension for r>0 by

Phi_f(r)=e^(-rH)f
=
sum_n a_n n^(-r)|n>.

Along the one-parameter arithmetic boundary flow, |n> has phase e^(-it log n). Therefore the spacetime field is

boxed:
Phi_f(r,t)
=
sum_n a_n e^{-(r+it)log n}.

Term by term,

partial_r Phi = -H Phi,
partial_t Phi = -i H Phi.

Hence

boxed:
(partial_r+i partial_t)Phi=0

and

boxed:
(partial_r^2+partial_t^2)Phi=0.

So the arithmetic Dirichlet-series bulk is literally the positive-frequency harmonic Hardy sector of the half-plane.

## 3. H is the Dirichlet-to-Neumann operator

At the boundary r=0,

Phi_f(0)=f.

Its outward radial derivative is

-partial_r Phi_f|_{r=0}=Hf.

Therefore

boxed:
Lambda_DtN = H = log N.

The logarithmic arithmetic Hamiltonian is exactly the Dirichlet-to-Neumann operator of the free harmonic number bulk.

This gives a precise holographic meaning to the ubiquitous log n.

## 4. Zeta is the boundary heat trace / thermal partition function

Since spec(H)={log n},

boxed:
Tr exp(-beta H)
=
sum_n n^(-beta)
=
zeta(beta),
Re beta>1.

Under the prime-Fock identification this same trace factorizes as

boxed:
zeta(beta)
=
product_p (1-e^{-beta log p})^(-1).

So zeta is simultaneously:
- the heat trace of the boundary DtN Hamiltonian;
- the thermal partition function of free bosonic prime modes;
- the reproducing-kernel diagonal normalization of the Dirichlet Hardy bulk.

These are three exact realizations of one object.

## 5. The critical half-density is the bulk normalizability boundary

The bulk coherent/evaluation vector at s=sigma+it is

k_s=sum_n n^(-conj(s))|n>.

Its norm is

||k_s||^2=zeta(2sigma).

Hence bounded bulk evaluation and normalizable coherent states exist exactly for

sigma>1/2.

The conformal boundary sigma=1/2 is therefore not inserted by hand: it is the normalizability boundary of the exact harmonic bulk.

## 6. Relation to the earlier prime-edge essential-spectrum no-go

The earlier no-go considered a direct sum of physical intervals L2(0,ell_p) with independent interior degrees of freedom. Minimal-domain packets on longer and longer edges then force [1,infinity) into the essential spectrum under endpoint-only sewing.

The present construction does NOT contradict that theorem.

Here the bulk is restricted to the on-shell harmonic/Hardy sector

Phi(r)=e^{-rH}f.

There are no independent interior wave packets. Every radial degree of freedom is determined by boundary data.

Consequently the relevant boundary DtN operator H has discrete spectrum log n and compact resolvent even though a naive off-shell direct-sum interval bulk has essential continuum.

This is precisely a holographic quotient: eliminate the interior bulk gauge/off-shell sector before spectral scalarization.

Thus the old no-go tells us which bulk was too large; it does not forbid a holographic boundary operator.

## 7. Completion and the two spectral layers

The free DtN spectrum is

{log n}.

These are microscopic Fock energies and cannot be identified with Riemann ordinates.

The completed xi zeros must arise, if the vacuum-spectrum hypothesis is right, from a second operator built after:
- Archimedean completion;
- sheet doubling/reflection;
- connected/Mobius cancellation;
- physical Schur/Feshbach quotient.

The clean distinction is

boxed:
microscopic DtN spectrum = {log n},

boxed:
collective completed fluctuation spectrum = candidate {gamma_k}.

This is analogous to constituents versus normal modes in an interacting many-body system.

## 8. Exact prime decomposition of the DtN generator

The earlier divisibility-projection identity becomes especially transparent here.

Let P_d project onto integers divisible by d. Then on basis |n>,

sum_{d>=2} Lambda(d) P_d |n>
=
[sum_{d|n}Lambda(d)]|n>
=
(log n)|n>.

Hence

boxed:
H
=
sum_{d>=2} Lambda(d)P_d
=
sum_p (log p) sum_{k>=1} P_{p^k}

on the finite-support core.

So the von Mangoldt current is literally the positive projection decomposition of the holographic DtN Hamiltonian.

This is a zero-independent positive parent for the microscopic arithmetic current.

## 9. New reconstruction target

The free arithmetic bulk is now completely explicit:

boundary:
H_ar=ell2(N) / H2(K_ar),

bulk propagation:
e^{-rH},

DtN:
H=log N,

partition function:
zeta(beta),

critical conformal boundary:
Re(s)=1/2,

local prime decomposition:
H=sum Lambda(d)P_d.

The remaining RH problem is therefore not to discover the free number bulk. It is to construct the COMPLETED fluctuation/scattering operator generated when this positive arithmetic DtN system is sewn to the real-place SU(1,1) channel and the reflected sheet.

The correct candidate should live on the boundary/physical quotient, not on a direct sum of unconstrained prime-edge interiors.
