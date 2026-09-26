# Adelic finite-place dark sector: conditional cold-fluid mechanism

Date: 2026-09-26
Status: new exact arithmetic calculation + conditional 4D effective-field model. This is NOT yet a derivation of dark matter from the adelic theory.

## 1. Inputs already derived independently

At the critical Haar/Hagedorn boundary, the local valuation law is

\[
\Pr(N_p=a)=(1-p^{-1})p^{-a},
\qquad a=0,1,2,\dots
\]

so

\[
\boxed{\mathbb E N_p=\frac1{p-1}.}
\]

The finite-place hyperbolic/Casimir coordinate gives

\[
\boxed{
\mu_p=\frac{2}{\sqrt{p-1}},
\qquad
\mu_p^2=\frac4{p-1}.
}
\]

These are exact ingredients already present in the arithmetic-shadow program.

## 2. Minimal 4D realization

Test the hypothesis that every finite place produces a neutral real-place scalar mode
\(\chi_p\) after adelic sewing, with physical mass

\[
m_p=M_*\mu_p
=
\frac{2M_*}{\sqrt{p-1}}.
\]

Use the ordinary 4D action

\[
S_{\rm hid}
=
-\frac12\sum_p\int d^4x\sqrt{-g}
\left[
(\nabla\chi_p)^2+m_p^2\chi_p^2
\right].
\]

This is only an effective ansatz.  The missing adelic reconstruction theorem must
derive this real-place field tower rather than assume it.

Now impose the critical Haar occupation normalization on the field variance:

\[
\boxed{
A_p^2
=
A_*^2\,\mathbb E N_p
=
\frac{A_*^2}{p-1}.
}
\]

For \(m_p\gg H\), the homogeneous scalar oscillates as

\[
\chi_p(t)
\simeq
A_p\,a^{-3/2}\cos(m_pt+\delta_p).
\]

Averaging over many oscillations gives the standard dust limit

\[
\langle \rho_p\rangle
=
\frac12m_p^2A_p^2a^{-3},
\qquad
\langle P_p\rangle
\simeq0.
\]

Substituting the arithmetic mass and Haar variance,

\[
\boxed{
\langle\rho_p\rangle
=
2M_*^2A_*^2
\frac{a^{-3}}{(p-1)^2}.
}
\]

Therefore the sum over finite places converges absolutely:

\[
\boxed{
\rho_{\rm fin}(a)
=
2M_*^2A_*^2\,\mathcal C_{\rm p}\,a^{-3},
\qquad
\mathcal C_{\rm p}
=
\sum_p\frac1{(p-1)^2}.
}
\]

So, conditional on the real-place scalar realization and coherent cold initial
conditions, the finite-place sector is automatically pressureless and has the exact
cosmological scaling of cold matter.

## 3. Number-theoretic dark coefficient

Normalize a single reference Archimedean mode with the same mass/amplitude scale,

\[
\rho_{\rm ref}
=
\frac12M_*^2A_*^2a^{-3}.
\]

Then

\[
\boxed{
\frac{\rho_{\rm fin}}{\rho_{\rm ref}}
=
C_{\rm adelic}
:=
4\sum_p\frac1{(p-1)^2}.
}
\]

The series is a genuine arithmetic constant.  Expanding

\[
\frac1{(p-1)^2}
=
\frac{p^{-2}}{(1-p^{-1})^2}
=
\sum_{k\ge2}(k-1)p^{-k}
\]

gives the prime-zeta representation

\[
\boxed{
C_{\rm adelic}
=
4\sum_{k\ge2}(k-1)P(k),
}
\]

where \(P(k)=\sum_p p^{-k}\) is the prime zeta function.

Numerically,

\[
\boxed{
C_{\rm adelic}
\approx 5.500260.
}
\]

This number is not fitted to cosmology; it comes only from the critical Haar
occupation law and the finite-place Casimir mass.

## 4. A striking low-prime concentration

The first four prime places contribute

\[
4\left[
\frac1{(2-1)^2}
+\frac1{(3-1)^2}
+\frac1{(5-1)^2}
+\frac1{(7-1)^2}
\right]
=
4+1+\frac14+\frac19.
\]

Hence

\[
\boxed{
C_{2,3,5,7}
=
\frac{193}{36}
=
5.361111\ldots
}
\]

The remainder from every prime \(p\ge11\) is only

\[
\boxed{
C_{\rm tail}
=
C_{\rm adelic}-\frac{193}{36}
\approx0.139149,
}
\]

so the first four primes carry about

\[
\boxed{97.47\%}
\]

of the total finite-place rest-energy coefficient.

The numerical proximity of \(193/36\) to the observed cosmological dark-to-baryonic
matter ratio is striking, but at present it is only a clue.  It must NOT be promoted
to a prediction unless the dynamics independently explains why the modes
\(p=2,3,5,7\) cluster as cold matter while the \(p\ge11\) tail does not.

## 5. Why a dynamical split is at least plausible

The masses decrease monotonically:

\[
m_p=\frac{2M_*}{\sqrt{p-1}}.
\]

Thus low primes are the heaviest modes and enter the oscillatory/cold regime first,
while high primes form an increasingly light tail.

For a threshold mass \(m_c\), the modes lighter than \(m_c\) satisfy approximately

\[
p>
P_c
\simeq
1+\left(\frac{2M_*}{m_c}\right)^2.
\]

Their fractional rest-energy tail obeys, using the prime number theorem,

\[
\sum_{p>P_c}\frac4{(p-1)^2}
\sim
\frac4{P_c\log P_c}.
\]

Hence

\[
\boxed{
f_{\rm light}
\sim
\frac{(m_c/M_*)^2}
{C_{\rm adelic}\,
\log\!\left(4M_*^2/m_c^2\right)}.
}
\]

