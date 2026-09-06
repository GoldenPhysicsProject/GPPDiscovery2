# Null-surface Einstein-bundle equation and transverse gluing

Date: 2026-09-05
Status: exact scalar ODE bridge formalized; NSF equivalence/metricity and holonomy structure are external literature; identification with LeBrun's holomorphic Einstein bundle remains open

## 1. Null-surface formulation supplies the missing real transverse gluing

The null-surface formulation (NSF) of general relativity uses a cut/null-surface function `Z(x,zeta,zetaBar)` and a conformal scale `Omega` on the bundle of null directions.  The null coordinates are generated from

`u = Z`, `omega = eth Z`, `omegaBar = ethBar Z`, `r = eth ethBar Z`.

For fixed ray labels and varying `r`, one moves along a null geodesic of the conformal metric `h`; `r` is affine for `h`.

The physical metric is written contravariantly as

`g^{ab} = Omega^2 h^{ab}`,

so covariantly `g_ab = Omega^{-2} h_ab`.  Thus `Omega` is exactly a conformal scale relative to `h`.

The vacuum/trace-free Einstein equation reduces along the null ray to the linear second-order scalar equation

`2 Omega_{,rr} = R_rr^NSF[h] Omega`.

Meanwhile the null contraction of the standard almost-Einstein scale equation is

`Omega'' + P_rr^std[h] Omega = 0`,

with `P_rr^std = Ric_rr^std/2` in four dimensions because the metric trace term vanishes on a null vector.

Hence the equations coincide under the explicit curvature-sign bridge

`R_rr^NSF = - Ric_rr^std`.

The sign is convention-dependent and is therefore kept explicit rather than silently identified.

Lean module:

`GppVerify/CelestialHolography/NullSurfaceEinsteinBundleBridge.lean`

commit `11b4a5dc017479d6eb0e7301e20cba4262e91d2e`.

It proves only the scalar coefficient identity; no differential-geometric equivalence is hidden in Lean.

## 2. NSF metricity is exactly the kind of transverse gluing GPP had isolated

NSF has two metricity conditions in addition to the raywise Einstein ODE.  The literature emphasizes that they are kinematical requirements ensuring the `S^2`-worth of null-direction-dependent metric data actually comes from one conformal spacetime metric and is independent of the celestial label.

This is structurally the same obstruction isolated in the GPP sky/Einstein-bundle programme:

- a second-order ODE gives a two-dimensional solution space on each null ray;
- arbitrary independent choices on each ray are too much data;
- a transverse compatibility condition across neighboring rays/skies is required to glue the raywise fibres into one geometric object.

NSF supplies such compatibility at the real smooth level through its metricity equations.

Therefore the real-smooth transverse gluing problem is not open in principle.  What remains is to translate this gluing into the intrinsic complex/holomorphic ambitwistor language and prove agreement with LeBrun's Einstein bundle.

## 3. Historical caution: 'Einstein bundle equation' is not evidence of LeBrun identity

Older NSF literature refers to the second-order conformal-factor ODE as the 'Einstein bundle equation', but the cited source traces this terminology to Kozameh--Newman work from 1984, before LeBrun's 1985 ambitwistor Einstein-bundle construction.

Therefore the shared phrase must NOT be used as historical proof that the NSF rank-two solution bundle and LeBrun's holomorphic `E -> G` were already identified.

The mathematical comparison is independent:

`E_NSF,gamma := {Omega(r) solving the null-surface scale ODE along gamma}`

is rank two over each null ray, and the NSF metricity equations provide transverse compatibility.

Current candidate chain:

`E_sky  ?=  E_NSF  ?=  E_LeBrun`.

The first arrow now has strong evidence from the identical projective/Sturm equation plus sky/cut correspondence; the second requires complexification, conformal-weight matching, holomorphic descent, and comparison with LeBrun's correspondence-space sheaf/operator definition.

## 4. Full nonlinear chiral architecture: both halves on one common geometry

Iyer--Kozameh--Newman, arXiv:gr-qc/9502020, explicitly decompose the Lorentz/O(3,1) connection into self-dual and anti-self-dual parts

`gamma = gamma^+ + gamma^-`.

They likewise split curvature by spacetime duality and internal duality into four blocks

`F = ^+F^+ + ^+F^- + ^-F^+ + ^-F^-`.

They state that the Einstein equations are almost encoded by the mixed-block vanishing

`^+F^- = ^-F^+ = 0`,

with an appropriate restriction/soldering of data.  The surviving `^+F^+` and `^-F^-` sectors and their respective connections are treated simultaneously on the same asymptotically flat gravitational background, and a soldering form identifies the Lorentz bundle with the spacetime tangent geometry.

This is a powerful external nonlinear benchmark for the GPP statement:

`one common null/conformal geometry + both chiral sectors + mixed-block/soldering constraints`.

It does NOT show that one generic chirality can be derived from the other.  On the contrary, it is consistent with GPP's no-go result that a full generic field cannot be manufactured from one pure chiral sector by Fourier/orientation relabelling alone.

## 5. Relation to the sky-Jacobi result

The modern sky-Jacobi construction gives an intrinsic projective structure along each null ray.  Its rank-two Sturm linearization matches the null almost-Einstein equation.  The split `(2,2)` working slice is signature-safe at the required level: the flat sky velocity form is `(1,1)`, nondegenerate but indefinite, so the curve is regular (sufficient for the original projective-structure theorem) even though not monotone/definite.

Thus the current real-smooth picture is:

`(N,H,Sigma)`

→ sky Jacobi/projective structure on every ray

→ rank-two projective/Sturm solution system `E_sky`

→ same scalar equation as NSF conformal scale `E_NSF`

→ NSF metricity gives transverse gluing into one spacetime metric

→ orientation reversal fixes the ray/sky geometry and swaps the two Hodge/Weyl labels

→ both nonlinear chiral connection sectors coexist on the same geometry.

## 6. Remaining hard theorem

The remaining googly closure is now sharply localized:

1. construct/complexify the sky/NSF rank-two system as a holomorphic bundle over complex null-geodesic/ambitwistor space;
2. prove its correspondence-space pullback and conformal weight agree with LeBrun's Einstein bundle;
3. identify the NSF metricity/transverse compatibility with the holomorphic descent/gluing condition;
4. then determine how the already-separated parity/Pin/Fourier/celestial operations act on that full bundle without collapsing them into one another.

This is substantially narrower than the original search for a pointwise `PT -> PT*` googly map.
