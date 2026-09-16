# Theta-deficit / Nyman / Casimir bridge — 2026-09-15

Status: exact derivations plus explicit topological and positivity obstructions. No RH proof claimed.

## 1. Canonical Casimir variable

Use

\[
u=s(s-1),\qquad s=\frac{1+\sqrt{1+4u}}2\quad(s>1\text{ for }u>0).
\]

For a nontrivial zero \(\rho=\beta+i\gamma\), the shadow-invariant folded spectral parameter is

\[
t_\rho=\rho(1-\rho)=\beta(1-\beta)+\gamma^2+i\gamma(1-2\beta).
\]

Thus \(\Re t_\rho>0\) in the critical strip and, since \(\gamma\neq0\),

\[
\Im t_\rho=0\iff \beta=\tfrac12.
\]

This is the canonical translation of the earlier safe fold:

\[
1-(\rho-\tfrac12)^2=t_\rho+\tfrac34.
\]

It does not add spectral information, but it aligns the fold with the functional equation, the \(sl_2\) Casimir, and the completion factor. Unlike the earlier mass-one choice, \(u>0\) now corresponds exactly to the full Euler half-plane \(s>1\).

For

\[
m_C(u)=\frac1{2s-1}\frac{\xi'}\xi(s)=\frac{d}{du}\log \xi(s(u)),
\]

the two elementary logarithmic-derivative terms collapse exactly:

\[
\frac1{2s-1}\left(\frac1s+\frac1{s-1}\right)=\frac1u.
\]

Hence in \(\phi_C(u)=u m_C(u)\) their isolated contribution is the constant \(1\), whose Loewner divided-difference kernel is zero. This is a coordinate simplification only: near \(u=0\) the zeta pole still cancels the \(1/u\) singularity globally, and no RH conclusion follows from this bookkeeping identity alone.

## 2. Theta Ward identity in Casimir form

Let

\[
\vartheta(y)=\sum_{n\in\mathbb Z}e^{-\pi n^2y},\qquad
K(x)=\vartheta(e^{2x})-1,
\]

and

\[
h(x)=e^{x/2}K(x).
\]

The exact theta Ward identity already established in the arithmetic principal-series manuscript gives

\[
\Phi(x)=\frac12 e^{x/2}(D+1)DK(x)
       =\frac12\left(h''(x)-\frac14h(x)\right),
\]

where \(\Xi(z)=2\int_0^\infty\Phi(x)\cos(zx)\,dx\).

Theta inversion gives \(\vartheta'(1)=-\vartheta(1)/4\). Since

\[
K'(0)=2\vartheta'(1)=-\frac12\vartheta(1),
\]

we obtain the exact boundary datum

\[
h'(0)=\frac12K(0)+K'(0)=-\frac12.
\]

Integrating the Riemann cosine formula twice by parts therefore gives

\[
\Xi(z)=\left(z^2+\frac14\right)
\int_0^\infty g(x)\cos(zx)\,dx,
\]

throughout the strip where the latter integral converges, with

\[
\boxed{g(x)=e^{-x/2}-e^{x/2}\bigl(\vartheta(e^{2x})-1\bigr).}
\]

The apparent poles at \(z=\pm i/2\) belong to the quotient representation \(\Xi(z)/(z^2+1/4)\), not to \(\Xi\).

## 3. Strict positivity and evenness of the theta-deficit kernel

For \(x\ge0\), put \(y=e^x\ge1\). Then

\[
\vartheta(y^2)-1=2\sum_{n\ge1}e^{-\pi n^2y^2}.
\]

Because \(t\mapsto e^{-\pi y^2t^2}\) is strictly decreasing on \((0,\infty)\),

\[
\sum_{n\ge1}e^{-\pi n^2y^2}
<\int_0^\infty e^{-\pi y^2t^2}\,dt
=\frac1{2y}.
\]

Therefore

\[
0<g(x)=y^{-1/2}-y^{1/2}(\vartheta(y^2)-1),\qquad x\ge0.
\]

Theta inversion

\[
\vartheta(e^{-2x})=e^x\vartheta(e^{2x})
\]

implies that the same formula extends evenly:

\[
g(-x)=g(x).
\]

Thus \(\Xi(z)/(z^2+1/4)\) is the cosine/Fourier transform, in the critical strip \(|\Im z|<1/2\), of an explicit strictly positive even kernel. Positivity alone is not claimed to force real zeros.

## 4. Continuum-minus-lattice and fractional-part representation

Again with \(y=e^x\),

\[
g(x)=2y^{1/2}\left[
\int_0^\infty e^{-\pi y^2t^2}\,dt
-\sum_{n\ge1}e^{-\pi y^2n^2}
\right].
\]

For any positive decreasing \(C^1\) function \(f\) with sufficient decay,

\[
\int_0^\infty f(t)\,dt-\sum_{n\ge1}f(n)
=\int_0^\infty \{t\}\,[-f'(t)]\,dt.
\]

Applying this to \(f(t)=e^{-\pi y^2t^2}\) gives the exact positive representation

\[
\boxed{
 g(x)=4\pi e^{5x/2}\int_0^\infty \{t\}\,t\,e^{-\pi e^{2x}t^2}\,dt.
}
\]

So the positive theta-deficit kernel is a Gaussian transform of the same fractional-part datum that generates the Nyman-Beurling space.

## 5. The Gaussian completion operator and its zero-free Mellin symbol

Define, initially on suitable functions,

\[
(Tf)(x)=4\pi e^{5x/2}\int_0^\infty f(t)t e^{-\pi e^{2x}t^2}\,dt.
\]

Then \(T\{t\}=g(x)\). Direct Mellin calculation gives

\[
\boxed{
\mathcal M_x(Tf)(s)=
2\pi^{-s/2-1/4}\Gamma\!\left(\frac{s}{2}+\frac54\right)
\mathcal M_t f\!\left(-s-\frac12\right).
}
\]

The Gamma multiplier has no zeros.

For \(f(t)=\{t\}\), use

\[
\int_0^\infty \{t\}t^{-\sigma-1}\,dt=-\frac{\zeta(\sigma)}{\sigma},
\qquad 0<\Re\sigma<1.
\]

With \(\sigma=s+1/2\) and \(\Gamma(1+\sigma/2)=(\sigma/2)\Gamma(\sigma/2)\), this simplifies to

\[
\boxed{
\mathcal M g(s)=
-\pi^{-(s+1/2)/2}\Gamma\!\left(\frac{s+1/2}{2}\right)
\zeta\!\left(s+\frac12\right).
}
\]

This is the completed zeta multiplier, shifted to the centered Mellin variable. Hence \(T\) preserves the bad-zero divisor and adds only a zero-free Archimedean factor.

## 6. Exact intertwining of Nyman generators

For \(0<\lambda\le1\), define the inverted Nyman generator

\[
f_\lambda(t)=\{\lambda t\}-\lambda\{t\}.
\]

For \(0<t<1\), both fractional parts are linear and \(f_\lambda(t)=0\), so this is exactly supported on the inverted Nyman half-line.

Scaling in the Gaussian transform gives

\[
T\{\lambda t\}(x)=\sqrt\lambda\,g(x-\log\lambda).
\]

Therefore

\[
\boxed{
Tf_\lambda(x)
=\sqrt\lambda\,g(x-\log\lambda)-\lambda g(x).
}
\]

Thus the Nyman fractional-part complex is mapped explicitly to half-density translation differences of the positive theta-deficit kernel.

## 7. Image of the Nyman target vector

Under inversion \(x\mapsto t=1/x\), the Nyman target constant \(1\in L^2(0,1)\) becomes \(f_0(t)=1_{(1,\infty)}(t)\) in \(L^2((1,\infty),t^{-2}dt)\). Its Gaussian image is elementary:

\[
Tf_0(x)
=4\pi e^{5x/2}\int_1^\infty t e^{-\pi e^{2x}t^2}\,dt
=2e^{x/2}e^{-\pi e^{2x}}.
\]

So the Nyman target maps to the first Archimedean theta seed.

## 8. Exact topology obstruction

The source Nyman norm becomes

\[
\|f\|^2=\int_1^\infty |f(t)|^2\frac{dt}{t^2}.
\]

Writing \(t=e^u\) and \(F(u)=e^{-u/2}f(e^u)\) identifies it with ordinary \(L^2(0,\infty,du)\). In these variables

\[
(Tf)(x)=\int_0^\infty F(u)\,\kappa(x+u)\,du,
\qquad
\kappa(v)=4\pi e^{5v/2}e^{-\pi e^{2v}}.
\]

On the full logarithmic line the corresponding reflection-convolution multiplier is the same Gamma factor above. By Stirling asymptotics its modulus decays exponentially along vertical frequency. Therefore \(T\) is injective (zero-free symbol) but is not bounded below in ordinary \(L^2\): high-frequency packets can have unit source norm and exponentially small image norm.

Consequences:

1. Ordinary Gaussian completion can erase the Nyman defect in norm even though it preserves it analytically.
2. A bounded chain equivalence cannot use the ordinary target \(L^2\) norm.
3. The natural exact candidate graph norm is the pullback/inverse-Gamma norm
   \[
   \|Tf\|_{\mathrm{graph}}:=\|f\|_{\mathrm{Nyman}},
   \]
   equivalently a Fourier norm weighted by the reciprocal squared Gamma multiplier.
4. This topology preserves the Nyman cokernel by construction, but by itself does not prove its vanishing. Additional positivity/coercivity must come from the completed shadow/co-Poisson structure, not merely from Gaussian smoothing.

## 9. Möbius isolation identity and where RH-strength convergence lives

For \(\lambda=1/m\), the image generator is

\[
G_m(x)=m^{-1/2}g(x+\log m)-m^{-1}g(x).
\]

Expanding the lattice part in the first theta seed shows that the coefficients \(c_m=-\mu(m)\) for \(m\ge2\) have the exact divisor-isolation property

\[
\sum_{\substack{m\mid n\\m\ge2}}(-\mu(m))=1\qquad(n>1).
\]

Formally, together with \(-\sum_{m\ge2}\mu(m)/m=1\), this isolates the first theta seed from the translation-difference family. The scalar identity \(\sum\mu(m)/m=0\) is PNT-level and unconditional, but convergence in the **Nyman/pullback graph norm** is exactly the hard global issue; ordinary smoothed convergence would not suffice.

## 10. First-order Gamma / Casimir factorization

Define the centered Archimedean outer factor

\[
B(q)=\pi^{-(q+1/2)/2}\Gamma\!\left(\frac{q+1/2}{2}\right).
\]

The co-Poisson scattering phase is exactly its reflected quotient:

\[
\boxed{
\chi_\infty\!\left(\frac12+q\right)=\frac{B(q)}{B(-q)}.
}
\]

The Gaussian-completion multiplier factors as

\[
2\pi^{-q/2-1/4}\Gamma\!\left(\frac q2+\frac54\right)
=(q+\tfrac12)B(q).
\]

On the logarithmic line put

\[
Q=D+\frac12,\qquad Q^*=-D+\frac12.
\]

Then

\[
\boxed{Q^*Q=-D^2+\frac14=:H_C.}
\]

For the first theta seed

\[
k_0(x)=2e^{x/2}e^{-\pi e^{2x}},
\]

one has the exact first-order identity

\[
\boxed{Q^*k_0(x)=4\pi e^{5x/2}e^{-\pi e^{2x}}=\kappa(x).}
\]

Thus the Nyman Gaussian completion is one first-order massive Casimir factor times the Archimedean outer Gamma factor. The same factorization appears in the co-Poisson phase through \(B(q)/B(-q)\). This is structural alignment, not a no-ghost theorem: any zero-free scalar multiplier alone leaves the Hardy bad-zero divisor unchanged.

## 11. The new primitive cancels the old theta boundary delta exactly

The manuscript's right-decaying Jacobi seed is

\[
\beta(x)=\sum_{n\ge1}e^{x/2-\pi n^2e^{2x}},
\qquad \Phi=(D^2-\tfrac14)\beta.
\]

Its even reflection \(\beta_{\rm e}(x)=\beta(|x|)\) has a cusp and obeys distributionally

\[
(D^2-\tfrac14)\beta_{\rm e}=\Phi-\frac12\delta_0.
\]

But the new theta-deficit kernel satisfies exactly

\[
\boxed{g(x)=e^{-|x|/2}-2\beta_{\rm e}(x).}
\]

For \(H_C=-D^2+1/4\),

\[
H_Ce^{-|x|/2}=\delta_0,
\qquad
H_C\beta_{\rm e}=\frac12\delta_0-\Phi.
\]

Therefore the singular boundary charges cancel before any parity split:

\[
\boxed{H_Cg=2\Phi}
\]

as a full-line distribution, with no delta source.  Equivalently, wherever ordinary derivatives are valid,

\[
\Phi=\frac12H_Cg.
\]

This reopens integration-by-parts manipulations that were invalid for the cusped primitive \(\beta_{\rm e}\), but it does not by itself establish positivity of the endpoint kernel.

## 12. The positive kernel is exactly the poleful completed zeta kernel

Put \(s=1/2+iz\). Since

\[
\xi(s)=\frac12s(s-1)\Lambda(s),
\qquad
s(s-1)=-(z^2+1/4),
\]

and

\[
\Xi(z)=\frac{z^2+1/4}{2}\,\widehat g(z)
\]

for the full-line Fourier transform, one gets

\[
\boxed{
\widehat g(z)=-\Lambda\!\left(\frac12+iz\right).
}
\]

Thus \(g\) is not an auxiliary smoothing kernel. It is the exact positive even Fourier kernel of the completed zeta function before the boundary polynomial \(s(s-1)\) removes the poles at \(s=0,1\). The hierarchy is

\[
\Lambda\xrightarrow{\;s(s-1)\;}\xi
\xrightarrow{\;\log\partial\;}\text{Weil/Nevanlinna data}.
\]

The two elementary pole terms in \(\xi'/\xi\) are exactly the logarithmic derivatives of this boundary polynomial.

## 13. Endpoint Bezoutian product rule and rank-one parity correction

Let

\[
p(z)=z^2+c^2,
\qquad G(z)=p(z)R(z).
\]

For the real-axis Laguerre Bezoutian

\[
\mathcal D_F(z,w)=2\frac{F(z)F'(w)-F'(z)F(w)}{z-w},
\]

direct algebra gives

\[
\boxed{
\mathcal D_G(z,w)
=p(z)p(w)\mathcal D_R(z,w)
+4(zw-c^2)R(z)R(w).
}
\]

For the Riemann case \(c=1/2\), \(G=\Xi\), and \(R=\widehat g/2\). If for an even real density \(f\) one writes the universal endpoint coordinate kernel

\[
K_f(a,b)=\frac12\int_{|(a+b)/2|}^\infty
 y\,f\!\left(y+\frac{a-b}{2}\right)
 f\!\left(y-\frac{a-b}{2}\right)\,dy,
\]

then the manuscript's Fourier normalization is \(\mathcal D_{\widehat f}=8\,\mathcal F_2K_f\). Consequently the product identity gives the exact coordinate formula

\[
\boxed{
K_\Phi(a,b)
=\frac14 H_{C,a}H_{C,b}K_g(a,b)
+\frac18\left(g'(a)g'(b)-\frac14g(a)g(b)\right),
}
\]

where \(H_C=-D^2+1/4\) acts in the indicated variable.

For \(a,b>0\) define the parity kernels

\[
K_f^\pm(a,b)=K_f(a,b)\pm K_f(a,-b).
\]

Since \(g\) is even and \(g'\) odd, the correction splits into two rank-one pieces:

\[
\boxed{
K_\Phi^+(a,b)
=\frac14H_{C,a}H_{C,b}K_g^+(a,b)
-\frac1{16}g(a)g(b),
}
\]

and

\[
\boxed{
K_\Phi^-(a,b)
=\frac14H_{C,a}H_{C,b}K_g^-(a,b)
+\frac14g'(a)g'(b).
}
\]

Because the manuscript proves that positivity of either \(K_\Phi^+\) or \(K_\Phi^-\) is individually equivalent to RH, the even route becomes the sharp rank-one domination problem

\[
\boxed{
H_{C,a}H_{C,b}K_g^+(a,b)\succeq\frac14g(a)g(b).
}
\]

This is an exact reformulation, not yet a proof.  The odd route is the exact rank-one compensation problem

\[
H_{C,a}H_{C,b}K_g^-(a,b)+g'(a)g'(b)\succeq0.
\]

Numerical spot checks made during this derivation showed the raw \(K_g^+\) matrices positive in the tested samples while \(K_g^-\) had a dominant negative direction, but those observations are only exploratory.  In fact the frequency-side squared-variable factorization shows that positivity of the appropriate \(g\)-kernel can itself retain RH-strength zero information, so no sign theorem for \(K_g^\pm\) is assumed here.

## 14. No-go checks made during this attack

Two tempting strengthenings were tested and rejected:

1. The positive continuum-minus-lattice error defining \(g\) is not completely monotone in its natural heat variable; higher alternating derivatives change sign. Therefore positivity of the quadrature error does not automatically produce a Stieltjes measure.
2. The endpoint kernel built from \(g\) is not automatically PSD merely because \(g>0\). Numerical tests of the full raw kernel exhibited a negative eigenvalue. Thus the new primitive removes the singular boundary source but does not trivialize the Laguerre/Nevanlinna positivity problem.

These failures are useful because they isolate what the new representation really buys: exact source cancellation, a zero-free chain map, and a rank-one endpoint reduction, not a generic positivity theorem.

## 15. Current frontier

The most concrete new candidates for the missing global closure are now:

1. **Endpoint rank-one domination:** prove
   \[
   H_{C,a}H_{C,b}K_g^+\succeq\frac14g\otimes g
   \]
   directly from the theta/fractional-part structure. This is exactly RH-equivalent but has only one explicit rank-one deficit after Casimir congruence.
2. **Nyman graph completion:** use the explicit zero-free Gaussian/Gamma map \(T\) to transport the exact Nyman/Tate complex into the theta representation, but retain the inverse-Gamma graph topology so the bad-zero cokernel cannot escape.
3. **Shadow doubling:** exploit the exact outer-factor relation \(B(q)/B(-q)=\chi_\infty(1/2+q)\). A successful doubled norm must cancel the noncoercive outer amplitude without using a zero-dependent inner factor; scalar multiplication alone cannot do this.
4. **Multiscale stabilization:** a single Gamma smoothing is injective but not bounded below. A scale family may form a Littlewood--Paley/Calderon frame, but componentwise smoothed density is insufficient unless one obtains a single arithmetic approximation synchronized across scales. That synchronization is another concrete form of the global no-escape theorem.

No claim is made that any of these final coercive estimates has been proved.