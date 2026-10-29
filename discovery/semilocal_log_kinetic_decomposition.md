# A log-kinetic decomposition of the completed semilocal Weil form

**2026-10-29 · Codex / Discovery2 · arithmetic spectral project**

## Scope and verification

This note works with the **actual** compactly supported one-sided Weil distribution from Daniel Toupin's \`arithmetic_principal_series_RH_program-34.tex\`, Section "The exact semilocal Weil form". No new sign assumption, zeta-zero input, or model contact is inserted. It gives an exact decomposition and a fixed-support semiboundedness theorem. The crucial signed prime discrepancy remains unsolved; consequently RH is **not** claimed.

Set \(L>0\) and let \(f\) be any complex-valued \(C_c^\infty(0,L)\) function, extended by zero to the real line. Define the Hermitian correlation
\[
C_f(y)=\int_\mathbb R \overline{f(t)}f(t+y)\,dt,\qquad
q_f(y)=C_f(y)+C_f(-y)=2\Re C_f(y)\quad(y\ge0).
\]
Then \(q_f(0)=2\|f\|_2^2\), \(q_f(y)=0\) for \(y\ge L\), and \(|q_f(y)|\le2\|f\|_2^2\). On a Fourier basis of \([0,L]\), the polarization of \(q_f\) reproduces exactly the manuscript's \(q_{mn}(y)\). Put
\[
w_{p,r}=(\log p)p^{-r/2},\quad a_{p,r}=r\log p,\quad
c_\infty=\log(4\pi)+\gamma.
\]

## 1. Exact full-form identity

The **completed** Weil form
\[
Q_L[f]=\int_0^L q_f(y)(e^{y/2}+e^{-y/2})\,dy
-c_\infty\|f\|_2^2
-\int_0^\infty \frac{e^{y/2}q_f(y)-q_f(0)}{2\sinh y}\,dy
-\sum_{p^r\le e^L}w_{p,r}q_f(a_{p,r})
\]
is **identically**
\[
\boxed{
Q_L[f]=\mathcal E_L[f]+\mathcal P_L[f]-c_\infty\|f\|_2^2
-\mathcal A_L[f]-\mathcal S_L[f]
}
\]
where
\[
\begin{aligned}
\mathcal E_L[f]&=\int_0^\infty\frac{q_f(0)-q_f(y)}{2\sinh y}\,dy
=\int_0^\infty\frac{\|f-T_yf\|_2^2}{2\sinh y}\,dy\ \ge0,\\
\mathcal P_L[f]&=\int_0^L q_f(y)(e^{y/2}+e^{-y/2})\,dy,\\
\mathcal A_L[f]&=\int_0^L\frac{e^{y/2}-1}{2\sinh y}q_f(y)\,dy,\\
\mathcal S_L[f]&=\sum_{p^r\le e^L}w_{p,r}q_f(a_{p,r}).
\end{aligned}
\]
Here \(T_yf(t)=f(t+y)\). The form \(\mathcal E_L\) is positive by an actual squared \(L^2\) norm. This is just algebraically splitting the gamma subtraction into \(q_f(y)-q_f(0)\) and \((e^{y/2}-1)q_f(y)\), including the essential \(y>L\) gamma tail. Do NOT truncate the first integral at \(L\).

With \(\widehat f(\xi)=\int_\mathbb R f(x)e^{-i\xi x}\,dx\), Plancherel yields
\[
\mathcal E_L[f]=\int_\mathbb R h(\xi)|\widehat f(\xi)|^2\,\frac{d\xi}{2\pi},\quad
h(\xi)=\int_0^\infty\frac{1-\cos(\xi y)}{\sinh y}\,dy
=\Re\big[\psi(\tfrac12+\tfrac{i\xi}{2})-\psi(\tfrac12)\big].
\]
The symbol satisfies \(h\ge0\) and \(h(\xi)=\log|\xi|+O(1)\) for \(|\xi|\to\infty\). Thus \(\mathcal E_L\) is a **positive logarithmic kinetic energy**; its finite-interval closed form has compact resolvent.

