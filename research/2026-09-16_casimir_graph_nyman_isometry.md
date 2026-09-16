# Casimir graph realization of the Nyman complex

## Setup

Use logarithmic coordinate u=log t and

Q = D + 1/2,   H_C = Q^* Q = -D^2 + 1/4.

Define the sawtooth field on R by

w(u) = (1 - {e^u}) e^{-u/2}.

Distributionally,

Qw = S = sum_{n>=1} n^{-1/2} delta_{log n} - e^{u/2}.

The canonical negative Casimir space is the range of Q equipped with

||Y||_{-1,C}^2 = <Y,H_C^{-1}Y>.

In Fourier variables Q has multiplier i tau + 1/2 and H_C has multiplier tau^2+1/4, hence

||Qf||_{-1,C}=||f||_2.

Thus Q is an exact isometry from L^2(R) onto the Casimir negative graph space.

## Nyman generators

For 0<lambda<=1 define the inverted/logarithmic Nyman generator

F_lambda(u)=e^{-u/2}({lambda e^u}-lambda {e^u}).

It vanishes for u<0. Since

e^{-u/2}{e^u}=e^{-u/2}-w(u),

one gets the exact identity

F_lambda(u)=(1-lambda)e^{-u/2}+lambda w(u)-sqrt(lambda) w(u+log lambda).

Because Q e^{-u/2}=0 and Q commutes with translations,

QF_lambda = lambda S - sqrt(lambda) T_{log lambda} S.

The continuum pieces cancel exactly, so

QF_lambda
 = lambda sum_{n>=1} n^{-1/2} delta_{log n}
   - sqrt(lambda) sum_{n>=1} n^{-1/2} delta_{log(n/lambda)}.

Thus the Nyman generators become pure differences of two arithmetic half-density combs.

## Target vector

The inverted Nyman target is

F_0(u)=e^{-u/2} 1_{u>0}.

Distributionally,

QF_0 = delta_0.

Therefore the Nyman-Beurling criterion transports isometrically to

RH iff delta_0 belongs to the H_C^{-1/2}-closure of span{QF_lambda:0<lambda<=1}.

This graph topology retains the Nyman-Burnol ghost exactly; it is not a smoothing topology that can erase the obstruction.

## Causal cutoff anomaly

The Green kernel of H_C on R is

G_C(x,y)=exp(-|x-y|/2).

The target norm is

<delta_0,H_C^{-1}delta_0>=1.

For the target-generator pairing, a same-index cutoff of the two combs is incorrect because it is not a cutoff in physical logarithmic position. Truncate instead at 0<=u<=L. Then the first comb has n<=e^L while the shifted comb has n<=lambda e^L. Hence

<delta_0,QF_lambda>_{-1,C;L}
 = lambda H_{floor(e^L)} - lambda H_{floor(lambda e^L)}.

Letting L->infinity gives

<delta_0,QF_lambda>_{-1,C}
 = -lambda log lambda.

This matches directly

<F_0,F_lambda>_{L^2}
 = integral_1^infinity ({lambda t}-lambda {t}) dt/t^2
 = -lambda log lambda.

The finite term is therefore a genuine causal boundary anomaly produced by the mismatch of the two physical support cutoffs, not an arbitrary renormalization constant.

## Discrete reciprocal subfamily

For lambda=1/m, m>=2,

{t/m}-(1/m){t} = floor(t)/m - floor(t/m).

On n<=t<n+1 this equals (n mod m)/m. Hence the discrete Nyman Gram matrix has the exact form

G_{m,k}
 = sum_{n>=1} [(n mod m)(n mod k)/(mk)] [1/n - 1/(n+1)].

With L=lcm(m,k), periodic grouping gives a finite digamma representation

G_{m,k}
 = (1/(mkL)) sum_{r=1}^L (r mod m)(r mod k)
   [psi((r+1)/L)-psi(r/L)],

where the r=L term vanishes because both remainders are zero.

The target correlations are

b_m = (log m)/m.

Thus finite Nyman projection in the Casimir graph is an explicit positive matrix problem with no zero input.

## Status

This does not prove RH. It does solve a structural problem left open in v34: the canonical Casimir negative graph topology preserves the Nyman complex and its ghost exactly. The remaining theorem is density/coercivity in this exact graph space, equivalently elimination of the Nyman-Burnol cokernel. The comb representation and causal cutoff anomaly provide a new source-level formulation for attacking that theorem.
