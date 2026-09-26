# Von Mangoldt half-density tower and an isothermal dark-halo asymptotic

Date: 2026-09-26

Status: exact number-theoretic asymptotic for a specific renormalized static-response ansatz. This is **not** yet a derived dark-matter theory. The gravitational coupling kernel and relativistic completion remain to be derived.

## 1. Input from the arithmetic-shadow program

The completed prime current already carries the positive half-density weight

\[
\frac{\Lambda(n)}{\sqrt n},
\]

with \(n=p^k\).  The finite-place transfer-mass coordinate is

\[
\mu_q=\frac{2}{\sqrt{q-1}}.
\]

For the infrared asymptotic the distinction between \(q=n\) and \(q=n-1\) is subleading, so introduce a physical inverse-length scale \(M_*>0\) and the model mass

\[
m_n=\frac{2M_*}{\sqrt n}.
\]

This assignment is an ansatz for the static gravitational response.  It is motivated by the exact finite-place mass coordinate, but the identification of \(\mu_q\) with a physical 4D mediator mass is not yet established.

## 2. Minimal convergent complement kernel

A raw positive Yukawa sum with weights \(\Lambda(n)n^{-1/2}\) is divergent because infinitely many finite-place modes accumulate at zero mass.  The first force-level subtraction that removes the universal massless piece is

\[
F(y):=1-(1+y)e^{-y}.
\]

It has

\[
F(0)=F'(0)=0,\qquad
F'(y)=ye^{-y}\ge0,
\]

and therefore

\[
0\le F(y)\le \min\{1,y^2/2\}.
\]

Define the dimensionless completed hidden response

\[
\boxed{
\mathcal D(x)
=
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
F\!\left(\frac{2x}{\sqrt n}\right).
}
\]

For every fixed \(x\), the series converges absolutely.  Indeed, for large \(n\),

\[
F\!\left(\frac{2x}{\sqrt n}\right)
\le
\frac{2x^2}{n},
\]

so the tail is dominated by

\[
2x^2\sum_n\frac{\Lambda(n)}{n^{3/2}}<\infty.
\]

The positive kernel \(F\) should be interpreted as a finite-place **complement response**, not as an ordinary positive Yukawa exchange.  Ordinary massive exchange is strongest at short distance and cannot by itself generate a dark-halo enhancement at large radius.  A derivation from the project's doubled Schur/Krein boundary system is therefore essential.

## 3. Exact asymptotic theorem from the prime number theorem

Let

\[
\psi(u)=\sum_{n\le u}\Lambda(n).
\]

The prime number theorem is

\[
\psi(u)\sim u.
\]

Write the response as the Stieltjes integral

\[
\mathcal D(x)
=
\int_{2^-}^{\infty}
u^{-1/2}
F(2x/\sqrt u)\,d\psi(u).
\]

Scale \(u=x^2v\).  The PNT and the integrable majorant supplied by

\[
F(y)\le\min(1,y^2/2)
\]

give

\[
\frac{\mathcal D(x)}{x}
\longrightarrow
\int_0^\infty
v^{-1/2}F(2/\sqrt v)\,dv.
\]

Put \(y=2/\sqrt v\).  Then

\[
v=\frac4{y^2},\qquad
dv=-\frac8{y^3}dy,
\]

so

\[
\int_0^\infty
v^{-1/2}F(2/\sqrt v)\,dv
=
4\int_0^\infty \frac{F(y)}{y^2}\,dy.
\]

