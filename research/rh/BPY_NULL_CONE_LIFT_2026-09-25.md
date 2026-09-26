# BPY two-copy null-cone lift and rapidity decomposition
## 2026-09-25 — Codex experiment

This note records a new zero-independent structural lift of the BPY two-copy law. It is
not an RH proof.

### 1. Modewise beta-gamma split

For one BPY Fourier mode, let A and B be the independent shape-two Gamma variables from
the two Gaussian copies. Put

S = A+B,                 Z = (A-B)/(A+B).

Standard beta-gamma algebra gives

S ~ Gamma(4,1),          Z has density (3/4)(1-z^2) 1_{[-1,1]}(z),

and S and Z are independent.

The density of Z is exactly the first-coordinate law of a uniform vector U on S^4.
Therefore we may enlarge the probability space and write Z=U_1 with U uniform on S^4.

For the BPY coefficient c_n=1/(pi n^2), define the six-vector

P_n = c_n S_n (1,U_n) in R^{1,5}.

With Minkowski form p_0^2-|p_sp|^2,

P_n^2 = 0,   P_n^0>0.

Thus every BPY mode is exactly a random future-null 5+1-dimensional momentum.  The
shape-four radial law is not accidental: the Lorentz-invariant null-shell measure in
1+5 dimensions has radial factor r^3 dr dOmega_4; the remaining factor e^{-r} is a
Boltzmann weight selecting a time orientation.

### 2. The two BPY copies are light-cone coordinates

Let

P = sum_n P_n = (T,V),       D = V_1.

Then P lies in the closed future Lorentz cone, because it is a sum of future-null
vectors.  Directly from the definitions,

T = Q_1+Q_2,
D = Q_1-Q_2,

so

Q_1 = (T+D)/2,
Q_2 = (T-D)/2,
Q_1 Q_2 = (T^2-D^2)/4.

The BPY center/relative coordinates therefore become

v = (1/2) log(Q_1/Q_2) = artanh(D/T),

u = (1/2) log(Q_1 Q_2)
  = log(T/2) + (1/2) log(1-(D/T)^2).

So the relative BPY coordinate is literally the rapidity of the total positive-energy
momentum in one spatial direction. The exchange involution J is the spatial reflection
D -> -D.

This gives a concrete representation-theoretic meaning to the principal-series
language: the even/odd BPY channels are parity channels in a positive-energy
1+5-dimensional null-cone parent.

### 3. Exact local and global Laplace transforms

For one mode and real parameters in the convergence cone,

E exp[-tau c(A+B)+h c(A-B)]
 = [(1+c(tau-h))(1+c(tau+h))]^{-2}
 = [(1+c tau)^2-c^2 h^2]^{-2}.

This is an exact Lorentz-quadratic denominator.

After multiplying all modes,

L(tau,h)
 = prod_n [(1+c_n tau)^2-c_n^2 h^2]^{-2}
 = L_Q(tau-h)L_Q(tau+h),

where

L_Q(s)
 = prod_{n>=1}(1+s/(pi n^2))^{-2}
 = (sqrt(pi s)/sinh(sqrt(pi s)))^2.

Hence the entire two-copy BPY parent has an explicit positive-energy cone transform with
no zero data.

### 4. Conditional spherical collapse

Condition on all radial variables S_n and put

p_n = c_n S_n / T,      sum p_n=1.

Then

D/T = sum_n p_n Z_n

is the first coordinate of

W = sum_n p_n U_n.

Because the U_n are independent and isotropic in R^5, W is isotropic. Conditional on
R=|W|, its direction is uniform on S^4. Therefore

D/T | R  = R Z,

with the same universal Z-density (3/4)(1-z^2).

Thus the entire infinite-dimensional relative BPY channel collapses, after conditioning,
to one scalar radius R in [0,1] and one universal S^4 angular coordinate. This is much
smaller than the original Gaussian field.

Equivalently,

v | R = artanh(R Z).

### 5. Route audit

The collapse does NOT by itself prove the odd/even contraction. Numerical quadrature of
the conditional angular law shows that the Fourier transform of artanh(R Z) changes sign
for generic fixed R. The special BPY weighting by

(Q_1 Q_2)^{1/4} u sinh(omega u)

also fails to make every fixed-(T,R) slice positive. Therefore any successful proof must
retain the global radial mixture. This agrees with the earlier fixed-center no-go but
localizes it more sharply: the missing sign is in the radial/null-cone completion, not
the universal S^4 angular channel.

### 6. New constructive target

The useful new target is to exploit the positive-energy cone support of P.

For any positive spectral measure supported in a future cone, standard
Osterwalder-Schrader kernels of the form

  int exp[-T(a+b)] exp[i D(a-b)] dmu(T,D)

are positive Gram kernels.

The BPY two-copy kernel is not yet in this form, because the Mellin/log-radius source
uses powers of the null coordinates (T+-D)/2 rather than a linear Laplace source.
However, for 0<alpha<1,

  q^alpha = [alpha/Gamma(1-alpha)]
            int_0^infty (1-e^{-tq}) t^{-1-alpha} dt,

so the BPY fractional insertion admits an exact boundary-subtracted Laplace
representation over the same positive-energy cone.

The next experiment should therefore be: carry the complete de Branges divided
difference through this double Bernstein representation before integrating out
(T,V). If its boundary terms cancel into the already-known pole plane, the remaining
kernel is an honest positive-energy OS square. If a signed term survives, its exact
form identifies the final obstruction.

This route uses extra structure absent from a generic symmetric moment-generating
function: every BPY mode is a future-null 1+5-dimensional momentum, and the arithmetic
n^{-2} tower supplies an explicit completed null-cone Laplace transform.
