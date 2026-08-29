# Golden reciprocal / unimodular bridge

## Motivation

The arithmetic conformal program already has reciprocal scale inversion, a unitary/self-dual center at scale 1, and orientation-reversing / orientation-preserving structures. The question is whether the golden ratio can arise from this structure without being inserted as a fitted constant.

## Exact algebra

Let r be a nonzero real scale. The reciprocal pair is (r, r^{-1}), with multiplicative midpoint 1. In logarithmic scale coordinates the pair is (+log r, -log r), centered at 0.

Inversion alone does not select r. Add the unit-splitting condition

    r - r^{-1} = 1.

Multiplying by r gives

    r^2 - 1 = r,

hence

    r^2 = r + 1.

The unique positive solution is the golden ratio varphi = (1+sqrt(5))/2. Thus the exact selection statement is not "inversion implies varphi" but

    reciprocal inversion + positive branch + unit additive split => varphi.

Squaring the split gives

    r^2 + r^{-2} = 3.

Therefore the squared reciprocal pair has determinant-one product 1 and trace 3. This is precisely the characteristic data of the smallest positive integer trace strictly above the parabolic threshold 2 for a reciprocal determinant-one 2x2 spectrum.

## Fibonacci / orientation bridge

The primitive integer transfer matrix

    F = [[1,1],[1,0]]

has determinant -1 and characteristic polynomial

    lambda^2 - lambda - 1.

Its eigenvalues are

    varphi, -varphi^{-1}.

So one primitive two-sector unimodular integer recurrence contains simultaneously:

- reciprocal eigenvalue magnitudes varphi and varphi^{-1};
- an orientation sign from det(F) = -1 and the negative conjugate eigenvalue;
- the unit splitting varphi - varphi^{-1} = 1.

Squaring removes the orientation reversal:

    F^2 = [[2,1],[1,1]], det(F^2)=1, tr(F^2)=3,

with positive reciprocal eigenvalues

    varphi^2, varphi^{-2}.

This is substantially more informative than a numerical golden-ratio coincidence. It suggests a specific theorem-search criterion for the GPP orientation/scale sector: derive the relevant two-sector transfer operator independently and test whether it is conjugate/equivalent to the primitive GL(2,Z) Fibonacci transfer or whether its orientation-preserving square has determinant 1 and minimal hyperbolic trace 3.

## Relation to old source material

Drive mining of ONONv1 recovered an earlier manuscript intuition: temperature inversion T <-> 1/T, equilibrium at T=1, and a proposed conjugate pair varphi and varphi^{-1}. The old manuscript overstates this as if inversion symmetry alone uniquely selected varphi. That is not mathematically correct. The corrected exact statement is the unit-split theorem above. The manuscript's inversion/equilibrium intuition can therefore be salvaged only if a unit-splitting, minimal-trace, primitive-integer-transfer, entropy extremality, or equivalent independent normalization is derived from the actual arithmetic/physical construction.

## Formal status

GPPVerify2 now contains `RiemannHypothesis/GoldenReciprocalScale.lean` with the intended exact theorem layer:

- golden quadratic;
- positivity/nonzero;
- unit split iff golden quadratic;
- reciprocal multiplicative midpoint 1;
- logarithmic inversion symmetry;
- squared reciprocal trace-three identity.

CI must certify the current workbench before these are reported as verified endpoints.

## Next tests

1. Search the existing singlet/doublet Dirac-orientation modules for a naturally derived 2x2 transfer/adjacency matrix.
2. Test whether massless orientation exchange is determinant -1 and whether the massive/orientation-preserving composition yields determinant +1.
3. Search the arithmetic scale/KMS flow for a primitive integer or Hecke recursion whose positive eigenvalue solves the golden quadratic.
4. Search Gr(2,4) complement/Plucker action for a rank-two invariant block with the same characteristic polynomial.
5. Do not identify varphi as fundamental unless one of these structures derives the extra selection condition rather than assuming it.
