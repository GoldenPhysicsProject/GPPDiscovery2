# Exact Gamma Wiener–Hopf analyticity and pole lattice

Define, for complex spectral parameter `z`,

\[
H_+(z)=\frac{1}{\pi}\Gamma\!\left(\frac12-\frac{i z}{2\pi}\right)^2,
\qquad
H_-(z)=\frac{1}{\pi}\Gamma\!\left(\frac12+\frac{i z}{2\pi}\right)^2.
\]

Euler reflection at

\[
w=\frac12+\frac{i z}{2\pi}
\]

gives

\[
\Gamma(w)\Gamma(1-w)
=\frac{\pi}{\sin(\pi w)}
=\frac{\pi}{\cosh(z/2)}.
\]

Therefore, as a meromorphic identity,

\[
\boxed{H_+(z)H_-(z)=\operatorname{sech}^2(z/2).}
\]

This is stronger than the real-axis numerical audit: it identifies the actual half-plane singularity structure.

The Gamma function has simple poles at `0,-1,-2,...` and no zeros. Hence `H_+` has double poles exactly when

\[
\frac12-\frac{i z}{2\pi}=-n,
\qquad n\in\mathbb Z_{\ge0},
\]

i.e.

\[
\boxed{z=-i\pi(2n+1),}
\]

all in the lower half-plane. Thus `H_+` is holomorphic and zero-free in the open upper half-plane.

Similarly `H_-` has double poles exactly at

\[
\boxed{z=+i\pi(2n+1),}
\]

all in the upper half-plane, so `H_-` is holomorphic and zero-free in the open lower half-plane.

Accordingly this is a genuine Wiener–Hopf factorization with the canonical analyticity assignment

\[
H_+\in\mathcal O(\mathbb H_+),
\qquad
H_-\in\mathcal O(\mathbb H_-).
\]

For real `k`, conjugation of Gamma gives

\[
H_-(k)=\overline{H_+(k)},
\]

hence

\[
|H_+(k)|^2=\operatorname{sech}^2(k/2).
\]

Because Gamma has no zeros, the scattering ratio

\[
S(k)=\frac{H_-(k)}{H_+(k)}
\]

is well-defined on the real axis and satisfies

\[
\boxed{|S(k)|=1.}
\]

Thus the real-axis factorization splits exactly into a positive transmission modulus and a pure phase.

The integer convolution hierarchy inherits the factorization without new analytic input:

\[
\boxed{
H_+(z)^m H_-(z)^m=\operatorname{sech}^{2m}(z/2),
\qquad m\ge1.
}
\]

Its pole lattice is unchanged, while pole orders scale from `2` to `2m`; the real-axis scattering phase becomes

\[
S_m(k)=S(k)^m,
\qquad |S_m(k)|=1.
\]

This gives an exact all-order Wiener–Hopf semigroup at the level of spectral factors. It is logically independent of the Fourier-transform/convolution theorem used to interpret `sech^{2m}` as the transform of the real-space density `rho_m`; only Euler reflection, the Gamma pole set, and Gamma zero-freeness are required.
