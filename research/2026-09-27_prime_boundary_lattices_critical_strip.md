# Prime Euler scattering has exact pole/zero lattices on the two boundaries of the critical strip

Date: 2026-09-27
Status: exact local meromorphic geometry and a global construction target. No RH proof.

## 1. Centered spectral coordinate

Write

s = 1/2 + iT

and, for a prime p,

a_p = p^(-1/2),
L_p = log p.

The relative local Euler scattering phase is

S_p(T)
=
zeta_p(1/2+iT)/zeta_p(1/2-iT)
=
(1-a_p e^(+iL_pT))/(1-a_p e^(-iL_pT)).

For real T,

|S_p(T)|=1,

and

S_p(-T)=S_p(T)^(-1).

## 2. Exact pole lattice

Poles satisfy

1-a_p e^(-iL_pT)=0.

Since

a_p=e^(-L_p/2),

this is

e^(-iL_pT)=e^(L_p/2).

Taking all logarithmic branches,

-iL_pT
=
L_p/2 + 2 pi i k,

so

boxed:
T_{p,k}^{pole}
=
- 2 pi k/L_p + i/2,
qquad k in Z.

Thus every local prime pole lies on the horizontal line

boxed:
Im T=+1/2.

In the s-plane,

Re s
=
1/2-Im T
=
0.

So the entire local pole lattice lies on the left boundary Re(s)=0 of the critical strip.

## 3. Exact zero lattice

Zeros satisfy

1-a_p e^(+iL_pT)=0,

hence

boxed:
T_{p,k}^{zero}
=
+ 2 pi k/L_p - i/2,
qquad k in Z.

Therefore every local zero lies on

boxed:
Im T=-1/2,

which maps to

boxed:
Re s=1.

So one prime channel has two exactly reflected boundary lattices:

zero lattice on Re(s)=1,
pole lattice on Re(s)=0.

The shadow map s -> 1-s exchanges them.

## 4. The local critical strip is forced by the TFD half-density

The distance of the two boundary lattices from the real T axis is exactly 1/2 because

a_p=p^(-1/2).

More generally, if the local Schmidt/Blaschke parameter were p^(-sigma_0), the same calculation would put the boundary lattices at

Im T=+/- sigma_0.

Thus the critical Haar half-density

a_p=p^(-1/2)

is exactly what gives the local analytic strip its width

boxed:
|Im T|<1/2.

Equivalently,

boxed:
0<Re s<1.

This is a genuine local geometric meaning of the critical strip: it is the common open strip between the zero and pole lattices of every prime TFD/Euler scattering channel.

## 5. The lattice spacing is Fourier-dual to the prime logarithmic length

For fixed p the real spacing is

boxed:
Delta T_p = 2 pi/log p.

Hence

boxed:
(log p)(Delta T_p)=2 pi.

This is the exact Fourier phase quantization associated with the prime delay line of length log p.

So one prime carries three equivalent data:

primitive logarithmic length L_p=log p,

modular energy E_p=log p,

boundary resonance spacing Delta T_p=2 pi/L_p.

## 6. Relation to the causal delay realization

The free inner delay is

phi_p(T)=e^(iL_pT).

The dressed local channel is

Theta_p^{in}(T)=B_{a_p}(phi_p(T)).

Its defect space is the TFD-dressed causal interval

L^2([0,L_p]).

The relative Euler phase is obtained by dividing out the free delay.

Thus:

- the dressed channel is causal/inner in the upper half-plane;
- the free-delay quotient is unitary on the real axis but acquires its pole lattice at Im T=+1/2;
- the reflected quotient has the zero lattice at Im T=-1/2.

This makes precise why boundary unitarity alone is insufficient: removing the free causal delay produces a relative all-pass object whose analytic domain is a strip, not the full upper half-plane.

## 7. Local-to-global interpretation

At every finite place:

boxed:
local singularities live only on the two boundaries of the critical strip.

There are no local Euler poles or zeros in

|Im T|<1/2.

Therefore any nontrivial zeta zero inside the critical strip is not a zero of an individual prime degree of freedom.

It is necessarily a collective singularity/resonance of the globally sewn infinite system.

This sharpens the microscopic/collective dictionary:

primes = local channels,

prime powers = repeated delay returns,

boundary lattices = local Euler resonances,

nontrivial zeros = global collective resonances after infinite prime--Archimedean sewing.

## 8. Rational endpoint cancellation

The k=0 local lattice points occur at

T=+i/2  (pole),
T=-i/2  (zero),

corresponding to

s=0,
s=1.

Every prime has the same endpoint pair.

The completed zeta function xi(s) is regular at s=0 and s=1 because the rational factor s(s-1), together with the Gamma/zeta continuation, removes the global endpoint singularity.

Thus the rational completion is naturally interpreted as an endpoint renormalization of a singularity shared by every local channel.

This does not mean one cancels infinitely many local poles one-by-one; only the globally analytically continued object is meaningful. It does identify the exact geometric location that the rational completion must repair.

## 9. Connection with the Schatten hierarchy

Each local factor is meromorphic in the full strip

|Im T|<1/2

with no local singularity there.

But the infinite prime product is not normally convergent in that full strip.

After removing repetitions m<k, the regularized product converges normally only in

|Im T| < 1/2 - 1/k.

For k=3 this gives

|Im T|<1/6.

So there are two distinct notions:

1. local analyticity strip: |Im T|<1/2;
2. naive infinite-product convergence strip after finite-order subtraction.

The missing adelic/Archimedean completion must recover the global meromorphic continuation across the gap between these two.

That gap is not caused by any single prime singularity. It is purely an infinite collective convergence problem.

## 10. New closure target

A natural operator goal is now:

Construct the renormalized infinite cascade of the local TFD-dressed delay systems in a way that

- preserves their common strip |Im T|<1/2;
- implements the rational/Archimedean endpoint completion;
- produces the exact completed scattering/Weyl function;
- is passive/positive on the physical half of the doubled space.

If the resulting completed transfer is Schur/causal in the required half-plane, the existing de Branges criterion would force the global resonances to the real T axis, i.e. Re(s)=1/2.

That final passivity theorem remains open.
