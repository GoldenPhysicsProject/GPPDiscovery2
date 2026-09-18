# Prime-gas thermodynamics as a transverse Casimir mass product

Date: 2026-09-18

Status: exact algebraic/thermodynamic identities derived from the local prime Gibbs radius and the previously established Cayley-Casimir map. No RH proof is claimed.

## 1. Beta-dependent local hyperbolic coordinates

For the number Gibbs state at beta>1, the p-adic occupation law is geometric with amplitude radius

a_{p,beta}=p^{-beta/2}.

Define

kappa_{p,beta}=artanh(a_{p,beta}),
r_{p,beta}=e^{-2kappa_{p,beta}}=(1-a)/(1+a),

and the associated Casimir mass

mu_{p,beta}=2sinh(kappa_{p,beta}).

Then

mu_{p,beta}^2
=
4 a^2/(1-a^2)
=
4/(p^beta-1).

At beta=1 this reduces to mu_p^2=4/(p-1), and p=5 is exactly the unit-mass channel.

## 2. Mass squared equals four times mean prime occupancy

For the local geometric Gibbs law

P_beta(N_p=n)=(1-p^{-beta})p^{-n beta},

the mean occupation is

E_beta[N_p]=1/(p^beta-1).

Therefore

mu_{p,beta}^2=4 E_beta[N_p].

Summing over primes,

(1/4) sum_p mu_{p,beta}^2
=
E_beta[Omega(n)],

where Omega(n) is the number of prime factors of n counted with multiplicity.

The sum is finite for beta>1 and diverges at beta=1 because it is asymptotic to sum_p p^{-beta}. Thus the Hagedorn boundary is exactly where the total local Casimir mass-squared budget diverges through infinitely many channels with individual mu_p->0 as p->infinity.

This is a collective threshold: each large-prime channel becomes massless, while the aggregate transverse mass budget diverges.

## 3. Euler factors as local mass factors

The local Euler/partition factor is

Z_{p,beta}=1/(1-p^{-beta}).

Using the mass identity,

Z_{p,beta}=1+mu_{p,beta}^2/4.

Hence

zeta(beta)
=
product_p (1+mu_{p,beta}^2/4).

This is an exact rewriting of the Euler product.

## 4. Internal energy as a weighted transverse-mass sum

The standard number-gas internal energy is

U(beta)
=
-zeta'(beta)/zeta(beta)
=
sum_p log(p)/(p^beta-1).

Therefore

U(beta)
=
(1/4) sum_p mu_{p,beta}^2 log p.

Thus the arithmetic internal energy is exactly the log-prime-weighted total of local Casimir mass squares.

The local entropy likewise becomes

S_{p,beta}
=
log(1+mu_{p,beta}^2/4)
+
(beta/4) mu_{p,beta}^2 log p,

and summing over p gives the global number entropy.

## 5. Important distinction between the two geometric laws

There are two geometric parameters in the current synthesis:

A. prime-gas/Poisson radius
a=p^{-beta/2},
whose squared amplitudes give the Euler Gibbs law and whose local partition is
Z_p=1/(1-a^2)=1+mu^2/4;

B. Cayley/causal radius
r=(1-a)/(1+a)=e^{-2kappa},
whose normalized causal Green coefficients are
(1-r)r^n.

At p=5, beta=1, r=phi^{-2}; the causal Green partition 1/(1-r)=phi is not the same object as the local Euler partition Z_5=5/4. Previous references to a 'one-sided oscillator partition Z_phi=phi' refer to the Cayley/causal law, not the original prime-gas Euler law.

## 6. Relation to Which Way Is Forward

The orientation paper identifies physical mass as a transverse norm in its doubled Klein/Clifford factorization. The identities above show that, on the arithmetic/Hardy side, each local prime Gibbs channel has a canonical transverse Casimir mass mu_{p,beta}. This is an exact internal dictionary on the arithmetic side.

No theorem yet identifies the physical transverse momentum norm |q| of the doubled Lorentzian model with mu_{p,beta}. A genuine unification requires an intertwiner.

## 7. RH relevance

The beta=1 Hagedorn point is simultaneously:
- the critical half-density local law a_p=p^{-1/2};
- the profinite boundary law forced by any dual RH ghost;
- the point where total expected prime occupation diverges;
- the point where sum_p mu_p^2 diverges, even though mu_p->0 prime-by-prime.

This clarifies the global threshold mechanism as an infinite accumulation of local massless channels. Whether the prime-Archimedean completion excludes the resulting boundary representation remains the no-escape theorem to prove.
