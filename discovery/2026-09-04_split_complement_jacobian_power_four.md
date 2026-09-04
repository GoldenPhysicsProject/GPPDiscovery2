# Split complement Jacobian: the same power four appears on the Grassmannian chart

## Exact calculation

On the invertible Gr(2,4) big cell, write

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad D=ad-bc.
\]

The split-signature Hodge/polarity complement is

\[
C_{\rm split}(A)=A^{-T}
=\frac1D\begin{pmatrix}d&-c\\-b&a\end{pmatrix}.
\]

In coordinates `(a,b,c,d)`, the derivative has a common denominator `D^2`.  Its cleared numerator matrix is

\[
N_C=
\begin{pmatrix}
-d^2 & cd & bd & -bc\\
cd & -c^2 & -ad & ac\\
bd & -ad & -b^2 & ab\\
-bc & ac & ab & -a^2
\end{pmatrix}.
\]

Direct symbolic calculation gives, and Lean formalization now targets/proves,

\[
\det N_C=-D^4.
\]

Hence for `D != 0`, because the four rows of the actual Jacobian each contribute a factor `D^{-2}`,

\[
\det dC_{\rm split}
=\frac{-D^4}{D^8}
=-D^{-4}.
\]

Therefore the absolute Jacobian scales as

\[
|\det dC_{\rm split}|=|D|^{-4}.
\]

## Why this is interesting

The exponent four was already forced independently on projective twistor space by the ambient rank-four volume form:

\[
D^3Z=\iota_E\varepsilon,
\qquad
D^3(cZ)=c^4D^3Z,
\qquad
K_{\mathbb{CP}^3}=\mathcal O(-4),
\]

and therefore by the canonical/Fourier weight reflection

\[
k\mapsto-k-4.
\]

We now also get a literal inverse fourth power from the Grassmannian polarity Jacobian itself.

This does **not** yet prove that the two are one global functorial measure transformation.  But it substantially strengthens the ambient-four-dimensional spine: the same rank-four exponent appears independently in both the projective-twistor canonical line and the split Gr(2,4) complement Jacobian.

## Current interpretation

The strongest safe statement is:

\[
\varepsilon_{ABCD}
\Rightarrow
\begin{cases}
\Lambda^2V\text{ polarity / Klein geometry},\\
K_{PT}=\mathcal O(-4),
\end{cases}
\]

while on the split big cell

\[
C_{\rm split}:A\mapsto A^{-T}
\quad\text{has}\quad
\det dC_{\rm split}=-D^{-4}.
\]

The next theorem to seek is a correspondence-space change-of-variables statement showing that this Grassmannian `-4` Jacobian and the twistor canonical `-4` twist are the two coordinate shadows of one determinant-line transformation.
