# Abel–Cesàro pole barrier and the exact two-point repair target

Date: 2026-09-14
Status: exact diagnosis + repair architecture; **not a proof of RH**

## 1. Why this note matters

The older Abel/Cesàro–Yakaboylu route is substantially closer to a correct structural statement than a blanket rejection would suggest. The elementary Haar/Cesàro selector is real and is already partly Lean-formalized. The failure occurs at one sharply identifiable step: the proof takes a positive Abel form that is defined only in a convergence strip and then sends the regulator through a pole to zero.

This note isolates that pole on the minimal reflection pair and connects it directly to the modern two-point Weil criterion and the prime–Archimedean completion problem.

---

## 2. What is already rigorous

For

\[
\omega_\varepsilon(f)
=\frac{\varepsilon}{2}\int_{-\infty}^{\infty}
 e^{-\varepsilon|u|}f(e^u)\,du,
\qquad \varepsilon>0,
\]

the character integral is

\[
\boxed{
\omega_\varepsilon(t^\alpha)
=\frac{\varepsilon^2}{\varepsilon^2-\alpha^2}}
\]

provided

\[
\boxed{|\Re\alpha|<\varepsilon.}
\]

The positivity

\[
\omega_\varepsilon(|g|^2)\ge0
\]

is genuine whenever the integral converges.

The focused Verify branch already contains:

- `AbelCesaroRegularization.lean`, formalizing positivity and the convergence-strip character formula;
- `CesaroMeanDivergence.lean`, formalizing that the symmetric inversion-invariant Cesàro mean diverges to `+infinity` for every `sigma != 1/2` and is finite at the center through the pre-existing `born_rule_cesaro` theorem.

Thus the elementary half-density selector is not the problem.

---

## 3. Exact location of the invalid regulator passage in `rh_cesaro_v2.tex`

For a finite combination of zero states, write

\[
\delta_{\max}
=\max_\rho\left|\Re\rho-\frac12\right|.
\]

The positive square

\[
\omega_\varepsilon\left(
\left|\sum_\rho c_\rho\chi_\rho\right|^2
\right)
\]

requires at least

\[
\boxed{\varepsilon>2\delta_{\max}.}
\]

The manuscript chooses `epsilon_0 > 2 delta_max` and then states that the integral is finite/positive for all `epsilon in (0,epsilon_0)`. This reverses the needed inequality. If `delta_max>0`, the interval `(0,epsilon_0)` necessarily contains regulators below the convergence threshold.

Therefore one cannot take

\[
\varepsilon\to0^+
\]

inside the positive Abel form unless

\[
\delta_{\max}=0.
\]

But that is exactly the desired RH conclusion for the chosen finite set. The old limit argument therefore crosses the very domain barrier whose absence it needs to prove.

The statement in the manuscript that the regularized pairing is finite “for any epsilon>0 regardless of the real parts” is incompatible with its own character theorem `|Re alpha|<epsilon`.

---

## 4. The minimal reflection-pair block makes the obstruction completely explicit

Take one zero candidate

\[
\rho=\frac12+\delta+i\gamma,
\]

and its functional-equation/reflection partner

\[
\rho^\#:=1-\bar\rho
=\frac12-\delta+i\gamma.
\]

For the two characters `chi_rho, chi_{rho#}`, the Abel Gram entries are

