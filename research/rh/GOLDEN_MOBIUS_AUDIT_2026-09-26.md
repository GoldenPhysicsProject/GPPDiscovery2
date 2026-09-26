# Golden Möbius audit of the RH boundary maps
## 2026-09-26 — Codex experiment

This note tests Daniel's observation that the equation φ²=φ+1 resembles the reciprocal /
Cayley / Schur algebra already present in the RH program.  The result is stronger than a
numerical coincidence, but it does **not** by itself prove RH.

### 1. The critical Cayley shadow and the golden map differ by one sign

The scalar Cayley shadow used throughout the program is

  B(x)=1-1/x.

The golden Möbius map is

  G(x)=1+1/x.

Exactly,

  G(x)=B(-x).

Thus the golden map is the sign-twisted Cayley shadow.

This sign matters.  B has fixed-point equation

  x²-x+1=0,

with discriminant -3, so its fixed points are elliptic/unitary.  G has fixed-point equation

  x²-x-1=0,

with discriminant +5, and its positive fixed point is the golden ratio

  φ=(1+sqrt(5))/2.

Projectively these maps are not conjugate by themselves: for a 2x2 representative M the
quantity (tr M)²/det M is invariant under conjugacy and scalar rescaling.  It equals +1 for
B and -1 for G.  The sign twist is therefore a genuine change of dynamical type, not a
coordinate relabeling.

### 2. The parity Sherman--Morrison maps are exactly translations

The pole-plane rank-one formulas give the two Möbius transforms

  O(x)=2x/(x+2),
  E(x)=-2x/(x-2).

Introduce the reciprocal coordinate

  y=2/x.

Then, exactly,

  y(O(x))=y+1,
  y(E(x))=y-1.

So the odd/even rank-one Schur updates are the two inverse unit translations in the
reciprocal projective coordinate.

This is a much cleaner structural statement than the original rational formulas.

### 3. Reciprocal duality + odd Schur update = golden dynamics

Let R(y)=1/y and T(y)=y+1.  Then

  T∘R(y)=1+1/y=G(y).

Therefore, if the physical shadow/Hodge duality on the same scalar coordinate y is the
reciprocal involution, one odd Schur update after one duality step is *exactly* the golden
map.

In the original x-coordinate y=2/x, the reciprocal involution y→1/y is

  x→4/x.

Thus the precise load-bearing statement for a genuine golden closure would be:

  does the completed arithmetic reflection act on the parity Schur scalar by x→4/x?

That is **not currently proved**.  The existing reflection laws act on several related
objects, but no identification of the concrete parity Schur scalar with this reciprocal
duality has yet been established.  This is now an exact testable target rather than a
numerological search.

### 4. The manuscript already contains φ^{-2} exactly

The v34 dyadic affine Cayley atlas proves

  |β|² ≤ 1/5

for a matched chart, and the worst-case relative precision margin is

  m=(1-|β|)/(1+|β|).

At the extremal radius |β|=1/sqrt(5),

  m=(sqrt(5)-1)/(sqrt(5)+1)
   =(3-sqrt(5))/2
   =φ^{-2}.

So the golden ratio was already present exactly in the RH manuscript, in a theorem, not as
a numerical fit.

The geometry is transparent.  At the worst Whitney-cell corner the Cayley
pseudohyperbolic radius is

  r=1/sqrt(5).

Writing r=tanh(a) gives

  a=asinh(1/2)=log φ.

Since

  (1-r)/(1+r)=exp(-2 artanh r),

the precision margin is

  exp(-2 log φ)=φ^{-2}.

Thus φ^{-2} is the exponential hyperbolic contraction across the unit-aspect affine cell.

### 5. Same contraction appears in golden dynamics

At the positive fixed point φ,

  G'(φ)=-1/φ².

Hence the magnitude of the stable multiplier of the golden map is exactly

  |G'(φ)|=φ^{-2},

the same constant as the dyadic Cayley precision margin.

Equivalently the matrix

  [[1,1],[1,0]]

for G squares to the Fibonacci matrix

  [[2,1],[1,1]],

whose eigenvalues are φ² and φ^{-2}.

So two independently derived pieces of the current RH architecture meet at the same exact
quantity:

1. affine Hardy/Cayley conditioning gives the contraction margin φ^{-2};
2. Schur-translation + reciprocal duality gives golden dynamics with stable multiplier
   φ^{-2}.

This is the strongest version of the connection found in this audit.

### 6. Important anti-overinterpretation check

The φ^{-2} atlas constant is not, by itself, an invariant of RH.  If one changes the
horizontal density/aspect ratio of the affine atlas, the uniform pseudohyperbolic radius
changes.  For normalized horizontal half-width h and scale ratio b,

  r²(q)= [h²+(q-1)²]/[h²+(q+1)²],   q∈[1,b],

and the worst case lies at an endpoint.  The standard h=1 Whitney choice gives r=1/sqrt(5)
at q=1 and hence φ^{-2}.  Denser horizontal sampling improves the constant.

