# Regulated scalar-box cut: exact small-mass logarithmic coefficient

Codex/GPT continuation, 2026-08-28.

Starting from the exact regulated two-particle cut used in `loops_from_cuts_celestial.pdf`, write

\[
C(c,d)=\frac{1}{8\pi}\frac{4}{\sqrt{d(d+4c)}}
\operatorname{artanh}\sqrt{\frac{d}{d+4c}},
\qquad c>0,\ d>0.
\]

For the physical variables in that paper,

\[
c=\mu^2(s+\mu^2),\qquad d=s(s+t)=-su>0.
\]

## Asymptotic extraction

Let

\[
r(c)=\sqrt{\frac{d}{d+4c}}=(1+4c/d)^{-1/2}.
\]

As `c -> 0+`,

\[
r(c)=1-\frac{2c}{d}+O(c^2),
\]

so

\[
1-r(c)=\frac{2c}{d}+O(c^2),\qquad 1+r(c)=2+O(c).
\]

Using

\[
\operatorname{artanh}r=\frac12\log\frac{1+r}{1-r},
\]

we obtain

\[
\operatorname{artanh}r(c)
=\frac12\log\frac{d}{c}+O(c).
\]

Also

\[
\frac{4}{\sqrt{d(d+4c)}}=\frac4d+O(c).
\]

Therefore

\[
\boxed{
C(c,d)
=\frac{1}{4\pi d}\log\frac{d}{c}+o\!\left(\log\frac1c\right)
}
\]

and in fact the next corrections are lower order than the logarithm. Equivalently,

\[
\boxed{
\lim_{c\to0^+}
\frac{C(c,d)}{\log(d/c)}
=\frac{1}{4\pi d}
}
\qquad(d>0).
\]

A high-precision numerical audit at several positive values of `d` and regulators down to `c=10^{-16}` converges to the coefficient `1/(4*pi*d)`.

Since `c=mu^2(s+mu^2)` and `d=-su`, fixed nonzero `s,u` give

\[
\log\frac{d}{c}
=\log\frac{-su}{\mu^2(s+\mu^2)}
=\log\frac{-u}{\mu^2}+o(1),
\]

hence

\[
\boxed{
C(s,t,\mu^2)
\sim
\frac{1}{4\pi(-su)}\log\frac{-u}{\mu^2}
}
\qquad \mu^2\to0^+.
\]

This is the expected collinear/infrared logarithm emerging directly from the celestial cut geometry, with its coefficient fixed by the exact cut normalization.

## Status and next use

This result is derived from the already exact closed cut formula and numerically audited, but the limit has not yet been promoted to Lean. The natural Verify2 target is the ratio limit in the boxed equation above, followed by transport through the dispersion representation. It does not by itself close the raised-box Feynman-simplex regulator limit; that remains the nested Beta-integral plus dominated-convergence frontier.
