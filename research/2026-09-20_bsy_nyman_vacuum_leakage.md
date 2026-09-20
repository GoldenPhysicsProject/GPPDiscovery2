# BSY integral = Nyman/Burnol vacuum leakage through the Cayley map

Date: 2026-09-20

This note identifies the quantitative Cayley defect developed in the active RH program with
the classical Balazard--Saias--Yor logarithmic criterion.

## 1. Cayley geometry

Use

beta(s)=(s-1)/s.

For s != 0,

1-|beta(s)|^2 = (2 Re(s)-1)/|s|^2.

This is formalized in

GppVerify/RiemannHypothesis/CayleyRadialDefect.lean.

Thus for every zero rho with Re rho>1/2,

a_rho=beta(rho)

lies strictly inside the disk, and its radial defect is

d_rho := 1-|a_rho|^2
       = (2 Re(rho)-1)/|rho|^2 >0.

## 2. Bad-zero Blaschke product

Let B be the Blaschke product in the Cayley disk formed from zeros rho of zeta with
Re rho>1/2, counted with multiplicity m_rho.

With the standard normalized Blaschke factors,

|B(0)|
=
prod_{Re rho>1/2} |a_rho|^{m_rho}.

Therefore

-log |B(0)|
=
sum_{Re rho>1/2} m_rho log(1/|a_rho|)
=
sum_{Re rho>1/2} m_rho log |rho/(1-rho)|.

This is exactly the zero sum appearing in the Balazard--Saias--Yor identity.

## 3. BSY identity

The classical theorem gives

I_BSY
:=
int_{-infty}^{infty}
  log|zeta(1/2+it)| /(1/4+t^2) dt

=
2 pi sum_{Re rho>1/2}
  m_rho log |rho/(1-rho)|.

Hence

boxed(I_BSY = -2 pi log |B(0)|).

This is a known theorem, not a new proof of the zero-sum formula.

## 4. Exact ghost-leakage identity

For the Nyman--Burnol model space

K_B=H2 minus B H2,

the Hardy vacuum 1 has defect

delta_vac
=
||P_{K_B}1||^2
=
1-|B(0)|^2.

Substituting the BSY identity gives the exact scalar relation

boxed(
delta_vac
=
1-exp(-I_BSY/pi)
).

Consequently the following are exactly equivalent:

RH
<=> B is constant
<=> K_B=0
<=> delta_vac=0
<=> I_BSY=0.

This does not add a new equivalence to RH; it identifies two previously separate
equivalent criteria as literally the same scalar defect under the Cayley/Hardy map.

## 5. Single-zero quantitative lower bound

If rho is any bad zero with Re rho>1/2, then all Blaschke factors have modulus <=1 at the
vacuum and

|B(0)|^2 <= |a_rho|^2.

Therefore

delta_vac
>=
1-|a_rho|^2
=
(2 Re(rho)-1)/|rho|^2.

So every bad zero injects a definite positive amount of vacuum leakage.

With multiplicity m_rho one has the stronger single-factor bound

delta_vac >= 1-(1-d_rho)^{m_rho}.

## 6. Aggregate defect / entropy coordinate

Define

D_inner := -log |B(0)|^2 = I_BSY/pi.

Then

delta_vac = 1-e^{-D_inner}.

The quantity D_inner is additive over bad-zero Blaschke factors:

D_inner
=
sum m_rho [-log(1-d_rho)].

For small radial defects,

-log(1-d_rho)
=
d_rho+O(d_rho^2),

so D_inner linearizes as the weighted total horizontal displacement

sum m_rho (2 Re(rho)-1)/|rho|^2

to first order.

This is a useful global defect coordinate because multiplicative inner losses become
additive.

## 7. Correction to the earlier "boundary modulus is blind" slogan

Ordinary boundary quadratic forms which depend only on |Z| cannot recover the detailed
Blaschke function B or the locations of its zeros.

However, once the interior normalization at the Hardy vacuum is fixed, the logarithmic
Poisson mean of the boundary modulus DOES recover the aggregate scalar |B(0)|.

Thus the correct statement is:

- boundary modulus is blind to the detailed inner factor;
- boundary logarithmic mean plus a fixed interior normalization detects the vacuum inner
  defect exactly.

BSY is precisely this Jensen/Poisson recovery.

## 8. New constructive target: determinant/entropy conservation

The active finite Möbius--Koszul bulk has determinant one, while the bordered Schur system
pushes arithmetic data into one global boundary response.

This suggests replacing the vague "no escaped trace" target by a multiplicative version:

prove conservation of the normalized logarithmic determinant / outer entropy through the
finite prime--Archimedean limit.

If the finite completed transfers have zero inner entropy and their logarithmic determinant
is uniformly integrable under the limiting process, then

I_BSY=0,

hence delta_vac=0 and RH.

The danger is now explicit: strong operator convergence alone does not preserve logarithmic
determinants or boundary log integrals. A zero approaching the boundary can lose determinant
mass in the limit.

Therefore the concrete analytic target is a uniform-integrability / determinant-class
estimate strong enough to interchange

lim_N int log |F_N|

with

int log |F|.

This is the multiplicative analogue of the previously identified trace-escape problem.

## 9. Why this may be more tractable

The BSY obstruction is a single nonnegative scalar rather than the full Weil quadratic form.
A proof does not need to reconstruct the entire bad-zero inner function. It is enough to
show no logarithmic determinant mass escapes at the Hardy vacuum.

Potential tools:
- Jensen/Poisson formula in the Cayley disk;
- Szego-type determinant identities for finite Toeplitz/Schur sections;
- Fuglede--Kadison determinants for lossless colligations;
- uniform lower bounds preventing boundary zeros from creating log singularities;
- the exact finite determinant-one Möbius bulk plus the Archimedean Schur seed.

This is not yet a proof. It is a reduction of the global ghost to determinant/entropy
conservation in the zero-independent finite completion.
