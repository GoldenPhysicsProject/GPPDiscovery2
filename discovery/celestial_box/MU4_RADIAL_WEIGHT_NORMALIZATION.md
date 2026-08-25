# Universal mu^4 radial-shell normalization

For the isolated D-dimensional massive-scalar \(\mu^4\) box sector, two-body phase space multiplies the numerator by the universal fixed-radius factor

\[
W(r)=\tanh r\,\operatorname{sech}^4 r,
\qquad r\in[0,\infty).
\]

This factor is exactly integrable before inserting the angular propagator kernel:

\[
\boxed{
\int_0^\infty \tanh r\,\operatorname{sech}^4 r\,dr=\frac14.
}
\]

Indeed,

\[
\frac{d}{dr}\operatorname{sech}^4 r
=-4\tanh r\,\operatorname{sech}^4 r.
\]

Therefore the normalized radial density

\[
\boxed{\rho_r(r)=4\tanh r\,\operatorname{sech}^4 r}
\]

has exact cumulative distribution

\[
\boxed{
F(R)=\int_0^R \rho_r(r)\,dr
=1-\operatorname{sech}^4 R.
}
\]

Using the cut-shell relation

\[
\operatorname{sech}r=\frac{2\mu}{M},
\qquad 0<\mu\le M/2,
\]

this becomes

\[
F(R)=1-\left(\frac{2\mu(R)}{M}\right)^4.
\]

The mode of the unnormalized radial density is the previously derived

\[
\tanh r_*=\frac1{\sqrt5},
\qquad
\mu_*=\frac{M}{\sqrt5},
\qquad
W_{\max}=\frac{16}{25\sqrt5}.
\]

A separate useful integral in the \(\mu\) coordinate is

\[
\boxed{
\int_0^{M/2}\mu^4\sqrt{1-\frac{4\mu^2}{M^2}}\,d\mu
=\frac{\pi M^5}{1024}.
}
\]

To verify it, set \(x=2\mu/M\):

\[
\int_0^1 x^4\sqrt{1-x^2}\,dx
=\frac12 B\!\left(\frac52,\frac32\right)
=\frac\pi{32}.
\]

These identities concern only the universal \(\mu^4\)-numerator times two-body phase-space weight. They do not normalize the complete cut, because the exact angular master kernel \(\mathcal J(r)\) and the remaining D-dimensional YM state/subtraction sectors are not included.
