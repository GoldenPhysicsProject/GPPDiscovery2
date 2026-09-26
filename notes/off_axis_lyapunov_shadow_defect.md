# Off-axis Lyapunov exponent = prime shadow-defect exponent

Date: 2026-09-26
Status: exact local identity + PNT asymptotic + explicit-formula exponent match. No RH proof.

## 1. Horizontal displacement as a nonunitary exponent

Write
\[
s=\frac12+\eta+it,
\qquad 0<|\eta|<\frac12.
\]
The local shadow/adjoint defect already derived in the project is
\[
|\delta_p(s)|^2
=
4p^{-1}\sinh^2(\eta\log p).
\]
Expanding the hyperbolic sine gives the exact identity
\[
\boxed{
|\delta_p(s)|^2
=
p^{-1+2|\eta|}
+p^{-1-2|\eta|}
-2p^{-1}.
}
\]
(The expression is even in \(\eta\).)

For a prime cutoff \(P\), define
\[
D_P(\eta)^2
:=
\sum_{p\le P}|\delta_p(s)|^2.
\]
By the prime number theorem and partial summation,
\[
\sum_{p\le P}p^{-1+2|\eta|}
\sim
\frac{P^{2|\eta|}}{2|\eta|\log P}.
\]
The other two terms are lower order. Hence
\[
\boxed{
D_P(\eta)^2
\sim
\frac{P^{2|\eta|}}{2|\eta|\log P},
\qquad
D_P(\eta)
\sim
\frac{P^{|\eta|}}
{\sqrt{2|\eta|\log P}}.
}
\]

With logarithmic length \(P=e^L\),
\[
\boxed{
D_{e^L}(\eta)
\sim
\frac{e^{|\eta|L}}{\sqrt{2|\eta|L}}.
}
\]

Thus the horizontal displacement from the principal line is exactly the
Lyapunov exponent of the accumulated all-prime first-order shadow mismatch.

## 2. The same exponent in the explicit formula

Let
\[
\rho=\frac12+\eta+i\gamma
\]
be a hypothetical zero with \(\eta>0\).  In the explicit formula,
the zero term in
\[
\psi(x)=x-\sum_\rho \frac{x^\rho}{\rho}+\cdots
\]
contributes after the half-density Stieltjes transform
\[
P_{1/2}(x)
=
\int_{1^-}^x u^{-1/2}\,d\psi(u)
\]
the term
\[
-\frac{x^{\rho-1/2}}{\rho-1/2}
\]
(up to the harmless lower-end constant).

Therefore the individual off-axis zero contributes to the completed
zero-frequency cutoff response \(q_L'(0)\), \(x=e^L\), a term of the form
\[
\boxed{
\frac{e^{(\eta+i\gamma)L}}{\eta+i\gamma}.
}
\]
After pairing with the conjugate zero, the real contribution has envelope
\[
\frac{2e^{\eta L}}{\sqrt{\eta^2+\gamma^2}}.
\]

So the same exponent \(\eta=\Re\rho-1/2\) appears in two independently
constructed objects:
\[
\boxed{
\text{off-line explicit-formula instability}
\quad\sim e^{\eta L},
}
\]
and
\[
\boxed{
\text{all-prime shadow/adjoint defect norm}
\quad\sim e^{\eta L}/\sqrt L.
}
\]

Possible oscillatory cancellation among zero terms prevents interpreting the
single-zero envelope as a pointwise asymptotic for the full response.  The
existing polynomial-growth criterion is the robust global statement.

## 3. Hellinger/fidelity catastrophe is stronger

For the shadow-related local geometric laws at
\(\sigma=1/2+\eta\) and \(1-\sigma=1/2-\eta\), the local Hellinger affinity is
\[
A_p(\eta)
=
\frac{
\sqrt{(1-p^{-1-2\eta})(1-p^{-1+2\eta})}
}{
1-p^{-1}
}.
\]
As \(p\to\infty\),
\[
-\log A_p(\eta)
=
\frac12p^{-1+2|\eta|}(1+o(1)).
\]
Therefore
\[
-\log\prod_{p\le P}A_p(\eta)
\sim
\frac{P^{2|\eta|}}{4|\eta|\log P}.
\]
For \(P=e^L\),
\[
\boxed{
\prod_{p\le e^L}A_p(\eta)
=
\exp\!\left[
-\frac{e^{2|\eta|L}}{4|\eta|L}(1+o(1))
\right].
}
\]

Thus a nonzero horizontal displacement causes an extremely strong global
orthogonality catastrophe.  The square-root scale of its logarithmic
fidelity loss is again \(e^{|\eta|L}/\sqrt L\), matching the explicit-formula
instability exponent.

## 4. Interpretation

The equality of exponents is not a proof of RH, but it removes another
degree of freedom from the physical interpretation.

The horizontal displacement
\[
\eta=\Re s-\frac12
\]
is simultaneously

1. the real growth/decay exponent of the Mellin mode
   \(e^{itL}e^{\eta L}\);
2. the Lyapunov exponent of the accumulated prime shadow/adjoint defect;
3. half the exponential rate in the shadow-sector fidelity catastrophe;
4. the exponential type of the corresponding off-axis term in the
   half-density explicit formula.

This quantitatively supports the view that an off-critical zero is exactly a
nonunitary leakage mode of the prime-product boundary system.

The remaining theorem is still implementability/no-escape: show that a
completed zeta zero must be represented by a normal mode in the fixed Haar
shadow sector.  If that is established, the off-axis sector is excluded both
qualitatively (Kakutani disjointness) and quantitatively (exponential
shadow-defect growth).
