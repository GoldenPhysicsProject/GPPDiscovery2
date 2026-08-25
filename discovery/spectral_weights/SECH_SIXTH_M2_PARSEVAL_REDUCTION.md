# Sech^6 reduction of the full-plane M2 convolution

Codex/GPT discovery track, 2026-08-25.

Let

P(lambda)=pi lambda/sinh(pi lambda)

with Fourier convention

P_hat(k)=int_R e^{-ik lambda} P(lambda) dlambda
        = pi/[2 cosh^2(k/2)].

For the full-plane three-factor convolution

I_R2 = int_R int_R P(x) P(y) P(x-y) dx dy,

convolution plus Parseval gives

I_R2 = (1/(2pi)) int_R P_hat(k)^3 dk.

Substituting the exact transform,

I_R2
 = (1/(2pi)) (pi^3/8) int_R sech^6(k/2) dk.

With u=k/2,

int_R sech^6(k/2) dk
 = 2 int_R sech^6 u du
 = 4 int_0^infty sech^6 u du.

The elementary antiderivative

H(u)=tanh u -(2/3)tanh^3 u +(1/5)tanh^5 u

satisfies

H'(u)=(1-tanh^2 u)^3=sech^6 u,

H(0)=0,
H(infinity)=1-2/3+1/5=8/15.

Therefore

int_0^infty sech^6 u du = 8/15,
int_R sech^6(k/2) dk = 32/15,

and hence

I_R2=(1/(2pi))(pi^3/8)(32/15)=2pi^2/15.

Thus a complete formal proof of the full-plane analytic input splits cleanly into two reusable theorems:

1. Fourier transform of P: P_hat(k)=pi/[2 cosh^2(k/2)];
2. half-line hyperbolic integral: int_0^infty sech^6 u du=8/15.

The second is directly accessible using the existing SechSquaredIntegral/SechFourthIntegral antiderivative infrastructure in GPPVerify2.
