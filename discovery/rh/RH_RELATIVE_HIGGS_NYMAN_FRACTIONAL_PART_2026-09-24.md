# RH relative Higgs field as the Nyman fractional-part fluctuation
## Date: 2026-09-24
## Status: exact Mellin identity and exact identification of the condensate subtraction

The relative-Higgs quotient has an elementary closed form in terms of the fractional-part function. This makes precise that the continuum condensate subtraction is the Nyman/Beurling subtraction.

For \(\Re s>1\),
\[
\zeta(s)=s\int_1^\infty \lfloor x\rfloor x^{-s-1}\,dx.
\]
Writing \(\lfloor x\rfloor=x-\{x\}\),
\[
\zeta(s)
=
\frac{s}{s-1}
-
s\int_1^\infty \{x\}x^{-s-1}\,dx.
\]
The right side continues to \(\Re s>0\), \(s\ne1\), because \(0\le\{x\}<1\) and the remaining integral is absolutely convergent there.

For the relative Higgs field
\[
H(s)=\frac{s-1}{s}\zeta(s),
\]
we therefore have the exact representation
\[
\boxed{
H(s)
=
1-(s-1)\int_1^\infty\{x\}x^{-s-1}\,dx,
\qquad \Re s>0.
}
\]

Thus the vacuum-removed arithmetic Higgs field is literally the Mellin transform of the bounded counting discrepancy \(\{x\}\).

Equivalently, the factorization
\[
Z^{\rm ar}=Z^{\rm vac}H
\]
is the operator version of
\[
\lfloor x\rfloor=x-\{x\}.
\]

This identifies the new Higgs formulation with the exact Nyman/Beurling fluctuation variable, rather than introducing a separate ad hoc field.

Important limitation: boundedness \(0\le\{x\}<1\) controls \(H\) itself but does not control \(H^{-1}\). The zeros of \(H\) are precisely the nontrivial zeta zeros, so proving a zero-independent lower bound for \(H\) in \(\Re s>1/2\) would already be RH-strength. The Higgs mechanism must therefore use the positive parent/current susceptibility rather than merely the pointwise size of the fractional-part field.

At the finite-cutoff CCM boundary, the previous exact identity
\[
q_L'(k)=-p_L^{\rm rel}(k)+R_{\infty,L}(k)
\]
shows that the RH-critical instability is exactly the logarithmic current of this fractional-part/relative-Higgs field, modulo a cutoff-tame Archimedean term.

This gives a precise synthesis:
\[
\text{continuum condensate subtraction}
\Longleftrightarrow
\text{fractional-part fluctuation}
\Longleftrightarrow
\text{Nyman boundary variable}
\Longleftrightarrow
\text{relative Higgs field}.
\]

The remaining theorem is still an inverse/current stability theorem, not a bound on the fluctuation amplitude alone.
