# Shadow-sector singularity and the corrected Haar selection theorem

Status: exact measure-theoretic mechanism; does not by itself prove RH.

## 1. Why this replaces the old ONON L2 claim

The old manuscript tried to argue that Haar measure made the Mellin character
square-integrable only at Re(s)=1/2.  That is not the correct statement.

There is, however, a sharp global measure-theoretic statement that *is* true.
The shadow-related prime product states belong to the same product-measure
sector only at Re(s)=1/2.  Away from that line they are mutually singular.

This is a much stronger and cleaner formulation of "the primes know the
unitary axis."

## 2. Local geometric laws

Let
\[
s=\sigma+it,\qquad 0<\sigma<1.
\]
For each prime define the normalized local geometric distribution
\[
\mu_{p,\sigma}(a)
=
(1-p^{-2\sigma})p^{-2\sigma a},
\qquad a\in\mathbf N_0.
\]
The shadow-reflected real part is \(1-\sigma\), with
\[
\mu_{p,1-\sigma}(a)
=
(1-p^{-2(1-\sigma)})p^{-2(1-\sigma)a}.
\]

At the critical line \(\sigma=1/2\) these coincide and reduce to
\[
(1-p^{-1})p^{-a},
\]
the Haar/Hagedorn valuation law already derived in the arithmetic-shadow
paper.

## 3. Hellinger affinity

Put
\[
r_p=p^{-2\sigma},
\qquad
r'_p=p^{-2(1-\sigma)}.
\]
The local Hellinger affinity is
\[
\begin{aligned}
A_p(\sigma)
&=
\sum_{a\ge0}
\sqrt{\mu_{p,\sigma}(a)\mu_{p,1-\sigma}(a)}\\
&=
\frac{\sqrt{(1-r_p)(1-r'_p)}}
{1-\sqrt{r_pr'_p}}\\
&=
\boxed{
\frac{
\sqrt{(1-p^{-2\sigma})(1-p^{-2+2\sigma})}
}{
1-p^{-1}
}.
}
\end{aligned}
\]

At \(\sigma=1/2\), \(A_p=1\) for every prime.

Let \(x=\sigma-1/2\ne0\).  Then the two square-root occupation amplitudes
differ at leading order by
\[
p^{-1/2-|x|}
\quad\hbox{and}\quad
p^{-1/2+|x|}.
\]
Consequently
\[
1-A_p(\sigma)
\asymp
p^{-1+2|x|}
\]
for large \(p\).  In particular there is \(c_x>0\) and \(p_0(x)\) such that
\[
1-A_p(\sigma)\ge \frac{c_x}{p}
\qquad(p\ge p_0(x)).
\]
Euler's divergence
\[
\sum_p\frac1p=\infty
\]
therefore gives
\[
\sum_p(1-A_p(\sigma))=\infty.
\]

By Kakutani's product-measure dichotomy, the infinite product measures
\[
\mu_\sigma=\bigotimes_p\mu_{p,\sigma},
\qquad
\mu_{1-\sigma}=\bigotimes_p\mu_{p,1-\sigma}
\]
are mutually singular whenever \(\sigma\ne1/2\), while they are identical at
\(\sigma=1/2\).

Hence
\[
\boxed{
\mu_\sigma\sim\mu_{1-\sigma}
\iff
\sigma=\frac12,
}
\]
where in fact the noncritical case is stronger than inequivalence:
\[
\boxed{
\sigma\ne\frac12
\Longrightarrow
\mu_\sigma\perp\mu_{1-\sigma}.
}
\]

## 4. Pure-state / orthogonality-catastrophe form

Use the normalized local vectors
\[
|\Omega_{p,\sigma,t}\rangle
=
\sqrt{1-p^{-2\sigma}}
\sum_{a\ge0}
p^{-a\sigma}e^{-iat\log p}|a\rangle.
\]

The shadow and Hilbert-adjoint choices can be phased so that their local
overlap is precisely \(A_p(\sigma)\).  Therefore the finite-prime overlap is
\[
\prod_{p\le P}A_p(\sigma).
\]
It tends to 1 on the critical line and to 0 for every
\(\sigma\ne1/2\):
\[
\boxed{
\lim_{P\to\infty}
\prod_{p\le P}A_p(\sigma)
=
\begin{cases}
1,&\sigma=1/2,\\
0,&\sigma\ne1/2.
\end{cases}
}
\]

So an arbitrarily small displacement away from the half-density line causes
a global prime-sector orthogonality catastrophe.

This is the product-state counterpart of the local Dirac defect
\[
|\delta_p(s)|^2
=
4p^{-1}\sinh^2((\sigma-\tfrac12)\log p).
\]

Indeed, for every \(\sigma\ne1/2\),
\[
\sum_p|\delta_p(s)|^2=\infty,
\]
whereas the sum is identically zero on the critical line.  The global
shadow/adjoint mismatch is therefore not a small perturbation off-axis; it is
non-Hilbert-Schmidt.

## 5. Representation-theoretic reading

This suggests the correct replacement for the old claim "Haar L2 forces the
critical line":

> The prime-product shadow and adjoint representations are in the same
> normal/Hilbert sector only on the half-density axis.  Off-axis they are
> disjoint product sectors.

This has a natural analogy with the Shale--Stinespring/Kakutani phenomenon:
infinitely many individually small local changes can become globally
non-unitarily implementable when their squared defects fail to sum.

## 6. What is still missing for RH

The theorem above does **not** imply that every zeta zero defines a vector in
the normal prime-product sector.  Analytic continuation can support
resonances outside a Hilbert representation; the modular-surface Eisenstein
example shows exactly this loophole.

To turn the singularity theorem into RH one must prove:

\[
\xi(\rho)=0
\quad\Longrightarrow\quad
\text{the completed zero mode is implemented in one common normal
shadow/adjoint representation}.
\]

If that implication is obtained independently from the completed
prime--Archimedean/celestial construction, mutual singularity rules out
\(\Re\rho\ne1/2\) immediately.

Thus the remaining theorem can be stated as a **normality/implementability
theorem for the completed resonance**, not merely as a vague spectral
correspondence.
