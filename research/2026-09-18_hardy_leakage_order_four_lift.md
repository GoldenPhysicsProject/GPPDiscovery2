# Hardy leakage as failure of the shadow-orientation lift to square to minus one

Date: 2026-09-18

Let a=1/2+omega with omega>0 and define on L2(R)

Theta_omega(t)=xi(a+it)/xi(a-it),
U_omega=M_{Theta_omega},
(RF)(t)=F(-t).

On the real line |Theta_omega|=1 and Theta_omega(-t)=conj(Theta_omega(t)). Hence

R U_omega R = U_omega*.

Define

K_omega=R U_omega.

Then K_omega is a self-adjoint involution:

K_omega*=K_omega,
K_omega^2=I.

Let Pi_+, Pi_- be the upper/lower Hardy projections and

Gamma=Pi_+-Pi_-.

Reflection exchanges the Hardy halves, so R Gamma R=-Gamma.

Define the orientation/shadow lift

J_omega=Gamma K_omega.

For f in H2_+=Ran Pi_+, let

H_omega f = Pi_- U_omega f

be the exact anticausal leakage operator from v34.

Then:

< f, J_omega^2 f >
=
< K_omega f, Gamma K_omega f >
=
||Pi_+K_omega f||^2-||Pi_-K_omega f||^2.

Because R exchanges H2_+ and H2_-,

||Pi_+K_omega f||
=
||Pi_-U_omega f||
=
||H_omega f||.

Since K_omega is unitary,

< f,(J_omega^2+I)f >
=
2||H_omega f||^2.

By polarization this gives the compressed operator identity

Pi_+(J_omega^2+I)Pi_+
=
2 H_omega* H_omega.

Consequences:

1. H_omega=0 iff J_omega^2=-I on H2_+.

2. Therefore RH is equivalent to the natural shadow/orientation lift being a genuine quarter-turn on every causal Hardy state for every omega>0.

3. The localized anti-inner crossing theorem translates directly: if RH fails, the leakage norm approaches 1 along shifts approaching the real part of an off-line zero. Hence

sup_{omega>0, f!=0}
< f,J_omega^2 f >/||f||^2
=
+1.

Under RH the same quadratic ratio is identically -1.

Thus the Hardy zero-one law becomes an order-four/order-two transition:

RH: causal shadow lift squares to -I;
not-RH: localized states approach J^2=+I.

This is an exact equivalence, not a proof of RH.

Important subtlety:
One must not demand global anticommutation {K,Gamma}=0. Even under RH the inner multiplier generally has a nontrivial model-space defect in the reverse Hardy direction corresponding to critical zeros. The correct condition is one-sided: K maps H2_+ into H2_- (equivalently U maps H2_+ into H2_+), which is exactly H_omega=0. On that causal subspace J^2=-I.

This theorem gives the precise operator interface to Which Way Is Forward: an independent intertwiner carrying its order-four geometric lift to J_omega on the causal arithmetic boundary would imply RH. Constructing such an intertwiner without assuming Hardy innerness is the new closure target.