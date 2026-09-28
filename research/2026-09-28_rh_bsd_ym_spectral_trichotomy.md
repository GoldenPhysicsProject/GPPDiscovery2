# Spectral trichotomy conjecture: RH, BSD, and Yang--Mills as sign, nullity, and gap of physical quotient operators

Date: 2026-09-28
Status: unifying research conjecture / programme architecture. No RH, BSD, or Yang--Mills proof is claimed.

## 1. The common operator data

After local-to-global sewing, quotient by null/gauge/coherent directions, and OS/Hodge reconstruction, consider a physical self-adjoint operator \(L_{\rm phys}\).

Three basic spectral invariants are:

\[
n_-(L_{\rm phys})
=
\dim E_{(-\infty,0)}(L_{\rm phys}),
\]

\[
n_0(L_{\rm phys})
=
\dim\ker L_{\rm phys},
\]

and

\[
\lambda_+(L_{\rm phys})
=
\inf\bigl(\operatorname{spec}L_{\rm phys}\setminus\{0\}\bigr)
\]
when the positive spectrum is separated from zero.

The current GPP synthesis suggests the three Millennium-type questions may occupy these three slots:

\[
\boxed{
\begin{array}{lll}
\text{RH-like statement} &:& n_-=0,\\
\text{BSD-like statement} &:& n_0=r,\\
\text{Yang--Mills mass gap} &:& \lambda_+>0.
\end{array}}
\]

This is the sign/nullity/gap trichotomy.

## 2. RH slot: eliminate negative/ghost directions

The finite Weil reflection form already has the property that an off-critical mirror pair contributes one negative ghost direction. After the ground-state transform, RH becomes the sharp Poincare inequality

\[
L_{\rm ar}\ge I
\quad\text{on the physical quotient}.
\]

Thus the RH-bearing content is positivity/stability: no complementary-series or ghost sector survives the completed quotient.

## 3. BSD slot: identify the kernel

For an elliptic curve \(E\), BSD predicts

\[
\operatorname{ord}_{s=1}L(E,s)
=
\operatorname{rank}E(\mathbb Q).
\]

A master Hodge/Fredholm model would seek

\[
\ker L_E
\cong
\text{physical Mordell--Weil/Selmer cohomology},
\]

so that

\[
\dim\ker L_E
=
\operatorname{rank}E(\mathbb Q).
\]

The determinant/response would then vanish to the same order as the kernel dimension, provided the central crossing is transverse and there are no hidden Jordan/nilpotent defects.

The Neron--Tate regulator is naturally the determinant of the induced metric on this harmonic/zero-mode space.

## 4. Yang--Mills slot: gap above cohomology/vacuum

For a gauge theory, the physical Hilbert space is obtained only after quotienting gauge-exact/null directions.

The desired mass-gap statement is then

\[
\operatorname{spec}(H_{\rm YM})
=
\{0\}\cup[m,\infty),
\qquad m>0,
\]

or for a Hodge/mass-squared operator

\[
L_{\rm YM}\ge m^2
\quad\text{on }\ker(L_{\rm YM})^\perp.
\]

So the Yang--Mills theorem occupies the positive-gap slot once the physical zero modes have been identified.

## 5. Why one proof may need all three ingredients

The three spectral questions are logically distinct, but the proof machinery may be inseparable.

### Kernel identification is needed before a gap theorem

One cannot prove the correct positive gap until the exact null/gauge/cohomological subspace is known and removed. This is the BSD-type task.

### Positivity is needed before OS/Hilbert reconstruction

If the reflected quotient form has negative directions, the physical Hilbert reconstruction fails or contains ghosts. This is the RH-type task.

### A gap/bounded inverse is needed for determinant and Schur control

On the orthogonal complement of the kernel, a positive gap provides a bounded Green operator. That is precisely what is needed to control Schur/Feshbach complements and pseudodeterminants, hence both the RH boundary reconstruction and BSD leading-term determinant.

Thus a master proof may cyclically use:

\[
\boxed{
\text{cohomology/nullity}
\longrightarrow
\text{positivity}
\longrightarrow
\text{gap}
\longrightarrow
\text{controlled inverse/determinant}
\longrightarrow
\text{cohomology and boundary reconstruction}.
}
\]

This gives a concrete sense in which solving one problem may require solving the structural content of the other two.

## 6. Supersymmetric/Hodge master candidate

A natural universal object is a cochain differential \(d\) with Hodge--Dirac operator

\[
D=d+d^*,
\qquad
L=D^2=dd^*+d^*d.
\]

Then automatically

\[
L\ge0,
\qquad
\ker L
\simeq
H^\bullet(d)
\]

whenever the Hodge theorem holds.

The three slots become:

- RH: prove the physical reflected form really is the quadratic form of the correct \(L\) after global arithmetic completion, so no ghost directions remain;
- BSD: identify the relevant cohomology \(H^\bullet(d_E)\) with Mordell--Weil/Selmer data and its metric with the Neron--Tate pairing;
- Yang--Mills: prove a uniform lower bound for \(L_{\rm YM}\) on the orthogonal complement of gauge cohomology.

This is especially suggestive because the arithmetic prime Koszul complex already has an explicit differential, contracting homotopy, and Hodge gap at finite cutoff. The unsolved RH theorem is the transfer from that positive bulk Hodge system to the physical reflected boundary quotient.

## 7. Determinant-line unification

If \(L\) is positive with finite-dimensional kernel and a gap on the complement, then a regularized determinant naturally separates into

\[
\text{zero-mode volume}
\times
\det{}'L.
\]

This is structurally the same decomposition needed for the refined BSD formula:
- zero-mode metric volume -> regulator;
- nonzero-mode determinant -> fluctuation/local factors;
- quotient indices/torsion -> finite arithmetic correction factors.

For RH, the same determinant-line machinery would encode the completed xi response after the ghost-free physical quotient.

For Yang--Mills, the pseudodeterminant/Green operator on the gapped complement controls massive fluctuations around the vacuum.

## 8. Strong falsifier

The trichotomy is useful only if one can construct problem-specific physical quotients from a common architecture.

A universal formalism that merely says "every positive operator has sign, kernel, and gap" explains nothing.

A serious common mechanism must simultaneously account for:
- the exact Weil reflection form and prime/Archimedean sewing for RH;
- curve-dependent Selmer/Mordell--Weil kernel and Neron--Tate height for BSD;
- nonperturbative gauge quotient, OS positivity, and cutoff-uniform continuum gap for Yang--Mills.

The value of the conjecture is therefore not that the three statements look alike, but that it predicts a shared Hodge/Schur/OS reconstruction mechanism whose three independent spectral outputs are sign, nullity, and gap.
