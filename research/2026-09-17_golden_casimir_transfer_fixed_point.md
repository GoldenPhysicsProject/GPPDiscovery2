# Golden Casimir transfer fixed point and finite-place causal factorization

Date: 2026-09-17
Status: exact operator/algebraic identities; no RH claim.

## 1. Casimir ground-state transform

For the discrete ghost variables q_n = n h_n, the weighted Casimir/Bergman energy satisfies

E_C(q) = |q_1|^2 + sum_{n>=1} |q_{n+1}-q_n|^2.

On l^2(N), with unilateral shift S e_n = e_{n+1}, define

L = 2I - S - S*.

Then for finitely supported q (and by form closure),

<q,Lq> = |q_1|^2 + sum |q_{n+1}-q_n|^2.

Thus the Casimir ghost ground-state transform is the standard half-line discrete Laplacian form.

## 2. Finite-place contraction and mass

For q>1 define the principal-series-center finite-place kernel

K_q := K_{q,1}(1/2) = (sqrt(q)+1)/(sqrt(q)-1),

and its reciprocal contraction

r_q := K_q^{-1} = (sqrt(q)-1)/(sqrt(q)+1).

Define

m_q^2 := 4/(q-1).

Then exactly

r_q + r_q^{-1} = 2 + m_q^2,

or equivalently

m_q^2 = (1-r_q)^2/r_q.

Hence the massive discrete Casimir operator factors as

L + m_q^2 I
 = r_q^{-1} (I-r_q S*) (I-r_q S).

Reversing causal/adjoint order gives

L + m_q^2 I - r_q P_1
 = r_q^{-1} (I-r_q S) (I-r_q S*),

where

P_1 = S* S - S S*

is the rank-one vacuum projection. Therefore the boundary vacuum source is exactly the ordering anomaly between the causal factor and its adjoint.

In the massless limit q -> infinity,

r_q -> 1,
m_q^2 -> 0,

and the ordering anomaly tends to P_1.

## 3. The unit-mass fixed point selects q=5

Unit mass means m_q^2=1, hence

4/(q-1)=1,

so uniquely

q=5.

Equivalently, define the induced spectral floor of the first-order causal factor by

R(r)=(1-r)^2.

The self-consistency condition that the contraction equal its own induced floor is

r=(1-r)^2.

This gives

r^2-3r+1=0.

The unique root in (0,1) is

r = (3-sqrt(5))/2 = phi^{-2}.

The discriminant is 5. For r_q this equation is equivalent to q=5.

Thus the RH boundary fixed-point condition independently selects the same discriminant 5 and the same stable eigenvalue phi^{-2} as the previously formalized minimal hyperbolic PSL2(Z) sector.

## 4. Exact modular transfer-matrix identification

The unit-mass recurrence

(I+L)u=0

has interior form

u_{n+1}=3u_n-u_{n-1},

with transfer matrix

C = [[3,-1],[1,0]] in SL2(Z).

The previously formalized minimal hyperbolic matrix is

A = [[2,1],[1,1]].

With

P = [[1,-1],[0,1]] in SL2(Z),

one has

A P = P C,

hence

P^{-1} A P = C.

Therefore the old minimal hyperbolic modular sector and the new unit-mass discrete Casimir transfer dynamics are the same SL2(Z) conjugacy class.

Both have characteristic polynomial

x^2 - 3x + 1,

stable root phi^{-2}, unstable root phi^2, and discriminant 5.

## 5. Fejer-Riesz / Wiener-Hopf factorization

On the bilateral spectral variable z with |z|=1,

the unit-mass discrete Casimir symbol is

1 + (2-z-z^{-1}) = 3-z-z^{-1}.

For r=phi^{-2},

3-z-z^{-1}
 = r^{-1}(1-rz)(1-rz^{-1}).

Thus phi^{-2} is the stable causal spectral factor of the unit-mass Casimir resolvent.

On the half-line the two possible factor orders differ by the rank-one vacuum anomaly described above.

