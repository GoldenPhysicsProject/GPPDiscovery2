# Honest four-dimensional MHV two-particle cuts: Yang--Mills and gravity

Codex/GPT discovery track, 2026-08-24.

## Scope

This note moves beyond the scalar-box numerator without assuming box-only reduction. It records the first honest helicity-dependent two-particle cut in the four-point MHV sector and the corresponding gravity cut obtained tree-by-tree through KLT/double copy. It is a four-dimensional cut statement. It does **not** capture D-dimensional `mu^2` information responsible for rational terms in nonsupersymmetric Yang--Mills or pure Einstein gravity.

All amplitudes below are color-stripped and all momenta are outgoing at each tree. Overall factors of the gauge coupling and `kappa/2` are suppressed until explicitly restored.

## Yang--Mills s-channel cut

Take external helicities

`1^- 2^- 3^+ 4^+`

and on-shell cut momenta `ell_1^2=ell_2^2=0` with `ell_1+ell_2=p_1+p_2`. In a standard crossing convention the cut is

`C_s^YM = sum_{h1,h2=+/-} A_L(1^-,2^-,ell_2^{h2},ell_1^{h1}) A_R((-ell_1)^{-h1},(-ell_2)^{-h2},3^+,4^+)`.

At four points a nonzero gluon tree has two negative helicities (MHV) or, equivalently by parity, two positive helicities. Since the left tree already contains `1^- 2^-`, its two cut legs must be positive. Since the right tree contains `3^+ 4^+`, its two cut legs must be negative. Thus the four-dimensional internal-helicity sum collapses to a single assignment:

`(h1,h2)=(+,+)` on the left, crossed to `(-,-)` on the right.

Therefore

`C_s^YM = A_4^tree(1^-,2^-,ell_2^+,ell_1^+) A_4^tree((-ell_1)^-,(-ell_2)^-,3^+,4^+)`.

Using Parke--Taylor,

`A_L = i <12>^4 / (<12><2 ell_2><ell_2 ell_1><ell_1 1>)`,

and

`A_R = i <(-ell_1)(-ell_2)>^4 / (<(-ell_1)(-ell_2)><(-ell_2)3><34><4(-ell_1)>)`.

Hence the exact cut integrand is their product. The phase associated with choosing spinors for `-ell` is convention-dependent but cancels from any convention-consistent physical cut. This expression is already an honest helicity numerator: no scalar numerator has been inserted and no integral basis has been assumed.

The next algebraic target is to simplify this product against the external Parke--Taylor amplitude and identify its dependence on the two uncut propagators. That simplification must be done before claiming a scalar-box coefficient.

## Gravity cut from tree-level KLT

For four gravitons with helicities

`1^{--} 2^{--} 3^{++} 4^{++}`,

four-dimensional helicity selection again leaves one internal graviton assignment: the left tree carries two positive-helicity cut gravitons and the right tree carries the crossed negative-helicity gravitons.

Use the stripped four-point KLT relation

`M_4^tree(1,2,3,4) = -i s_12 A_4^tree(1,2,3,4) A_4^tree(1,2,4,3)`

(up to the conventional overall `(kappa/2)^2` factor). Then the gravity cut is

`C_s^GR = M_L(1^{--},2^{--},ell_2^{++},ell_1^{++}) M_R((-ell_1)^{--},(-ell_2)^{--},3^{++},4^{++})`,

with each `M_L,M_R` replaced by its own KLT bilinear. This is the correct cut-level double copy. It is **not** the statement that a single color ordering of the Yang--Mills cut should simply be squared.

## What is and is not established

Established at discovery level:

1. In the four-dimensional four-point MHV sector the pure-gluon two-particle helicity sum has exactly one nonzero assignment.
2. The Yang--Mills cut is therefore exactly a product of two Parke--Taylor trees, written above.
3. The corresponding gravity cut is exactly the product of two four-graviton trees and admits a tree-by-tree KLT representation.

Not established here:

1. A reduction of the pure-Yang--Mills one-loop amplitude to boxes only. Such a statement is false in generic nonsupersymmetric Yang--Mills because triangles, bubbles and rational terms occur.
2. Recovery of rational terms from this four-dimensional cut. D-dimensional unitarity or an equivalent `mu^2` bookkeeping is required.
3. A box-only claim for generic pure Einstein gravity. No-triangle behavior is theory- and sector-dependent and cannot be assumed here.
4. The celestial transform of these helicity numerators. That is the next bridge after the momentum-space cut has been simplified and checked.

## Immediate next calculation

Simplify the Yang--Mills product on the cut to

`A_4^tree(1^-,2^-,3^+,4^+) x R_s(ell_1,ell_2)`

for an explicit rational spinor function `R_s`. Then compare `R_s` with the scalar-box cut denominator. Separately, repeat the calculation with `D=4-2 epsilon` loop momentum `L=ell+mu` so that `mu^2`-dependent terms are visible before dispersion/celestial transformation.
