# Riemann zeros as logarithmic resonances of the von-Mangoldt halo response

Date: 2026-09-26
Status: analytic derivation at explicit-formula/Mellin level; rigorous endpoint and distributional error control still required before promoting the bounded-remainder statement to an RH equivalence.

## 1. Starting response

The current finite-place gravitational-response candidate is

\[
\mathcal D(x)
=
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
F\!\left(\frac{2x}{\sqrt n}\right),
\qquad
F(y)=1-(1+y)e^{-y}.
\]

Equivalently, with the Chebyshev function
\[
\psi(u)=\sum_{n\le u}\Lambda(n),
\]
\[
\mathcal D(x)
=
\int_{2^-}^{\infty}
u^{-1/2}F(2x/\sqrt u)\,d\psi(u).
\]

The PNT term \(d\psi(u)\sim du\) gives the already-derived leading asymptotic

\[
\boxed{\mathcal D(x)\sim4x.}
\]

## 2. Mellin coefficient of a zero term

The explicit formula contains the formal zero contribution

\[
\psi_\rho(u)=-\frac{u^\rho}{\rho},
\]

so

\[
d\psi_\rho(u)=-u^{\rho-1}\,du.
\]

Its contribution to the smoothed half-density response is therefore

\[
\mathcal D_\rho(x)
=
-\int
u^{\rho-3/2}
F(2x/\sqrt u)\,du.
\]

After \(u=x^2v\),

\[
\mathcal D_\rho(x)
=
-x^{2\rho-1}M_F(\rho)
\]

with

\[
M_F(\rho)
=
\int_0^\infty
v^{\rho-3/2}F(2/\sqrt v)\,dv.
\]

Set \(y=2/\sqrt v\). Then

\[
M_F(\rho)
=
4^\rho
\int_0^\infty
y^{-2\rho}F(y)\,dy.
\]

Since \(F'(y)=ye^{-y}\), integration by parts gives

\[
\int_0^\infty y^{-2\rho}F(y)\,dy
=
\frac{\Gamma(3-2\rho)}{2\rho-1},
\]

initially in the absolutely convergent strip and then by analytic/oscillatory continuation where appropriate. Hence

\[
\boxed{
M_F(\rho)
=
4^\rho
\frac{\Gamma(3-2\rho)}{2\rho-1}.
}
\]

The Gamma function has no zeros, so this smoothing does not erase any nontrivial zero away from \(\rho=1/2\).

## 3. Critical zeros give log-periodic ripples

Under RH,

\[
\rho=\frac12+i\gamma,
\]

so

\[
x^{2\rho-1}=x^{2i\gamma}
=e^{2i\gamma\log x}.
\]

Therefore a conjugate zero pair contributes a real bounded oscillation in logarithmic radius:

\[
\boxed{
\mathcal D_{\gamma}(x)
=
-2\Re\!\left[
M_F(\tfrac12+i\gamma)
e^{2i\gamma\log x}
\right].
}
\]

Thus the zero ordinate \(\gamma\) becomes a log-radius resonance frequency \(2\gamma\).

The coefficient is

\[
M_F(\tfrac12+i\gamma)
=
4^{1/2+i\gamma}
\frac{\Gamma(2-2i\gamma)}{2i\gamma}.
\]

For large \(\gamma\),

\[
\boxed{
|M_F(\tfrac12+i\gamma)|
\sim
4\sqrt{\pi\gamma}\,e^{-\pi\gamma}.
}
\]

So the smooth complement kernel exponentially suppresses high-zero resonances.

## 4. Off-line zeros become anomalous power-law halo modes

For a hypothetical zero

\[
\rho=\frac12+\eta+i\gamma,
\qquad
\eta>0,
\]

the same term carries

\[
x^{2\rho-1}
=
x^{2\eta}e^{2i\gamma\log x}.
\]

Hence

\[
\boxed{
\text{horizontal zero displacement }\eta
\longleftrightarrow
\text{radial anomalous exponent }2\eta.
}
\]

This is the static-response counterpart of the previously derived off-axis Lyapunov exponent in logarithmic scale.

For the provisional force law

\[
a_{\rm hid}(r)
=
\alpha\frac{GM_b}{r^2}\mathcal D(M_*r),
\]

the PNT term gives

\[
a_{\rm hid}^{(0)}(r)\sim\frac{\mathrm{const}}r.
\]

A critical zero gives a correction of the form

\[
\boxed{
\delta a_\gamma(r)
\propto
\frac{
\cos(2\gamma\log(M_*r)+\phi_\gamma)
}{r^2},
}
\]

while an off-line zero gives

\[
\boxed{
\delta a_\rho(r)
\propto
r^{-2+2\eta}
\cos(2\gamma\log(M_*r)+\phi_\rho).
}
\]

So RH corresponds, in this response family, to the absence of anomalous positive radial powers in the zero-sector correction to \(\mathcal D(x)\).

## 5. Possible new smoothed RH criterion

Because the transform multiplier

\[
M_F(\rho)
=
4^\rho\Gamma(3-2\rho)/(2\rho-1)
\]

does not vanish at nontrivial zeros, it is plausible that a sufficiently sharp bounded-remainder statement

\[
\boxed{
\mathcal D(x)-4x=O(1)
}
\]

(or a closely related bounded/tempered statement after exact pole/trivial-zero counterterms) is equivalent to RH.

The forward direction is strongly suggested by the exponentially damped critical-line zero series. The converse is suggested because any zero with \(\Re\rho>1/2\) creates an \(x^{2\Re\rho-1}\) term.

This must be proved with the exact Riemann explicit formula, lower-end contributions, trivial zeros, pole terms, and possible multiplicities included. It is not yet recorded as a theorem.

## 6. Number-physics interpretation

The same arithmetic current now has three representations:

\[
\boxed{
\Lambda(n)n^{-1/2}
}
\]

is simultaneously

1. the generator weight of the prime modular/AFT flow;
2. the causal Dirichlet boundary-anomaly weight;
3. the spectral weight whose PNT continuum produces an isothermal \(1/r\) force response.

The Riemann zeros then control the fluctuations around the continuum law.

This gives a particularly sharp physical reading of the explicit formula:

\[
\boxed{
\text{primes determine the mean medium;}
\qquad
\text{zeros determine its coherent log-scale resonances.}
}
\]

That statement is exact at the arithmetic transform level; identifying the response with actual gravity remains conditional on deriving the AFT-to-metric coupling.