## 6. Geometric causal kernel and thermality

For 0<r<1 define

b_r(z)=(1-r)/(1-rz)
      = sum_{n>=0}(1-r) r^n z^n.

Its coefficients

p_n=(1-r)r^n

form a geometric probability distribution.

For r=r_q,

mean(N)=r_q/(1-r_q)=(sqrt(q)-1)/2,

var(N)=r_q/(1-r_q)^2=(q-1)/4.

Hence unit variance is equivalent to q=5 and r=phi^{-2}.

The parity polarization and collision probability are both

E[(-1)^N]
 = sum_n p_n^2
 = (1-r_q)/(1+r_q)
 = q^{-1/2}.

Therefore the Renyi-2 entropy is exactly

H_2(p)= -log(sum p_n^2) = (1/2) log q.

This is the arithmetic half-density energy scale in entropy form.

At q=5,

r=phi^{-2},
1-r=phi^{-1},
p_n=phi^{-(2n+1)},
mean=phi^{-1},
var=1,
H_2=(1/2)log 5.

The Shannon entropy is

H = -log(1-r) - [r/(1-r)] log r
  = sqrt(5) log phi.

## 7. One-sided oscillator partition vs shadow-paired kernel

Write r_q=e^{-beta_q}, so

beta_q=log K_q.

The geometric law is the Gibbs distribution of a unit-spaced oscillator. Its one-sided partition function is

Z_q = 1/(1-r_q) = (sqrt(q)+1)/2.

At q=5,

beta_5=2 log phi,
Z_5=phi.

Since K_5=phi^2,

K_{5,1}(1/2)=Z_5^2.

Moreover K_q=Z_q^2 iff q=5. Thus q=5 is the unique finite-place center where the shadow-paired kernel is exactly the square of an identical one-sided causal thermal partition.

## 8. Power response as a Casimir resolvent

For |z|=1 let

lambda(z)=|1-z|^2.

Then for general q,

|b_{r_q}(z)|^2
 = 1/[1+((q-1)/4) lambda(z)].

At q=5 this becomes

|b_phi(z)|^2 = 1/[1+lambda(z)].

Therefore the golden causal filter is the minimum-phase spectral factor of the unit-mass discrete Casimir resolvent, and its Schur defect is the bounded Casimir transform

1-|b_phi|^2 = lambda/(1+lambda).

This gives an internal reason for phi: it is the unique stable causal spectral factor compatible with unit Casimir mass / unit geometric variance.

## 9. Integral-transfer arithmetic

The general transfer matrix

C_q = [[2+m_q^2,-1],[1,0]]

has determinant 1 and eigenvalues r_q^{-1}, r_q.

If q is an integer >1, C_q is integral exactly when q-1 divides 4, i.e.

q in {2,3,5}.

The corresponding traces are 6,4,3. Hence q=5 uniquely gives the minimal hyperbolic integral trace 3.

This independently reproduces the earlier minimal-hyperbolic selection.

## 10. RH relevance and honest boundary

The discoveries above do not prove RH. They sharpen the no-ghost problem:

- the Casimir ghost energy is the homogeneous half-line Laplacian form;
- the target vacuum is the unilateral-shift index projection P_1;
- finite-place center kernels generate a canonical family of massive causal factorizations;
- q=5 is the unique unit-mass/unit-variance/self-consistent member and is exactly the previously formalized golden modular sector;
- causal/adjoint reversal produces the target boundary projection as a rank-one anomaly.

The next mathematical target is to combine the arithmetic multiple-sum ghost equations with this causal factorization. A possible route is to prove a Rellich/no-resonance theorem: no nonzero homogeneous finite-energy sequence satisfying all arithmetic dilation constraints can survive as a zero-energy boundary resonance of the massless shift Laplacian. Another route is to build the finite-place massive resolvent family into a zero-independent graph norm whose q->infinity limit is strong enough to force the missing l^2/local-Dirichlet regularity.