Therefore the atlas occurrence alone is coordinate/design dependent.

The Schur/reciprocal composition is more interesting because the unit translation is
forced algebraically by the Sherman--Morrison formulas.  The unresolved question is
whether the reciprocal duality acts on that *same* scalar.

### 7. Concrete next experiment

Define the parity boundary scalar x from the exact finite CCM/Schur reduction, transform to
y=2/x, and compute the action of:

* functional-equation reflection,
* pole-plane Hodge duality,
* radical continuation,
* BPY exchange J,

on y.

If any one acts as y→1/y (equivalently x→4/x), then the completed two-step boundary dynamics
is exactly

  y→1+1/y,

with stable fixed point φ and contraction φ^{-2}.

That would make the golden ratio structural rather than merely an atlas-conditioning
constant.

Lean target started in:
  GppVerify/RiemannHypothesis/GoldenMobiusAudit.lean

No RH proof is claimed here.


### 8. Stronger hyperbolic-geometric identification

There is an exact geometric reason the same constant occurs in the dyadic atlas and in
golden dynamics.

A real 2x2 matrix of negative determinant acts on the upper half-plane as an
orientation-reversing isometry by inserting complex conjugation.  For the golden matrix

  M = [[1,1],[1,0]],

the corresponding upper-half-plane isometry is

  g(z) = (conj(z)+1)/conj(z) = 1 + 1/conj(z).

Its boundary action is exactly

  x -> 1 + 1/x.

At the normalized center of an affine Hardy chart,

  g(i) = 1+i.

But i and 1+i are precisely the center and horizontal edge point of the unit-aspect
normalized Whitney cell used in the dyadic atlas.  Therefore the worst same-height atlas
step is literally one golden Möbius step.

Their hyperbolic distance is

  d_H(i,1+i) = 2 asinh(1/2) = 2 log(phi).

The Cayley pseudohyperbolic radius is

  tanh(d_H/2) = tanh(log phi) = 1/sqrt(5),

and the relative precision margin is

  exp(-d_H) = phi^(-2).

So the chain is exact:

  golden boundary map
    -> normalized Whitney step i -> 1+i
    -> hyperbolic length 2 log phi
    -> Cayley radius 1/sqrt(5)
    -> stable/precision multiplier phi^(-2).

This does not make phi an RH invariant, because changing the atlas aspect ratio changes the
cell displacement.  It does show that the phi^(-2) already present in v34 is the natural
hyperbolic contraction of the *specific standard dyadic Hardy atlas*, not an accidental
algebraic simplification.


### 9. Modular-group interpretation (structural clue, not closure)

The translation T(y)=y+1 is one standard modular generator.  The reciprocal operation
R(y)=1/y is the orientation-reversing partner of the usual modular inversion
S(y)=-1/y.  Therefore the golden word

  G = T R

is an orientation-reversing PGL(2,Z) element.  Its square is

  G^2 = [[2,1],[1,1]] in SL(2,Z),

with trace 3 and eigenvalues phi^2 and phi^(-2).

This is notable because the v34 global automorphic lift already lives on
SL(2,Z)\H through the Eisenstein series.  The same two elementary operations that appear
separately in the RH architecture are therefore the modular generators in disguise:

* the parity Sherman--Morrison boundary update gives T after y=2/x;
* reciprocal/shadow duality would give R;
* the automorphic completion supplies the ambient modular geometry.

The trace-three hyperbolic element G^2 is the discriminant-five / golden geodesic.  Its
stable eigenvalue is phi^(-2), exactly the dyadic Hardy conditioning constant found above.

This suggests a concrete global test: express the completed automorphic boundary/Feshbach
transfer in the same projective impedance coordinate y.  If functional-equation reflection
acts as R and the rank-one pole update acts as T, the completed return map is a modular
word.  The shortest nontrivial hyperbolic word is then the golden one above.

Nothing here proves that the physical return map actually equals G or G^2.  Until that
coordinate identification is established, the modular observation is a structural clue
only.


### 10. The actual completed shadow quotient is reciprocal — and this changes the audit

There is now a direct arithmetic reciprocal, not merely a hypothetical one.

For the centered Cayley coordinate

  beta(s)=(s-1)/s,

functional-equation shadow gives exactly

  beta(1-s)=1/beta(s)

away from s=0,1.

Likewise the manuscript's projective half-density coordinate

  w(s)=exp(2 pi (s-1/2))

satisfies

  w(1-s)=1/w(s).

Most importantly, the actual completed Hardy/de Branges shadow quotient

  Theta_a(z)=F(a+z)/F(a-z)

satisfies identically

  Theta_a(-z)=1/Theta_a(z)

where numerator and denominator are nonzero.  For F=xi and z=it this is the concrete
completed transfer used by the RH Hardy criterion.

So the reciprocal involution itself is genuine arithmetic structure.

### 11. Same-coordinate test: the naive golden closure fails in the natural impedance chart

