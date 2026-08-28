# Exact spectrum of the Gr(2,4) opposite-chart Jacobian

Codex/GPT continuation, 2026-08-28.

This analytically audits the uploaded `grassmannian_mass_theorem.py`.

## Transition map

On the overlap where

\[
D=ad-bc\neq 0,
\]

the script uses

\[
F(a,b,c,d)=\frac1D(-b,a,-d,c).
\]

The exact Jacobian matrix is

\[
J_F=
\begin{pmatrix}
\frac{bd}{D^2} & -\frac{bc}{D^2}-\frac1D & -\frac{b^2}{D^2} & \frac{ab}{D^2}\\
-\frac{ad}{D^2}+\frac1D & \frac{ac}{D^2} & \frac{ab}{D^2} & -\frac{a^2}{D^2}\\
\frac{d^2}{D^2} & -\frac{cd}{D^2} & -\frac{bd}{D^2} & \frac{ad}{D^2}-\frac1D\\
-\frac{cd}{D^2} & \frac{c^2}{D^2} & \frac{bc}{D^2}+\frac1D & -\frac{ac}{D^2}
\end{pmatrix}.
\]

Symbolic factorization gives the characteristic polynomial

\[
\boxed{
\chi_{J_F}(\lambda)
=
\left(\lambda-\frac1D\right)
\left(\lambda+\frac1D\right)
\left(\lambda^2+\frac1{D^2}\right)
}
\]

or equivalently

\[
\chi_{J_F}(\lambda)
=\lambda^4-\frac1{D^4}.
\]

Therefore the four eigenvalues are exactly

\[
\boxed{
\frac1D,\quad -\frac1D,\quad \frac{i}{D},\quad -\frac{i}{D}
}
\]

for every point of the overlap.

Hence every eigenvalue has the same magnitude

\[
\boxed{|\lambda_j|=\frac1{|D|}},
\]

so the script's numerical observation that the *mean* magnitude is `1/|det A|` is true for the much stronger reason that every eigenvalue individually has that magnitude.

Also

\[
\det J_F=-\frac1{D^4},\qquad \operatorname{tr}J_F=0.
\]

## Important correction to the uploaded Python interpretation

At the sample point `(a,b,c,d)=(1,0,0,1)`, so `D=1`, the exact Jacobian is

\[
J_0=
\begin{pmatrix}
0&-1&0&0\\
0&0&0&-1\\
1&0&0&0\\
0&0&1&0
\end{pmatrix}.
\]

Its spectrum is

\[
\{-1,1,-i,i\},
\]

and

\[
J_0^2\neq -I.
\]

Therefore the lines in `grassmannian_mass_theorem.py` claiming that this Jacobian *is* a complex structure with `J^2=-I` and eigenvalues only `±i` are false for the actual four-coordinate Jacobian used by the script. The Python check itself would print `J^2 = -I: False`.

The correct exact statement is a quarter-turn/root-of-unity spectrum scaled by `1/D`:

\[
\operatorname{spec}(J_F)=D^{-1}\{1,-1,i,-i\}.
\]

In particular,

\[
\boxed{J_F^4=D^{-4}I}
\]

whenever the Jacobian is diagonalizable (and the distinct roots for `D != 0` imply it is diagonalizable over C). Thus this fourth-order relation actually holds everywhere on the overlap.

This is structurally more interesting for the project's spin-1/2 / 4pi / orientation program than the incorrect claim `J^2=-I`: the derivative carries all four fourth roots of unity, not a single complex-structure pair.

## Physical dictionary boundary

The pure geometry proves the inverse determinant scale exactly. It does **not** by itself prove that `|D|` is physical mass. The uploaded header also contains an internal inconsistency: it says both `D` is the mass parameter and `m=0 -> |D|=1`. If physical mass is to be a function of the determinant scale, that function/normalization must be stated explicitly and derived from spinor kinematics.

Next tasks:

1. formalize the characteristic-polynomial / fourth-power identity in Verify2;
2. derive the precise relation of `D=p23` to a Lorentz-invariant spinor mass quantity;
3. investigate whether the four-root spectrum supplies the correct geometric origin of the zitter factor-of-two / 4pi spinor structure;
4. do not use the old `J^2=-I` claim downstream.
