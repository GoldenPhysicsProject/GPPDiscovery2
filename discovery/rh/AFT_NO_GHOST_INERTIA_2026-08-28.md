# AFT no-ghost inertia obstruction

Date: 2026-08-28

## Result

The exact zero-side quartet model in the arithmetic principal-series work shows that an off-critical quartet contributes an indefinite rank-two block

\[
2\bigl(u\otimes u-v\otimes v\bigr),
\]

with

\[
u(t)=e^{-At}\cos Bt,\qquad v(t)=e^{-At}\sin Bt,
\]

where, for a centered zero \(\zeta=\delta+i\gamma\),

\[
A=\gamma^2-\delta^2,\qquad B=-2\delta\gamma.
\]

The negative channel disappears exactly when \(B=0\), hence for a nonreal zero exactly when \(\delta=0\), i.e. on the critical line.

This gives a decisive constraint on the new Fisher/Gamma idea. A strictly positive change of ambient metric cannot by itself remove the negative channel. At the schematic level

\[
q(x,y)=x^2-y^2
\]

remains indefinite after any strictly positive scalar reweighting, and also after positive diagonal reweighting

\[
q_{a,b}(x,y)=a x^2-b y^2,\qquad a,b>0,
\]

because the pure odd vector \((0,1)\) still has negative norm.

Therefore the exact Fisher/Gamma kernel

\[
\kappa_{2\pi}(\lambda)=|\Gamma(1+i\lambda)|^2>0
\]

can provide the **ambient positive Hilbert metric** and can flatten the Archimedean Plancherel weight, but it cannot prove RH merely by positive reweighting of an already indefinite completed arithmetic form.

The only remaining viable mechanism is genuinely cohomological:

\[
\boxed{
\text{the odd channel must become exact/null and be quotiented out.}
}
\]

Equivalently, AFT needs a true arithmetic no-ghost theorem, not just a better positive kernel.

## Consequence for the construction

This sharpens the architecture:

1. Fisher/Gamma/KL builds the positive ambient one-particle metric at the real place.
2. Dirichlet heat boundary anomalies build the zero-independent prime block with exact von Mangoldt coefficients.
3. The prime--Archimedean completion is a relative trace/supertrace.
4. The Tate boundary cokernel is the correct odd ghost model.
5. AFT must construct a differential/boundary condition for which the bad odd sector is exact or null in physical cohomology.
6. Only after that quotient can the surviving heat trace be positive and yield the arithmetic OS criterion.

This also rules out a tempting but insufficient strategy: multiplying the Weil form, quartet block, or relative trace by the positive Fisher/Gamma response cannot change the inertia of an existing finite-dimensional ghost block when the reweighting is nondegenerate.

## Formalization

Added to GPPVerify2:

`GppVerify/CelestialHolography/ArithmeticNoGhostInertia.lean`

It proves the finite algebraic statement that strictly positive scalar or diagonal reweighting preserves the negative pure-odd direction of the model ghost form.

## Status

No RH proof. The result is a useful obstruction because it removes an entire class of false closure attempts and makes the required theorem more precise: **construct the quotient**, not merely the metric.
