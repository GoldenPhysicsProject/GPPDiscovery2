# One-ghost reduction of the completed Gamma-prime-pole Krein square

Date: 2026-09-21

Start from the exact v34 decomposition, for q>1,

Delta_q B(a,b)
=
<Gamma_q(a),Gamma_q(b)>
+<Prime_q(a),Prime_q(b)>
-<Pole0_q(a),Pole0_q(b)>
-<Pole1_q(a),Pole1_q(b)>,

with

Gamma density:
  e^{-q x}/(1-e^{-2x}),

Pole0 density:
  e^{-q x},

Pole1 density:
  e^{-(q-1)x},

and common boundary feature (1-e^{-a x}).

## 1. Exact Gamma tower expansion

Since

1/(1-e^{-2x}) = sum_{k>=0} e^{-2kx},

the Gamma Gram kernel decomposes orthogonally as

<Gamma_q(a),Gamma_q(b)>
=
sum_{k>=0} G_{q+2k}(a,b),

where

G_r(a,b)
=
int_0^infinity e^{-r x}(1-e^{-a x})(1-e^{-b x}) dx.

The k=0 term is exactly G_q, which is the negative Pole0 channel.

Therefore the completed Krein square simplifies identically to

boxed(
Delta_q B(a,b)
=
sum_{k>=1} G_{q+2k}(a,b)
+
P_q(a,b)
-
G_{q-1}(a,b)
).

No approximation and no RH input enter.

Thus after the elementary Gamma cancellation there is exactly ONE negative boundary channel:
the s=1 pole feature.

## 2. Meaning of the remaining ghost

The surviving negative mode is

g_{q-1,a}(x)
=
e^{-(q-1)x/2}(1-e^{-a x}).

It is the boundary channel associated with the pole of zeta at s=1.

This matches the independent causal/Mobius analysis:
the formal inverse 1/zeta must vanish at s=1 in order to cancel the zeta pole.

The Casimir-harmonic finite inverse constructed on 2026-09-19 satisfies

M_N^C(1)=0

exactly for every finite N.

Thus the one-ghost Krein reduction and the Casimir-completed Mobius boundary condition are
addressing the same distinguished obstruction from opposite sides.

## 3. Why a same-semigroup contraction is impossible

Let H_+ be the cyclic spectral space of the positive Gamma-tail plus prime measure and H_-
the cyclic space of the remaining pole measure.

All feature vectors have the form

F_+(a)=(I-e^{-aX_+})v_+,
F_-(a)=(I-e^{-aX_-})v_-.

Suppose a contraction C existed with

C F_+(a)=F_-(a)

for every a>0 and with the natural limiting relation C v_+=v_-.

Then

C e^{-aX_+}v_+ = e^{-aX_-}v_-

for every a.

Hence C intertwines the multiplication semigroups on their cyclic subspaces. By the
spectral theorem, such a contractive cyclic intertwiner requires the negative spectral
measure to be dominated by the positive spectral measure.

Below the first prime support x=log 2, the positive continuous density is

rho_+(x)=e^{-(q+2)x}/(1-e^{-2x}),

whereas

rho_-(x)=e^{-(q-1)x}.

Their ratio is

rho_+(x)/rho_-(x)
=
e^{-3x}/(1-e^{-2x}).

This is <1 exactly when

e^{3x}-e^x-1>0,

i.e. x>log(lambda_pl), where lambda_pl is the plastic constant, before x reaches log 2.

Therefore same-parameter semigroup domination is impossible. This recovers the v34
ultraviolet-support obstruction in operator-intertwiner form.

## 4. Consequence

A successful half-step map cannot preserve the boundary semigroup a -> e^{-aX}.

It must be genuinely nonlocal in the boundary parameter: Fourier/Poisson/scattering,
functional shadow, or an equivalent transform must occur BEFORE the positive quotient.

This sharply explains why:
- identity gluing fails;
- positive q-averages fail;
- local prime contractions fail;
- a nonlocal Tate/co-Poisson or scattering map remains viable.

## 5. Connection to the first-order Ward geometry

The BPY Ward operation is -partial_a partial_b. Under null coordinates

a=c-d,
b=c+d,

one has

-4 partial_a partial_b = partial_d^2-partial_c^2,

the 1+1 indefinite quadratic form factorized by a first-order Dirac operator.

Thus the one surviving s=1 ghost should be regarded as a boundary mode of the null Ward
system, not as another positive local particle channel. The nonlocal arithmetic map must
move this mode through the functional-equation/shadow boundary before squaring.

Current next target:
test the exact co-Poisson/Tate involution on the one-ghost reduced feature family and ask
whether its transformed s=1 boundary vector lands in the closure of the positive
prime-plus-Gamma tail with contractive norm.