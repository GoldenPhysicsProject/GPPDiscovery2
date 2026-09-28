# Pullback-metric theorem: replace the KMS metric search by one ambient self-adjoint intertwiner

Date: 2026-09-28
Status: exact abstract operator lemma plus a concrete arithmetic target. No RH claim.

The current finite simple-even theorem asks for a positive metric \(G\) on the finite even Weil block such that
\[
GA_+=A_+^*G,
\qquad
Ge_0=\eta.
\]

The finite self-dual divisor geometry suggests a better way to obtain BOTH identities at once.

## 1. Abstract pullback theorem

Let \(V\) be the finite even Weil coordinate space and \(\mathcal H\) a Hilbert space.

Suppose
\[
B:V\to\mathcal H
\]
is injective and
\[
\widetilde A=\widetilde A^*
\]
is self-adjoint on \(\mathcal H\), with the intertwining relation
\[
\boxed{
BA_+=\widetilde A B.
}
\]

Define
\[
\boxed{
G=B^*B.
}
\]

Then \(G>0\) and
\[
\begin{aligned}
GA_+
&=
B^*BA_+\\
&=
B^*\widetilde A B\\
&=
A_+^*B^*B\\
&=
\boxed{
A_+^*G.
}
\end{aligned}
\]

So the metric-symmetrization condition is automatic.

Now suppose the cross-resolvent displacement vector is represented by the SAME ambient boundary state:
\[
b=Be_0,
\qquad
\eta=B^*b.
\]
Then
\[
\boxed{
\eta=B^*Be_0=Ge_0.
}
\]

Therefore the two previously separate KMS metric identities reduce to ONE geometric statement:

> Find an injective arithmetic embedding \(B\) of the even Weil block into a genuinely self-adjoint ambient self-dual system, such that the finite Weil pencil is intertwined with the ambient operator and the displacement functional is the Riesz pullback of the vacuum boundary state.

## 2. Why the finite divisor/KMS geometry supplies the natural ambient Hilbert space

At primorial/prime-power cutoff, the normalized subgroup states
\[
v_d
=
|H_d|^{-1/2}\mathbf1_{H_d}
\subset
\ell^2(\mathbb Z/N\mathbb Z)
\]
have Gram
\[
\langle v_d,v_e\rangle
=
\frac{\gcd(d,e)}{\sqrt{de}},
\]
exactly the critical KMS/TFD metric.

Thus if the finite Weil block is obtained by transporting the critical arithmetic transfer through these subgroup states, the desired metric is not an unknown matrix:
\[
\boxed{
G_{\rm KMS}=B^*B
}
\]
is simply the pullback of the ordinary positive \(\ell^2(\mathbb Z/N\mathbb Z)\) metric.

Fourier self-duality is already unitary in the ambient space:
\[
\mathcal F_Nv_d=v_{N/d}.
\]

So the positivity that looked mysterious after scalarization is automatic before scalarization.

## 3. Candidate arithmetic embedding

The continuous critical arithmetic map is
\[
\mathcal E
=
Z_{\rm crit}
=
\sum_{n\ge1}n^{-1/2}U_n,
\]
with the exact sewing relation
\[
Z_{\rm crit}\mathcal F=JZ_{\rm crit}.
\]

At finite divisor cutoff, the subgroup-state synthesis map
\[
B_N:
(c_d)_{d\mid N}
\longmapsto
\sum_{d\mid N}c_dv_d
\]
has
\[
B_N^*B_N=K_N,
\]
the critical GCD/KMS Gram.

This is the finite algebraic shadow of \(Z_{\rm crit}\).

The next concrete task is to compose the finite Fourier/Weil projection with \(B_N\) and test whether the resulting map intertwines the finite even Weil operator with an ambient self-adjoint compression.

## 4. Consequence for the cross-resolvent

If the intertwiner exists, then for real \(z\) below the even ground,
\[
\begin{aligned}
f(z)
&=
\eta^*(A_+-z)^{-1}e_0\\
&=
\langle Be_0,
(\widetilde A-z)^{-1}
Be_0\rangle_{\mathcal H}.
\end{aligned}
\]

Hence
\[
\boxed{
f(z)>0
}
\]
and every spectral residue is nonnegative.

Strict positivity/cyclicity then gives the simple-even ground and strict parity interlacing needed by the finite spectral-triple convergence programme.

Thus the KMS metric route is better reframed as an AMBIENT SELF-ADJOINT REALIZATION problem.

## 5. Relation to the global physical Casimir

This is precisely the finite version of the desired global construction:

\[
\text{prime/divisor Hodge bulk}
\xrightarrow{B}
\text{self-dual additive Hilbert space}
\xrightarrow{\text{physical compression}}
C_{\rm phys}.
\]

The critical KMS metric is the pullback metric; it should never need to be guessed independently.

This may be the finite theorem that links:
- prime subgroup/Hodge geometry;
- Poisson self-duality;
- the simple-even finite Weil ground;
- the positive Weyl function;
- the eventual self-adjoint principal-series Casimir.

## 6. Cheap falsifier

At finite \(N\), build the subgroup synthesis matrix \(B_N\) explicitly and test candidate transported Weil operators by the stronger residual
\[
\boxed{
\|B_NA_+-\widetilde A B_N\|.
}
\]

If this does not vanish/tend to zero for any natural ambient self-adjoint \(\widetilde A\), the KMS metric mechanism should be abandoned.

If it does, both
\[
GA_+=A_+^*G
\]
and
\[
Ge_0=\eta
\]
become consequences instead of independent miracles.
