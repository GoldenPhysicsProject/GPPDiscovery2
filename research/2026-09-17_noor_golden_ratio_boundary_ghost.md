# Golden-ratio de Branges boundary for the strong Nyman-Baez-Duarte ghost

Date: 2026-09-17
Status: synthesis of published Hardy-space results with exact GPP Casimir/Bergman identities. No RH claim.

## 1. The exact literature input

S. Waleed Noor, Advances in Mathematics 350 (2019), gives a Hardy-space model of the strong Baez-Duarte criterion. Let

N=span{h_k:k>=2} subset H^2(D),

with

h_k(z)=1/(1-z) log((1+z+...+z^(k-1))/k).

Published results used here:

- RH iff 1 belongs to closure(N).
- Equivalently, RH iff closure(N)=H^2.
- Unconditionally, (I-S)N is dense in H^2, where S is the unilateral shift.
- The formal inverse is multiplication by psi(z)=1/(1-z), which is unbounded on H^2.
- If D_{delta_1} is the local Dirichlet space at the boundary point 1, then

  N^perp intersect D_{delta_1}={0}.

Thus any nonzero strong-Nyman ghost must escape precisely through the boundary regularity failure at z=1.

## 2. The golden ratio is forced by the boundary operator

For psi(z)=1/(1-z), the associated non-extreme de Branges-Rovnyak pair (b,a) satisfies

b/a=psi,
|a|^2+|b|^2=1 on |z|=1,
a outer and a(0)>0.

The rational solution used by Noor is

phi=(1+sqrt(5))/2,

a(z)=phi(1-z)/(phi+1-z)=phi(1-z)/(phi^2-z),
b(z)=phi/(phi^2-z).

This phi is forced, not decorative. If one starts with

a(z)=c(1-z)/(d-z),
b(z)=c/(d-z),

then b/a=1/(1-z). Boundary normalization gives

d=c^2,
3c^2=c^4+1.

Hence x=c^2 obeys

x^2-3x+1=0.

Analyticity/outer-ness requires d>1, selecting

c^2=(3+sqrt(5))/2=phi^2,

so c=phi and d=phi^2.

Therefore the golden ratio is the canonical normalization constant of the unbounded inverse-shift boundary model.

## 3. Exact Casimir/Baez-Duarte identification

The recent GPP Casimir graph calculation produced the weighted sequence norm

||x||^2=sum_{n>=1}|x_n|^2/[n(n+1)].

Noor's intermediate weighted Bergman space A has exactly the same coefficient norm under

Psi(x)(z)=sum_{n>=0}x_{n+1} z^n.

Thus the GPP Casimir/Brownian model is not merely analogous to Noor's construction: it is the same weighted Hilbert space before his final unitary map to H^2.

Noor's isometry is

