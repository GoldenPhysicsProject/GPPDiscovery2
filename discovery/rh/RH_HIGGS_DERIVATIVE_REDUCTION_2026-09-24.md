# RH Higgs derivative reduction — 2026-09-24

Status: exact finite-cutoff identities; RH not proved.

Let V_y be the causal right shift on H_L=L2(0,L).

For each prime p<e^L define
T_{p,beta}=I-p^{-beta/2}V_{log p}
and the positive mass
H_P(beta)=sum_p T_{p,beta}^* T_{p,beta}.

Differentiation gives exactly

2 H_P'(1)
=
W_prim
-
2 sum_p (log p)/p V_{log p}^*V_{log p},

where

W_prim
=
sum_p (log p)/sqrt(p) (V_{log p}+V_{log p}^*)

is the primitive-prime part of the Weil prime block.

Therefore

W_prim=2H_P'(1)+R_P,

with R_P>=0 and ||R_P||=O(L^2) by the elementary estimate
sum_{p<e^L}(log p)/p <= sum_{n<e^L}(log n)/n=O(L^2).

The remaining prime powers k>=2 form

R_pp
=
sum_p sum_{k>=2,p^k<e^L}
(log p)p^{-k/2}(V_{k log p}+V_{k log p}^*).

Since ||V_y+V_y^*||<=2 and
sum_{k>=2}p^{-k/2}=p^{-1}/(1-p^{-1/2}),
we obtain the zero-independent elementary bound

||R_pp||=O(L^2).

Hence

W_P=2H_P'(1)+E_P,
||E_P||=O(L^2).

So all nonlinear Euler/Higgs fluctuations are already subexponential; only the primitive-prime linear mode can carry exponential instability.

For the healed trivial/pole block

W_02=2 int_0^L cosh(y/2)(V_y+V_y^*) dy,

define the positive continuum Higgs form

H_0(beta)
=
int_0^L [(e^y+1)/y]
(I-e^{-beta y/2}V_y)^*
(I-e^{-beta y/2}V_y) dy

on its natural quadratic-form domain.

Its beta derivative is regular and satisfies exactly

W_02=2H_0'(1)+R_0,

where

R_0
=
2 int_0^L (1+e^{-y}) V_y^*V_y dy
>=0

and ||R_0||<=2(L+1).

Therefore

W_02-W_P
=
2 [H_0'(1)-H_P'(1)]
+
O_form(L^2).

The Archimedean real-place contribution has already been proved uniformly bounded below, independently of L. Thus the full RH-strength instability is reduced, modulo polynomial error, to the critical beta derivative of the difference of two positive Higgs masses:

Delta H_L(beta)=H_0(beta)-H_P(beta).

The continuous Higgs density is

(e^y+1)/y ~ e^y/y,

which is exactly the expected continuum prime density in logarithmic coordinate. The remaining theorem is therefore a linearized Higgs/Feshbach stability theorem: show Delta H_L'(1) is bounded below by e^{o(L)} on the physical localized test class.

The corrected many-prime causal Hodge bulk from the preceding result has
D_L^2 >= (1+o(1))e^L/L,
so ||D_L^-1||=O(sqrt(L)e^{-L/2}).
This is exactly the scale capable of converting an e^{L/2} coherent linear boundary coupling into a polynomial Schur/Feshbach energy.

Next target: derive 2 Delta H_L'(1) as that Schur/Feshbach response, including the causal boundary commutator.