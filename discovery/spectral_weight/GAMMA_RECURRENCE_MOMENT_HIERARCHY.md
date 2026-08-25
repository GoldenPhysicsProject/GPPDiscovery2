# Gamma recurrence and a non-Fourier moment hierarchy for rho_m

Codex/GPT discovery track, 2026-08-25.

Start from the normalized convolution-family density

rho_m(x)
 = 2^(2m-1)/(pi Gamma(2m)) |Gamma(m+i x)|^2,
 m>=1.

The one-step Gamma recurrence gives

|Gamma(m+1+i x)|^2
 = (m^2+x^2)|Gamma(m+i x)|^2.

Using Gamma(2m+2)=(2m+1)(2m)Gamma(2m), the normalized densities therefore satisfy the exact recursion

boxed:

rho_{m+1}(x)
 = [2(m^2+x^2)/(m(2m+1))] rho_m(x).

This is equivalent to the polynomial chamber/gluing formula but is particularly useful for moments because it requires no Fourier transform.

## Variance from normalization alone

Let

M_{m,n}=int_R x^(2n) rho_m(x) dx.

Since every rho_m has unit mass, M_{m,0}=1. Integrating the density recursion gives

1
 = 2/[m(2m+1)] [m^2 + M_{m,1}].

Hence

boxed:

M_{m,1}=m/2.

Because rho_m is even, its mean vanishes, so

boxed:

Var(rho_m)=m/2.

Thus the variance law can be derived from Gamma recurrence plus normalization, independently of the characteristic-function calculation.

## Full even-moment recursion

Multiply the density recursion by x^(2n) and integrate:

M_{m+1,n}
 = 2/[m(2m+1)] [m^2 M_{m,n}+M_{m,n+1}].

Equivalently,

boxed:

M_{m,n+1}
 = [m(2m+1)/2] M_{m+1,n} - m^2 M_{m,n}.

This supplies an algebraic triangular recursion for all even moments once one row/column of the hierarchy is known.

For n=0 it reproduces M_{m,1}=m/2 immediately.

## Relation to the convolution semigroup

The Fourier statement

rho_{m+n}=rho_m * rho_n

implies additivity of cumulants. The recurrence above is independent of that Fourier input and therefore provides a useful cross-check and a more Lean-friendly route to low moments. In particular, the variance law m/2 can be formalized before the logistic/Beta Fourier bridge is complete.
