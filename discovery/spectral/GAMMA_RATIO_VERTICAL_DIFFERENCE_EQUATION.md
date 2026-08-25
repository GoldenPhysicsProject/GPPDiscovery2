# Gamma scattering ratio: exact vertical difference equation

Codex/GPT discovery track, 2026-08-25.

For the half-Gamma factors

\[
H_+(z)=\frac{\Gamma(\frac12-\frac{i z}{2\pi})^2}{\pi},\qquad
H_-(z)=\frac{\Gamma(\frac12+\frac{i z}{2\pi})^2}{\pi},
\]

define

\[
B(z)=\frac{H_+(z)}{H_-(z)}.
\]

Put

\[
a(z)=\frac12-\frac{i z}{2\pi}.
\]

Since `1-a(z)=1/2+iz/(2pi)`,

\[
B(z)=\left[\frac{\Gamma(a(z))}{\Gamma(1-a(z))}\right]^2.
\]

Under the vertical shift `z -> z+2 pi i`,

\[
a(z+2\pi i)=a(z)+1,
\]

while

\[
1-a(z+2\pi i)=-a(z).
\]

Using `Gamma(w+1)=w Gamma(w)` and `Gamma(-a)=Gamma(1-a)/(-a)` gives

\[
\frac{\Gamma(a+1)}{\Gamma(-a)}
=-a^2\frac{\Gamma(a)}{\Gamma(1-a)}.
\]

Squaring removes the sign, so

\[
\boxed{
B(z+2\pi i)=a(z)^4 B(z).
}
\]

For the integer convolution chamber `B_m=B^m`,

\[
\boxed{
B_m(z+2\pi i)=a(z)^{4m}B_m(z).
}
\]

This exact difference equation is a more appropriate structural handle than an `H^infty` inner-function interpretation. It directly generates the polynomial growth under repeated vertical translation and is compatible with the double-zero lattice `z=i pi(2n+1)`.

The reflection formula also gives

\[
\boxed{
B(z)=\frac{\Gamma(a(z))^4\sin^2(\pi a(z))}{\pi^2}.
}
\]

Hence the upper-half-plane zeros correspond to positive integral values of `a`, while the Gamma factor controls the non-Hardy growth. The raw ratio therefore sits naturally in a Gamma/difference-equation class rather than the bounded-type Hardy class.
