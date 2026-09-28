# KMS metric route to the missing simple-even theorem for finite Weil ground states

Date: 2026-09-28
Status: exact abstract implication plus a concrete arithmetic target. No claim that the required metric identity has yet been proved for the actual CCM/Weil matrices.

The 2025 zeta-spectral-triple construction has two explicit missing steps. The first is to prove that the smallest finite Weil eigenvalue is simple and its eigenvector is even. The current GPP parity formalization already contains the determinant-ratio machinery needed for this once one has a positive cross-resolvent below the even ground.

The critical Bost--Connes KMS metric suggests a direct way to manufacture that positivity.

## 1. Existing cross-resolvent identity

For the parity blocks \(A_+\) (even) and \(A_-\) (odd), the verified rank-one Sylvester structure yields a determinant ratio of the form
\[
\boxed{
\frac{\det(A_--z)}
{\det(A_+-z)}
=
f(z),
}
\]
where
\[
f(z)
=
\eta^\dagger(A_+-z)^{-1}e_0
\]
in the coordinate model.

The current Lean thread proves abstractly:
- if \(f(z)>0\) for every real \(z<\lambda_{\min}(A_+)\), then the odd block has no eigenvalue below the even ground;
- with the no-common-eigenvalue boundary condition, the odd ground lies strictly above the even ground;
- positive residues give strict parity interlacing.

The missing arithmetic input is positivity of this cross-resolvent.

## 2. A positive metric makes the cross-resolvent a genuine Weyl function

Suppose there exists a positive-definite metric operator \(G\) on the finite even space such that
\[
\boxed{
GA_+=A_+^\dagger G
}
\]
and
\[
\boxed{
Ge_0=\eta.
}
\]

Then
\[
f(z)
=
\eta^\dagger(A_+-z)^{-1}e_0
=
\langle e_0,(A_+-z)^{-1}e_0\rangle_G
\]
up to the fixed convention for linear/antilinear slots.

For real
\[
z<\lambda_{\min}(A_+),
\]
the operator \(A_+-z\) is strictly positive in the \(G\)-Hilbert structure, so
\[
\boxed{
f(z)>0.
}
\]

Moreover its spectral representation is
\[
f(z)
=
\sum_j
\frac{|\langle e_j,e_0\rangle_G|^2}
{\lambda_j-z},
\]
so every residue is nonnegative, and strictly positive whenever the boundary vector is cyclic.

Thus the entire parity/interlacing package follows from ONE positive metric identity.

## 3. Why the naive metric search failed and why KMS may repair it

Earlier finite-matrix experiments searched for a generic positive commuting metric in the raw CCM basis. That route failed: some actual arithmetic cross-resolvent residues change sign, so no universal positive metric of the naive commuting form exists.

This does NOT kill the metric mechanism.

The correct metric is not expected to be an arbitrary Euclidean reweighting of the already-scalarized CCM matrix. The current programme has since identified the critical KMS midpoint Hilbert form BEFORE scalarization:
\[
\langle\mu_m,\mu_n\rangle_{\rm mid}
=
\delta_{mn}n^{-1/2},
\]
and, after including the additive \(ax+b\) channel, its finite Gram operators are exactly the divisibility projectors.

Therefore the correct test is:

\[
\boxed{
\text{Does the full finite Bost--Connes KMS Gram, transported into the even Weil block, satisfy }
G_{\rm KMS}e_0=\eta
\text{ and symmetrize the cross-resolvent pencil?}
}
\]

This is a materially different question from the already-killed raw commuting-metric ansatz.

## 4. Modular theory explains the desired boundary-vector relation

In a KMS standard form, imaginary half-time naturally identifies an operator with its reflected adjoint channel. The arithmetic half-density
\[
n^{-1/2}
\]
is exactly the modular midpoint coefficient.

The finite Weil cross-resolvent couples:
- the vacuum/boundary vector \(e_0\);
- the displacement functional \(\eta\);
- even and odd parity blocks.

So \(Ge_0=\eta\) is precisely the finite-dimensional shadow of the desired OS/KMS statement:
\[
\boxed{
\text{reflected boundary functional}
=
\text{KMS Riesz representative of the vacuum boundary vector}.
}
\]

If true, the cross-resolvent becomes a standard positive Weyl function rather than an indefinite scalar matrix element.

## 5. Consequence for the two missing spectral-triple steps

If the KMS metric identity holds and the boundary vector is cyclic:

1. the even and odd eigenvalues strictly interlace;
2. the parity ground ordering is fixed;
3. the lowest state is simple and lies in the even sector.

That settles the FIRST missing step of the zeta-spectral-triple programme.

The SECOND missing step is then attacked by the vacuum-gap criterion:
\[
\|u_\lambda-k_\lambda\|^2
\le
2\epsilon_\lambda/\Delta_\lambda.
\]

Strict interlacing plus quantitative residue control supplies the finite excitation gap \(\Delta_\lambda\), while prolate/Riemann tail estimates supply \(\epsilon_\lambda\).

Thus the same KMS cross-resolvent mechanism could settle both missing steps in sequence.

## 6. Quantitative version required

Positivity alone gives ordering but not the lower bound needed for vacuum convergence.

From
\[
f(z)=\sum_j\frac{c_j}{\lambda_j-z},
\qquad c_j>0,
\]
one must obtain explicit lower control on the first pole/zero separation.

The arithmetic target is therefore:
- prove \(c_0\) is not super-exponentially smaller than the Riemann-tail scale;
- bound the regular remainder of \(f\) near the ground pole;
- deduce a lower bound for the first parity/interlacing gap.

Even a polynomial relative gap
\[
\Delta_\lambda
\gtrsim
\lambda^4\epsilon_\lambda
\]
would be sufficient by the edge-derivative hierarchy.

## 7. Immediate falsifier

At each finite cutoff, transport the explicitly known critical \(ax+b\) KMS Gram into the CCM parity basis and numerically check:
\[
\|G_{\rm KMS}A_+-A_+^\dagger G_{\rm KMS}\|,
\qquad
\|G_{\rm KMS}e_0-\eta\|.
\]

If these do not tend to zero under the correct finite-level embedding, this KMS-metric realization is wrong and should be abandoned.

If they vanish exactly (or by a provable projection identity), the missing cross-resolvent positivity theorem becomes ordinary spectral theory.
