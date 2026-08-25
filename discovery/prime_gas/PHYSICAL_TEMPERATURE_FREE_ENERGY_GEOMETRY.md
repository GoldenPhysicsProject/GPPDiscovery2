# Zeta prime gas: physical-temperature free-energy geometry

For the canonical zeta gas, with

\[
\beta=1/T>1,\qquad Z(\beta)=\zeta(\beta),\qquad
\Psi(\beta)=\log Z(\beta),
\]

write

\[
E=-\Psi'(\beta),\qquad
g=\Psi''(\beta)=\operatorname{Var}_\beta(\log n)>0,
\]

and

\[
C(T)=\frac{dE}{dT}=\beta^2g(\beta)>0.
\]

The Helmholtz free energy is

\[
F(T)=-T\log Z(1/T)=-T\Psi(\beta).
\]

The canonical identities give

\[
\boxed{\frac{dF}{dT}=-S},
\]

and therefore

\[
\boxed{
\frac{d^2F}{dT^2}
=-\frac{dS}{dT}
=-\frac{C(T)}{T}
=-\beta^3 g(\beta)<0.
}
\]

Thus the zeta-gas Helmholtz free energy is strictly concave as a function of physical temperature throughout the entire convergence phase \(0<T<1\). Equivalently,

\[
\boxed{
\frac{dS}{dT}=\frac{C}{T}=\beta^3g>0.
}
\]

This is the physical-temperature counterpart of

\[
S'(\beta)=-\beta g<0.
\]

The Fisher line element may be rewritten as

\[
d\tau=\sqrt g\,d\beta=-\frac{\sqrt C}{T}\,dT,
\]

so its magnitude is

\[
\boxed{|d\tau|=\frac{\sqrt C}{T}\,dT.}
\]

Near the Hagedorn-like boundary \(T\to1^-\), since

\[
\beta-1=\frac{1-T}{T},\qquad
g(\beta)\sim\frac1{(\beta-1)^2},
\]

one obtains

\[
\boxed{C(T)\sim\frac1{(1-T)^2}},
\]

and hence

\[
\left|\frac{d\tau}{dT}\right|
\sim\frac1{T(1-T)}.
\]

Therefore the critical boundary remains at infinite Fisher distance, with logarithmic distance divergence, while the heat capacity diverges quadratically.

For the entropy,

\[
S(\beta)=\frac{\beta}{\beta-1}-\log(\beta-1)+O(1)
\]

becomes

\[
\boxed{
S(T)=\frac1{1-T}-\log(1-T)+O(1)
}
\]

as \(T\to1^-\) (the regular \(\log T\) contribution is absorbed in \(O(1)\)).

These statements require only the absolutely convergent zeta Gibbs phase \(\beta>1\); no analytic continuation or RH input is used.
