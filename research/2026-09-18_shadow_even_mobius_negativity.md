> **v21 correction, 2026-09-20.** Which Way Is Forward? v21 no longer interprets
> the four-lift Hilbert carrier as a finite gauge/Haar quotient.  The simultaneous reversal
> is an anti-linear real structure relative to the microscopic complex structure, and
> `(1+D)/2` is the corresponding real-part projection.  The calculation below remains a
> valid statement about the linear shadow-even compression of the finite Möbius operator,
> and it still proves that symmetry/compression alone does not create positivity.  It must
> not be cited as the physical Hilbert-space quotient mechanism of v21.  See
> `2026-09-20_v21_real_structure_primitive_character_RH_target.md`.

# Shadow-even Haar averaging self-adjointizes the finite Möbius bulk but does not make it positive

Date: 2026-09-18

This calculation was prompted by the upgraded Which Way Is Forward? v14, whose finite
orientation model distinguishes a genuine Z2 Haar/deck average from mere symmetry and also
warns that symmetry alone does not eliminate coherent observables.

The same distinction is exact in the finite arithmetic occupation cube.

## 1. Binary four-prime occupation cube

Take four binary prime channels.  Let the Hilbert basis be e_A indexed by subsets
A of {1,2,3,4}.  Let S_j adjoin j when it is not already occupied, so the shifts commute
and are nilpotent.

At the centered boundary z=0 define the finite Möbius creation operator

M = prod_{j=1}^4 (I-S_j).

For every subset A,

M e_A
=
sum_{B superset A} (-1)^{|B|-|A|} e_B.

Let J be occupation complement,

J e_A = e_{A^c}.

This is the finite shadow involution and J^2=I.

The finite critical-line Krein theorem already gives

M^* J = J M.

## 2. Haar/deck projection

The exact finite Z2 Haar average is

P_+=(I+J)/2.

On Ran(P_+), J acts as +I. Since M^*=J M J,

(P_+ M P_+)^*
=
P_+ M^* P_+
=
P_+ J M J P_+
=
P_+ M P_+.

Thus the shadow-even compression is an ordinary Hermitian operator.

This is the precise arithmetic analogue of the equal-lift Haar projection in
Which Way Is Forward? v14.

## 3. Exact negative shadow-even vector

Define

v_0=e_empty+e_{1234},

v_2=sum_{|A|=2}e_A,

x=v_0-v_2.

Complement preserves both v_0 and v_2, so

Jx=x,

and x lies exactly in the Haar/deck-even subspace.

Now compute q=<x,Mx>.

Only even cardinality layers contribute because x vanishes on odd layers.

For A=empty,

sum_{B superset empty} (-1)^|B| x_B
=
1 - 6 + 1
=
-4.

For each |A|=2,

sum_{B superset A} (-1)^{|B|-2} x_B
=
(-1)+(+1)
=
0.

For A={1,2,3,4}, the contribution is +1.

Therefore

boxed(<x,Mx>=-4+0+1=-3).

The norm is

||x||^2=2+6=8,

so the Rayleigh quotient is exactly

-3/8.

Hence

P_+ M P_+

is Hermitian but indefinite.

By continuity, the same negative direction persists for sufficiently small positive real
z in

M(z)=prod_j(I-p_j^{-z}S_j),

for any fixed four distinct primes p_j.

## 4. General even-middle-layer formula

For n=2m binary channels, consider

x=(e_empty+e_full)-sum_{|A|=m}e_A.

This vector is complement-even.  At z=0 one finds

<x,Mx>
=
3 + C(2m,m) - 2(-1)^m C(2m,m).

When m is even this reduces to

3-C(2m,m),

which is negative for every m>=2.  Thus n=4,8,12,... already have explicit
shadow-even negative directions of this elementary layer-symmetric form.

The n=4 case is the first.

## 5. Consequence

The finite Haar/deck quotient does one important job:
it turns the J-self-adjoint Krein bulk into an ordinary Hermitian compression.

It does NOT solve positivity.

Therefore the orientation/Haar idea must not be used as

"average the two shadow lifts, then positivity follows."

The correct architecture is

prime Krein bulk
  + Archimedean/nonlocal coupling
  -> completed constraint/Schur map
  -> physical shadow-even quotient
  -> positive Hilbert form.

This matches the older no-positive-bulk-reweighting theorem and the new v14 warning that
symmetry is not enough.

## 6. Relation to the RH target

The bad-zero Hardy defect lives after the global boundary completion, not in the naive
finite prime cohomology.  The calculation above explains why.

A fixed Haar involution correctly determines the metric symmetry, but an independent
Archimedean/nonlocal map must still remove the finite negative directions before the
infinite boundary limit.

This makes the remaining theorem more specific:

construct a zero-independent prime-Archimedean boundary map L_N such that
1. it intertwines the finite shadow involution;
2. its image/Schur quotient is Haar-even;
3. the induced Hilbert form is positive;
4. the resulting causal transfer is an isometry;
5. the finite maps converge strongly to the completed xi boundary transfer.

If such a construction exists, positivity is imported by the completed coupling rather
than assumed as Weil positivity.
