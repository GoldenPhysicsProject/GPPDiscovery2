# RH relative causal gauge — exact pole subtraction before scalarization
## Date: 2026-09-24
## Status: exact causal-operator identities; RH-equivalent endpoint criterion; no RH proof

This note sharpens the causal-shift formulation by removing the exponentially large
trivial-character channel *before* taking the scalar boundary value.

## 1. The continuous pole channel is itself a causal gauge

Let (H_L=L^2(0,L)), let (V_y) be the right causal shift, let (X) be
multiplication by (x), and let (partial=rac d{dx}) on the Volterra domain
with left boundary value zero.

Define
[
A_L f
=
int_0^L e^{y/2}V_yf,dy
=
int_0^x e^{(x-u)/2}f(u),du.
]

Because (V_yf(x)=0) for (y>x), the upper cutoff (L) is automatic. Direct
differentiation gives
[
oxed{
A_L=(partial-	frac12)^{-1}
}
]
on the natural Volterra core.

The causal commutator obeys
[
[X,V_y]=yV_y.
]
Therefore
[
[X,A_L]
=
int_0^L y e^{y/2}V_y,dy.
]

But causal convolution of the kernel (e^{y/2}) with itself is
[
int_0^y e^{u/2}e^{(y-u)/2},du
=
y e^{y/2}.
]
Hence
[
oxed{
[X,A_L]=A_L^2.
}
]

Consequently the logarithmic gauge connection of the continuous pole gauge is
the gauge itself:
[
oxed{
A_L^{-1}[X,A_L]=A_L.
}
]

## 2. Arithmetic causal gauge

At half density define
[
Z_L
=
sum_{nge1}n^{-1/2}V_{log n},
qquad
M_L=Z_L^{-1},
]
where the sums are finite on (H_L) because (V_{log n}=0) for (nge e^L).

The exact logarithmic connection is
[
oxed{
P_L
=
Z_L^{-1}[X,Z_L]
=
sum_{n<e^L}
rac{Lambda(n)}{sqrt n}V_{log n}.
}
]

## 3. Relative gauge removes the zeta pole algebraically

Define on the common causal core
[
oxed{
R_L=Z_LA_L^{-1}.
}
]

All causal convolution operators commute on this core. Since
[
[X,A_L^{-1}]
=
-A_L^{-1}[X,A_L]A_L^{-1}
=
-I,
]
we obtain
[
egin{aligned}
R_L^{-1}[X,R_L]
&=
A_LZ_L^{-1}
left(
[X,Z_L]A_L^{-1}
+
Z_L[X,A_L^{-1}]
ight)\
&=
P_L-A_L.
end{aligned}
]

Thus
[
oxed{
R_L^{-1}[X,R_L]=P_L-A_L.
}
]

This is the exact connected pole subtraction. The exponentially large free
trivial-character connection and the arithmetic prime connection are combined
before any endpoint functional is applied.

In the initial Mellin/Laplace half-plane, if (w=s+	frac12), the symbols are
[
Z: zeta(w),
qquad
A: rac1{w-1},
]
so
[
oxed{
R: (w-1)zeta(w).
}
]
The pole at (w=1) has been removed at the operator level.

## 4. The RH-equivalent scalar is an endpoint anomaly of the relative connection

Let (mathbf 1) denote the constant function and let
[
ell_L f=f(L^-)
]
on functions with a defined left endpoint value.

Because
[
V_ymathbf1(L^-)=1
qquad(0le y<L),
]
we have
[
ell_LA_Lmathbf1
=
int_0^Le^{y/2},dy
=
2(e^{L/2}-1),
]
and
[
ell_LP_Lmathbf1
=
sum_{n<e^L}rac{Lambda(n)}{sqrt n}.
]

Therefore
[
-ell_L
left(
R_L^{-1}[X,R_L]
ight)mathbf1
=
2(e^{L/2}-1)
-
P_{1/2}(e^L^-).
]

The exact v34 one-scalar response is
[
q_L'(0)
=
2e^{L/2}
-
P_{1/2}(e^L)
+
c_infty
+
rac23e^{-3L/2}
-
arctan(sinh(L/2)).
]

Away from the discrete cutoff values (L=log n), the endpoint convention is
irrelevant and hence
[
oxed{
q_L'(0)
=
-ell_L
left(
R_L^{-1}[X,R_L]
ight)mathbf1
+
b_infty(L),
}
]
where
[
oxed{
b_infty(L)
=
2+c_infty
+rac23e^{-3L/2}
-arctan(sinh(L/2)).
}
]

The correction (b_infty(L)) is uniformly bounded and converges to
[
2+c_infty-racpi2.
]

Thus the existing one-scalar theorem becomes the exact operator criterion
[
oxed{
RH
iff
ell_L
left(
R_L^{-1}[X,R_L]
ight)mathbf1
=
O((1+L)^M)
	ext{ for some finite }M.
}
]

Equivalently, RH fails exactly when the completed relative causal connection
develops a super-polynomial endpoint anomaly.

## 5. Relation to the massive co-Poisson operator

The inverse pole gauge is the first-order chiral factor
[
A_L^{-1}=partial-rac12.
]

The shadow factor is
[
partial+rac12.
]

Their product gives
[
oxed{
-(partial-	frac12)(partial+	frac12)
=
-partial^2+rac14
=
K_0.
}
]

Thus the positive massive co-Poisson operator previously found in the project is
exactly the doubled product of the two chiral trivial-character gauge inverses.

In Mellin language the two first-order factors are the elementary (w=1) and
(w=0) completion factors. After adjoining the nonvanishing Archimedean
Gamma factor, the completed relative symbol is the completed zeta/Xi symbol.

This is an exact structural synthesis:
[
	ext{causal zeta gauge}
+
	ext{pole gauge subtraction}
+
	ext{shadow chiral factor}
longrightarrow
	ext{co-Poisson massive completion}.
]

## 6. Why this is useful but not yet RH

The relative gauge removes the leading (e^{L/2}) pole mode before scalarization,
so the critical half-density split no-go is avoided at the algebraic level.

However, the remaining endpoint functional (ell_L) is still singular in bare
(L^2), and the relative connection contains the full arithmetic difficulty.
A proof now needs a completed positive/semibounded boundary norm in which

1. the two chiral pole modes are quotiented by (K_0);
2. the Archimedean Gamma channel is attached;
3. the endpoint readout of the relative logarithmic connection has only
   (e^{o(L)}) growth (polynomial is enough).

The corrected causal Koszul boundary-gap theorem supplies a massive bulk Green
scale, but the naive one-propagator no-go shows that this relative connection is
not automatically a regular matrix element of that Hodge inverse.

The next target is therefore precise: build a chiral/relative Feshbach system for
(R_L), not for (Z_L) and (A_L) separately, and control only its completed
endpoint anomaly.
