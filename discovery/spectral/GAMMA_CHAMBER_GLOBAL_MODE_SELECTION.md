# Gamma chamber global mode selection

The certified adjacent chamber recurrence has real step factor

\[
r_k(x)=\frac{2((k+1)^2+x^2)}{(k+1)(2k+3)},
\]

with exact sign trichotomy

\[
r_k(x)>1\iff k+1<2x^2,
\quad
r_k(x)=1\iff k+1=2x^2,
\quad
r_k(x)<1\iff 2x^2<k+1.
\]

Therefore any positive chamber sequence satisfying `rho_{k+1}=r_k rho_k` is globally unimodal. Put `a=2x^2`.

- If `a` is not a positive integer, the unique maximum occurs at `k=floor(a)`.
- If `a=n` is a positive integer, `rho_{n-1}=rho_n` and these two adjacent chambers are the only global maxima.
- If `a=0`, `k=0` is the unique maximum and the sequence strictly decreases afterward.

No convolution hypothesis is used. This is purely the exact Gamma recurrence plus positivity of every chamber.

Formalization target: state the result first for an abstract positive sequence with the certified step-factor recurrence, then instantiate it for the normalized Gamma/Wiener--Hopf chamber density once the real-valued positivity bridge is in scope.
