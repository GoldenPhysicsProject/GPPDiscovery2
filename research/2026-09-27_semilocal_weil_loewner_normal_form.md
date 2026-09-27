# Exact Loewner normal form of the semilocal Weil matrix

Date: 2026-09-27
Status: exact algebraic reformulation of the existing semilocal matrix. No RH assumption.

## 1. Starting matrix

Fix support length L>0 and the Fourier frequencies

x_n = 2 pi n / L.

Let Psi be the completed one-sided Weil distribution restricted to [0,L]. Define

S_L(x) = Psi[ sin(x y) ],
C_L(x) = Psi[ cos(x y) ].

The semilocal kernels are

q_mn(y)
= [sin(x_m y)-sin(x_n y)]/[pi(n-m)],  m != n,

q_nn(y)
= 2(1-y/L) cos(x_n y).

The semilocal Weil matrix is Q_mn=Psi[q_mn].

## 2. Off-diagonal entries are already a divided-difference kernel

Set

b_L(x)=-(2/L) S_L(x).

Since
x_m-x_n=(2 pi/L)(m-n),

for m != n,

boxed:
Q_mn = [b_L(x_m)-b_L(x_n)]/(x_m-x_n).

The only apparent obstruction to a literal Loewner matrix is the diagonal. We have

b_L'(x_n)=-(2/L) Psi[y cos(x_n y)],

while

Q_nn
=2 C_L(x_n) -(2/L)Psi[y cos(x_n y)]
=b_L'(x_n)+2 C_L(x_n).

## 3. Boundary alias correction

Define the odd entire boundary-completed phase

boxed:
f_L(x)
=
b_L(x)
+
(2/L) sin(Lx) C_L(x)

=
(2/L) Psi[
 -sin(xy)+sin(Lx)cos(xy)
].

At every lattice frequency x_n,

sin(L x_n)=0,
cos(L x_n)=1.

Therefore

f_L(x_n)=b_L(x_n)

and

f_L'(x_n)
=
b_L'(x_n)+2 C_L(x_n)
=
Q_nn.

Consequently the entire semilocal matrix is exactly the confluent Loewner matrix of one scalar function:

boxed:
Q_mn =
  (f_L(x_m)-f_L(x_n))/(x_m-x_n),  m != n,
  f_L'(x_n),                       m = n.

No zero ordinates enter f_L. It is built only from the completed pole, real-place, and finite prime-power data below the support cutoff.

Because S_L is odd and C_L is even,

f_L(-x)=-f_L(x),

so the parity symmetry of Q is automatic.

## 4. Quasiperiodic extension

For a common boundary twist theta, use

x_{n,theta}=2 pi(n+theta)/L.

The differences remain integer-periodic, so the same truncated exponential correlation calculation goes through. Define

f_{L,theta}(x)
=
b_L(x)
+
(2/L) sin(Lx-2 pi theta) C_L(x).

Then

sin(Lx_{n,theta}-2 pi theta)=0,
cos(Lx_{n,theta}-2 pi theta)=1,

and the corresponding twisted semilocal matrix is exactly the Loewner matrix of f_{L,theta} on the shifted lattice {x_{n,theta}}.

Thus the boundary condition appears as the interpolation phase in a scalar Loewner problem.

## 5. Why this is potentially useful

For real interpolation nodes, positivity of a confluent Loewner matrix is precisely the finite matrix-monotonicity/Pick-interpolation condition on the supplied values and derivatives.

Therefore the semilocal Weil positivity problem can be recast, at every finite support length, as a scalar Pick-interpolation problem for the zero-independent completed phase f_L.

This is stronger than merely observing the rank-two displacement identity

D_0 Q-Q D_0 = |beta><eta|-|eta><beta|.

That identity is the standard low-displacement-rank shadow of the Loewner representation.

The exact finite question becomes:

Does the arithmetic Hermite data

{ f_L(x_n), f_L'(x_n) }

admit a Pick/Herglotz interpolant without subtracting the lowest eigenvalue?

Under RH the answer is yes because Q is the restricted Weil Gram matrix. A proof must obtain it directly from the prime--Archimedean construction.

## 6. Zero mode

At n=0,

Q_00=f_L'(0).

The existing screw-function relation is

Psi_screw(L) = (L/2) Q_00.

Hence

boxed:
Psi_screw(L) = (L/2) f_L'(0).

The known scalar criterion RH iff Psi_screw(L)>=0 for all L is therefore the first derivative test of the same Loewner phase whose higher finite matrices encode the semilocal positivity problem.

So the scalar screw criterion and the finite semilocal Gram hierarchy are not separate objects: they are the first-order and higher-order Loewner tests of one completed arithmetic phase.

## 7. New attack

A possible route is now to seek a direct Herglotz representation of f_L (or a canonical Möbius transform of it) from the causal Dirichlet/Poisson construction.

If one can prove that f_L belongs to the Pick class on the relevant real interval for every L, then every semilocal Q is positive. Since the zero mode already carries an exact RH criterion, such a theorem would prove RH.

The point is not to assume matrix positivity and invoke Loewner's theorem, but to derive the analytic Pick property from the explicit prime--Archimedean boundary transfer.

A second route is to exploit the quasiperiodic theta family: the same physical boundary distribution generates Loewner matrices on every shifted Fourier lattice. This may give enough interpolation rigidity to promote finite lattice positivity to a global Pick property once a uniform causal estimate is found.
