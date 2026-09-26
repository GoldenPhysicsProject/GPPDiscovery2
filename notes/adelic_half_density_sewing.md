# Adelic half-density sewing: Dirichlet weights as finite-Haar amplitude times real principal-series phase

Date: 2026-09-26
Status: exact local/global algebra. No RH claim.

## 1. The product-formula split

Let \(m\ge1\) be an integer.

At the real place, on
\[
H_\infty=L^2(\mathbf R_+,dx),
\]
use the unitary dilation
\[
(U_m^\infty f)(x)=m^{1/2}f(mx).
\]
For the generalized Mellin mode \(f_s(x)=x^{-s}\),
\[
U_m^\infty f_s
=
m^{1/2-s}f_s.
\]

At the finite places, let
\[
\widehat{\mathbf Z}=\prod_p\mathbf Z_p,
\qquad
\Omega_f=1\in L^2(\widehat{\mathbf Z}),
\]
and use the normalized divisibility isometry
\[
(V_m^f F)(x)
=
\sqrt m\,1_{m\widehat{\mathbf Z}}(x)F(x/m).
\]
Since
\[
\mu(m\widehat{\mathbf Z})=\frac1m,
\]
one has
\[
\langle\Omega_f,V_m^f\Omega_f\rangle
=m^{-1/2}.
\]

Multiplying the finite and real factors gives
\[
\boxed{
\langle\Omega_f,V_m^f\Omega_f\rangle
\cdot
m^{1/2-s}
=
m^{-s}.
}
\]

Thus every Dirichlet monomial has an exact adelic sewing:
\[
\boxed{
m^{-s}
=
\underbrace{m^{-1/2}}_{\text{finite-Haar overlap}}
\;
\underbrace{m^{1/2-s}}_{\text{real half-density dilation character}}.
}
\]

This is the square-root form of the adelic product formula.  Multiplication by
\(m\) scales additive Haar measure at the real place by \(m\), while its
finite-adelic modulus is
\[
|m|_f=\prod_p|m|_p=m^{-1}.
\]
The two Jacobians cancel globally.

## 2. Principal-series meaning

On
\[
s=\frac12+it,
\]
the Archimedean factor becomes
\[
m^{1/2-s}=m^{-it}=e^{-it\log m},
\]
a pure unitary phase.  Therefore
\[
\boxed{
m^{-1/2-it}
=
\text{finite-place Haar amplitude}
\times
\text{Archimedean principal-series phase}.
}
\]

Under the 1D conformal dictionary
\[
h=s,
\]
this is exactly the conformal dilation character of a weight
\[
h=\frac12+it.
\]
The 2D scalar celestial notation is merely
\[
\Delta=2h=1+2it.
\]

So the ubiquitous arithmetic half-density is not assigned wholly to either
the prime sector or the real/celestial sector.  It is the interface factor
created by splitting a globally measure-preserving adelic dilation into its
finite and Archimedean components.

## 3. Prime powers are repeated local propagation

For \(m=p^a\),
\[
p^{-as}
=
p^{-a/2}e^{-iat\log p}.
\]
The local Euler factor on the principal line is therefore
\[
\frac1{1-p^{-s}}
=
\sum_{a\ge0}
p^{-a/2}e^{-iat\log p}.
\]

Interpretation:
- \(a\) is local occupation / repeated traversal number;
- \(p^{-a/2}\) is the finite-Haar transmission amplitude;
- \(a\log p\) is the additive logarithmic propagation length;
- \(e^{-it a\log p}\) is the unitary real-place/celestial phase.

The logarithmic generator adds the energy
\[
\log p=\Lambda(p^a)
\]
to every repeated prime orbit, producing the von-Mangoldt current.

This makes the local scattering picture exact:
\[
\boxed{
\text{prime }p
=
\text{finite-place channel},
\quad
\log p
=
\text{channel length/energy},
\quad
p^{-1/2}
=
\text{Haar transmission amplitude}.
}
\]

## 4. Why the critical line is special locally but RH remains global

For every fixed prime, the geometric series above is perfectly convergent on
the critical line because \(p^{-1/2}<1\).  The obstruction is not local.

The full Euler product fails ordinary convergence there because
\[
\sum_p p^{-1/2}
\]
diverges.  Thus the global completed state must be obtained by a genuinely
adelic/prime--Archimedean completion rather than by multiplying the local
channels naively.

Off the principal line,
\[
s=\frac12+\eta+it,
\]
the real-place factor becomes
\[
m^{-\eta-it}.
\]
It is no longer a unitary dilation character in the fixed Lebesgue
half-density metric.  Its shadow partner has the opposite real exponent.
The all-prime shadow/adjoint defect then grows with Lyapunov exponent
\(|\eta|\), as recorded in the companion off-axis Lyapunov note.

## 5. Consequence for the physical picture

This gives a sharper architecture than "primes are particles":

\[
\boxed{
\text{finite places set amplitudes}
\quad+\quad
\text{real/celestial place supplies unitary phases}
\quad=\quad
\text{Dirichlet/Euler propagation}.
}
\]

A zeta zero on the critical line is then a global destructive-interference
condition of this sewn adelic propagation.  In the BPY realization this is
literally a unitary survival-amplitude zero:
\[
\Xi(t)=0
\iff
\langle\psi,e^{itX}\psi\rangle=0.
\]

The missing RH theorem is to prove that the completed global arithmetic
zero condition has no additional nonunitary analytic resonances outside this
unitary sewing.  Equivalently: completed prime--Archimedean sewing must be
causal/normal with no escaped shadow sector.
