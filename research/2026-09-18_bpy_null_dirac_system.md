# The BPY two-copy colligation is an exact 1+1 first-order Dirac system

Date: 2026-09-18

This is a new structural reading of the exact BPY reflection identity in v34, motivated by
the doubled-null and first-order factorization results in Which Way Is Forward? v14.

## 1. BPY even/odd components

The exact BPY construction uses

u=x+y,
v=x-y,
c=(1-2t)u/2,
d=v/2.

For one spectral exponential,

Phi_z = exp[i z (c-d)],

J Phi_z = exp[i z (c+d)].

The Haar/reflection projections are

f_+ = P_+ Phi_z
    = exp(i z c) cos(z d),

f_- = P_- Phi_z
    = -i exp(i z c) sin(z d).

The same formulas hold termwise for every finite linear combination.

## 2. Exact first-order Dirac equations

Differentiate:

partial_c f_+ = i z f_+,

partial_d f_- = -i z f_+,

hence

boxed(partial_c f_+ + partial_d f_- = 0).

Similarly,

partial_d f_+ = -i z f_-,

partial_c f_- = i z f_-,

so

boxed(partial_d f_+ + partial_c f_- = 0).

For F=(f_+,f_-)^T,

boxed[(partial_c I + partial_d sigma_x)F=0].

This is the massless 1+1 first-order Dirac/Weyl equation in a real two-component basis.

## 3. Chiral/null diagonalization

Define

g_R=f_++f_-,
g_L=f_+-f_-.

Then

g_R=exp[i z(c-d)],
g_L=exp[i z(c+d)],

and the system becomes

(partial_c+partial_d)g_R=0,
(partial_c-partial_d)g_L=0.

Thus the two original BPY copies are literally the two null chiral solutions; the
reflection J exchanges d -> -d and therefore exchanges the two chiral directions.

The P_+ and P_- variables are their equal and relative combinations.

## 4. RH as a first-order flux/polarization inequality

The exact BPY theorem says

L_omega >=0

iff

||f_-||_{mu_omega} <= ||f_+||_{mu_omega}

on the analytic exponential subspace.

Therefore RH is equivalent to contractive domination of the relative component of an
explicit first-order Dirac solution space by its equal/orientation-even component.

This turns the BPY problem into a weighted first-order energy estimate.

The measure in (u,c,d) variables has positive weight

u sinh(omega u) q((u+2d)/2)q((u-2d)/2)

(up to the fixed Jacobian), with c ranging over a finite interval determined by u.

The Dirac differential itself is fixed and zero-independent.  All arithmetic/Riemann
content sits in the positive BPY weight q and in the analytic subspace.

## 5. Relation to the v14 doubled-null architecture

Which Way v14 has a massless doubled parent whose first-order system splits into two
chiral halves at zero transverse mass and locks them when a transverse magnitude is
turned on.

The BPY system is an exact arithmetic analogue at the level of operator architecture:
- g_R and g_L are two null/chiral first-order directions;
- f_+ is the equal/orientation-even combination;
- f_- is the relative/orientation-odd combination;
- J swaps the two chiral directions;
- the desired physical Hilbert condition is domination of the odd relative channel.

No physical identification is claimed.  The gain is that the RH contraction is now a
specific first-order Dirac energy/flux inequality rather than a generic positive-kernel
request.

## 6. Supersymmetric relative-coordinate generator

For fixed u define

Psi_u(v)=sqrt(q((u+v)/2) q((u-v)/2)),

A_u = d/dv - Psi_u'/Psi_u.

Then for k=z/2,

A_u[Psi_u cos(kv)] = -k Psi_u sin(kv),

A_u[Psi_u sin(kv)] = +k Psi_u cos(kv).

Thus on each algebraic two-mode pair A_u is a quarter-turn:

A_u^2=-k^2

on that pair.

However A_u is not skew-adjoint in the BPY Hilbert metric.  The difference between the
cosine and sine norms is precisely the metric-compatibility content that RH needs.

This reproduces the same lesson as CayleyShadowDirac:
the order-four/quarter-turn algebra is automatic; Hilbert compatibility is the hard sign.

## 7. New constructive target

Try to prove the BPY contraction by a first-order energy estimate for the Dirac system
rather than by direct moment inequalities.

The desired estimate is

integral |f_-|^2 dmu_omega
<=
integral |f_+|^2 dmu_omega.

Because F satisfies a fixed first-order PDE, integrate an appropriate Dirac current over
the (c,d) strip for each u. The bulk divergence is zero before weighting; after inserting
the BPY weight the only obstruction is an explicit derivative of the relative-coordinate
weight.

Thus the next calculation is to derive the exact weighted current identity and determine
whether its bulk defect can be written as the already-positive supersymmetric potential
A_u^* A_u plus a boundary term with fixed sign.

If that succeeds, it would attack the missing contraction directly without zero data.
