# Non-Fourier moment hierarchy from the normalized Gamma recurrence

Let

\[
\rho_m(x)=\frac{2^{2m-1}}{\pi\Gamma(2m)}\,|\Gamma(m+ix)|^2,
\qquad m\ge1,
\]

and suppose only the already established normalization \(\int\rho_m=1\). The Gamma recurrence gives

\[
\rho_{m+1}(x)=\frac{2(m^2+x^2)}{m(2m+1)}\rho_m(x).
\]

For even raw moments

\[
M_{m,n}:=\int_{\mathbb R}x^{2n}\rho_m(x)\,dx,
\]

this implies the exact recurrence

\[
\boxed{
M_{m,n+1}
=\frac{m(2m+1)}2\,M_{m+1,n}-m^2M_{m,n}.
}
\]

No Fourier transform is used.

Starting from \(M_{m,0}=1\), the first moments follow algebraically:

\[
\boxed{M_{m,1}=\frac m2},
\]

\[
\boxed{M_{m,2}=\frac{3m^2+m}{4}},
\]

\[
\boxed{M_{m,3}=\frac{m(15m^2+15m+4)}8}.
\]

Therefore

\[
\kappa_2=\frac m2,
\qquad
\kappa_4=M_{m,2}-3M_{m,1}^2=\frac m4,
\]

and

\[
\kappa_6=M_{m,3}-15M_{m,2}M_{m,1}+30M_{m,1}^3=\frac m2.
\]

Thus the first three nonzero cumulants of the convolution family can be recovered from normalization plus the Gamma recursion alone, independently of the transform identity
\(\widehat\rho_m=\operatorname{sech}^{2m}(k/2)\).

This gives a second formalization path: establish the normalized Gamma-family recurrence first, then derive finite moment/cumulant identities using integration linearity and normalization, postponing the full Fourier/Beta integral bridge.