## 2. Pole part: exactly rank two, but indefinite

Define \(A_\pm(f)=\int_0^L f(x)e^{\pm x/2}dx\). Then
\[
\boxed{\mathcal P_L[f]=2\Re\big(A_+(f)\overline{A_-(f)}\big).}
\]
It is **not** generally a positive square. The underlying self-adjoint rank-two operator on \(L^2(0,L)\) is
\[
P_L=|e^{x/2}\rangle\langle e^{-x/2}|
+|e^{-x/2}\rangle\langle e^{x/2}|.
\]
Its two nonzero eigenvalues, computed without a zeta zero or numerical fit, are
\[
\boxed{\lambda_\pm(P_L)=L\pm 2\sinh(L/2).}
\]
In particular \(\lambda_-(P_L)=L-2\sinh(L/2)<0\) for every \(L>0\). For \(\lambda=5/2\), \(L=2\log(5/2)\), the exact pole eigenvalues are approximately \(3.93258146374831\) and \(-0.26741853625169\). **Do not claim pole positivity**: its single negative direction must be compensated by the rest of the genuine completed form.

## 3. Bounded gamma tilt, uniformly in support length

The remaining gamma tilt has \(|\mathcal A_L[f]|\le2 I(L)\|f\|_2^2\), with
\[
I(L)=\int_0^L\frac{e^{y/2}-1}{2\sinh y}\,dy.
\]
Make the substitution \(t=e^{-y/2}\). One obtains the **closed expression**
\[
\boxed{
I(L)=\log\frac{2}{1+e^{-L/2}}
-\frac12\log\frac{2}{1+e^{-L}}
+\frac\pi4-\arctan(e^{-L/2})
}
\]
and, for every finite \(L>0\),
\[
0<I(L)<\frac12\log2+\frac\pi4=1.13197175367742\ldots.
\]
The potentially singular gamma correction is therefore exactly a positive logarithmic kinetic energy plus a **uniformly bounded** operator. The only support-growth issues lie elsewhere (pole and prime sector).

## 4. Exact PNT Ward cancellation and single residual source

Define the continuous prime-number-theorem mean
\[
\mathcal C_L[f]=\int_0^L e^{y/2}q_f(y)dy
\]
and its **signed arithmetic discrepancy**
\[
\mathcal R_L[f]=\mathcal C_L[f]-\sum_{p^r\le e^L}w_{p,r}q_f(r\log p).
\]
No estimate is assumed about \(\mathcal R_L\). The exact pole decomposition gives
\[
\mathcal P_L[f]-\mathcal C_L[f]
=\int_0^L e^{-y/2}q_f(y)dy=:\mathcal M_L[f].
\]
Since \(e^{-|x-y|/2}\) is a positive Fourier-covariance kernel,
\[
\mathcal M_L[f]=\int_\mathbb R|\widehat f(\xi)|^2\frac{1}{\xi^2+1/4}\frac{d\xi}{2\pi}\ge0.
\]
Therefore the completed one-sided Weil form has the **exact representation**
\[
\boxed{
Q_L[f]=\mathcal E_L[f]+\mathcal M_L[f]
-c_\infty\|f\|_2^2-\mathcal A_L[f]+\mathcal R_L[f].
}
\]
The **only prime-counting input** is the signed discrepancy \(\mathcal R_L\); no Euler product or zeta zero has been assumed positive. Because \(\mathcal A_L\) is uniformly bounded, the central missing assertion is a genuine *one-sided* lower domination for \(\mathcal R_L\), against the explicit log-kinetic plus massive covariance and scalar term, over **all** support lengths and admissible \(f\). Proving that would yield the complete Weil positivity criterion (and thus RH); it is not a statement we have established.

## 5. What can be proved for every fixed support \(L\)

