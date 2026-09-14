# Screw–heat–Bernstein–Fredholm bridge

Date: 2026-09-14
Status: exact analytical synthesis, not a proof of RH

## Purpose

This note connects four objects that had already been constructed separately in the current RH program:

1. the completed prime–Archimedean boundary distribution `W`;
2. Suzuki's scalar screw/box functional `Psi(L)`;
3. the arithmetic heat trace `K(t)`;
4. the BPY/Fredholm inverse-spectrum moments.

The new point is an exact zero-independent transform between the screw functional and the heat trace, followed by a reciprocal-measure identification with the BPY cumulant/Fredholm data.

Throughout,

\[
F(z)=\frac{\xi(\tfrac12+z)}{\xi(\tfrac12)}.
\]

The current manuscript gives the zero-independent identities

\[
\Psi(L)=\langle \mathcal W,(L-a)_+\rangle,
\]

\[
\int_0^\infty e^{-rL}\Psi(L)\,dL
=\frac1{r^2}\frac{\xi'}{\xi}\!\left(\frac12+r\right),
\qquad r>\frac12,
\]

and

\[
\mathscr K(t)=\langle \mathcal W,g_t\rangle,
\qquad
g_t(L)=\frac{e^{-L^2/(4t)}}{\sqrt{4\pi t}},
\]

with

\[
\int_0^\infty e^{-st}\mathscr K(t)\,dt
=\frac1{2\sqrt s}\frac{\xi'}{\xi}\!\left(\frac12+\sqrt s\right)
\]

in the safe half-plane `s>1` (equivalently the shifted massive-resolvent formula with `s=1+u`).

## Theorem 1: exact Gaussian screw-to-heat bridge

Define

\[
\boxed{
\mathscr B(t):=\int_0^\infty \Psi(L)g_t(L)\,dL,
\qquad t>0.}
\]

Then

\[
\boxed{\mathscr B'(t)=\mathscr K(t),\qquad t>0,}
\]

and, with the natural `t\downarrow0` normalization,

\[
\boxed{\mathscr B(t)=\int_0^t\mathscr K(u)\,du.}
\]

### Proof in the safe Laplace region

For `s>1`, use the standard subordination integral

\[
\int_0^\infty e^{-st}g_t(L)\,dt
=\frac{e^{-\sqrt s L}}{2\sqrt s}.
\]

Hence, by truncation/Fubini in the absolutely convergent safe region,

\[
\begin{aligned}
\mathcal L_t\mathscr B(s)
&=\frac1{2\sqrt s}
\int_0^\infty e^{-\sqrt sL}\Psi(L)\,dL\\
&=\frac1{2\sqrt s}\frac1s
\frac{\xi'}{\xi}\!\left(\frac12+\sqrt s\right)\\
&=\frac1s\mathcal L_t\mathscr K(s).
\end{aligned}
\]

Therefore

\[
s\mathcal L\mathscr B(s)=\mathcal L\mathscr K(s).
\]

Since `Psi(0)=0` in the box-functional normalization, the Gaussian approximate-identity limit gives `B(0)=0`. Uniqueness of the Laplace transform yields `B'=K` for positive time. This proof avoids informal integration by parts against the renormalized singular real-place distribution.

Formally the same identity is `Psi''=W` followed by the heat equation `partial_t g_t=partial_L^2 g_t`; the Laplace proof is the safe version of that calculation.

## Corollary 2: RH is exactly a Bernstein property of the Gaussian screw average

The manuscript already proves

\[
\mathrm{RH}\iff \mathscr K\text{ is completely monotone on }(0,\infty).
\]

Since `B'=K` and `B(0)=0`, it follows that

\[
\boxed{
\mathrm{RH}\iff \mathscr B\text{ is a Bernstein function}.}
\]

Thus Suzuki's pointwise screw criterion and the arithmetic OS/heat criterion admit a direct transform bridge:

\[
\Psi
\xrightarrow{\text{half-line Gaussian average}}
\mathscr B
\xrightarrow{d/dt}
\mathscr K.
\]

This is not a proof. For a generic nonnegative `Psi`, positivity of its Gaussian average does not imply complete monotonicity of its derivative.

Indeed

\[
\partial_tg_t(L)
=g_t(L)\left(\frac{L^2}{4t^2}-\frac1{2t}\right)
\]

changes sign at `L=sqrt(2t)`. Therefore the map `Psi -> K` is not positivity preserving by a pointwise positive kernel. This identifies exactly why Suzuki positivity cannot simply be pushed through Gaussian smoothing to prove heat positivity.

## Corollary 3: spectral form under RH

Under RH the screw function has the exact expansion

\[
\Psi(L)=2\sum_{\gamma>0}m_\gamma
\frac{1-\cos(\gamma L)}{\gamma^2}.
\]

Because

\[
\int_0^\infty 2g_t(L)\cos(\gamma L)\,dL=e^{-\gamma^2t},
\]

we obtain

\[
\boxed{
\mathscr B(t)=\sum_{\gamma>0}m_\gamma
\frac{1-e^{-\gamma^2t}}{\gamma^2},}
\]

and hence

\[
\boxed{
\mathscr K(t)=\sum_{\gamma>0}m_\gamma e^{-\gamma^2t}.}
\]

Thus `B` is the integrated heat trace.

Its Bernstein/Lévy measure is

\[
\boxed{
\eta=\sum_{\gamma>0}\frac{m_\gamma}{\gamma^2}
\,\delta_{\gamma^2}.}
\]

## Corollary 4: reciprocal spectral duality with the BPY cumulant measure

The BPY cumulant/Stieltjes program defines

\[
\mu_n=2\sum_{\gamma>0}m_\gamma\gamma^{-2n-2}
\qquad(n\ge0)
\]

under RH. In terms of the screw Bernstein measure `eta`,

\[
\boxed{
\frac{\mu_n}{2}
=\int_0^\infty \lambda^{-n}\,\eta(d\lambda).}
\]

Equivalently, if `R(lambda)=1/lambda`, the BPY Stieltjes measure is twice the reciprocal pushforward of the screw Bernstein measure with the same weights:

\[
\nu_{\rm BPY}
=2R_*\eta.
\]

So the heat/screw program and the BPY cumulant/Fredholm program are not merely parallel RH criteria. They are the direct-spectrum and inverse-spectrum descriptions of the same hypothetical positive operator.

## Corollary 5: the single-operator triad

If the missing arithmetic positivity theorem produces a positive operator `H` with spectrum `gamma^2` and trace-class inverse, then all three central objects become

\[
\boxed{
\mathscr K(t)=\operatorname{Tr}(e^{-tH}),}
\]

\[
\boxed{
\mathscr B(t)=\operatorname{Tr}\bigl(H^{-1}(I-e^{-tH})\bigr),}
\]

and

\[
\boxed{
F(z)=\det(I+z^2H^{-1}).}
\]

Thus the Fredholm operator `A` of the earlier target is simply

\[
A=H^{-1}.
\]

The screw function probes the integrated direct heat spectrum; the BPY cumulants probe negative moments of that same spectrum; the Fredholm determinant packages the inverse spectrum.

This provides a useful design constraint on any proposed prime–Archimedean construction: it should not separately manufacture a heat operator and a Fredholm operator. A correct closure should produce one positive `H`, with the determinant, heat trace, screw Bernstein measure, and BPY moments following from functional calculus.

## Corollary 6: zero-independent safe determinant reconstruction from the heat trace

For real `w>1`, the safe Laplace identity gives

\[
\frac{d}{dw}\log F(\sqrt w)
=\int_0^\infty e^{-wt}\mathscr K(t)\,dt.
\]

Integrating from `w=1` gives the exact zero-independent formula

\[
\boxed{
\log\frac{F(\sqrt w)}{F(1)}
=\int_0^\infty
\frac{e^{-t}-e^{-wt}}{t}\,\mathscr K(t)\,dt,
\qquad w>1.}
\]

Under RH this is simply

\[
\sum_{\gamma>0}m_\gamma
\log\frac{\gamma^2+w}{\gamma^2+1}.
\]

The important point is that `K` already retains the complete centered xi determinant in the safe domain; no zero list is needed to define the reconstruction. The missing theorem remains positivity/no-escaped-trace, not divisor recovery.

## What this does and does not solve

### New useful synthesis

- It gives an exact transform `Psi -> B -> K`.
- It makes `RH <=> B is Bernstein` explicit.
- It identifies the screw Bernstein measure and BPY cumulant measure as reciprocal spectral measures.
- It collapses the desired heat, screw, cumulant, and Fredholm constructions to one positive operator `H` with `H^{-1}` trace class.
- It gives a safe-domain determinant reconstruction directly from the zero-independent arithmetic heat trace.

### No proof claim

The sign problem has not disappeared. The derivative kernel from `Psi` to `K` changes sign, so the known scalar criterion `Psi(L)>=0` cannot be converted into heat complete monotonicity by a generic positive transform. Conversely, constructing `H>=0` with the required arithmetic trace is essentially the remaining global polarization/no-escaped-trace theorem.

## Next attacks suggested by the bridge

1. Search for a zero-independent prime–Archimedean construction of `H` for which the already known relative boundary trace is `Tr(e^{-tH})`. The key extra requirement is trace conservation in the cutoff limit.
2. Use the identity `B'=K` to transport finite-section errors between the screw/Fejer cutoff and heat cutoff. A quantitative estimate on the derivative of the Gaussian average may convert the existing rank-one high-zero tail analysis into a trace-tightness criterion.
3. Express the BPY Hausdorff inequalities as negative-moment inequalities of the same candidate heat spectral measure. This may reveal a coercive criterion stronger than Hilbert–Schmidt convergence but weaker than direct trace-norm convergence.
4. Test whether the doubled Mobius–Archimedean generalized pencil produces both sides of the reciprocal spectrum simultaneously. If its positive metric completion yields `H`, no second Fredholm construction should be needed.
5. Look for a Ward identity whose boundary term is exactly `B(t)`, since the derivative then supplies `K(t)` automatically. This may be a cleaner target than asking the Ward operation to produce the heat trace in one step.
