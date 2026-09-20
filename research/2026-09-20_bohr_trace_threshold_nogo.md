# Trace-threshold no-go for positive height-Sobolev completion

Date: 2026-09-20

Continue the exact Bohr-Hilbert arithmetic shadow lift.

For sigma>1/2 the reduced-rational coefficients a_sigma(r/s) form a unit vector in
l2(Q_+^x).

One would like to recover the scalar arithmetic shadow quotient by the orbit evaluation

Ev_t(a)=sum_{(r,s)=1} a(r/s) exp[-it log(r/s)].

A natural attempt is to strengthen the Hilbert norm by a positive arithmetic height
weight (rs)^delta and then use Cauchy-Schwarz.

## Exact threshold calculation

Suppose

||a||_{sigma,delta}^2
=
sum |a_sigma(r/s)|^2 (rs)^(2delta).

The same Euler estimates as in the unweighted norm show that this is finite only if

2(sigma-delta)>1,

i.e.

delta<sigma-1/2.

On the other hand Cauchy-Schwarz for point evaluation requires

sum_{(r,s)=1}(rs)^(-2delta)<infinity.

Since this is bounded by / comparable to zeta(2delta)^2 up to the coprimality Euler
factor, it is finite iff

2delta>1,

i.e.

delta>1/2.

Therefore there exists a positive height exponent delta for which both the vector norm and
the evaluation dual norm are finite iff

1/2 < delta < sigma-1/2,

which is possible iff

boxed(sigma>1).

Thus the ordinary Euler half-plane is EXACTLY the positive Sobolev/height trace threshold.

## Consequence

No graph norm obtained merely by inserting a positive power of the reduced rational height
can extend the arithmetic Kronecker-orbit evaluation into 1/2<sigma<=1.

In particular, the missing half-strip continuation cannot come from:
- generic L2 trace theory;
- a positive polynomial/height Sobolev reweighting;
- the fixed Haar metric alone.

The extension must exploit SIGNED arithmetic cancellation (Mobius / prime-Archimedean
completion) or a genuinely nonlocal graph condition.

This strengthens the previous periodization/topology no-go.  The obstruction is not a
technical weakness of one Gamma norm; it is the codimension/height count of the reduced
rational trace itself.

At sigma>1, choose any delta with 1/2<delta<sigma-1/2 and the Cauchy-Schwarz trace becomes
bounded, recovering the region where the ordinary Euler product already converges.

At sigma<=1 no such positive-height Hilbert trace can exist.

This identifies the required new theorem very sharply:
a successful trace must use cancellation that is invisible to absolute Hilbert majorants.