T f(z)=(((1-z)f(z))')/(1-z),

mapping H^2 isometrically onto A, and Phi=T^{-1} Psi maps the weighted sequence model to the strong-Nyman Hardy model.

This gives the exact chain

Casimir negative graph
 <-> weighted Baez-Duarte sequence space
 <-> weighted Bergman A
 <-> Hardy H^2.

## 4. Local Dirichlet regularity in coefficient tails

For f(z)=sum_{n>=0}c_n z^n, membership in D_{delta_1} is equivalent to existence of the radial boundary value a=f(1) and

(f-a)/(z-1) in H^2.

If

q_n=sum_{j>n} c_j,

then

D_{delta_1}(f)=sum_{n>=0}|q_n|^2.

Now let x=(x_n) be the weighted-sequence vector with R=Psi x=T f. From

x_N=N c_N-sum_{j=0}^{N-1}c_j,

one gets

C_N:=sum_{j=0}^N c_j
=-(N+1) h_{N+1},

where

h_m=sum_{j>=m} x_j/[j(j+1)].

If L=lim_{m->infinity} m h_m exists, then a=-L and

q_N=(N+1)h_{N+1}-L.

Hence the local Dirichlet condition becomes the explicit tail regularity condition

sum_{N>=0}|(N+1)h_{N+1}-L|^2 < infinity.

This is the exact boundary regularity missing from the bare Casimir graph norm.

## 5. Exact ground-state transform of the Casimir tail energy

The GPP discrete ghost variables obey the Casimir Dirichlet energy

E(h)=sum_{n>=1} n(n+1)|h_n-h_{n+1}|^2.

Set

q_n=n h_n.

Termwise,

n(n+1)|h_n-h_{n+1}|^2
=|q_n-q_{n+1}|^2+|q_n|^2/n-|q_{n+1}|^2/(n+1).

Therefore, under the natural vanishing boundary term,

E(h)=|h_1|^2+sum_{n>=1}|q_n-q_{n+1}|^2.

The sharp Hardy mode h_n=c/n corresponds exactly to q_n=c constant and saturates the lower bound E(h)>=|h_1|^2.

Thus finite Casimir energy controls only the discrete derivative Delta q in l^2. Noor's local Dirichlet condition is substantially stronger: q must approach a limit in l^2.

This pinpoints the ultraviolet escape channel exactly.

## 6. Arithmetic ghost equation in q variables

The Ramanujan/cyclotomic orthogonality calculation gave

sum_{k>=1} h_{mk}=h_1/m.

Writing h_n=q_n/n gives

sum_{k>=1} q_{mk}/k=h_1

for every m.

If q-L belongs to l^2 (the local Dirichlet condition above), convergence of these harmonic multiple sums forces L=0: otherwise the L/k component diverges.

Then q belongs to l^2, and Cauchy-Schwarz gives absolute convergence of each multiple sum. Moreover

|h_1| <= (sum_k |q_{mk}|^2)^(1/2) (sum_k 1/k^2)^(1/2).

As m->infinity the first factor tends to zero because q in l^2, hence h_1=0.

With the stronger divisor-weighted summability obtained from q in l^2, ordinary Mobius inversion over multiples then gives h=0.

This rederives, in the Casimir tail variables, the mechanism behind Noor's theorem N^perp intersect D_{delta_1}={0}.

## 7. New exact target

The current closure problem can therefore be stated sharply:

Prove, from zero-independent arithmetic/shadow/Casimir structure, that every strong-Nyman ghost satisfying

E(h)<infinity,
sum_k h_{mk}=h_1/m for all m,

also satisfies the boundary upgrade

n h_n - L in l^2

for some L.

Noor then kills the ghost.

This is not yet proved and is RH-hard in content. But it is a much more precise target than an unspecified adelic density lemma: the exact missing theorem is a Casimir-to-local-Dirichlet regularity upgrade at the single boundary point z=1.

## 8. Relation to the entropy boundary

The same boundary point is the arithmetic Hagedorn point of the normalized Nyman transfer

Z_N(s)=((s-1)/s)zeta(s),

whose finite logarithmic response at s=1 is 1-gamma_E, where gamma_E is Euler's constant.

Do not confuse the two constants:

- gamma_E is Euler-Mascheroni and produces the finite arithmetic Hagedorn response 1-gamma_E;
- phi is the golden ratio and is forced by the de Branges-Rovnyak normalization of the unbounded inverse shift.

They occur at the same boundary obstruction but play mathematically different roles.

A positive golden split is

1/phi + 1/phi^2 = 1,

whereas phi+(1-phi)=1 is algebraically true but has a negative second term because 1-phi=-1/phi.

## 9. Operator form of the golden boundary defect

Write r=phi^{-2}. Then

b(z)=phi^{-1}/(1-r z),

so M_b=phi^{-1}(I-rS)^{-1}.

The de Branges defect operator satisfies the exact conjugated identity

(I-rS)(I-M_b M_b^*)(I-rS^*)
 = r(2I-S-S^*)-r^2 P_0,

because r^2-3r+1=0 and SS^*=I-P_0.

Thus the golden-ratio de Branges defect is conjugate to a discrete half-line Laplacian with a rank-one boundary correction. This is a concrete Hodge/Dirichlet operator at the same boundary where the Casimir ghost escapes.

Potential next step: compare this explicit Robin-Laplacian defect form with the Casimir ground-state transform in Section 5 and determine whether the arithmetic multiple-sum constraints supply the missing compactness/local-Dirichlet upgrade.
