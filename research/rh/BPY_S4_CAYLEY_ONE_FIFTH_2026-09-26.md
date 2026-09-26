# BPY S^4 angular law meets the RH Cayley one-fifth radius
Date: 2026-09-26
Status: exact probability/algebra observation; elementary moments being formalized in Lean 4.33.1. No RH claim.

## 1. Two-copy BPY angular variable

For one Fourier mode of the BPY two-copy construction, let A,B be independent Gamma(2,1)
variables. Set

S=A+B,
Z=(A-B)/(A+B).

Beta-gamma algebra gives U=A/(A+B)~Beta(2,2), hence Z=2U-1 has density

  f_Z(z) = (3/4)(1-z^2),  -1<=z<=1.

This is exactly the first-coordinate law of a uniform point on S^4 subset R^5.

Therefore

  E[Z]=0,
  E[Z^2]=1/5.

The second moment is elementary:

  (3/4) int_{-1}^1 z^2(1-z^2) dz
  = (3/4)(2/3-2/5)
  = 1/5.

## 2. Total two-copy Cayley coordinate

In the null-cone lift, write total future-cone momentum as P=(T,V), and D=V_1.
Then

  Q1=(T+D)/2,
  Q2=(T-D)/2,

and the natural exchange-odd Cayley coordinate is

  C = (Q1-Q2)/(Q1+Q2) = D/T = tanh(v),

where v=(1/2)log(Q1/Q2) is the BPY relative rapidity.

Conditioning on the radial mixture gives

  D/T = R Z,   0<=R<=1,

with the same universal S^4 coordinate Z. Thus

  E[(D/T)^2 | R] = R^2/5 <= 1/5.

So the BPY two-copy geometry contains an exact L^2 one-fifth angular scale.

## 3. Exact match with the RH dyadic Cayley radius

The v34 affine Hardy/Cayley atlas has worst-cell bound

  |beta|^2 <= 1/5,

hence radius

  |beta| <= 1/sqrt(5).

The BPY angular variable has

  E[Z^2]=1/5=(1/sqrt(5))^2.

This is a new exact cross-route coincidence:

  BPY S^4 coordinate variance = dyadic Hardy worst Cayley radius squared.

Through the already formalized identity

  (1-1/sqrt(5))/(1+1/sqrt(5)) = phi^(-2),

the same one-fifth scale also produces the golden dyadic precision margin.

## 4. Why this might matter

If the completed odd BPY transfer reduced purely to the first S^4 harmonic, its angular
norm relative to the radial/even channel would acquire an exact factor 1/sqrt(5), giving
a strict contraction for free.

That would fit the existing Lean endpoint

  contractive completed transfer -> two-point Weil positivity -> RH.

## 5. Critical caveat

The full relative rapidity is

  v=artanh(RZ)=RZ+(RZ)^3/3+(RZ)^5/5+...

so it contains every odd spherical harmonic, not only the l=1 coordinate mode. Multiplication
by Z on full L^2 has operator norm 1, not 1/sqrt(5). Therefore E[Z^2]=1/5 alone does NOT
prove the required operator contraction.

The useful next test is precise: decompose the actual BPY odd transfer into Gegenbauer
harmonics on S^4 and determine whether the completed Gamma/pole/radial weighting suppresses
the higher odd harmonics strongly enough that the full transfer norm remains <=1.

If the transfer projects only through the first harmonic after the co-Poisson/connected
quotient, the one-fifth identity becomes load-bearing. If higher harmonics survive at full
strength, it is another structural coincidence only.

Lean target:
  GppVerify/RiemannHypothesis/BPYAngularCayley.lean
