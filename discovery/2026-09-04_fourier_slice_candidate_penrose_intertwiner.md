# Fourier-slice candidate for the actual Penrose googly intertwiner

## New reduction

The incidence/polarity work suggests that the missing field-level theorem is a four-dimensional Fourier-slice theorem in projective/homogeneous clothing.

Use the symmetric full Fourier normalization that appears in split twistor scattering theory:

\[
\widehat F(W)
=\frac{1}{(2\pi)^2}
\int_{\mathbb R^4} e^{-i Z\cdot W}F(Z)\,d^4Z.
\]

For an invertible or non-invertible graph 2-plane

\[
W_A=\{(x,A^Tx):x\in\mathbb R^2\},
\]

define the vector-plane X-ray/Radon integral

\[
R_A F=\int_{\mathbb R^2}F(x,A^Tx)\,d^2x.
\]

The ordinary annihilator plane is

\[
W_A^\circ
=\{(-Ay,y):y\in\mathbb R^2\}.
\]

The phase vanishes identically on the incidence pair:

\[
(x,A^Tx)\cdot(-Ay,y)=0.
\]

This is the same algebra already formalized by `IncidenceKernelGoogly.lean`.

## Exact Fourier-slice calculation

Using symmetric Fourier inversion,

\[
F(z)=\frac{1}{(2\pi)^2}\int e^{+iz\cdot\xi}\widehat F(\xi)\,d^4\xi,
\]

we obtain formally for Schwartz data

\[
\begin{aligned}
R_A F
&=\frac{1}{(2\pi)^2}
  \int d^4\xi\,\widehat F(\xi)
  \int d^2x\,
  e^{i x\cdot(\xi_L+A\xi_R)}\\
&=\frac{1}{(2\pi)^2}(2\pi)^2
  \int d^2y\,\widehat F(-Ay,y)\\
&=R_{A^\circ}\widehat F.
\end{aligned}
\]

Thus the dimension-four / dimension-two symmetric normalization cancels exactly:

\[
\boxed{R_A F=R_{A^\circ}(\mathcal F F).}
\]

This is precisely the shape of the desired commuting square before projectivization.

## Why this looks like the missing googly theorem

The split Penrose transform is an X-ray transform on real twistor space `RP^3`; spacetime points are projective lines, equivalently 2-planes in `R^4` under the Klein correspondence.  The full twistor-to-dual-twistor Fourier transform is explicitly

\[
f(W)=\frac{1}{(2\pi)^2}\int d^4Z\,e^{-iZ\cdot W}F(Z).
\]

Hence the ordinary Fourier-slice theorem says exactly that integrating the source twistor representative over the line/plane and integrating its full Fourier transform over the annihilator dual line/plane reconstruct the same bulk datum.

Combined with the split metric identification

\[
W^\circ\leftrightarrow W^{\perp_{2,2}}
\]

and the already-proved orientation relabelling of Hodge chirality, this is the strongest concrete candidate so far for

\[
P_-\circ D_\varepsilon
=R_{\mathfrak o}\circ P_+.
\]

## Critical caveat

The calculation above is straightforward for Schwartz functions on the vector space `R^4`, but projective twistor wavefunctions are homogeneous and the full Fourier integral is generally distributional.  The twistor literature explicitly notes this issue: homogeneous functions of definite weight make the naive full Fourier integral diverge at zero or infinity and require distributional/projective interpretation.

Therefore the exact remaining analytic problem is no longer vague:

1. formulate the Fourier-slice theorem for homogeneous tempered distributions of degree `k` on `R^4`;
2. prove the Fourier transform has degree `-k-4`;
3. descend the vector-plane slice identity to projective line/X-ray data on `RP^3`;
4. identify the target line with annihilator/split polarity, already solved at finite-dimensional coordinate level;
5. match the resulting bulk spinor field with orientation-reversed chirality.

If this projective distributional descent works, the linear Penrose googly square is essentially closed.

## Literature checks

- Mason/Skinner-style split twistor scattering gives the two complementary half-Fourier transforms and their composition as the symmetric full four-dimensional Fourier transform with prefactor `(2π)^-2`.
- Split Penrose/X-ray literature identifies the real Penrose transform with integration of homogeneous twistor functions along projective lines in `RP^3`.
- The full Fourier transform of homogeneous twistor data is treated distributionally, exactly matching the technical issue isolated above.

These are external checks only; the GPP mechanism remains the ambient-four/polarity/incidence construction.
