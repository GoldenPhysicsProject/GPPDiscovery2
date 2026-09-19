# Exact adjacent-cell / divisibility-zeta factorization

Date: 2026-09-19

This resumes the discrete Hardy/Nyman cell attack after the first-order orientation work.

Let

Y_n(s)=zeta(s)(n^{1-s}-(n+1)^{1-s}),   n>=1.

For Re(s)>1,

Y_n(s)
=
sum_{m>=1}
[n 1_{n|m}-(n+1)1_{n+1|m}] m^{-s}.

Take a finitely supported cell vector

x=(x_1,...,x_N),

and form

F_x(s)=sum_{n=1}^N x_n Y_n(s)
      =sum_{m>=1} a_m(x)m^{-s}.

## 1. Exact first-order factorization

Set

x_0=0,
x_{N+1}=0,

and define the adjacent-cell boundary derivative

g_1=x_1,
g_d=x_d-x_{d-1}  (2<=d<=N+1).

Then direct reindexing gives, for every m>=1,

boxed(
a_m(x)
=
sum_{d|m, 1<=d<=N+1} d g_d
).

Equivalently, on finite support,

C
=
Z_div o D o Delta,

where

(Delta x)_1=x_1,
(Delta x)_d=x_d-x_{d-1},

(Dg)_d=d g_d,

and

(Z_div h)_m=sum_{d|m}h_d.

Thus multiplication by the common zeta channel becomes:
1. a first-order adjacent-cell boundary derivative;
2. multiplication by the boundary label d;
3. the ordinary divisibility zeta transform.

No analytic continuation or RH hypothesis enters.

## 2. Exact Möbius inverse

If

a_m=sum_{d|m}h_d,

then ordinary Möbius inversion gives

h_n=sum_{d|n}mu(n/d)a_d.

Therefore

boxed(
n g_n
=
sum_{d|n}mu(n/d)a_d
).

This is the exact finite algebraic inverse of the common zeta filter.

## 3. Vacuum inverse and the Mertens-1 sequence

The Hardy vacuum 1 has Dirichlet coefficients

a_1=1,
a_m=0  (m>1).

Its formal inverse therefore satisfies

n g_n=mu(n),

so

g_n=mu(n)/n.

Since x_n is the cumulative sum of the adjacent differences,

boxed(
x_n
=
M_1(n)
:=
sum_{d<=n} mu(d)/d
).

Thus the canonical formal inverse of the zeta channel on the orthonormal arithmetic cells is exactly the weighted Mertens sequence M_1.

This recovers the same sequence previously obtained from the causal distributional inverse, now by a purely finite triangular calculation.

## 4. Exact finite interpolation and the boundary-at-infinity charge

Take the truncated vector

x_n^{(N)}=M_1(n), 1<=n<=N,

with x_{N+1}^{(N)}=0.

Then

g_d=mu(d)/d  (1<=d<=N),

while the final boundary jump is

g_{N+1}=-M_1(N).

Consequently the first N Dirichlet coefficients of F_{x^(N)} agree EXACTLY with the vacuum:

a_1=1,
a_m=0, 2<=m<=N.

All failure is pushed beyond the cutoff and into the terminal boundary charge

-(N+1)M_1(N)

at d=N+1 together with the unresolved higher divisor tail.

This is the discrete arithmetic analogue of every other boundary obstruction in the project:
the local differential is exact; the only issue is whether the far endpoint disappears in the correct Hilbert/graph topology.

## 5. Literal inverse versus dense-range inverse

The cell basis is orthonormal before the common zeta filter. Hence the formal inverse vector belongs literally to the input Hilbert space iff

sum_{n>=1}|M_1(n)|^2 < infinity.

That is stronger than what RH asks for. RH/Nyman only requires the vacuum to belong to the CLOSURE of the filtered range, not that the canonical Möbius inverse itself be square summable.

Therefore failure of M_1 in l2 would not be a counterexample to RH; it would only show that the minimum algebraic inverse is not a literal Hilbert vector.

The correct problem is boundary capacity:
can one modify the far tail of finite cell vectors while preserving the exact low-order Möbius cancellation so that the filtered vectors converge to the vacuum in Hardy norm with bounded/controlled input energy?

## 6. First-order orientation interpretation

The factor Delta is the discrete orientation-sensitive operation. Constants are invisible to the interior difference and survive only at endpoints.

This is the exact discrete counterpart of the continuous pattern

first-order signed generator -> positive square after boundary conditions.

The Möbius coefficients do not appear as a mysterious global inverse; they are the first-order boundary data required to invert the divisibility zeta transform.

The terminal term -(N+1)M_1(N) is the discrete version of the boundary charge that repeatedly appears in the theta, co-Poisson and BPY integrations by parts.

## 7. Immediate target

Construct a sequence of finitely supported corrections y^(N), supported only in the far tail, such that

- the first N arithmetic output coefficients remain delta_{m1};
- the Hardy norm of T_Z(x^(N)+y^(N))-1 tends to zero;
- the corrected input norms remain controlled in the graph topology.

This is a finite boundary-control problem.  It avoids assuming a bounded global Möbius inverse.

A successful construction would prove density of the arithmetic cell range, hence eliminate the Nyman/Burnol inner defect.

The obstruction, if any, must be an asymptotic boundary charge at infinity rather than local arithmetic invertibility.
