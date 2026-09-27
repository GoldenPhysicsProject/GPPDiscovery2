# BPY gamma hierarchy as a dyadic cascade of celestial Plancherel heat times

Date: 2026-09-27
Status: exact probability identities for the positive gamma-sum variables already used in the RH program. This does not prove any zero-location statement.

## 1. The BPY gamma-sum variable

Let (Gamma_{2,j}) be independent unit-scale gamma variables of shape two and define

[
S_2
=
sum_{jge1}
rac{2}{pi^2j^2}Gamma_{2,j}.
]

The sum converges almost surely and in (L^1), since the coefficients are summable.

Its finite truncations are the (S_{2,N}) variables already used in the BPY approximation/no-go analysis.

Its Laplace transform is

[
oxed{
F_2(q)
=
mathbb E e^{-qS_2}
=
prod_{jge1}
left(
1+rac{2q}{pi^2j^2}
ight)^{-2}.
}
]

## 2. The celestial Plancherel random heat time

The normalized celestial Plancherel multiplier satisfies

[
h(q)
=
operatorname{sech}^2left(rac{sqrt q}{2}ight).
]

Euler's product gives

[
oxed{
h(q)
=
prod_{kge0}
left(
1+rac{q}{pi^2(2k+1)^2}
ight)^{-2}.
}
]

Therefore (h) is the Laplace transform of the positive random variable

[
oxed{
S_P
=
sum_{kge0}
rac{1}{pi^2(2k+1)^2}Gamma'_{2,k},
}
]

with independent shape-two gamma variables.

This is the same random heat time used in the Plancherel regularization of the arithmetic RH heat trace.

## 3. Exact odd/even decomposition

Split the BPY sum into odd and even indices.

The odd part is

[
S_2^{m odd}
=
sum_{kge0}
rac{2}{pi^2(2k+1)^2}Gamma_{2,2k+1}.
]

Hence

[
oxed{
S_2^{m odd}
overset d=
2S_P.
}
]

The even part is

[
S_2^{m even}
=
sum_{kge1}
rac{2}{pi^2(2k)^2}Gamma_{2,2k}
=
sum_{kge1}
rac{1}{2pi^2k^2}Gamma_{2,2k}.
]

If (S_2') is an independent copy of (S_2), then

[
oxed{
S_2^{m even}
overset d=
rac14 S_2'.
}
]

The two pieces are independent because they use disjoint gamma families.

Therefore

[
oxed{
S_2
overset d=
2S_P+rac14S_2',
}
]

with (S_P) and (S_2') independent.

## 4. Exact Laplace functional equation

Taking Laplace transforms gives

[
oxed{
F_2(q)
=
h(2q),
F_2(q/4).
}
]

This is also immediate by splitting the product defining (F_2) into odd and even (j).

Thus the celestial Plancherel heat-time law is exactly the odd-scale factor in a self-similar decomposition of the BPY gamma hierarchy.

## 5. Iterated perpetuity representation

Iterating

[
S_2
overset d=
2S_P+rac14S_2'
]

gives

[
S_2
overset d=
2S_{P,0}
+rac{2}{4}S_{P,1}
+rac{2}{4^2}S_{P,2}
+cdots,
]

where the (S_{P,j}) are iid copies of (S_P).

Hence

[
oxed{
S_2
overset d=
2sum_{jge0}4^{-j}S_{P,j}.
}
]

Correspondingly,

[
oxed{
F_2(q)
=
prod_{jge0}
h!left(rac{2q}{4^j}ight).
}
]

The convergence follows from the geometric scaling and finite mean of (S_P).

## 6. SU(1,1) interpretation

From the preceding discovery, the normalized Plancherel density is the vacuum spectral law of the tensor-square noncompact SU(1,1) generator, and

[
h(q)
=
mathbb E e^{-qS_P}.
]

Therefore the positive gamma hierarchy used in the BPY construction is an infinite dyadic cascade of the same celestial/SU(1,1) heat-time building block.

Schematically,

[
oxed{
	ext{BPY gamma hierarchy}
=
	ext{Plancherel block}
+
rac14	ext{(self-similar copy)}
}
]

and recursively

[
oxed{
	ext{BPY hierarchy}
=
sum_{jge0}
	ext{dyadically scaled Plancherel blocks}.
}
]

## 7. Why this matters and what it does not prove

The BPY state and the celestial Plancherel regularizer had previously entered the RH program as two separate positive constructions.

The identity above shows that their underlying positive random variables are not independent structures: the Plancherel heat-time law is exactly the odd-index component of the BPY gamma hierarchy, while the even-index component reproduces a scaled copy of the whole hierarchy.

This gives a concrete renormalization/self-similarity relation between the BPY and celestial channels.

It does **not** bypass the existing finite-truncation no-go theorem and does not prove RH. The unresolved issue remains the polarized/global prime--Archimedean positivity, not positivity of these scalar random variables.
