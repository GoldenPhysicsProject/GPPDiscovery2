# Haar-profinite internal mass law from finite-place Casimir weights

Date: 2026-09-26
Status: exact probability theorem from the critical Haar valuation law and the finite-place mass coordinate. Physical interpretation as dark matter is hypothetical.

## 1. Haar random profinite integer

Let

\[
X\sim {\rm Haar}(\widehat{\mathbf Z}).
\]

For each prime \(p\), put

\[
N_p=v_p(X).
\]

The normalized Haar measure gives independent geometric valuations

\[
\boxed{
\Pr(N_p=a)
=
(1-p^{-1})p^{-a},
\qquad
a=0,1,2,\dots
}
\]

with

\[
\mathbb E N_p=\frac1{p-1},
\qquad
{\rm Var}(N_p)=\frac{p}{(p-1)^2}.
\]

Because

\[
\sum_p\Pr(N_p\ge1)=\sum_p\frac1p=\infty,
\]

independence and Borel--Cantelli imply that a Haar-typical profinite integer has
nonzero valuation at infinitely many primes.

So the critical finite-place state is an infinite soft arithmetic cloud, not a finite
integer factorization.

## 2. Casimir-weighted internal mass

Use the already derived finite-place transfer/Casimir mass

\[
\mu_p=\frac{2}{\sqrt{p-1}}.
\]

Define the nonnegative random variable

\[
\boxed{
\mathcal M(X)
=
M_*\sum_p\mu_p N_p
=
2M_*\sum_p\frac{N_p}{\sqrt{p-1}}.
}
\]

Its expectation is

\[
\frac{\mathbb E\mathcal M}{M_*}
=
2\sum_p
\frac1{(p-1)^{3/2}}
=:C_1.
\]

The series converges, with

\[
\boxed{
C_1\approx3.4368.
}
\]

Because \(\mathcal M\ge0\) and \(\mathbb E\mathcal M<\infty\),

\[
\boxed{
\mathcal M(X)<\infty
\quad\text{for Haar-almost every }X.
}
\]

Thus a Haar-typical profinite state contains infinitely many occupied finite places but
has finite Casimir-weighted total mass.

## 3. Exact Laplace transform

For a single prime,

\[
\mathbb E(e^{-t\mu_pN_p})
=
(1-p^{-1})
\sum_{a\ge0}
p^{-a}e^{-t\mu_pa}
=
\frac{1-p^{-1}}
{1-p^{-1}e^{-t\mu_p}}.
\]

Independence gives

\[
\boxed{
\mathbb E
\exp\!\left[-t\frac{\mathcal M}{M_*}\right]
=
\prod_p
\frac{1-p^{-1}}
{1-p^{-1}\exp[-2t/\sqrt{p-1}]}
\qquad(t\ge0).
}
\]

Although the separate Euler product \(\prod_p(1-p^{-1})\) vanishes, the ratio product
above converges: for large \(p\),

\[
1-
\frac{1-p^{-1}}
{1-p^{-1}e^{-2t/\sqrt{p-1}}}
=
O(p^{-3/2}).
\]

This defines a universal arithmetic probability law for the hidden internal mass.

## 4. Variance

Independence gives

\[
\frac{{\rm Var}(\mathcal M)}{M_*^2}
=
\sum_p
\mu_p^2\,{\rm Var}(N_p)
=
4\sum_p\frac{p}{(p-1)^3}.
\]

Hence

\[
\boxed{
\frac{{\rm Var}(\mathcal M)}{M_*^2}
\approx10.0904.
}
\]

The hidden mass law is therefore broad rather than monochromatic.

## 5. Mass-square functional

There is a second natural positive observable,

\[
\boxed{
\mathcal Q(X)
=
\sum_p\mu_p^2N_p
=
4\sum_p\frac{N_p}{p-1}.
}
\]

Its expectation is

\[
\boxed{
\mathbb E\mathcal Q
=
4\sum_p\frac1{(p-1)^2}
=
C_2
\approx5.500260.
}
\]

Its exact Laplace transform is

\[
\boxed{
\mathbb E(e^{-t\mathcal Q})
=
\prod_p
\frac{1-p^{-1}}
{1-p^{-1}\exp[-4t/(p-1)]}.
}
\]

Again the infinite occupation number is harmless because the Casimir weighting makes
the observable integrable.

## 6. Spectral-density asymptotics

The mass map

\[
m_p=\frac{2M_*}{\sqrt{p-1}}
\]

gives

\[
p
=
1+\frac{4M_*^2}{m^2}.
\]

Using the prime number theorem, the unweighted number of prime channels in a mass
interval has asymptotic density

\[
dN_{\rm prime}(m)
\sim
\frac{8M_*^2}
{m^3\log(1+4M_*^2/m^2)}
\,dm
\]

toward small \(m\).

Multiplying by the mean Haar occupation

\[
\langle N_p\rangle
=
\frac{m^2}{4M_*^2}
\]

gives the occupied-channel density

\[
\boxed{
dN_{\rm occ}(m)
\sim
\frac{2}
{m\log(1+4M_*^2/m^2)}
\,dm.
}
\]

Multiplying once more by the rest energy \(m\) gives

\[
\boxed{
dE(m)
\sim
\frac{2}
{\log(1+4M_*^2/m^2)}
\,dm.
}
\]

Thus the infinite accumulation of channels at \(m=0\) has finite energy: the energy
density per unit mass interval actually tends to zero logarithmically in the deep IR.

## 7. Dark-sector interpretation

A possible physical interpretation is that an Archimedean excitation carries an
unobserved profinite internal coordinate \(X\).  Its finite-place cloud then contributes
the universal internal mass \(\mathcal M(X)\).

This would produce a broad neutral hidden mass distribution from Haar measure alone,
rather than one manually chosen WIMP mass.

However, nothing above proves:

- that spacetime particles carry such an internal profinite coordinate;
- that \(\mathcal M\) is the operator appearing in the 4D stress tensor;
- that the states are stable;
- that they are produced with the cosmological abundance required for dark matter;
- that their phase-space distribution clusters correctly.

Those are the next physical reconstruction problems.

The exact mathematical survivor is:

\[
\boxed{
\text{Haar-critical profinite state}
+
\mu_p=2/\sqrt{p-1}
\Longrightarrow
\text{infinite soft occupation with finite universal mass law}.
}
\]
