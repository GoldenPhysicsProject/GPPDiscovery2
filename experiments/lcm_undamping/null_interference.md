# A shifted xi filter has zero self-energy and measurable cross-energy

Write z=s−1/2, H(z)=ξ(1/2+z), θ=1/4, A(z)=H(z+θ), D(z)=H(z−θ), and F=AD. All these entire functions are real on the real axis and H is even. For real packets use the polarized Weil zero sum [U,V]_P=Σ P-zero r U(r)V(−r), counting multiplicity, in centered coordinates. Reflection makes this symmetric. In this note the transforms are A and h and their real linear combinations, where h(z)=(1/(z+b)+1/(z+conj b))/2, b=2+14i. The inverse Laplace packet for h is exp(−2u)cos(14u) on the positive half-line. A is obtained directly from the theta transform or the completed zeta formula. On every fixed vertical strip A decays exponentially in height times a polynomial; its inverse bilateral Laplace transform and its derivatives decay faster than any fixed exponential on the real log line by contour shifting. The zero sums converge absolutely, also for h,h by the standard zero count. These are extended test packets. Finite smooth time cutoffs and mollification recover their energies by the explicit formula (exponential correlation tails and bounded variation at the origin).

## Nullness and reflection

A(−z)=D(z). Hence [A,A]_F=Σ F(r)=0 exactly. The stronger statement [H,V]_H=0 for every admissible V follows pointwise from H(r)=0. The mixed pairing [A,h]_F is strictly negative by the arithmetic enclosure below. Consequently the shifted filter is isotropic but outside the radical. The two-dimensional matrix for A,h has determinant −[A,h]_F². This gives both signs for the shifted model independently of the size of [h,h]_F. A positive semidefinite form always sends a zero-energy vector to the radical by polarization or Cauchy–Schwarz. The distinction here is operational. Both models obey the same global reflection. Also every positive semidefinite form has this radical property, but the converse is false without additional assumptions (a negative definite form is one example).

## Arithmetic enclosure on the same packet

Put U=A+h/10000. The carrier 14 and quarter shift were inherited from the targeted comparison. No zero ordinates enter the program. For P=H or F let m=P′/P. On Re z=c=5/4, the residue theorem and evenness give

    [A,h]_P = (1/π)∫₀∞ Re{m(z)[A(z)h(−z)+D(z)h(z)]} dt,
    [A,A]_H = (1/π)∫₀∞ Re{2m_H(z) A(z)D(z)} dt,    z=c+it.

The contours enclose all centered zeros, leaving the poles of the rational tests outside. One justification uses the paired Hadamard partial fractions for m and closes each pole term separately on the two verticals. On these verticals the horizontal distance from every zero is ≥1/2. For |Im r|>2(1+|z|) the paired terms are O(|z|/|r|²); for the remaining terms the zero count and separation give a polynomial bound in |z|. This permits dominated passage to the limit against the decaying xi filters. For the rational self-energy use [h,h]_P=(Re m(b)/Re b+Re(m(b)/b))/2 by the exponential-packet formula. The underlying ζ evaluations on the integration line have real parts 3/2, 7/4, 2. Only arithmetic-side values enter the sign certificate.

## Enclosure bounds used by the reproducer

Integrate to T=180 in panels of width 1/8. Each complex integrand before taking the real part is holomorphic on the complex t-disks of radius 1/4 about the panel midpoints. There the zeta arguments have real part in [1.25,2.25], imaginary magnitude <181. The rational test denominators have real-part magnitude ≥1/2. Elementary bounds |ζ(s)|≤5 and |ζ′/ζ(s)|≤72 follow from absolute convergence, log n≤8 n^(1/8), and the integral test. Euler's digamma series gives |ψ(w)|≤1+3|w−1| for Re w≥5/8. The gamma integral gives |Γ(w)|≤Γ(Re w)≤2 for this range of w=s/2, by log convexity between 1/2 and 3/2. Substitution gives |xi|<200000 and |xi′/xi|<400 throughout the disks, so 10^18 bounds each displayed integrand. For n=30 Gauss–Legendre nodes per panel, the rule integrates the degree-(2n−1) Taylor polynomial exactly. The Cauchy remainder and positive weights bound the total integration error before division by π by 2T·10^18·4^(−2n)/(1−1/4). Nodes, weights and special-function values are themselves enclosed in Arb balls.

For real t≥T rotate the gamma integral by π/4 (or the opposite angle for negative height). Then |Γ(x+it/2)|≤Γ(x)(cos(π/4))^(−x) exp(−πt/8). On the three real integration lines this gives |xi|≤10(1+t)² exp(−πt/8), while the same digamma and Euler bounds give |xi′/xi|≤20(1+t) for t≥T. Each integrand is bounded by 10^5(1+t)^5 exp(−πt/8). The integral of this majorant from T is at most its value at T divided by π/8−5/(1+T), by logarithmic differentiation. The script adds both errors before checking strict inequalities. Run null_interference.py with python-flint 0.9.0.

## Scope

The same U separates the two complete functions, with no Hilbert positivity assumption. Passing from [H,V]_H=0 to nonnegativity of the quotient requires a new estimate. The radical identity alone supplies no sign on that quotient. All calculations here concern the arithmetic Weil form; they do not specify the operator in the separate finite divisor-graph construction.

The computed enclosures are [A,h]_F = −0.00016502726298 ± 4.00e−15, [U,U]_F = −2.935662172e−8 ± 1.91e−18 and [U,U]_H = 2.3225890e−7 ± 3.74e−15.