Since \(F'(y)=ye^{-y}\), integration by parts gives

\[
\int_0^\infty\frac{F(y)}{y^2}\,dy
=
\int_0^\infty e^{-y}\,dy
=1.
\]

Hence

\[
\boxed{
\mathcal D(x)\sim4x
\qquad (x\to\infty).
}
\]

This coefficient \(4\) is not fitted.  It comes from the half-density exponent, the von Mangoldt/PNT density, the square-root finite-place mass law, and the twice-vanishing complement kernel.

## 4. Why the von Mangoldt factor is load-bearing

If one used only the Haar weight \(n^{-1/2}\) on primes, prime density contributes \(dp/\log p\) and the continuum spectral density would behave like

\[
\frac{dm}{m^2\log(M_*/m)},
\]

producing an approximately \(1/[r\log r]\) force.

The exact arithmetic current instead carries

\[
(\log p)p^{-1/2}.
\]

The \(\log p\) cancels the \(1/\log p\) prime sparsity.  Equivalently, using the full von Mangoldt tower,

\[
d\psi(u)\sim du.
\]

That cancellation changes the asymptotic from nearly isothermal to exactly isothermal at leading order:

\[
\boxed{
\mathcal D(M_*r)\sim4M_*r.
}
\]

This is the strongest reason to use the *generator/current* weight rather than bare Haar occupancy in a gravitational-response model.

## 5. Static halo consequence of the response ansatz

Assume provisionally that a baryonic source of mass \(M_b\) produces an additional inward radial acceleration

\[
\boxed{
a_{\rm hid}(r)
=
\alpha\frac{GM_b}{r^2}\,
\mathcal D(M_*r),
}
\]

with dimensionless coupling \(\alpha>0\).

Then the number-theoretic asymptotic gives

\[
\boxed{
a_{\rm hid}(r)
\sim
\frac{4\alpha GM_bM_*}{r}.
}
\]

Therefore the circular speed satisfies

\[
v_c^2(r)=r[a_N(r)+a_{\rm hid}(r)]
\longrightarrow
\boxed{
4\alpha GM_bM_*
}
\]

once the Newtonian baryonic term \(GM_b/r\) is subdominant.

The equivalent enclosed halo mass is

\[
M_{\rm hid}(<r)
=
\alpha M_b\mathcal D(M_*r)
\sim
4\alpha M_bM_*r,
\]

so

\[
\boxed{
\rho_{\rm hid}(r)
=
\frac1{4\pi r^2}\frac{dM_{\rm hid}}{dr}
\sim
\frac{\alpha M_bM_*}{\pi r^2}.
}
\]

Thus the simplest completed von-Mangoldt half-density response produces the asymptotic density law of a singular isothermal halo:

\[
\boxed{\rho_{\rm hid}\propto r^{-2}.}
\]

This is a genuine mathematical consequence of the stated response ansatz, not a fitted radial profile.

## 6. Spectral-density derivation

For primitive primes,

\[
m_p\simeq\frac{2M_*}{\sqrt p},
\qquad
w_p=(\log p)p^{-1/2}.
\]

Using \(d\pi(p)\sim dp/\log p\),

\[
w_p\,d\pi(p)
\sim
p^{-1/2}dp.
\]

With

\[
p=\frac{4M_*^2}{m^2},
\qquad
|dp|=\frac{8M_*^2}{m^3}dm,
\]

one obtains

\[
\boxed{
d\nu(m)
\sim
\frac{4M_*}{m^2}\,dm.
}
\]

The hidden arithmetic tower therefore has an infrared spectral density proportional to \(m^{-2}\).  The response kernel \(F(mr)\) then yields

\[
\int_0^\infty \frac{F(mr)}{m^2}\,dm
=
r\int_0^\infty\frac{F(y)}{y^2}\,dy
=r,
\]

which is the continuum origin of the \(1/r\) force.

## 7. Immediate phenomenological stress test

A universal fixed \(\alpha M_*\) gives

\[
v_\infty^2
=
4\alpha GM_bM_*,
\]

hence

\[
v_\infty^4\propto M_b^2.
\]

The observed baryonic Tully--Fisher scaling is approximately \(v_f^4\propto M_b\), so the naive universal-scale version is not phenomenologically sufficient.

To reproduce that scaling one would need an emergent source-dependent infrared scale satisfying

\[
\alpha M_*
\propto M_b^{-1/2}.
\]

Equivalently, introducing an acceleration scale \(a_0\),

\[
M_*
=
\frac1{4\alpha}
\sqrt{\frac{a_0}{GM_b}}
\]

would give

\[
v_\infty^2=\sqrt{GM_ba_0}.
\]

No such source dependence has been derived.  It would have to emerge from the global gravitational/holographic boundary condition, not be inserted by hand.

## 8. What has actually been learned

The calculation does **not** show that finite adelic places are dark matter.

It does establish a nontrivial structural fact:

> Combining the project's exact half-density von-Mangoldt current with its square-root finite-place mass coordinate produces, after the minimal convergent complement subtraction, an asymptotically linear response \(\mathcal D(x)\sim4x\).  If this response enters the 4D gravitational force, its effective halo is automatically isothermal.

That is precisely the radial scaling required for asymptotically flat galaxy rotation curves.

The next load-bearing tasks are:

1. derive the complement kernel \(F\) from the completed prime--Archimedean Schur/Krein or influence-functional action rather than postulating it;
2. determine whether the same metric response lenses light correctly;
3. derive the cosmological stress tensor and test whether the finite-place sector has a pressureless/clustering limit;
4. determine whether the infrared scale \(M_*\) is universal or dynamically tied to a source/horizon scale;
5. check whether the full prime-power mass assignment should use \(n\), \(p\), or the local-place coordinate \(q=p^f\); the leading PNT asymptotic above is stable when the von Mangoldt tower is used, but the microscopic interpretation differs.

Until item 1 is obtained, this should be treated as a sharp candidate mechanism and an exact number-theoretic scaling theorem, not as a dark-matter solution.