\[
G_\varepsilon(s,s')
=\omega_\varepsilon(\chi_{\bar s}\chi_{s'}).
\]

The cross exponents vanish:

\[
\bar\rho+\rho^\#-1=0,
\qquad
\overline{\rho^\#}+\rho-1=0,
\]

while the diagonal exponents are `+2 delta` and `-2 delta`. Hence, in its honest convergence domain

\[
\varepsilon>2|\delta|,
\]

we have the exact matrix

\[
\boxed{
G_\varepsilon(\delta)
=
\begin{pmatrix}
a_\varepsilon&1\\
1&a_\varepsilon
\end{pmatrix},
\qquad
 a_\varepsilon
=\frac{\varepsilon^2}{\varepsilon^2-4\delta^2}.}
\]

For `epsilon>2|delta|`,

\[
a_\varepsilon>1,
\]

so the eigenvalues

\[
\lambda_+=a_\varepsilon+1,
\qquad
\lambda_-=a_\varepsilon-1
\]

are both nonnegative. The Abel form is genuinely positive there.

If `delta != 0`, however, the positive domain terminates at the pole

\[
\boxed{\varepsilon=2|\delta|.}
\]

There is no positive-integral path from that domain to `epsilon=0`.

---

## 5. What the old proof was implicitly doing

The rational formula has a meromorphic continuation through the regulator variable. If one **formally** continues it below the pole and then sends `epsilon -> 0`,

\[
a_\varepsilon\longrightarrow0,
\]

so

\[
G_\varepsilon^{\rm mer}
\longrightarrow
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

That limiting swap matrix has eigenvalues `+1,-1`; its antisymmetric vector `(1,-1)` gives `-2`.

This is exactly the negative test vector appearing in the already formalized `TwoPointCriterion.lean`:

> positivity on the single reflection pair `{rho,1-conj rho}` forces the pair to collapse to a fixed point, hence `Re rho=1/2`.

So the old proof did not discover a false algebraic limit. It discovered the **correct zero-side reflection matrix**, but reached it by meromorphically continuing a positive Abel form across a pole and then carrying positivity across that continuation. That last transfer of positivity is the invalid step.

This is an unusually sharp diagnosis.

---

## 6. Pole-barrier formulation of RH

For every nontrivial zero `rho`, put

\[
\delta_\rho=\left|\Re\rho-\frac12\right|.
\]

The Abel reflection-pair Gram family has a positive-integral realization down to arbitrarily small positive regulator **if and only if**

\[
\delta_\rho=0.
\]

Thus, at the level of zero states,

\[
\boxed{
\mathrm{RH}
\iff
\text{no nontrivial-zero reflection pair has a positive-regulator Abel pole barrier.}}
\]

This is an equivalent criterion, not a proof. Its value is that it tells us exactly what any repair must accomplish: it must replace the illegal crossing of `epsilon=2|delta|` by a different completed positive construction that reaches the zero-regulator boundary without analytic continuation through an indefinite sector.

---

## 7. Connection to the modern prime–Archimedean program

The current program has precisely the sort of replacement mechanism that the old proof lacked.

### 7.1 Same zero-side endpoint

`TwoPointCriterion.lean` proves that pair positivity of the zero-side reflection form is already equivalent to RH. Therefore no additional content can be extracted by manipulating the zero-side swap matrix itself.

### 7.2 Analytic content must enter before the zero-side limit

The modern target is an independently positive arithmetic object:

\[
\mathscr K(t),
\qquad
\mathscr J(a,b),
\qquad
m_*(u),
\qquad
\phi(u)=u m_*(u),
\]

with equivalent positivity formulations such as

\[
[\mathscr K(t_i+t_j)]\succeq0,
\]

\[
[\mathscr J(a_i,a_j)]\succeq0,
\]

or the Loewner kernel

\[
[\phi^{[1]}(u_i,u_j)]\succeq0.
\]

These formulas are built directly from the completed prime–Archimedean distribution in a safe domain and do not require carrying an Abel state through an off-line pole.

### 7.3 Interpretation

The old Abel parameter was trying to perform two jobs at once:

1. regularize the noncompact Haar direction;
2. project the arithmetic resonance space onto the shadow-fixed physical sector.

Off the critical line those jobs conflict, producing the pole barrier.

The newer multichannel/Schur/Hodge picture suggests the repair: keep the positive regularization in its honest domain, make the prime and Archimedean modes internal channels, and obtain the physical reflection form as a **positive Schur boundary quotient** rather than a meromorphic continuation of the bare Abel Gram.

This is exactly consistent with the independent same-space metric no-go: a bounded metric on the original one-channel sine space cannot repair the problem. A genuine dilation/completion is required.

---

## 8. Lean target

The following facts are elementary and worth certifying next:

1. for `delta != 0`, there is no sequence `epsilon_n>0` with `epsilon_n -> 0` and `2|delta|<epsilon_n` for every `n`;
2. the finite reflection-pair Abel matrix has entries
   \[
   [[a,1],[1,a]],\quad a=epsilon^2/(epsilon^2-4delta^2)
   \]
   in the convergence domain;
3. `epsilon>2|delta|` implies `a>1` and the two real quadratic eigenmodes are nonnegative;
4. the meromorphic zero-regulator limit for `delta !=0` is the swap matrix and the antisymmetric vector has value `-2`;
5. therefore positivity of an actual Abel integral cannot be transferred to that limit without an additional theorem crossing the pole barrier.

These statements would connect `AbelCesaroRegularization.lean`, `CesaroMeanDivergence.lean`, and `TwoPointCriterion.lean` into one formal diagnostic chain.

The first, third-domain, and rational-limit parts are now encoded in the focused Verify candidate module `AbelCesaroPoleBarrier.lean`; CI status must still be checked before calling that new module certified.

---

## 9. Research judgment

The old Haar/Abel proof should **not** be thrown away. Its strongest corrected content is:

- the critical half-density is exactly the unique finite inversion-symmetric Cesàro locus;
- the Abel regularization is genuinely positive in its convergence domain;
- the reflection-pair algebra is exactly the right minimal RH obstruction;
- the only failed move is carrying that positivity through the off-critical regulator pole.

The modern problem is therefore not to replace the whole argument. It is to replace one illegal analytic continuation by a zero-independent positive prime–Archimedean boundary completion.

That repair is precisely what the current Ward/Löwner/Hardy/Hodge program is trying to construct.

---

## 10. New causal–shadow factorization of the Abel kernel

The regularized character kernel has the exact factorization

\[
\boxed{
\frac{\varepsilon^2}{\varepsilon^2-\alpha^2}
=
\frac{\varepsilon}{\varepsilon-\alpha}
\frac{\varepsilon}{\varepsilon+\alpha}.}
\]

This is more than an algebraic curiosity. The two factors are precisely the normalized one-sided Laplace transforms of the forward and reflected half-lines:

\[
C_\varepsilon^+(\alpha)
:=\varepsilon\int_0^\infty e^{-\varepsilon u}e^{\alpha u}\,du
=\frac{\varepsilon}{\varepsilon-\alpha},
\qquad \Re\alpha<\varepsilon,
\]

and

\[
C_\varepsilon^-(\alpha)
:=\varepsilon\int_0^\infty e^{-\varepsilon u}e^{-\alpha u}\,du
=\frac{\varepsilon}{\varepsilon+\alpha},
\qquad -\Re\alpha<\varepsilon.
\]

Thus the full two-sided Abel strip

\[
|\Re\alpha|<\varepsilon
\]

is exactly the domain in which **both causal orientations are simultaneously stable**.

On the unitary/principal-series axis `Re alpha=0`, write `alpha=i gamma`. Then

\[
C_\varepsilon^-(i\gamma)
=\overline{C_\varepsilon^+(i\gamma)},
\]

and therefore

\[
\boxed{
\omega_\varepsilon(t^{i\gamma})
=
C_\varepsilon^+(i\gamma)
\overline{C_\varepsilon^+(i\gamma)}
=
\left|\frac{\varepsilon}{\varepsilon-i\gamma}\right|^2.}
\]

So **the Abel/Haar kernel is already a norm square on the critical line**. More generally, for real `epsilon>0`,

\[
C_\varepsilon^-(\alpha)
=\overline{C_\varepsilon^+(\alpha)}
\quad\Longleftrightarrow\quad
\alpha+\bar\alpha=0
\quad\Longleftrightarrow\quad
\Re\alpha=0,
\]

away from trivial denominator singularities.

This is exactly the Rosati/adjoint pattern that appeared independently in the later Cayley-polarization attack: **shadow/reflection equals Hilbert adjoint precisely on the unitary axis**.

There is an equally sharp all-scale statement. A fixed exponent belongs to the two-sided positive Abel domain for every `epsilon>0` iff

\[
|\Re\alpha|<\varepsilon\quad\text{for every }\varepsilon>0,
\]

which is equivalent to

\[
\boxed{\Re\alpha=0.}
\]

For the zero self-pairing exponent

\[
\alpha=\bar\rho+\rho-1=2\left(\Re\rho-\frac12\right),
\]

this says:

\[
\boxed{
\text{forward and shadow Abel channels are jointly stable at every scale}
\iff \Re\rho=\frac12.}
\]

Again this is an exact RH-equivalent criterion once `rho` is restricted to nontrivial zeros; it is not itself the missing arithmetic proof. But it substantially clarifies the concept behind the original route. The old “Haar self-duality forces the critical line” intuition can be rewritten rigorously as:

> the half-density line is the unique locus on which the causal transfer and its shadow are genuine Hilbert adjoints at every regularization scale.

The remaining arithmetic theorem is to prove that the completed prime–Archimedean resonance realization is required to satisfy that all-scale causal–shadow adjointness. This is essentially the same content as the modern Hardy no-leak / positive Schur-completion theorem, now seen directly inside the old Abel kernel.
