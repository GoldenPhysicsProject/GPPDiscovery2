# The det3 Euler determinant as the renormalized infinite product of prime TFD dressings

Date: 2026-09-27
Status: exact algebraic factorization plus standard convergence estimates. No RH claim.

## 1. Local coherent dressing multiplier

For one prime let

a_p = p^(-1/2),
z_p(s) = p^(1/2-s).

The normalized TFD/Blaschke defect multiplier is

f_p(s)
=
sqrt(1-a_p^2)/(1-a_p z_p(s)).

Since

a_p z_p(s)=p^(-s),

we have

[
oxed{
f_p(s)
=
rac{sqrt{1-p^{-1}}}{1-p^{-s}}.
}
]

The naive infinite product does not converge on the critical boundary because the first two coherent jets are too large.

## 2. Exact logarithmic jet expansion

For |a z|<1,

[
log f_a(z)
=
rac12log(1-a^2)-log(1-a z).
]

Expanding,

[
log f_a(z)
=
a z
+
rac{a^2}{2}(z^2-1)
+
sum_{mge3}rac{a^m z^m}{m}
-
sum_{kge2}rac{a^{2k}}{2k}.
]

For the prime spectral variables,

[
a_p z_p(s)=p^{-s},
qquad
a_p^2(z_p(s)^2-1)=p^{-2s}-p^{-1}.
]

Thus the first two nontrivial local jets are exactly

[
p^{-s},
qquad
rac12(p^{-2s}-p^{-1}).
]

The s-dependent pieces are precisely the m=1 and m=2 Euler-log channels.

## 3. Canonical third-order renormalized TFD multiplier

Define

[
oxed{
widetilde f_p(s)
=
f_p(s)
exp!left[
-p^{-s}
-rac12left(p^{-2s}-p^{-1}ight)
ight].
}
]

Then

[
egin{aligned}
log widetilde f_p(s)
&=
rac12left[log(1-p^{-1})+p^{-1}ight]\
&quad+
left[
-log(1-p^{-s})
-p^{-s}
-rac12p^{-2s}
ight].
end{aligned}
]

The first bracket is O(p^(-2)).

The second bracket is

[
sum_{mge3}rac{p^{-ms}}{m}.
]

Therefore the prime sum converges normally on compact subsets of

[
oxed{Re s>1/3.}
]

So the renormalized infinite TFD dressing

[
widetilde F(s)
=
prod_p widetilde f_p(s)
]

is a well-defined holomorphic nonzero product in the same half-plane in which the third regularized Euler determinant exists.

## 4. Exact det3 identity

Let

[
D(s)e_p=p^{-s}e_p.
]

The third regularized determinant satisfies

[
-logdet_3(I-D(s))
=
sum_p
left[
-log(1-p^{-s})
-p^{-s}
-rac12p^{-2s}
ight].
]

Define the finite positive vacuum constant

[
oxed{
C_{m vac}
=
prod_p
sqrt{1-p^{-1}},
e^{1/(2p)}.
}
]

Its logarithm converges because

[
rac12left[log(1-p^{-1})+p^{-1}ight]
=
O(p^{-2}).
]

Hence

[
oxed{
widetilde F(s)
=
C_{m vac},
det_3(I-D(s))^{-1},
qquad
Re s>1/3.
}
]

This is an exact identity.

Therefore the det3 regularized Euler determinant is, up to one finite universal vacuum normalization, literally the infinite product of prime TFD coherent dressings after subtracting their first two local jets.

## 5. Why order three is forced

At the critical boundary Re(s)=1/2,

the first jet has size

[
|p^{-s}|=p^{-1/2},
]

whose prime sum diverges strongly.

The second jet has size

[
|p^{-2s}|=p^{-1},
]

whose prime sum also diverges.

The third and all higher jets satisfy

[
sum_p |p^{-3s}|
=
sum_p p^{-3/2}
<infty.
]

Thus

[
oxed{
	ext{det3 is the minimal renormalization that makes the global prime TFD dressing absolutely summable at the half-density boundary.}
}
]

This gives a direct coherent-state meaning to the Schatten threshold.

## 6. Recovery of zeta and the exact two-channel obstruction

The standard identity is

[
logzeta(s)
=
P(s)+rac12P(2s)-logdet_3(I-D(s)).
]

Using the TFD product,

[
oxed{
zeta(s)
=
C_{m vac}^{-1}
exp!left[
P(s)+rac12P(2s)
ight]
widetilde F(s).
}
]

So the entire unresolved local divergence at the critical boundary is concentrated in exactly the two exponentiated jets

[
P(s),
qquad
rac12P(2s).
]

Everything m>=3 is already the convergent renormalized TFD dressing.

This is the same two-channel obstruction found independently by:
- Schatten regularization;
- coherent K0 tail subtraction;
- normal/anomalous TFD covariance;
- rigged prime Weyl systems.

They are now four representations of one object.

## 7. Vacuum renormalization interpretation

The factor

[
sqrt{1-p^{-1}}
]

is exactly the local TFD vacuum overlap.

The naive global vacuum overlap

[
prod_psqrt{1-p^{-1}}
]

vanishes.

The compensating factor

[
e^{1/(2p)}
]

removes the divergent first term of its logarithm, leaving the finite product C_vac.

Thus the same third-order renormalization simultaneously:
1. renormalizes the Euler determinant;
2. renormalizes the infinite product of local TFD coherent dressings;
3. renormalizes the critical global vacuum overlap.

This makes the global Hagedorn/Fock escape and the det3 threshold the same analytic phenomenon.

## 8. Concrete Archimedean completion target

The two remaining divergent jets are explicit:

[
J_1(s)=P(s),
qquad
J_2(s)=rac12P(2s).
]

Under the universal SU(1,1) K1 transform they correspond to the first two nonvacuum compact modes already identified as

[
P_1(x)=2x,
qquad
P_2(x)=2x^2-rac12.
]

Therefore the missing Archimedean sewing is genuinely finite-rank at the level of local coherent jets:

[
oxed{
	ext{complete the }(P_1,P_2)	ext{ boundary block;}
quad
	ext{the renormalized TFD tail is already globally summable.}
}
]

The remaining challenge is not convergence. It is the sign/contractivity of the completed two-channel Schur block.