All terms beyond \(\mathcal E_L\) are bounded operators for each fixed \(L\): \(\mathcal P_L\) has rank two, \(\mathcal A_L\) has norm at most \(2I(L)\), and \(\mathcal S_L\) is a *finite* sum of bounded translations with norm at most \(2\sum_{p^r\le e^L}w_{p,r}\). Therefore
\[
Q_L[f]\ge \mathcal E_L[f]-B(L)\|f\|_2^2
\]
where one valid explicit constant is
\[
\boxed{
B(L)=c_\infty+[2\sinh(L/2)-L]+2I(L)
+2\sum_{p^r\le e^L}w_{p,r}.
}
\]
The sharp negative pole cost \(2\sinh(L/2)-L\) is used, not the huge absolute-value bound for its positive direction.

The log-kinetic form domain consists of \(f\in L^2(\mathbb R)\) supported in \([0,L]\), satisfying \(\int h(\xi)|\widehat f(\xi)|^2d\xi<\infty\). It is a closed form. Because \(h(\xi)\to+\infty\), bounded energy controls the high-frequency Fourier tail; compact spatial support plus the Kolmogorov-Riesz compactness criterion makes this form domain compactly embedded in \(L^2(0,L)\). The bounded perturbation Q therefore has a self-adjoint semibounded Friedrichs representation with **compact resolvent**. It has only finitely many nonpositive eigenvalues for each fixed \(L\).

This gives a rigorous **finite negative-index theorem at every fixed support**, and explains why large N Galerkin spectra are governed by a handful of low modes. It does not tell us that the finite negative index is zero for every L. Establishing that uniform sign is exactly the unsolved arithmetic step.

## 6. Independent high-precision check at λ=5/2, N=0

Using the actual finite prime powers 2,3,4,5 and 50-digit mpmath quadrature, with \(f=1/\sqrt L\) on \([0,L]\), \(q(y)=2(1-y/L)\), our independently recomputed terms are
\[
\begin{array}{ll}
\mathcal E_L=1.1712889280020722294,&
\mathcal P_L=3.928884004574249204,\\
\mathcal A_L=0.4911005259679680637,&
\mathcal S_L=1.4616502015043849344,\\
c_\infty=3.1082399118708236536,&
Q_L=+0.039182293233144781752.
\end{array}
\]
Alternatively \(\mathcal M_L=1.38074399695050053\), \(\mathcal R_L=1.08648980611936374\), giving the same \(Q_L\) by the second exact decomposition. This agrees with the team's independent Arb interval certificate \(+0.03918229323314478175\pm4\cdot10^{-25}\). The single mode does not establish positivity for all \(N,L\).

Further checks: formula for \(I(L)\) agrees with numerical integration to \(<10^{-48}\) at four sample supports; the pole rank-two matrix reproduces Fourier \(q_{mn}\) integrals for multiple \(m,n\) to double precision. Both types of tests are supplemental to the exact proofs.

## 7. Relation to physical program and fake controls

The positive \(\mathcal E_L+\mathcal M_L\) is an explicit Archimedean Gaussian/strip candidate, but \(\mathcal R_L\) remains a **signed, nonlocal distribution**, not a covariance automatically. The decomposition should be compared with Astra's gamma-oscillator background and with Turbo's true E1 sector. Test fake \(F_\theta(s)=\zeta(s-\theta)\zeta(s+\theta)\): local prime Fock covariance and functional symmetry are fake-blind, whereas the **correct real-place completion and nonlocal signed discrepancy** must reject it. No deletion of \(\mathcal R_L\), replacement by variance, or insertion of a tuned positive contact is permitted.

**Next attack:** derive a zero-independent lower bound for \(\mathcal R_L[f]\) across arbitrary L and f, or construct a nonlocal prime–Archimedean intertwiner enforcing \(Q_L\ge0\), while tracking the genuinely indefinite rank-two pole. Both would be proof strength; current work establishes only exact structural decomposition and finite-support spectral control.

## Sources/provenance

- Original mathematical form: \`arithmetic_principal_series_RH_program-34.tex\`, “The exact semilocal Weil form.”
- Earlier team Arb matrix: \`GPPDiscovery2/discovery/arb_semilocal_weil_matrix.py\`.
- Earlier prime–pole mean-field Ward observation in Astra's bridge notes and PR #11.
- Current derivation: Codex, October 29; does not claim pole positivity or an all-support theorem.
