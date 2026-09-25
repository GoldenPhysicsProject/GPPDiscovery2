# RH causal Koszul boundary gap — corrected operator-valued Hodge estimate
## Date: 2026-09-24
## Status: exact finite-cutoff operator identity + unconditional asymptotic consequence from PNT

This note corrects the interrupted many-prime Koszul-gap argument.

The earlier scalar-coefficient CAR identity omitted a real issue in the causal-shift realization: the prime coefficients commute with each other, but they do not doubly commute with one another's adjoints. The Hodge square therefore acquires explicit boundary commutators. Keeping those terms does **not** destroy the gap on the critical half-density line. Their total norm is lower order than the diagonal many-prime Hodge mass.

No RH claim is made here. The result supplies a rigorous bulk Green suppression scale for the connected-boundary/Feshbach program.

## 1. Causal shifts

Let
[
H_L=L^2(0,L)
]
and for (0le ale L)
[
(V_af)(x)=
egin{cases}
f(x-a),&ale xle L,\
0,&0le x<a.
end{cases}
]

Then (V_aV_b=V_{a+b}) when (a+b<L), and (0) once the shift exits the interval. The adjoint is
[
(V_b^*f)(x)=
egin{cases}
f(x+b),&0le xle L-b,\
0,&L-b<xle L.
end{cases}
]

For the full-line translation (U_{a-b}f(x)=f(x+b-a)), direct substitution gives
[
V_aV_b^*=M_{mathbf 1_{A_{a,b}}}U_{a-b},
qquad
V_b^*V_a=M_{mathbf 1_{B_{a,b}}}U_{a-b},
]
with
[
A_{a,b}=[a,min(L,L+a-b)],
]
[
B_{a,b}=[max(0,a-b),L-b].
]

Hence
[
[V_a,V_b^*]
=
M_{mathbf 1_{A_{a,b}}-mathbf 1_{B_{a,b}}}U_{a-b}.
]

The multiplier only takes values in ({-1,0,1}). Therefore
[
oxed{|[V_a,V_b^*]|le 1.}
]

This is the exact boundary defect. In the infinite/bilateral translation representation it vanishes; on the finite causal interval it is supported entirely by the truncation boundary.

## 2. Prime Koszul differential with operator coefficients

Let (X=e^L), let (mathcal P_X={ple X:p	ext{ prime}}), and put
[
a_p=log p,qquad
q_p=p^{-s},qquad
T_p(s)=I-q_pV_{a_p}.
]

On the fermionic Fock space (Lambda(mathbb C^{mathcal P_X})), let (arepsilon_p,iota_p) satisfy the CAR
[
{arepsilon_p,arepsilon_q}=0,
qquad
{iota_p,iota_q}=0,
qquad
{arepsilon_p,iota_q}=delta_{pq}I.
]

Define
[
d_s=sum_{ple X}T_p(s)otimesarepsilon_p,
qquad
D_s=d_s+d_s^*.
]

Because the (V_{a_p}) commute, the (T_p) commute and therefore
[
d_s^2=0.
]
Likewise the (T_p^*) commute, so ((d_s^*)^2=0).

Expanding the Hodge square and using the CAR yields the exact identity
[
oxed{
D_s^2=H_{0,s}+B_s,
}
]
where
[
H_{0,s}
=
sum_{ple X}
left(
T_pT_p^*otimesarepsilon_piota_p
+
T_p^*T_potimesiota_parepsilon_p
ight)
]
and
[
oxed{
B_s
=
sum_{substack{p,qle X\p
e q}}
[T_p,T_q^*]otimesarepsilon_piota_q.
}
]

Thus the only failure of the scalar CAR square is an explicit connected prime-prime boundary operator.

Since
[
[T_p,T_q^*]
=
q_poverline{q_q}[V_{a_p},V_{a_q}^*],
]
we have
[
oxed{
|[T_p,T_q^*]|
le |q_p||q_q|.
}
]

## 3. Critical half-density lower bound

Now put
[
s=rac12+it.
]
Then
[
|q_p|=p^{-1/2}.
]

By the reverse triangle inequality,
[
|T_pf|
ge (1-p^{-1/2})|f|,
qquad
|T_p^*f|
ge (1-p^{-1/2})|f|.
]

