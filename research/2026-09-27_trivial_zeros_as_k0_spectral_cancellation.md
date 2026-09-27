# Trivial zeta zeros as exact spectral cancellation of the compact SU(1,1) ladder

Date: 2026-09-27
Status: exact analytic and spectral identities. No RH claim.

## 1. Remove the spurious s=0 Gamma pole first

Write the completed zeta function as
\[
\xi(s)
=
\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Using
\[
\Gamma(1+s/2)=\frac{s}{2}\Gamma(s/2),
\]
we get the cleaner exact form
\[
\boxed{
\xi(s)
=
(s-1)\pi^{-s/2}
\Gamma(1+s/2)\zeta(s).
}
\]

The factor s has now been absorbed into the Gamma function.

Thus the remaining Gamma poles occur exactly at
\[
s=-2,-4,-6,\ldots,
\]
and these are exactly the trivial zeros of zeta.

## 2. Center at the critical line

Put
\[
s=\frac12+z.
\]

Then
\[
\Gamma(1+s/2)
=
\Gamma\left(\frac54+\frac z2\right).
\]

Its poles are
\[
\frac54+\frac z2=-n,
\qquad n=0,1,2,\ldots,
\]
i.e.
\[
\boxed{
z=-\left(2n+\frac52\right).
}
\]

The trivial zeta zeros
\[
s=-2(n+1)
\]
occur at the identical centered locations
\[
z=s-\frac12
=
-\left(2n+\frac52\right).
\]

Therefore every remaining Gamma pole is canceled pointwise by a trivial zeta zero.

## 3. Those locations are the spectrum of a shifted compact SU(1,1) generator

In the universal k=1/2 module,
\[
K_0e_n=\left(n+\frac12\right)e_n.
\]

Define
\[
\boxed{
A_{\rm triv}
=
2K_0+\frac32 I.
}
\]

Then
\[
A_{\rm triv}e_n
=
\left(2n+\frac52\right)e_n.
\]

Hence
\[
\boxed{
\operatorname{spec}(A_{\rm triv})
=
\left\{
\frac52,\frac92,\frac{13}2,\ldots
\right\}.
}
\]

The centered trivial zeros are exactly
\[
\boxed{
z=-\operatorname{spec}(A_{\rm triv}).
}
\]

So the full trivial-zero sequence is literally the negative spectrum of a shifted compact generator of the same SU(1,1) module already producing the Gamma/Plancherel positivity structures.

## 4. Gamma as the inverse zeta determinant of the compact ladder

For the arithmetic progression
\[
A_{\rm triv}=2(N+5/4),
\]
the spectral zeta function is a rescaled Hurwitz zeta:
\[
\zeta_{A_{\rm triv}+z}(w)
=
\sum_{n\ge0}
(2n+5/2+z)^{-w}
=
2^{-w}
\zeta_H\left(w,\frac54+\frac z2\right).
\]

The standard zeta-determinant identity therefore gives, up to a z-independent nonzero normalization constant,
\[
\boxed{
\det\nolimits_\zeta(A_{\rm triv}+z)
\propto
\Gamma\left(\frac54+\frac z2\right)^{-1}.
}
\]

Equivalently,
\[
\boxed{
\Gamma\left(\frac54+\frac z2\right)
\propto
\det\nolimits_\zeta(A_{\rm triv}+z)^{-1}.
}
\]

Thus the Archimedean Gamma factor is the inverse spectral determinant of the compact K0 ladder.

## 5. Exact trivial-sector cancellation in xi

The centered completed function can be written
\[
\xi\left(\frac12+z\right)
=
\left(z-\frac12\right)
\pi^{-1/4-z/2}
\Gamma\left(\frac54+\frac z2\right)
\zeta\left(\frac12+z\right).
\]

Using the determinant form,
\[
\boxed{
\xi\left(\frac12+z\right)
\propto
\pi^{-z/2}
\frac{
\left(z-\frac12\right)\zeta(1/2+z)
}{
\det_\zeta(A_{\rm triv}+z)
}.
}
\]

Now
\[
(z-\tfrac12)\zeta(1/2+z)
\]
is entire: the factor cancels the zeta pole at s=1.

At every
\[
z=-\lambda_n,
\qquad
\lambda_n\in\operatorname{spec}(A_{\rm triv}),
\]
the numerator has a trivial zeta zero while the determinant in the denominator has a zero of the same order.

The quotient is regular.

Therefore the completed xi function performs an exact spectral cancellation:
\[
\boxed{
\text{compact Archimedean ladder pole}
+
\text{arithmetic trivial zero}
\longrightarrow
\text{regular completed state}.
}
\]

## 6. Hodge/no-ghost interpretation

This suggests a much sharper interpretation of the compact K0 sector.

It is not merely a convenient source of the Gamma function.

Its spectrum is precisely the sequence that is removed by the trivial zeros in the completed arithmetic object.

So one can view
\[
A_{\rm triv}
\]
as an explicitly paired exact sector:
- the Archimedean determinant supplies poles at \(-\operatorname{spec}A_{\rm triv}\);
- the arithmetic zeta factor supplies zeros at exactly the same points;
- completion quotients the pair away.

Only the nontrivial zeros remain as uncanceled global spectral data.

This is structurally the kind of exact/null cancellation sought in the earlier Hodge/no-ghost program.

## 7. Relation to K0/K1 polarization

The same universal SU(1,1) module now has three exact roles:

1. \(K_0\) heat/resolvent geometry gives the Gamma/digamma positive defect;
2. a shifted \(K_0\) spectrum gives the entire trivial-zero cancellation ladder;
3. \(K_1\) gives the continuous hyperbolic-secant/Plancherel spectral geometry.

So the trivial zeros live in the compact polarization, while the nontrivial critical-line problem lives in the continuous principal-series polarization after the compact exact sector has been canceled.

This suggests that the desired physical quotient should remove the paired K0 trivial complex before testing positivity/causality in the K1 channel.

## 8. What this does not show

The cancellation of Gamma poles by trivial zeros is classical and exact; expressing the pole lattice as the shifted K0 spectrum is the new representation-theoretic packaging here.

It does not constrain the nontrivial zeros.

The open theorem remains: prove that after exact compact-sector cancellation and adelic sewing, the remaining transfer function is causal/inner so its nontrivial resonances lie on the real K1/principal-series axis.
