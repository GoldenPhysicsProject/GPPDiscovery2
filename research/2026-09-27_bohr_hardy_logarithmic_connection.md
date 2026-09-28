# The prime-torus logarithmic connection is regular in H2 throughout Re(s)>1/2

Date: 2026-09-27
Status: exact zero-independent Hardy-space identity. No RH claim.

This strengthens the Bohr-Hardy zeta/Mobius cancellation by differentiating before scalarization.

## 1. Internal zeta and Mobius fields

On the compact prime torus K_ar define, for sigma=Re(s)>1/2,

Z_s
=
sum_{n>=1} n^(-s) chi_n,

M_s
=
sum_{n>=1} mu(n)n^(-s)chi_n.

Both belong to H2(K_ar), and the prior result gives

Z_s M_s = 1

in H1 for every sigma>1/2.

Moreover the H2 derivatives exist locally uniformly:

partial_s Z_s
=
-sum_n (log n)n^(-s)chi_n,

partial_s M_s
=
-sum_n mu(n)(log n)n^(-s)chi_n,

because powers of log n do not change the half-density convergence threshold.

## 2. The von Mangoldt current is itself an H2 vector

Define

boxed:
P_s
=
sum_{n>=2} Lambda(n)n^(-s)chi_n.

Since Lambda(n)<=log n,

||P_s||_2^2
=
sum_n Lambda(n)^2 n^(-2sigma)
<=
sum_n (log n)^2 n^(-2sigma)
<infinity

for every sigma>1/2.

Thus the microscopic arithmetic logarithmic current is a genuine Hilbert vector throughout the open critical half-plane.

## 3. Exact logarithmic-connection identity below the scalar Euler domain

For a finite prime set P,

Z_{s,P}
=
product_{p in P}(1-p^(-s)z_p)^(-1),

M_{s,P}
=
product_{p in P}(1-p^(-s)z_p),

and

M_{s,P} Z_{s,P}=1.

Differentiate:

M_{s,P} partial_s Z_{s,P}
=
- Z_{s,P} partial_s M_{s,P}.

Expanding by Dirichlet convolution gives exactly

boxed:
-M_{s,P} partial_s Z_{s,P}
=
P_{s,P},

where P_{s,P} contains the prime-power von Mangoldt terms supported on P.

As P grows:
- M_{s,P}->M_s in H2;
- partial_s Z_{s,P}->partial_s Z_s in H2;
- hence their products converge in H1;
- P_{s,P}->P_s in H2, hence also locally in H1.

Therefore

boxed:
-M_s partial_s Z_s
=
P_s
=
Z_s partial_s M_s

in H1(K_ar) for every Re(s)>1/2.

This is an exact internal logarithmic gauge identity below the ordinary Euler-product domain.

## 4. Why the scalar logarithmic derivative has poles while the internal current does not

At the scalar phase point alpha_0=(1,1,...), ordinary evaluation is justified only in Re(s)>1 and gives

E_0(P_s)
=
sum_n Lambda(n)n^(-s)
=
-zeta'(s)/zeta(s).

But P_s itself is a holomorphic H2-valued function for Re(s)>1/2.

Thus a nontrivial zeta zero does NOT correspond to a singularity of the internal prime current.

It corresponds to a singularity of the scalar reconstruction/evaluation of that regular current.

This is a sharper holographic statement:

boxed:
internal arithmetic gauge field is regular;
bulk-to-scalar reconstruction develops the resonance pole.

The zeros therefore behave like poles of a boundary response map, not singular microscopic prime configurations.

## 5. Connected BPY image of the current

The bounded intertwiner C_s from the prime-torus Hardy space to the connected BPY field can be applied directly:

boxed:
J_conn(s):=C_s P_s

is a well-defined L2(BPY) vector for every Re(s)>1/2, locally holomorphic after accounting for the already established local holomorphy of C_s.

In the safe region the uncentered current synthesis splits into:
- a coherent vacuum scalar proportional to E_0(P_s)=-zeta'/zeta;
- the bounded connected vector J_conn(s).

So the logarithmic-derivative poles again live only in the rank-one reconstruction channel.

## 6. A useful completion identity

Let

a(s)=2 xi(s)=A_infty(s) zeta(s).

In Re(s)>1,

a(s) E_0(P_s)
=
-2 xi(s) zeta'(s)/zeta(s)
=
-A_infty(s) zeta'(s).

This quantity alone still retains the s=1 pole structure.

But the full completed logarithmic derivative satisfies

boxed:
a(s) [xi'(s)/xi(s)]
=
2 xi'(s),

which is entire.

Therefore the physically completed current should not be assembled as the prime scalar current alone. The Archimedean derivative term is exactly what converts the singular logarithmic response into the entire derivative of the completed vacuum amplitude.

This is another precise instance of:
complete/grade first, scalarize second.

## 7. New reconstruction target

The prime-torus theory now supplies, throughout Re(s)>1/2:

- invertible internal boson/Mobius pair Z_s M_s=1;
- regular H2 logarithmic current P_s;
- bounded connected BPY images C_s M_s and C_s P_s.

All scalar poles are introduced by the same singular boundary functional E_0.

Therefore an RH proof through this route should seek a completed boundary triple / Schur observable which replaces E_0 by a bounded physical reconstruction after adding the Archimedean channel.

The target is not to regularize P_s itself. It is already regular.

The target is to prove that the completed reconstruction of P_s is a Herglotz/Weyl response whose only allowed singularities are physical principal-series boundary modes.
