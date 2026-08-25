# Collapsed Mehler-Fock spectral moments

Codex/GPT discovery track, 2026-08-25.

For the exact collapsed density

q(lambda) = pi lambda^2 / cosh(pi lambda),

the even moments are closed by the Dirichlet beta function. Using

sech(pi x)=2 sum_{n>=0} (-1)^n exp(-(2n+1) pi x),

and termwise integration on x>0,

int_0^infty x^N sech(pi x) dx
 = 2 N! / pi^(N+1) * beta(N+1).

Therefore, for m>=0,

int_R lambda^(2m) q(lambda) dlambda
 = 4 (2m+2)! beta(2m+3) / pi^(2m+2).

In particular the total mass is

int_R q(lambda) dlambda = pi/4,

because beta(3)=pi^3/32.

Hence the normalized probability density

rho_q(lambda)=(4/pi) q(lambda)

has moments

E[lambda^(2m)]
 = 16 (2m+2)! beta(2m+3) / pi^(2m+3).

The first values are

E[1]=1,
E[lambda^2]=5/4,
E[lambda^4]=61/16.

This is a separate normalized spectral law from rho(lambda)=2 lambda/sinh(pi lambda); the two should not be conflated. The result is harmonic-analysis data, not an amplitude theorem.