The ultralight end therefore carries parametrically little energy even though there
are infinitely many finite places.

This solves one immediate consistency concern: the spectrum accumulates at zero mass,
but the Haar/Casimir weighting makes the total energy finite and strongly dominated
by the first few primes.

## 6. Linear perturbations

For a coherently oscillating massive scalar, the nonrelativistic effective sound speed
on comoving wavenumber \(k\) is of order

\[
c_{s,p}^2
\sim
\frac{k^2}{4a^2m_p^2}.
\]

Therefore the low-prime modes behave like ordinary collisionless cold matter whenever

\[
\frac{k}{a}\ll m_p.
\]

The very-light prime tail would remain smooth on progressively larger scales, giving
a possible split into

\[
\text{clustered low-prime sector}
+
\text{smooth/light high-prime sector}.
\]

A proper Boltzmann perturbation calculation is required before comparing this with
CMB, lensing, or structure-growth data.

## 7. Important distinction from a pure vacuum-polarization model

Simply integrating out finite-place fields in their vacuum generally produces
cosmological-constant and higher-curvature terms.  That is NOT enough to obtain dark
matter.

The dust result above requires a state carrying conserved/coherent finite-place
excitations.  In other words,

\[
\boxed{
\text{finite places as vacuum correction}
\neq
\text{dark matter},
}
\]

whereas

\[
\boxed{
\text{finite-place massive modes in an oscillatory number state}
\longrightarrow
w\simeq0,\quad\rho\propto a^{-3}.
}
\]

This is the first hard discriminator for the adelic-dark-sector idea.

## 8. Relation to the older structural-dark-matter manuscript

The older manuscript attempts to obtain dark matter from a hidden
\(\mathbf C^2\) Grassmannian sector and a postulated compactification scale.
The present route is conceptually different and more tightly tied to the arithmetic
work:

\[
\text{finite places}
\to
\text{Haar valuation law}
\to
\text{Casimir masses}
\to
\text{real-place massive tower}
\to
\text{cold-fluid limit}.
\]

It does not require identifying a hidden \(\mathbf C^2\) sector with Standard Model
gauge neutrality, nor does it presently derive a galactic halo profile.

## 9. Load-bearing missing theorem

The real physics problem is now sharply stated:

**Adelic real-place reconstruction target.**
Construct, from a global adelic field/state and without inserting a dark sector by hand,
a real-place effective theory whose finite-place internal spectrum has

\[
m_p^2\propto\frac4{p-1}
\]

and whose critical-state covariance is

\[
\langle |\chi_p|^2\rangle\propto\frac1{p-1}.
\]

If this theorem holds, the pressureless scaling and the convergent arithmetic coefficient
above follow automatically.

After that, the next tests are:
1. derive the epoch-dependent cold/smooth split from \(m_p/H(a)\);
2. solve the linear Einstein-Boltzmann system for the prime tower;
3. test whether the clustered coefficient is naturally \(193/36\) or the full
   \(C_{\rm adelic}\);
4. derive halo-scale behavior rather than fitting a profile;
5. check Bullet-Cluster-type lensing and early-universe constraints.

No dark-matter discovery is claimed at this stage.


## 10. Correction: occupation energy and field-amplitude energy are different moments

The critical cylinder law naturally lives in an occupation-number basis.  Therefore the
most canonical Fock interpretation is

\[
\rho_p
=
(1-p^{-1})
\sum_{a\ge0}p^{-a}|a\rangle\langle a|,
\qquad
\langle N_p\rangle=\frac1{p-1}.
\]

If a finite-place quantum has real-place rest mass

\[
m_p=M_*\mu_p=\frac{2M_*}{\sqrt{p-1}},
\]

then the normal-ordered particle Hamiltonian

\[
H_{\rm phys}
=
\sum_p m_p N_p
\]

has expectation

\[
\boxed{
\frac{\langle H_{\rm phys}\rangle}{M_*}
=
C_1
:=
2\sum_p\frac1{(p-1)^{3/2}}
\approx3.4368.
}
\]

This converges.  In contrast,

\[
\sum_p\langle N_p\rangle
=
\sum_p\frac1{p-1}
\]

diverges logarithmically (prime-harmonically).  The boundary state therefore contains an
infinite soft occupation cloud but can carry finite physical rest energy.

The coefficient

\[
C_2
=
4\sum_p\frac1{(p-1)^2}
\approx5.500260
\]

computed above is instead the expectation of the dimensionless mass-square weighted number:

\[
\boxed{
C_2
=
\left\langle
\sum_p\frac{m_p^2}{M_*^2}N_p
\right\rangle.
}
\]

Equivalently it is the coefficient obtained if the real-place field covariance is taken
directly proportional to the Haar occupation without the canonical oscillator factor
\(1/m_p\).

For an ordinary canonically normalized oscillator,

\[
\langle \chi_p^2\rangle
\sim
\frac{\langle N_p\rangle}{m_p},
\]

so the mass-term energy \(m_p^2\langle\chi_p^2\rangle\) scales as
\(m_p\langle N_p\rangle\), i.e. with \(C_1\), not \(C_2\).

Therefore:

\[
\boxed{
C_1\approx3.4368
\text{ is the canonical particle-energy constant;}
}
\]

\[
\boxed{
C_2\approx5.500260
\text{ is a second mass moment and requires an additional noncanonical/geometric
normalization to become an energy-density ratio.}
}
\]

In particular the numerical proximity of the first-four-prime partial sum
\(193/36=5.361111\ldots\) to the cosmological dark/baryonic ratio must be treated as
numerology until the stress tensor is derived and shown to probe \(C_2\) rather than
\(C_1\).

This correction strengthens the research program by identifying exactly which observable
must emerge from the adelic gravitational coupling.
