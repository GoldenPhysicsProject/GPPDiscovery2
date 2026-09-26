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
