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

## Centered divisibility source

For lambda=1/m define

c_m(n)=1/m-1_{m|n}.

Then the source has the exact form

QF_{1/m}
 = sum_{n>=1} n^{-1/2} c_m(n) delta_{log n}.

The primitive relation is

sum_{j=1}^n c_m(j) = (n mod m)/m.

Thus the reciprocal Nyman family is the family of centered divisibility combs.

Under Haar measure on the profinite integers,

E[c_m]=0,

E[c_m c_k]
 = 1/lcm(m,k)-1/(mk)
 = (gcd(m,k)-1)/(mk).

In particular distinct prime divisibility observables are orthogonal in the profinite Haar metric. The coupling which destroys this simple primewise orthogonality is therefore the Archimedean logarithmic-scale Green kernel, not unique factorization itself.

## Casimir Green kernel as Brownian covariance

For atoms at log i and log j,

(i j)^(-1/2) G_C(log i,log j)
 = (i j)^(-1/2) exp(-|log i-log j|/2)
 = 1/max(i,j).

Therefore, with the canonical causal summation,

G_{m,k}
 = sum_{i,j>=1} c_m(i)c_k(j)/max(i,j).

Since

1/max(i,j)
 = sum_{n>=max(i,j)} [1/n - 1/(n+1)],

summation by parts recovers the absolutely convergent remainder formula above.

Moreover

1/max(i,j)=min(1/i,1/j),

which is exactly the covariance kernel of standard Brownian motion sampled at times 1/i and 1/j. Thus the same exact Gram form has four simultaneous interpretations:

Nyman fractional-part Gram = Casimir negative graph energy = centered divisibility Green form = Brownian covariance sampled on reciprocal integers.

## Status

This does not prove RH. It does solve a structural problem left open in v34: the canonical Casimir negative graph topology preserves the Nyman complex and its ghost exactly. The remaining theorem is density/coercivity in this exact graph space, equivalently elimination of the Nyman-Burnol cokernel. The comb representation, causal cutoff anomaly, centered divisibility form, and Brownian Green factorization provide a new source-level formulation for attacking that theorem.
