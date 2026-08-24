# Honest four-dimensional MHV two-particle cuts: Yang--Mills and gravity

Codex/GPT discovery track, 2026-08-24.

## Scope

This note moves beyond the scalar-box numerator without assuming box-only reduction. It records the first honest helicity-dependent two-particle cut in the four-point MHV sector and the corresponding gravity cut obtained tree-by-tree through KLT/double copy. It is a four-dimensional cut statement. It does **not** capture D-dimensional `mu^2` information responsible for rational terms in nonsupersymmetric Yang--Mills or pure Einstein gravity.

All amplitudes below are color-stripped and all momenta are outgoing at each tree. Overall factors of the gauge coupling and `kappa/2` are suppressed until explicitly restored.

## Yang--Mills s-channel cut

Take external helicities

`1^- 2^- 3^+ 4^+`.

Choose the cut routing so that `ell_1,ell_2` are outgoing from the left tree. Then the correct momentum-conservation equations are

`p_1+p_2+ell_1+ell_2=0`,

and

`-ell_1-ell_2+p_3+p_4=0`.

Equivalently `ell_1+ell_2=-(p_1+p_2)=p_3+p_4`. An earlier version of this note wrote `ell_1+ell_2=p_1+p_2` while simultaneously declaring all tree momenta outgoing; that sign was inconsistent and is corrected here.

The cut is

`C_s^YM = sum_{h1,h2=+/-} A_L(1^-,2^-,ell_2^{h2},ell_1^{h1}) A_R((-ell_1)^{-h1},(-ell_2)^{-h2},3^+,4^+)`.

At four points a nonzero all-gluon tree has two negative helicities (MHV) or, by parity, two positive helicities. Since the left tree already contains `1^- 2^-`, its two cut legs must be positive. Since the right tree contains `3^+ 4^+`, its two crossed cut legs must be negative. Thus the four-dimensional internal-gluon helicity sum collapses to a single assignment:

`(h1,h2)=(+,+)` on the left, crossed to `(-,-)` on the right.

Therefore

`C_s^YM = A_4^tree(1^-,2^-,ell_2^+,ell_1^+) A_4^tree((-ell_1)^-,(-ell_2)^-,3^+,4^+)`.

Using Parke--Taylor,

`A_L = i <12>^4 / (<12><2 ell_2><ell_2 ell_1><ell_1 1>)`,

and

`A_R = i <(-ell_1)(-ell_2)>^4 / (<(-ell_1)(-ell_2)><(-ell_2)3><34><4(-ell_1)>)`.

A convention-consistent spinor simplification using the two cut momentum-conservation equations gives the standard scalar-box-cut form

`C_s^YM = -i A_4^tree(1^-,2^-,3^+,4^+) * s*t / (D_1 D_2)`,

for the routing

`D_1=(ell_1+p_1)^2`,

`D_2=(ell_1-p_4)^2`,

with `s=(p_1+p_2)^2` and `t=(p_2+p_3)^2`. The overall `i`/sign changes if a different amplitude or cut-propagator convention is adopted; the invariant content is that the helicity numerator on this cut is exactly the external MHV tree times `s t`, while the loop-momentum dependence is entirely the pair of uncut scalar propagators.

Thus in this specific four-dimensional gluon MHV cut one genuinely recovers the scalar-box cut structure from the helicity trees rather than inserting it by hand:

`(helicity cut)/(external tree) proportional to s*t/(D_1 D_2)`.

A direct numerical spinor-helicity audit over multiple external and cut scattering angles verifies the displayed identity to floating-point precision; the accompanying `mhv_cut_audit.py` records that check. The identity itself follows algebraically from Parke--Taylor plus momentum conservation; the numerical audit is not being used as the proof.

This does **not** imply that the complete pure-Yang--Mills one-loop amplitude is box-only: triangles, bubbles and rational terms are not excluded by one two-particle cut, and four-dimensional cuts miss the `mu^2` information that controls rational pieces.

## Gravity cut from tree-level KLT

For four gravitons with helicities

`1^{--} 2^{--} 3^{++} 4^{++}`,

four-dimensional helicity selection again leaves one internal graviton assignment: the left tree carries two positive-helicity cut gravitons and the right tree carries the crossed negative-helicity gravitons.

Use the stripped four-point KLT relation

`M_4^tree(1,2,3,4) = -i s_12 A_4^tree(1,2,3,4) A_4^tree(1,2,4,3)`

(up to the conventional overall `(kappa/2)^2` factor). Then the gravity cut is

`C_s^GR = M_L(1^{--},2^{--},ell_2^{++},ell_1^{++}) M_R((-ell_1)^{--},(-ell_2)^{--},3^{++},4^{++})`,

with each `M_L,M_R` replaced by its own KLT bilinear. This is the correct cut-level double copy. It is **not** the statement that a single color ordering of the Yang--Mills cut should simply be squared.

The next gravity calculation is to simplify the KLT product into external four-graviton tree times its explicit cut rational function, keeping both Yang--Mills orderings visible until the KLT Mandelstam factors are combined.

## What is and is not established

Established at discovery level:

1. In the four-dimensional four-point MHV sector the pure-gluon two-particle helicity sum has exactly one nonzero assignment.
2. The Yang--Mills cut is therefore exactly a product of two Parke--Taylor trees.
3. That product simplifies, for the routing above, to `-i A_tree * s*t/(D_1 D_2)`: the scalar-box cut structure and `s t` helicity numerator are derived from the trees rather than assumed.
4. The corresponding gravity cut is exactly the product of two four-graviton trees and admits a tree-by-tree KLT representation.

Not established here:

1. A reduction of the pure-Yang--Mills one-loop amplitude to boxes only. Such a statement is false in generic nonsupersymmetric Yang--Mills because triangles, bubbles and rational terms occur.
2. Recovery of rational terms from this four-dimensional cut. D-dimensional unitarity or an equivalent `mu^2` bookkeeping is required.
3. A box-only claim for generic pure Einstein gravity. No-triangle behavior is theory- and sector-dependent and cannot be assumed here.
4. The celestial transform of these helicity numerators.

## Immediate next calculation

1. Simplify the gravity KLT cut against the external four-graviton tree.
2. Repeat Yang--Mills with `D=4-2 epsilon` loop momentum `L=ell+mu`, so that `mu^2`-dependent terms are visible before dispersion/celestial transformation.
3. Feed the derived four-dimensional `s t` numerator into the already-closed scalar dispersion/regulator geometry as the first honest helicity-weighted celestial cut.
