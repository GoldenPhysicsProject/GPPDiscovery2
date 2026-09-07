# Ambidextrous Penrose ray quotients and the LeBrun weight target

Date: 2026-09-07
Status: exact finite GPP algebra + external dual-local-twistor / ambitwistor bundle conventions; global LeBrun identification open

## 1. Mirror Penrose quotient

The ordinary Penrose local-twistor quotient already gave, along a null ray,

`Q_L = T_gamma^aligned / <Z_gamma>`

with a two-dimensional projective/Sturm system.  Under the null-spinor little group

`lambda -> a lambda`, `lambdatilde -> a^{-1} lambdatilde`,

its state has character `a^{-1}`.

The standard dual local-twistor connection gives the mirror construction.  Restrict the primed primary spinor to the ray line

`pi_{A'} = xt lambdatilde_{A'}`

and contract the unprimed secondary component with `lambda` to obtain `pt`.  After a constant phase/sign normalization, the projected mirror equations are

`xt' = pt`,
`pt' = -U xt`,

with the same `U=P(k,k)` up to the global curvature-sign convention.

Thus the dual quotient `Q_R` carries exactly the same projective Sturm generator as `Q_L`.

Under the same little-group action, `Q_R` has the opposite character `a^{+1}`.

Formalized in

`GppVerify/CelestialHolography/AmbidextrousPenroseRayQuotients.lean`

commit `591f362aa217d3aacb0c73eca9abd4e1e4422fc7`.

## 2. Correct neutral tautological twists

With `L_lambda` defined as the actual tautological line spanned by `lambda`, its character is `a^{+1}`.  Therefore

`L_lambda tensor Q_L`

is little-group neutral.

Similarly, the actual line `L_lambdatilde` has character `a^{-1}`, so

`L_lambdatilde tensor Q_R`

is neutral.

This corrects an earlier schematic notation `L_lambda^* tensor Q_L`.  With the above convention for the actual tautological line, the dual is wrong: the line itself cancels the quotient character.

The direct product `Q_L tensor Q_R` is also little-group neutral, but it is rank four and must not be confused with LeBrun's rank-two Einstein bundle.

## 3. Ambidextrous interpretation

At the exact finite level the two one-sided constructions therefore satisfy

`P(Q_L) = P(Q_R) = P(E_projective)`

in the sense that both are the same two-dimensional Sturm/projective carrier after the stated phase convention.

Their vector representatives differ by opposite tautological characters.  There is **no proved canonical isomorphism**

`L_lambda tensor Q_L ≅ L_lambdatilde tensor Q_R`

because the unprimed and primed spinor lines remain genuinely distinct.  A parity/reality/spin structure would be additional geometric data.

This realizes Penrose's TN40 demand for complete symmetry between twistor and dual-twistor variables more faithfully than any attempted pointwise identification `S ≅ S'`.

## 4. Relation to modern projective ambitwistor line bundles

In standard four-dimensional projective ambitwistor space, the redundant anti-diagonal scaling is

`Z -> a Z`, `Ztilde -> a^{-1} Ztilde`.

The modern literature identifies `O(1,-1)` as the global little-group line bundle.  A section of `O(p,q)` has anti-diagonal character `a^(p-q)`.

Hence the present calculation determines only

`p-q = -1` for `Q_L`,
`p-q = +1` for `Q_R`.

It does **not** determine a unique pair `(p,q)`.

The reason is structural: simultaneous scaling of both ray spinors rescales the null tangent and therefore the affine parameter.  The two components `(field, derivative)` of a Sturm state then acquire different diagonal weights.  The ray quotient is therefore better thought of as a weighted first-jet / projective-connection solution system than as two copies of one scalar line bundle.

This is the next formal target.

## 5. LeBrun / Eastwood caution

The generic LeBrun construction over complex ambitwistor space has a standard **rank-two** holomorphic Einstein bundle `E -> G`, with nonzero holomorphic sections corresponding to Einstein representatives.

The right-flat nonlinear-graviton literature also contains formulas such as

`E ≅ Omega^1 P tensor L^{-2} ≅ J^vee tensor L^{-1}`.

Those are one-sided/right-flat specializations with different rank bookkeeping; they must not be mechanically identified with the generic rank-two ambitwistor bundle or the present two-dimensional ray quotient.

A historically important clue nevertheless survives: Eastwood/Penrose-era constructions repeatedly involve **twisted** forms, projective spinor homogeneity, and extra scale factors.  The new little-group calculation shows that such twists are not optional bookkeeping: the raw Penrose quotient really is weighted.

## 6. Current target

The corrected bundle-level problem is

`glue(L_lambda tensor Q_L) ?= glue(L_lambdatilde tensor Q_R) ?= E_LeBrun`

with the following unresolved pieces:

1. determine the full weighted-jet / diagonal reparametrization law;
2. recover the complete holomorphic transition data, not only the anti-diagonal character;
3. prove sky/NSF metricity gives transverse descent across neighboring rays;
4. compare that descent with LeBrun's correspondence-space kernel construction;
5. identify the resulting rank-two holomorphic bundle with generic `E`.

Main formal spine updated at commit `8930aa2d3faf7a3794fca61836ccb37fc22178af`.

No CI certification claimed.
