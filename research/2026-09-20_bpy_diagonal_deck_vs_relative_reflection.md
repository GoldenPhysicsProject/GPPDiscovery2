# Exact diagonal deck quotient inside the BPY reflection model

Date: 2026-09-20

The upgraded Which Way Is Forward? v14 distinguishes a simultaneous/diagonal orientation
reversal, which may be a genuine deck redundancy, from a relative half-flip, which remains
observable. The two-copy BPY realization contains exactly this distinction.

## 1. BPY variables

The positive BPY measure is

d mu_omega(t,x,y)
=
(x+y)sinh(omega(x+y)) q(x)q(y) dt dx dy,

with t in [0,1] and q even.

Define the two oriented linear arguments

a=(1-t)y-tx,
b=(1-t)x-ty.

The arithmetic exponential is

Phi_z=exp(i z a),

and the BPY reflection J swaps x and y, hence swaps a and b.

## 2. A different involution is the true diagonal deck symmetry

Define

D0(t,x,y)=(1-t,-y,-x).

Then D0^2=I.

Under D0,

u=x+y -> -u,

and because q is even,

q(-y)q(-x)=q(y)q(x).

Also

(-u)sinh(-omega u)=u sinh(omega u),

so D0 preserves mu_omega.

Now compute the oriented arguments:

a(D0(t,x,y))
=
t(-x)-(1-t)(-y)
=
(1-t)y-tx
=
a,

and similarly

b(D0(t,x,y))=b.

Therefore

D0 Phi_z=Phi_z,

D0 J Phi_z=J Phi_z

for every z.

Thus the entire arithmetic exponential sector is already D0-even.  The map D0 is a genuine
measure-preserving deck redundancy of this realization, whereas J is a distinct relative
reflection carrying nontrivial arithmetic information.

## 3. Quotient coordinates

Put

u=x+y,
v=x-y,
c=(1-2t)u/2.

Under D0,

u -> -u,
v -> v,
c -> c.

Hence the D0 quotient is represented by u>0 with

|c|<=u/2,
v in R.

After pairing u and -u and using dt=dc/u, the positive measure becomes, up to the already
fixed normalization,

d mu_omega^quot
=
sinh(omega u)
q((u+v)/2)
q((u-v)/2)
dc du dv,

u>0, |c|<=u/2.

On these quotient variables the relative reflection is simply

J:(u,c,v)->(u,c,-v).

The exponential and its reflection are

Phi_z=e^{iz(c-v/2)},
J Phi_z=e^{iz(c+v/2)}.

Therefore

P_+ Phi_z=e^{izc} cos(zv/2),
P_- Phi_z=-i e^{izc} sin(zv/2).

This recovers the v34 center/relative formulas, now with an exact deck-quotient meaning.

## 4. Direct gauging of J is impossible if the xi kernel is to be preserved

For any nonzero real z,

P_- Phi_z=-i e^{izc} sin(zv/2)

is nonzero on a positive-measure set because q>0 on the real line and v is not supported at
0.

Therefore the arithmetic exponential subspace is not contained in the J-even space.

Replacing every f by its J-Haar average P_+f would change the exact de Branges form from

<Jf,f>=||P_+f||^2-||P_-f||^2

to the strictly different positive form

||P_+f||^2.

Thus J cannot be interpreted as a gauge/deck redundancy without changing the arithmetic
kernel, except after proving P_-=0, which is stronger than and not the actual RH condition
on individual states.

The correct identification is:

D0 = complete/diagonal deck redundancy;
J  = relative orientation observable / Krein fundamental symmetry.

## 5. Graph reconstruction is the physical-section problem

When P_+ is injective on the arithmetic subspace M_omega, define

C_omega(P_+f)=P_-f.

Then

M_omega={g+C_omega g : g in P_+M_omega}.

The diagonal quotient supplies the base/orientation-neutral variables, but it does not
determine C_omega.  The latter reconstructs the relative oriented lift.

The RH criterion is exactly

||C_omega||<=1 for every omega>0.

This is structurally the same kind of missing map as the physical section Pi_phys in
Which Way Is Forward? v14: quotient/folding determines the base, while a dynamical
intertwiner must reconstruct the hidden relative channel without violating the positive
metric.

The gain is conceptual but exact: the v14 diagonal orientation quotient does exist inside
the BPY model, but it is D0, not J. This prevents the wrong move of identifying reflection
positivity with gauge averaging.