The remaining question is whether the *unit translation* from the pole Sherman--Morrison
update acts on this same reciprocal coordinate.

The natural linearized Schur/Herglotz impedance of a scalar transfer q is

  m(q)=(1+q)/(1-q).

Under the exact arithmetic shadow q -> 1/q,

  m(1/q) = -m(q).

Thus reciprocal shadow becomes a sign flip in the impedance coordinate.

If the rank-one boundary update is the unit translation m -> m+1, then shadow followed by
feedback gives

  m -> 1-m,

which is an involution, not the golden map.  Its fixed point is 1/2.

This is an important no-go.  The direct argument

  shadow = reciprocal
  and
  Sherman--Morrison = translation
  therefore
  golden map

is valid only if *both operations are written in one and the same projective coordinate*.
In the standard Schur/Herglotz coordinate conversion, they are not: the reciprocal
Schur action becomes sign reversal before the additive rank-one law is applied.

The finite parity pole scalars make the same point.  Functional-equation reflection
exchanges the light-cone pole classes s=0 and s=1.  In the parity basis
c=p+q, s=p-q it acts as c->c, s->-s.  Quadratic parity responses
<c,A^{-1}c> and <s,A^{-1}s> are therefore individually reflection-invariant, not
reciprocated.  So the previously proposed concrete condition x->4/x is not forced by
the existing parity symmetry.

### 12. What survives

Three exact golden facts survive the no-go:

1. the dyadic affine Hardy atlas has exact worst-cell margin phi^{-2};
2. the golden PGL(2,Z) word T R has stable multiplier phi^{-2};
3. the arithmetic shadow really is reciprocal on beta(s), w(s), and Theta.

What is **not** established is that the physical arithmetic rank-one update is T in one of
those reciprocal coordinates.  In the natural Herglotz coordinate it is instead paired
with sign reversal and gives an affine involution.

Therefore the golden ratio should currently be treated as an exact geometric conditioning
constant / modular structural clue, not as the missing RH positivity mechanism.

A genuine revival would require finding a different *arithmetically canonical* projective
coordinate in which:
  (i) completed shadow is reciprocal, and
  (ii) the actual pole/Feshbach update is unit translation.
The coordinate may not be chosen merely to conjugate the maps into that form; it must be
defined independently from the arithmetic operator.


### 13. Stronger result: the canonical Suzuki boundary pair contains the golden word exactly

The previous no-go applies to the Herglotz impedance coordinate. But the Suzuki
0/pi boundary pair has a more primitive homogeneous coordinate in which the golden word
is exact.

Recall the already-proved reflection algebra

  A(-z) = -B(z),
  B(-z) = -A(z).

Define the projective boundary ratio

  q(z)=A(z)/B(z).

Then, wherever A and B are nonzero,

  q(-z)=1/q(z).

Now perform the elementary boundary-frame shear

  (A,B) -> (A+B,B).

On q this acts as

  q -> q+1.

Therefore reflection followed by the unit shear is exactly

  q -> 1 + 1/q.

This is the golden Möbius map, in the SAME projective boundary coordinate.

No zeta input is needed for the identity; it is a theorem of the canonical Suzuki
reflection pair itself. If the reflected-and-sheared boundary ratio is a fixed point,

  q = 1 + 1/q,

then

  q^2=q+1,

and positivity/reality would select q=phi.

This is stronger than the earlier hypothetical x->4/x construction: the reciprocal and
the translation genuinely coexist on one canonical homogeneous boundary ratio.

### 14. Relation to the Sherman--Morrison scalar

There is an exact projective conjugacy explaining the coefficient 2 in the finite pole
formulas.

Write the homogeneous pair as (A,B)=(2,x), so

  q=A/B=2/x.

The unit shear (A,B)->(A+B,B) gives

  (2,x) -> (2+x,x).

Renormalizing the first homogeneous coordinate back to 2 gives

  x -> 2x/(x+2),

which is exactly the odd Sherman--Morrison map.

Likewise swapping the homogeneous coordinates,

  (2,x)->(x,2),

and renormalizing the first coordinate to 2 gives

  x -> 4/x,

exactly the previously introduced poleDual map.

So oddSchur and poleDual are not arbitrary formulas: they are the affine-chart
representatives of unit shear and coordinate swap on a two-dimensional projective
boundary pair.

This makes the remaining identification precise:

  Does the concrete finite CCM pole-response homogeneous pair coincide, after the natural
  residue normalization, with the canonical Suzuki 0/pi boundary pair?

If yes, the golden map is literally the composite arithmetic boundary operation.
If no, the golden structure remains a separate canonical boundary-frame symmetry.

The existing data are suggestive but do not yet prove the identification:
* the finite Weyl response is a ratio of two boundary amplitudes;
* the Suzuki pair is the canonical reflected Weyl pair;
* the pole coefficient 1/2 is exactly what makes the Sherman--Morrison inverse-response
  shift a unit translation.

The next proof target is therefore not another numerical phi match. It is an exact
intertwiner between these two boundary pairs.
