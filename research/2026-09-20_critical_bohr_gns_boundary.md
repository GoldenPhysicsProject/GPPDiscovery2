# Critical Bohr sector, orthogonality catastrophe, and principal-series GNS boundary

Date: 2026-09-20

Continue from 2026-09-20_bohr_hilbert_arithmetic_shadow_lift.md.

For sigma>1/2 the local prime state is

Omega_{p,sigma}
=
-r |+1>
+(1-r^2)|0>
+(1-r^2) sum_{m>=1} r^m |-m>,

r=p^-sigma,

and the vacuum-sector infinite tensor product exists because sum_p r^2<infinity.

## 1. Critical representation leaves the vacuum sector

At sigma=1/2,

r_p^2=1/p

and

sum_p r_p^2=sum_p 1/p=infinity.

Equivalently the local vacuum overlap is

<0|Omega_{p,1/2}>=1-1/p,

so the finite-prime vacuum fidelity is

prod_{p<=P}(1-1/p)^2,

which tends to zero by Euler/Mertens.

Thus the critical arithmetic phase state is not a vector in the same incomplete infinite
tensor product sector as the vacuum.

One may nevertheless define the infinite tensor product using the sequence
{Omega_{p,1/2}} itself as the reference sequence. This is a different GNS/ITP sector.

## 2. Local arithmetic-flow overlap

Let U_p(t)|n>=p^{i n t}|n>. For general sigma let x=p^-2sigma and z=p^{it}. Then

K_{p,sigma}(t)
=
<Omega_{p,sigma},U_p(t)Omega_{p,sigma}>

=
x z + (1-x)^2/(1-x z^-1)

=
(1-2x+x z)/(1-x z^-1).

At t=0 this is 1.

At sigma=1/2, x=1/p. Expanding at large p,

K_{p,1/2}(t)
=
1 + [z+z^-1-2]/p + O(p^-2)

=
1 - 4 sin^2(t log p/2)/p + O(p^-2).

Hence

1-Re K_{p,1/2}(t)
=
4 sin^2(t log p/2)/p + O(p^-2).

For fixed t!=0,

sum_p sin^2(t log p/2)/p
=
(1/2)sum_p 1/p
-(1/2) Re sum_p p^(-1+it)

diverges. The oscillatory prime sum is conditionally convergent for t!=0 by the prime
number theorem plus partial summation, whereas sum_p1/p diverges.

Therefore the infinite-product overlap obeys

boxed(
prod_p K_{p,1/2}(t)=0
for every t!=0
)

in the standard infinite-product sense.

Thus the arithmetic dilation flow sends the critical reference vector into mutually
orthogonal sectors for every nonzero time. It is not strongly continuous in this single
incomplete tensor-product representation.

## 3. Interpretation

This is the operator-theoretic version of the previously derived coherent-state boundary

K_sigma(t,u)=zeta(2sigma+i(u-t))/zeta(2sigma)
 -> delta(t-u)

as sigma->1/2+.

The half-density line is therefore a genuine representation boundary:
- sigma>1/2: normalizable all-prime states in a vacuum Fock/ITP sector;
- sigma=1/2: delta-normalized principal-series continuum;
- ordinary Stone evolution must be realized after a direct-integral/rigged-Hilbert
  completion, not inside the vacuum ITP sector.

This also explains why attempts to take a strong vector limit sigma->1/2 fail even though
every state has norm one.

## 4. Consequence for the first-order RH operator

The desired global first-order shadow Dirac cannot be constructed by simply taking the
vacuum-sector limit of the finite-prime Dirac/Fock operators.

The correct object must be a boundary representation in which:
1. the principal-series parameter is continuous;
2. critical states are delta-normalized;
3. shadow acts as the orientation exchange gamma -> -gamma;
4. Hilbert adjoint is fixed by the Plancherel measure;
5. the completed arithmetic scalar section is a controlled distribution/Hardy boundary
   value rather than an ordinary vector evaluation.

This is consistent with the Mellin/Haar and celestial principal-series structures in
Which Way Is Forward? v14.

## 5. What this does not prove

The critical GNS transition is unconditional arithmetic structure. It does not say that
every zeta zero is represented by a tempered principal-series state. That remains the
arithmetic admissibility/causal trace theorem.

It does, however, rule out another class of naive closure arguments: a strong limit in the
ordinary prime-Fock vacuum Hilbert space cannot be the critical RH completion because the
critical state is in an inequivalent representation.