Since (arepsilon_piota_p) and (iota_parepsilon_p) are complementary orthogonal projections,
[
H_{0,s}
ge
m(X)I,
]
where
[
m(X)=
sum_{ple X}(1-p^{-1/2})^2.
]

For the connected boundary defect,
[
|B_s|
le
b(X)
:=
sum_{substack{p,qle X\p
e q}}rac1{sqrt{pq}}.
]

Therefore
[
oxed{
D_s^2ge g(X)I,
qquad
g(X):=m(X)-b(X).
}
]

Writing
[
S_1(X)=sum_{ple X}p^{-1/2},
qquad
S_2(X)=sum_{ple X}p^{-1},
]
this becomes
[
oxed{
g(X)=pi(X)-2S_1(X)+2S_2(X)-S_1(X)^2.
}
]

## 4. Asymptotic gap

By the prime number theorem with partial summation,
[
pi(X)sim rac{X}{log X},
qquad
S_1(X)simrac{2sqrt X}{log X},
]
while
[
S_2(X)=O(loglog X).
]

Hence
[
g(X)
=
rac{X}{log X}
-
rac{4X}{log^2X}
+
o!left(rac{X}{log X}ight).
]

Therefore
[
oxed{
g(X)simrac{X}{log X}>0
}
]
for all sufficiently large (X).

Equivalently, with (X=e^L),
[
oxed{
D_{1/2+it,L}^2
ge
left(1+o(1)ight)rac{e^L}{L}I,
}
]
uniformly in (t), because the estimate only uses (|p^{-1/2-it}|=p^{-1/2}).

Consequently
[
oxed{
|D_{1/2+it,L}^{-1}|
=
O(sqrt L,e^{-L/2}).
}
]

This is the same Green suppression scale suggested by the interrupted scalar-coefficient argument, now with the causal boundary commutators kept honestly.

## 5. Numerical sanity check for the explicit lower bound

The reproducibility script accompanying this note evaluates
[
g(X)=pi(X)-2S_1(X)+2S_2(X)-S_1(X)^2.
]

Representative values:

- (X=10^2): (g(X)approx-13.12);
- (X=10^3): (g(X)approx-13.02);
- (X=10^4): (g(X)approx326.32);
- (X=10^5): (g(X)approx4550.24);
- (X=10^6): (g(X)approx47051.15).

The finite explicit bound becomes positive well before asymptopia. These figures are validation only; the theorem is the analytic estimate above.

## 6. Why this matters for the RH frontier

The result changes the interpretation of the Koszul route.

The causal prime system is **not** a direct scalar CAR sum. Its failure is exactly a boundary interaction:
[
B_s
=
sum_{p
e q}[T_p,T_q^*]otimesarepsilon_piota_q.
]

But this connected boundary interaction is relatively small compared with the many-prime bulk mass:
[
rac{|B_s|}{m(X)}
=
O!left(rac1{log X}ight).
]

Thus the finite prime Hodge bulk becomes more massive with the cutoff even after causal truncation.

At support scale (L),
[
|D_L^{-1}|
=
O(sqrt L,e^{-L/2}),
]
which is precisely the suppression scale capable of neutralizing a single coherent boundary vector of size (e^{L/2}) up to polynomial factors.

This still does **not** prove RH. The load-bearing theorem remains the exact connected scalar extraction:

construct the completed prime/pole/Archimedean Weil boundary response as a bounded number of matrix elements or a Schur/Feshbach compression of this massive causal Hodge bulk, with only (e^{o(L)}) residual error.

The new point is that the causal Koszul bulk itself now has the required asymptotic Green scale after its true boundary defect is included.

## 7. Next exact target

Use the commuting Euler product
[
M_L=prod_{p<e^L}(I-p^{-1/2}V_{log p}),
qquad
Z_L=M_L^{-1},
]
and the already exact identity
[
P_L=M_L[X,Z_L]
=
sum_nrac{Lambda(n)}{sqrt n}V_{log n}.
]

The top-degree fermionic product maps the Fock vacuum to the top state with bosonic amplitude (M_L). This suggests the correct connected observable is not a product of two separately bounded half-density maps, but a **one-insertion logarithmic derivative of the top-degree amplitude**:
[
-[X,M_L]M_L^{-1}=P_L.
]

The next calculation should derive this one-insertion response as an exact graded Green/Feshbach matrix element of the massive (D_L), then attach the pole and Archimedean completion before scalarization.

That is the immediate frontier.
