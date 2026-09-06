# Codex/GPT research rotation — 2026-09-06 11:28Z

Scope: Codex/GPT lane only. No Claude-owned files, branches, notes, or records inspected.

## Verify2 / continuous Gamma chamber

Cold changed-Lean #928 failed on the lower crossing theorem while full Build #2074 passed. The quotient-normalization proof was replaced by the already-certified defect identity

\[
F_c(x)-1=\frac{2x^2-c}{c(2c+1)}
\]

and positivity of the denominator, using `div_neg_iff_of_pos_right`. Verify2 repair commit: `525fba354de93f15f356097b6b8d918cef4c4a95`.

The continuous-to-discrete bridge was then added at Verify2 commit `3031828459b8cb8043676ae92c1376a63d6f03e8`:

\[
F_{k+1}(x)=\operatorname{rhoStepFactor}(k,x),\qquad F_c(x)>0\quad(c>0).
\]

Fresh cold/full CI is pending on the new head.

## Yang–Mills full-conic physical residue normalization

New exact identity on the existing full stereographic tree chart. With

\[
q=r^2+u^2+v^2,
\]

the unique angle-dependent adjacent cubic propagator is exactly

\[
p_{12}^2=p_{34}^2
=-\frac{4E^2 q}{(1+r^2)(1+u^2+v^2)}.
\]

On the triple-cut conic `q=0`, where `u^2+v^2=-r^2`, the ratio has the finite, surviving-coordinate-independent limit

\[
\frac{p_{12}^2}{q}\Big|_{q=0}
=-\frac{4E^2}{1-r^4}.
\]

Therefore every full-conic transverse q-residue has a fixed physical propagator normalization

\[
[p_{12}^2 A]_{q=0}
=-\frac{4E^2}{1-r^4}[qA]_{q=0}.
\]

This removes one normalization ambiguity before physical sewing. It does **not** construct the opposite crossed tree, perform factor-preserving topology subtraction, or produce a master coefficient.

Executable audit: `discovery/generalized_cuts/full_conic_physical_propagator_normalization_audit.py`, created at `bf8fcd9106332c5604419d8bea2190ffca87bcfa` and added to the Ds=4 YM baseline workflow at `7e4f6666b251051e3825dc55311677f182df9348`. Discovery CI #30 is running.

## Other active fronts

- Scalar celestial cut -> dispersion -> raised-box regulator endpoint remains closed: `J_epsilon(S,T) -> 1/6`.
- Prime-gas normalized countable quadratic fluctuation geometry remains certified at `R(beta,eta)<1/2` for real beta and eta>0. No stronger bound promoted this rotation.
- Principal-series / completed-zeta / Weil boundary unchanged: Delta=2s and critical-line tangent-response statements remain formal; the missing RH-critical theorem is unconditional positivity/PSD of the completed prime-plus-Archimedean explicit-formula/Weil form.
- Continuous Gamma/Mehler–Fock front: next analytic formalization boundary remains the arbitrary-c normalized density/heat-mixture convolution semigroup; the new `F_{k+1}=rhoStepFactor(k)` theorem ties the continuous chamber algebra directly to the existing integer Lean hierarchy.

## Next frontier

1. Terminal Verify2 cold/full CI on `3031828459b8cb8043676ae92c1376a63d6f03e8`; repair any cold failure.
2. Terminal Discovery CI #30 for the physical propagator normalization audit.
3. Construct the factor-preserving opposite full-conic crossed tree with uncut denominators retained, then form honest `C^(4)=C^(V_m)-C^(S)` and only afterward perform Badger topology subtraction/large-z extraction.
4. Lean-promote the arbitrary-c heat-mixture convolution semigroup separately from Gamma-density identification.
