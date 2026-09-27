# Prime TFD states are exactly the rank-one de Branges--Rovnyak defects of the local Blaschke channels

Date: 2026-09-27
Status: exact local and finite-cascade kernel identities. The infinite adelic renormalized limit remains open. No RH proof.

## 1. One prime: Blaschke transfer and its defect kernel

Let
\[
B_a(z)=\frac{z-a}{1-az},
\qquad 0<a<1.
\]

Its Schur/de Branges--Rovnyak defect kernel is
\[
D_a(z,w)
=
\frac{
1-B_a(z)\overline{B_a(w)}
}{
1-z\bar w
}.
\]

A direct algebraic calculation gives
\[
\boxed{
D_a(z,w)
=
\frac{1-a^2}
{(1-az)(1-a\bar w)}.
}
\]

Therefore
\[
\boxed{
D_a(z,w)=f_a(z)\overline{f_a(w)},
\qquad
f_a(z)=\frac{\sqrt{1-a^2}}{1-az}.
}
\]

So the defect space of a single Blaschke factor is rank one.

## 2. The defect vector is exactly the TFD coherent state

The prime TFD/SU(1,1) coherent state is
\[
|\Omega_a\rangle
=
\sqrt{1-a^2}
\sum_{m\ge0}a^m e_m.
\]

Its Hardy boundary amplitude is
\[
\langle z|\Omega_a\rangle
=
\frac{\sqrt{1-a^2}}{1-az}
=
f_a(z).
\]

Hence
\[
\boxed{
D_a(z,w)
=
\langle z|\Omega_a\rangle
\overline{\langle w|\Omega_a\rangle}.
}
\]

Thus the local TFD state is not merely analogous to the local scattering defect: it **is the defect vector** of the local Blaschke colligation.

For a prime,
\[
a=a_p=p^{-1/2}.
\]

## 3. Boundary probability is the Poisson/group-delay kernel

On the unit circle z=e^{i\theta},
\[
|f_a(e^{i\theta})|^2
=
\frac{1-a^2}{1-2a\cos\theta+a^2}
=
\boxed{\mathcal P_a(\theta)}.
\]

But the same Poisson kernel is
\[
\frac{d}{d\theta}
\arg B_a(e^{i\theta}).
\]

Therefore the following three objects are literally identical:
\[
\boxed{
\text{TFD boundary probability density}
=
\text{de Branges defect intensity}
=
\text{Blaschke Wigner--Smith delay}.
}
\]

This closes the local coherent-state/scattering/de Branges triangle exactly.

## 4. Product rule for defect kernels

Let B_1 and B_2 be Schur functions. Then
\[
1-B_1B_2\overline{B_1B_2}
=
(1-B_1\bar B_1)
+
B_1\bar B_1(1-B_2\bar B_2).
\]

Therefore
\[
\boxed{
D_{B_1B_2}(z,w)
=
D_{B_1}(z,w)
+
B_1(z)\overline{B_1(w)}
D_{B_2}(z,w).
}
\]

Iterating for a finite cascade
\[
B^{(N)}=\prod_{j=1}^N B_j
\]
gives
\[
\boxed{
D_{B^{(N)}}(z,w)
=
\sum_{j=1}^N
\left(
\prod_{k<j}B_k(z)
\right)
D_{B_j}(z,w)
\overline{
\left(
\prod_{k<j}B_k(w)
\right)
}.
}
\]

If each B_j is a one-prime Blaschke factor, every D_{B_j} is rank one.

Hence
\[
\boxed{
D_{B^{(N)}}=
\sum_{j=1}^N
F_j\otimes F_j^*
}
\]
with transported TFD feature vectors
\[
F_j(z)
=
\left(\prod_{k<j}B_k(z)\right)f_{a_j}(z).
\]

The finite prime cascade therefore has an explicit positive Gram factorization.

## 5. Quotients turn the RH sign into a defect-kernel domination problem

Suppose A and B are nonvanishing Schur/inner functions in a domain and form
\[
\Theta=\frac{A}{B}.
\]

Then
\[
1-\Theta(z)\overline{\Theta(w)}
=
\frac{
B(z)\overline{B(w)}
-
A(z)\overline{A(w)}
}{
B(z)\overline{B(w)}
}.
\]

Since
\[
B\bar B-A\bar A
=
(1-A\bar A)-(1-B\bar B),
\]
we get
\[
\boxed{
D_\Theta(z,w)
=
\frac{
D_A(z,w)-D_B(z,w)
}{
B(z)\overline{B(w)}
}.
}
\]

Multiplication by the nonzero scalar feature 1/B is a congruence. Therefore
\[
\boxed{
D_\Theta\succeq0
\iff
D_A-D_B\succeq0.
}
\]

This is exactly the mathematical form of the prime-versus-Archimedean no-ghost problem.

## 6. Interpretation for the shifted completed-zeta transfer

The RH program already uses a shifted transfer
\[
\Theta_\omega(z)
=
\frac{
\xi(1/2-\omega-iz)
}{
\xi(1/2+\omega-iz)
}.
\]

On the real boundary it is unitary. RH is equivalent to the appropriate analytic/Schur contractivity of this transfer for every omega>0.

The factorization of xi separates:
- an Archimedean/rational transfer;
- the finite-prime Euler/scattering cascade.

The local calculation above says the prime-side defect kernel is a positive sum of transported TFD rank-one features **before** the relative Archimedean quotient is taken.

Thus the global problem has the exact schematic form
\[
\boxed{
D_{\rm completed}
\sim
D_\infty-D_{\rm prime}.
}
\]

The missing theorem is precisely
\[
\boxed{
D_\infty\succeq D_{\rm prime}
}
\]
after the correct infinite-prime renormalization and rational/idele sewing.

This is the kernel version of the existing odd-transfer contraction criterion.

## 7. Why local positivity never proved RH

Every one-prime defect is positive:
\[
D_p=f_p\otimes f_p^*\succeq0.
\]

Every finite raw prime cascade also has a positive defect kernel.

But the completed zeta transfer is a **relative quotient**. Its defect is an Archimedean defect minus a prime defect after congruence.

Therefore local positivity is automatic and insufficient. The load-bearing statement is a global kernel domination theorem.

This recovers, in one line, the distinction that earlier AFT/OS work reached by a much longer route.

## 8. Concrete next target

The newly identified universal SU(1,1) module gives explicit realizations for both sides:
- prime defect vectors are TFD coherent states;
- the Archimedean Plancherel/Gamma sectors are K1/K0 polarizations of the same module.

The next constructive problem is therefore to write the Archimedean defect kernel in the **same feature coordinates** as the finite-prime TFD vectors and test whether the renormalized difference admits a positive Gram factorization.

That is substantially more specific than searching for an abstract Hilbert--Polya operator.
