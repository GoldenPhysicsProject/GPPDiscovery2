# Shadow Euler heat kernel: RH as complete monotonicity of the completed inverse-Casimir heat trace

Date: 2026-09-28
Status: exact transform equivalence plus an exact identification of the prime contribution in the absolute Euler domain. No RH proof.

This note connects the completed Shadow Euler Casimir/Stieltjes formulation to the previously derived critical KMS prime heat norm.

## 1. Start from the unconditional centered Casimir response

Let
\[
F(u)
=
\frac{\xi(\frac12+\sqrt u)}{\xi(\frac12)},
\qquad
m(u)
=
\frac{F'(u)}{F(u)}
=
\frac1{2\sqrt u}
\frac{\xi'}{\xi}\left(\frac12+\sqrt u\right),
\]
with the removable value at \(u=0\).

The previous Shadow Euler completion gives
\[
\boxed{
\mathrm{RH}
\iff
m \text{ is a Stieltjes function.}
}
\]

Under RH,
\[
m(u)
=
\sum_{\gamma>0}
\frac1{u+\gamma^2}.
\]

## 2. Laplace/heat representation

Use
\[
\frac1{u+\lambda}
=
\int_0^\infty e^{-ut}e^{-\lambda t}\,dt.
\]

Under RH,
\[
\boxed{
m(u)
=
\int_0^\infty e^{-ut}K_\xi(t)\,dt,
\qquad
K_\xi(t)=\sum_{\gamma>0}e^{-t\gamma^2}.
}
\]

Thus \(K_\xi\) is the heat trace of the inverse-Casimir spectral operator
\[
H_{\rm phys}^2=C_{\rm phys}-\frac14.
\]

It is positive and completely monotone:
\[
(-1)^n K_\xi^{(n)}(t)
=
\sum_\gamma \gamma^{2n}e^{-t\gamma^2}
\ge0.
\]

Conversely, if the inverse Laplace transform \(K_\xi\) of the zero-independent function \(m\) is completely monotone, Bernstein's theorem gives
\[
K_\xi(t)
=
\int_{[0,\infty)}e^{-\lambda t}\,d\mu(\lambda)
\]
for a positive measure \(\mu\), hence
\[
m(u)
=
\int_{[0,\infty)}
\frac{d\mu(\lambda)}{u+\lambda},
\]
so \(m\) is Stieltjes and RH follows.

Therefore
\[
\boxed{
\mathrm{RH}
\iff
K_\xi=\mathcal L^{-1}_{u\to t}m
\text{ is completely monotone.}
}
\]

This is the heat-kernel version of the positive-Fredholm/ principal-series criterion.

## 3. The prime part is EXACTLY the previously found KMS heat norm

Put
\[
r=\sqrt u,
\qquad
s=\frac12+r.
\]

In the absolute Euler domain \(r>1/2\),
\[
\frac{\zeta'}{\zeta}(s)
=
-\sum_{n\ge2}\Lambda(n)n^{-s}.
\]

Therefore the prime contribution to \(m(u)\) is
\[
m_{\rm prime}(u)
=
-\frac1{2r}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}e^{-r\log n}.
\]

Use the standard subordination identity
\[
\boxed{
\frac{e^{-a\sqrt u}}{2\sqrt u}
=
\frac1{\sqrt{4\pi}}
\int_0^\infty
t^{-1/2}
e^{-ut-a^2/(4t)}\,dt.
}
\]

Then
\[
\boxed{
m_{\rm prime}(u)
=
-\int_0^\infty e^{-ut}K_P(t)\,dt,
}
\]
where
\[
\boxed{
K_P(t)
=
\frac1{\sqrt{4\pi t}}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\exp\left[-\frac{(\log n)^2}{4t}\right].
}
\]

But this is exactly the critical Bost--Connes/KMS prime heat norm previously derived independently:
\[
K_P(t)
=
\frac1{\sqrt{4\pi t}}
\left\|e^{-L^2/(8t)}J\right\|_{\rm mid}^2,
\]
with modular frequency \(L\mu_n=(\log n)\mu_n\).

So the Shadow Euler Stieltjes response and the KMS prime-current construction meet EXACTLY under square-root subordination.

## 4. The sign explains the global problem

The prime heat norm itself is positive:
\[
K_P(t)\ge0.
\]

But it enters the logarithmic derivative with a MINUS sign:
\[
m_{\rm prime}
=
-\mathcal L K_P.
\]

This recovers, in the strongest possible form, the recurring warning:
\[
\boxed{
\text{local prime positivity is not global RH positivity.}
}
\]

The completed Archimedean, pole/contact, and vacuum-renormalization channels must combine with \(-K_P\) to produce the physical heat trace
\[
K_\xi(t).
\]

Thus the exact remaining target can be stated as a HEAT TRACE COMPLETION theorem:

> Construct a zero-independent completed heat density \(K_{\rm comp}(t)\) from the self-dual prime valuation system plus the Archimedean Fourier/Hodge channel, prove
> \[
> K_{\rm comp}(t)
> =
> \mathcal L^{-1}
> \left[
> \frac1{2\sqrt u}
> \frac{\xi'}{\xi}(\tfrac12+\sqrt u)
> \right](t),
> \]
> and prove \(K_{\rm comp}\) completely monotone.

Then RH follows.

## 5. Why the self-dual divisor geometry is the right completion space

The new finite divisor geometry supplies:
- positive local prime valuation precisions;
- exact critical KMS metric;
- exact finite Fourier duality \(d\leftrightarrow N/d\);
- exact centered reflection \(\ell\leftrightarrow-\ell\);
- the product formula coupling \(\ell_\infty\) to \(\sum_pv_p\log p\).

The subordination kernel
\[
\frac1{\sqrt{4\pi t}}
e^{-(\log n)^2/(4t)}
\]
is itself a Gaussian heat kernel in the LOGARITHMIC SCALE coordinate.

Therefore the prime current \(K_P(t)\) is literally the heat content of the discrete valuation/lattice refinements after projection onto the global scale line.

The Archimedean place must supply the self-dual boundary/reflection completion of that same heat problem.

This gives a much more concrete interpretation of the current physical Casimir:
\[
\boxed{
C_{\rm phys}-\frac14
=
\text{globally sewn logarithmic Hodge Laplacian}.
}
\]

## 6. Connection to Yang--Mills and BSD

The same architecture now takes a heat-kernel form.

For Yang--Mills, a mass gap is equivalent to large-time decay
\[
\operatorname{Tr}'e^{-tH_{\rm YM}}
\sim e^{-m t}
\]
on the physical quotient.

For BSD, rank is the dimension of the zero-mode sector, which appears as the nondecaying term of a Hodge heat trace:
\[
\lim_{t\to\infty}\operatorname{Tr}e^{-t\Delta}
=
\dim\ker\Delta.
\]

For RH, the desired completed arithmetic heat kernel has no negative/nonunitary Casimir modes and is the positive heat trace
\[
K_\xi(t)=\sum_\gamma e^{-t\gamma^2}.
\]

So the sign/nullity/gap trichotomy becomes:
- RH: positivity/completely monotone arithmetic heat trace;
- BSD: constant large-time zero-mode multiplicity;
- YM: exponential large-time decay above the zero mode.

This makes the common Hodge/heat-kernel language exact rather than metaphorical.

## 7. Immediate proof target

The highest-value theorem is now:

\[
\boxed{
K_{\rm Arch}(t)+K_{\rm vac}(t)-K_P(t)
=
\operatorname{Tr}e^{-tH_{\rm phys}^2}
}
\]

for a positive self-adjoint \(H_{\rm phys}^2\) constructed directly from the self-dual divisor/KMS/Poisson quotient.

The prime term is already an exact norm square.
The missing work is to identify the Archimedean/vacuum channels as the boundary correction that turns the signed explicit-formula heat density into the heat trace of the physical Schur complement.
