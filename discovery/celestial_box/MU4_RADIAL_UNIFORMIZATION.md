# Exact uniformization of the universal mu^4 radial law

For the isolated D-dimensional massive-scalar \(\mu^4\) box sector after two-body phase space, the normalized radial density is

\[
\rho_r(r)=4\tanh r\,\operatorname{sech}^4 r,
\qquad r\ge 0,
\]

with cumulative distribution

\[
F_R(r)=1-\operatorname{sech}^4 r.
\]

Define

\[
U:=\operatorname{sech}^4 R.
\]

Because \(r\mapsto \operatorname{sech}^4 r\) decreases from \(1\) to \(0\), for \(0\le u\le1\),

\[
\Pr(U\le u)
=\Pr\!\left(R\ge \operatorname{arsech}(u^{1/4})\right)
=1-F_R\!\left(\operatorname{arsech}(u^{1/4})\right)
=u.
\]

Hence

\[
\boxed{U=\operatorname{sech}^4R\sim\mathrm{Uniform}(0,1).}
\]

Using the cut-shell relation

\[
\operatorname{sech}R=\frac{2\mu}{M},
\]

we obtain the equivalent exact statement

\[
\boxed{
\left(\frac{2\mu}{M}\right)^4\sim\mathrm{Uniform}(0,1)
}
\]

for the universal numerator-times-phase-space radial measure, before inserting the angular propagator kernel.

Thus the induced \(\mu\)-density is elementary:

\[
\boxed{
\rho_\mu(\mu)
=\frac{64\mu^3}{M^4},
\qquad 0\le \mu\le \frac M2.
}
\]

Indeed its CDF is

\[
F_\mu(\mu)
=\left(\frac{2\mu}{M}\right)^4.
\]

Therefore all universal \(\mu\)-moments close exactly:

\[
\boxed{
\mathbb E[\mu^q]
=\frac{4}{q+4}\left(\frac M2\right)^q,
\qquad q>-4.
}
\]

In particular,

\[
\mathbb E[\mu]=\frac{2M}{5},\qquad
\mathbb E[\mu^2]=\frac{M^2}{6},\qquad
\mathbb E[\mu^4]=\frac{M^4}{32}.
\]

This uniformization applies only to the universal \(\mu^4\) numerator times two-body phase-space radial weight. The full cut includes the angular master kernel \(\mathcal J(r)\), helicity data, the complete D-dimensional gluon-state sum, and subtraction sectors, which distort this simple probability law.
