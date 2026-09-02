# On-shell reconstruction test for the googly dual field

## Result

The earlier statement that the nonlinear twistor `B` field is simply independent of the almost-complex deformation was too strong.

In Sharma's chiral spacetime action

S[e,Gamma] = integral Sigma^(ab) wedge (d Gamma_ab + kappa^2 Gamma_a^c wedge Gamma_cb),

the equation of motion of Gamma sets kappa^2 Gamma equal to the ASD spin connection determined by the metric/tetrad. Sharma's twistor construction separately reconstructs an off-shell spacetime metric from the almost-complex deformation V, while the Penrose transform of B gives Gamma.

Therefore the dependency chain on shell is

V -> metric/tetrad -> ASD spin connection Gamma,
B ->(Penrose) Gamma.

If the Penrose transform is injective after quotienting by B -> B + bar-nabla chi, or equivalently is an isomorphism on the relevant physical cohomology classes, then at fixed V the physical B-class is unique. If an inverse Penrose transform is available on the relevant image, then

[B] = P_B^{-1}(Gamma(metric(V))).

Thus B may be an independent first-order/off-shell variable while carrying no independent on-shell physical information.

## What this does and does not establish

This strongly supports Daniel's hypothesis that the conventional second-chirality field may be a dual/oriented lift of the same underlying geometric data rather than a second independent physical geometry.

It does NOT yet show that the reconstruction map is literally charge+orientation conjugation, nor that it coincides with Grassmannian complement, celestial shadow, CPT, or the half-flip quotient. Those identifications remain to be proved.

## Next exact tests

1. Identify the precise quotient/cohomology class of Sharma's B under B -> B + bar-nabla chi.
2. Verify that the Penrose map from that quotient to Gamma is injective/surjective under the boundary conditions used.
3. Write the explicit composite G[V] = P_B^{-1}(Gamma(metric(V))).
4. Linearize G around flat space and compare it to the split-signature full Fourier / light-transform operator already identified.
5. Check whether G transforms the canonical twistor degree +2 to -6 and whether its square closes to identity modulo gauge/orientation.
6. Compare the induced action on observables with the diagonal character (q,t)->(-q,-t), keeping gravity's analogue of q as a representation/conjugacy label rather than literal electric charge.

## Falsifier

If two gauge-inequivalent B classes have the same Penrose image Gamma for fixed V, or if generic on-shell solutions require B data not determined by the reconstructed metric, the strong one-lift hypothesis fails in this formulation.
