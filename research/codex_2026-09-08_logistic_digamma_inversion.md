# Codex research note: logistic digamma inversion bridge

## Exact identity

Let

\[
\mu(u)=\frac{\pi}{2}\operatorname{sech}^2(\pi u),\qquad
D(t)=\Re\psi\!\left(\frac12+it\right)-\psi\!\left(\frac12\right),\qquad
q(t)=\Im\psi\!\left(\frac12+it\right).
\]

A classical inversion formula for the digamma function is

\[
\psi(x)=\frac{\pi}{2}\int_{\mathbb R}
\log\!\left(x-\frac12+iu\right)\operatorname{sech}^2(\pi u)\,du.
\]

Specializing to \(x=\tfrac12+it\) gives

\[
\boxed{\psi\!\left(\frac12+it\right)=\mathbb E_\mu[\log(i(t+U))]}.
\]

Hence

\[
\boxed{D(t)=\mathbb E_\mu\!\left[\log\frac{|t+U|}{|U|}\right]}
\]

and, from the principal branch of the logarithm,

\[
q(t)=\frac{\pi}{2}\mathbb E_\mu[\operatorname{sgn}(t+U)].
\]

The logistic CDF of \(\mu\) is

\[
F(t)=\frac{1+\tanh(\pi t)}2,
\]

so

\[
\boxed{q(t)=\frac{\pi}{2}\tanh(\pi t)}.
\]

In principal-value form, differentiating the real logarithmic potential gives

\[
\boxed{D'(t)=\operatorname{PV}\,\mathbb E_\mu\!\left[\frac1{t+U}\right]}.
\]

Thus the real digamma score \(D\) and the Barnes phase \(q\) are the real and imaginary projections of one exact logistic logarithmic potential.  This is useful for the remaining \(A_4\) obstruction because

\[
K=\mathbb E_\mu[tD(t)D'(t)]
\]

can now be viewed as a virial/Hilbert-transform functional of the same probability law, rather than as an unrelated hyperbolic double integral.

## Validation and status

`discovery/principal_series_logistic_digamma_inversion_audit.py` checks the complex inversion, the centered real potential, and the phase/CDF projection to more than 55 decimal digits at several nontrivial points.

The inversion formula is classical; a convenient source is A. Dixit, A. Kabza, V. Moll, C. Vignat, *Modified Nörlund Polynomials*, Eq. (2.2), which cites the original proof.  This note does not claim a proof of the remaining candidate

\[
K=-\frac34+\log2+\frac{\pi^2}{24}.
\]

That evaluation remains the next analytic target.

## Scope discipline

This is an exact principal-series/spectral identity.  It does not imply global Weil positivity and does not promote any RH claim.
