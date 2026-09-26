# TFD covariance completion and the origin of the two RH boundary channels

Date: 2026-09-26
Status: exact local covariance algebra plus a global interpretation target. No RH proof.

Let r in (0,1) be a half-density amplitude. Define

C(r)=r^2/(1-r^2),
A(r)=r/(1-r^2).

For a prime mode r_p=p^(-1/2), C_p=1/(p-1) and A_p=sqrt(p)/(p-1).

The Euler geometric resolvent splits exactly as

x/(1-x)=x/(1-x^2)+x^2/(1-x^2).

At real half-density x=r this says the odd repetition channel is A(r) and the even repetition channel is C(r).

## Normal ordering produces the local ghost

The normal-ordered two-mode covariance matrix is

Gamma_NO(r) = [[C,A],[A,C]].

Its determinant is

det Gamma_NO = C^2-A^2 = -C < 0.

Thus its indefiniteness is not mysterious: it is exactly what results when the vacuum half-quantum is removed from a pure squeezed covariance.

Restore the canonical vacuum term:

Gamma(r) = [[C+1/2,A],[A,C+1/2]].

Then

det Gamma = 1/4.

The two ordinary eigenvalues are

lambda_- = C+1/2-A = (1-r)/(2(1+r)),

lambda_+ = C+1/2+A = (1+r)/(2(1-r)),

and

lambda_- lambda_+ = 1/4.

So the full local TFD covariance is positive and pure, while its normal-ordered part is a Krein/ghost form.

## Exact Cayley identification

Define the Cayley contraction

q_Cayley(r)=(1-r)/(1+r).

Then

lambda_- = q_Cayley/2,
lambda_+ = 1/(2 q_Cayley).

For a prime half-density r=p^(-1/2),

q_Cayley = (sqrt(p)-1)/(sqrt(p)+1),

which is exactly the finite-place Cayley coordinate already used in the arithmetic conformal construction.

With r=tanh(kappa),

q_Cayley=e^(-2 kappa),

hence the covariance eigenvalues are

lambda_± = (1/2)e^(±2 kappa).

At p=5, kappa=log(phi), so

lambda_- = phi^(-2)/2,
lambda_+ = phi^2/2.

This is an exact identification of the p-adic Cayley coordinate with the squeezed-quadrature anisotropy of the local modular TFD state.

## Mass-entanglement identity

Since

mu^2=4C=4 sinh^2(kappa),

and

tr Gamma = 1+2C = cosh(2 kappa),

we have

mu^2 = 2(tr Gamma - 1).

Thus the finite-place mass-square coordinate is exactly the excess covariance above the pure vacuum baseline.

This is a precise local sense in which the arithmetic mass coordinate measures entanglement/squeezing rather than an independently inserted mass number.

## Why this matters for the RH ghost

The completed RH boundary object is a signed prime-Archimedean form. Local prime OS/TFD sectors are positive before normal ordering, yet the prime current entering the explicit formula is a vacuum-subtracted/relative object. The calculation above shows that this subtraction creates an indefinite local two-channel form automatically.

Therefore a plausible interpretation of the missing Archimedean completion is:

the real place is the renormalized vacuum completion that restores positivity after the infinite arithmetic half-quanta are subtracted.

This is only a structural interpretation at present. A literal sum of 1/2 over primes diverges and cannot be used. The required completion must be the already isolated zeta-regularized/Archimedean boundary distribution, not an unrenormalized diagonal shift.

## Archimedean channel uses the same covariance law

For E=2 pi lambda, let

C_infty(E)=1/(e^E-1),
A_infty(E)=sqrt(C_infty(1+C_infty))=1/(2 sinh(E/2)).

Then the celestial principal-series weight is

P(lambda)=pi lambda/sinh(pi lambda)
         = E A_infty(E).

So the real-place thermal spectral weight is modular energy times the same anomalous covariance function that resums the odd finite-place repetition channel.

This makes the two-channel Archimedean completion problem considerably more rigid:

- finite m=1 channel: anomalous TFD covariance;
- finite m=2 channel: normal TFD covariance;
- m>=3: Schatten/Fock bulk already controlled;
- real place: continuum anomalous covariance with the same universal function.

The missing global theorem is therefore a renormalized vacuum-completion/sewing theorem, not a search for arbitrary positive weights.

## Formalization

The local identities have been added to
GppVerify/RiemannHypothesis/PrimeModularCovariance.lean
on branch codex/rh-boundary-closure.

They include:
- C_p=1/(p-1);
- mu_p^2=4C_p;
- A^2=C(1+C);
- odd/even repetition split;
- det Gamma_NO=-C;
- det Gamma=1/4;
- exact Cayley eigenvalues.

No claim is made yet that the branch builds under Lean 4.33.1; the repository-wide migration build remains separately unresolved.
