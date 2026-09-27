# Archimedean completion as pole mode minus the trivial-zero oscillator ladder

Clarification from the continuation audit: “pole mode” below means the pole
of the isolated rational/Archimedean summand. The entire completed function
\(\xi(s)\) has no pole at \(s=1\); the \(1/(s-1)\) term is cancelled by
\(\zeta'/\zeta(s)\) in the full logarithmic derivative. Matching elementary
resolvent shapes is not by itself a proved identification of two physical
random variables or of the complete boundary system.

Date: 2026-09-27
Status: exact algebraic/spectral decomposition of the real-place boundary density. No RH claim. No external search used.

The completed real-place density already isolated in the RH program is

w_infty(x)
=
e^{-x/2}+e^{x/2}
-
e^{-x/2}/(1-e^{-2x}),
for x>0.

Expand the thermal denominator:

e^{-x/2}/(1-e^{-2x})
=
sum_{k>=0} e^{-(2k+1/2)x}.

The k=0 term cancels the explicit e^{-x/2}. Therefore

boxed:
w_infty(x)
=
e^{x/2}
-
sum_{k>=1} e^{-(2k+1/2)x}.

This is exact.

## Spectral meaning of the exponents

Use the centered variable r=s-1/2.

The growing mode e^{x/2} has Laplace pole

int_0^infty e^{-rx} e^{x/2} dx
=
1/(r-1/2),

which is exactly the completed-zeta pole at s=1.

The k-th decaying mode has

int_0^infty e^{-rx} e^{-(2k+1/2)x} dx
=
1/(r+2k+1/2).

Its pole occurs at

r=-(2k+1/2),

hence

s=1/2+r=-2k.

Therefore the entire negative Archimedean ladder is located exactly at the trivial zeta zeros

s=-2,-4,-6,...

The missing k=0 ladder pole would be at s=0. It is cancelled exactly by the rational e^{-x/2} term already present in the completed real-place density.

So the real-place completion has the exact signed spectral interpretation

boxed:
Archimedean boundary
=
s=1 escape/pole mode
-
trivial-zero ladder.

No nontrivial zero data enter.

## Renormalized Laplace formula

Because w_infty has a singularity at x=0, the existing boundary distribution uses one subtraction:

<nu_infty,phi>
=
A_infty(1) phi(0)
+
int_0^infty w_infty(x)[phi(x)-phi(0)e^{-x}] dx.

For phi_r(x)=e^{-rx}, r>1, the ladder form gives

A_infty(r)
=
A_infty(1)
+
[1/(r-1/2)-2]
-
sum_{k>=1}
[
1/(r+2k+1/2)
-
1/(2k+3/2)
].

This equals exactly

1/(r+1/2)
+
1/(r-1/2)
-
(1/2)log pi
+
(1/2) psi(r/2+1/4).

The subtraction is therefore just the convergent relative resolvent normalization of one unstable pole mode against the stable trivial-zero ladder.

## Relation to the critical Gibbs escape mode

For beta=1+epsilon, the zeta Gibbs law satisfies

epsilon log N => Exp(1).

Its limiting Laplace transform is

1/(1+s).

Thus the global beta->1 mass escape is a one-sided exponential boundary mode.

The centered completed-zeta pole contribution 1/(r-1/2) is the same elementary resolvent shape after the natural shift of spectral origin from beta=1 to r=1/2.

This does not by itself identify the full real place with the Gibbs escape variable: the trivial-zero/metaplectic ladder remains essential. It does show that the previously separate "pole channel" and "critical Gibbs escape" are the same rank-one resolvent geometry.

## Completed arithmetic boundary as one positive mode against two positive baths

The prime boundary measure is

nu_p
=
sum_{n>=2} Lambda(n)n^{-1/2} delta_{log n}.

The real-place decomposition suggests the signed schematic form

W
=
nu_escape
-
nu_triv
-
nu_prime

after the common subtraction/renormalization at x=0.

Here

nu_escape(dx) = e^{x/2} dx,

nu_triv(dx)
=
sum_{k>=1} e^{-(2k+1/2)x} dx,

and nu_prime is the positive von-Mangoldt half-density comb.

Thus all negative channels are positive objects individually:
the trivial-zero oscillator tower and the prime-power return measure.
The only positive counter-channel is the completed pole/escape mode, plus its renormalized contact term.

This makes the no-ghost problem look like a rank-one/low-rank completion against two positive baths rather than an arbitrary signed distribution.

## Operator target

A useful next construction is a supersymmetric/Friedrichs-type boundary system with:

1. one escape mode carrying the s=1 pole;
2. a discrete metaplectic bath at s=-2k;
3. the logarithmic prime-return bath at x=log n;
4. the existing rational/idele sewing enforcing the s<->1-s reflection.

The target is not to declare the signed measure positive. It is to show that after the physical Schur/Hodge quotient its Weyl function is the already exact m_*(u) and its spectral measure is positive.

This note sharpens the real-place input: the Archimedean channel is no longer opaque. It is exactly one pole mode minus the trivial-zero ladder.
