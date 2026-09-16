# Causal supercharge completion of the theta-deficit kernel — 2026-09-15

Status: exact derivations. No RH proof claimed.

## 1. Start from the Green-completed theta deficit

For x >= 0 define

\[
g(x)=e^{-x/2}-e^{x/2}K(x),\qquad K(x)=\vartheta(e^{2x})-1.
\]

The even continuation of g satisfies

\[
H_C g=2\Phi,\qquad H_C=-D^2+\frac14.
\]

The direct cosine transform of g converges only for |Im z|<1/2, because g(x)~e^{-x/2}; this is exactly the completion-pole boundary. Thus positivity of g cannot simply be Laplace-transferred to the safe Euler ray s>1.

## 2. Apply the first-order Casimir supercharge before crossing the boundary

Let

\[
Q=D+\frac12,\qquad Q^*=-D+\frac12,
\qquad H_C=Q^*Q.
\]

For x>0 put

\[
q(x):=(Qg)(x).
\]

Since Q annihilates e^{-x/2},

\[
q(x)=-e^{x/2}(K'(x)+K(x)).
\]

Writing y_n=\pi n^2e^{2x},

\[
K(x)=2\sum_{n\ge1}e^{-y_n},\qquad
K'(x)=-4\sum_{n\ge1}y_ne^{-y_n},
\]

so

\[
\boxed{
q(x)=2e^{x/2}\sum_{n\ge1}(2y_n-1)e^{-y_n}>0
}\]

for all x>=0, since y_n>=pi>1/2. Moreover q decays super-exponentially as x->+infinity.

The adjoint first-order factor gives

\[
\boxed{Q^*q=H_Cg=2\Phi.}
\]

Thus the dangerous e^{-x/2} mode is removed before taking a one-sided transform.

At x=0,

\[
q(0)=1-\frac12\vartheta(1)>0.
\]

## 3. Entire one-sided transform

Define

\[
A(z)=\int_0^\infty q(x)e^{izx}\,dx.
\]

Because q is super-exponentially decreasing, A is entire.

From Q^*q=2\Phi and the Riemann representation

\[
\Xi(z)=2\int_0^\infty\Phi(x)\cos(zx)\,dx,
\]

integration by parts gives

\[
\Xi(z)
=q(0)-z\int_0^\infty q(x)\sin(zx)\,dx
+\frac12\int_0^\infty q(x)\cos(zx)\,dx.
\]

Equivalently, define

\[
\boxed{E(z)=q(0)+\left(\frac12+iz\right)A(z).}
\]

For real q,

\[
E^\#(z)=\overline{E(\bar z)}
=q(0)+\left(\frac12-iz\right)A(-z),
\]

and hence

\[
\boxed{\Xi(z)=\frac{E(z)+E^\#(z)}2.}
\]

This is a zero-independent entire causal/shadow decomposition. It does not prove that E or E^# is Hermite-Biehler; that is a new exact positivity/contractivity target.

## 4. Safe real-axis representation

Put s=1/2+r with r>0, so z=-ir. Since A is entire, no continuation is needed. One gets

\[
\boxed{
\xi\!\left(\frac12+r\right)
=q(0)+\int_0^\infty q(x)
\left[r\sinh(rx)+\frac12\cosh(rx)\right]dx.
}
\]

The kernel in brackets is strictly positive for r>0, x>0. This yields scalar positivity directly from the boundary-quotiented positive q, but does not by itself imply the Loewner/Pick hierarchy.

Equivalently,

\[
\xi(s)=q(0)+\frac12\left[sA\!\left(-i(s-\tfrac12)\right)
+(1-s)A\!\left(i(s-\tfrac12)\right)\right].
\]

## 5. Interpretation

The hierarchy is now

\[
g>0\quad\xrightarrow{Q}\quad q>0\text{ and super-exponential}
\quad\xrightarrow{Q^*}\quad2\Phi>0.
\]

The first-order factor Q kills exactly the completion boundary mode that limited the transform of g to |Im z|<1/2. The causal amplitude E is therefore entire and genuinely one-sided. The remaining theorem is not existence or convergence of the causal completion, but its Hilbert-space contractivity/Hermite-Biehler property.

This route should be compared directly with the Hardy leakage quotient and endpoint Laguerre-Nevanlinna kernel; no claim of equivalence by a bounded intertwiner is made here yet.