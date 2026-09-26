# Golden Möbius / finite-place audit — exact results and physical no-go
Date: 2026-09-26
Status: exact algebra + Lean formalization on codex/rh-boundary-closure; no RH claim.

## Exact identities now formalized

1. The RH Cayley coordinate
   beta(s)=(s-1)/s
   obeys
   beta(1-s)=beta(s)^(-1).

2. In the Suzuki pair
   A(z)=(z-i)I(z), B(z)=(z+i)I(-z),
   q(z)=A(z)/B(z)
   obeys q(-z)=q(z)^(-1).

3. The homogeneous-frame shear A -> A+B acts by q -> q+1.
   Therefore reflection followed by that frame shear is exactly
   q -> 1 + 1/q.
   Fixed points obey q^2=q+1.

4. The Suzuki ratio factors as
   q(z)=[(z-i)/(z+i)] [I(z)/I(-z)].
   The elementary factor (z-i)/(z+i) is exactly beta(s) under
   s=(z+i)/(2i). The arithmetic information is therefore isolated in I(z)/I(-z).

5. The dyadic Hardy worst-cell precision margin is exactly phi^(-2), and this also equals
   the reciprocal of the independently defined finite-place shadow kernel at q=5,
   s=1/2:
      margin = K_{5,1}(1/2)^(-1)=phi^(-2).

6. Stronger uniqueness: write a hyperbolic trace t>=3 and positive discriminant root d>1
   with d^2=t^2-4. If the center finite-place kernel shape
      (d+1)/(d-1)
   equals the expanding hyperbolic eigenvalue
      (t+d)/2,
   then algebra factors the matching equation as
      (t-3)(d+t+2)=0.
   Positivity forces t=3, hence d^2=5.
   Thus the discriminant-five / golden match is uniquely selected by the matching
   equation inside the hyperbolic trace family; it is not a generic identity.

## Important physical no-go

The frame shear q->q+1 is not automatically the actual arithmetic rank-one feedback.

The canonical odd Weyl/Herglotz coordinate is a Cayley transform of q. Functional
reflection becomes sign reversal there, and the known unit feedback is additive in the
reciprocal-Weyl coordinate. In that physical scalar coordinate the known
reflection+feedback composite is

   m -> 1-m,

an involution with fixed point 1/2, not golden dynamics.

Moreover, the Suzuki frame shear does not become a constant translation in reciprocal
Weyl coordinates; its increment already differs at q=0 and q=1. Therefore no single
constant rank-one feedback realizes the Suzuki frame shear globally.

This kills the naive claim that the golden word itself is the physical CCM return map.

## Correct dynamical statement

For G(x)=1+1/x, one step reverses sides of phi, so [phi,infinity) is NOT invariant.
The correct invariant statement is for the square:

   G^2(x)=(2x+1)/(x+1).

For x>=phi, G^2(x)>=phi and

   (G^2)'(x)=1/(x+1)^2 <= phi^(-4),

with equality at x=phi.

## Interpretation

The golden ratio is genuinely present in three mutually consistent structures:

- the minimal trace-3 PGL/SL(2,Z) hyperbolic word;
- the discriminant-five finite-place shadow kernel at the principal-series center;
- the standard dyadic Hardy/Cayley conditioning margin.

But the currently known arithmetic Weyl feedback uses a different linearized coordinate
and gives an involution, so these identities do not yet provide RH closure.

The useful next question is narrower: is there a genuine completed boundary operation
(other than functional reflection + standard rank-one feedback) whose action is the
Suzuki homogeneous-frame shear? If not, golden is structural geometry only.

Lean: GppVerify/RiemannHypothesis/GoldenMobiusAudit.lean
