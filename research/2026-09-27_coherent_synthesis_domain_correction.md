# Coherent synthesis: trace class is already reached at the second tail

Date: 2026-09-27. Status: exact correction and domain theorem. This corrects the operator-ideal interpretation in the earlier “two channels as HS and nuclear obstructions” note.

## 1. The operators being compared

On one common paired module \(\mathcal K=\ell^2(\mathbb N_0)\), put
\[
r_p=p^{-1/2},\qquad
R_p^{(k)}=\sqrt{1-p^{-1}}\sum_{n\ge k}p^{-n/2}e_n,
\quad
V_k c=\sum_p c_p R_p^{(k)}
\]
initially for finitely supported \(c\).
It remains true that \(\|R_p^{(k)}\|=p^{-k/2}\).

The diagonal Euler operator \(D(s)\) on \(\ell^2(\mathcal P)\) is a different operator. Its singular values are \(|p^{-s}|\); nothing below changes its Schatten thresholds or the det3 identity.

## 2. The second tail is nuclear on Hilbert space

The \(n\)-th row of \(V_k\) is
\[
a_n(p)=\sqrt{1-p^{-1}}p^{-n/2}.
\]
For \(n\ge2\),
\[
\|a_n\|_2^2=P(n)-P(n+1)
\le2^{-(n-2)}[P(2)-P(3)].
\]
Therefore
\[
V_2=\sum_{n\ge2}|e_n\rangle\langle a_n|
\]
is an absolutely summable rank-one expansion, and
\[
\boxed{\|V_2\|_{\mathfrak S_1}
\le \sum_{n\ge2}\sqrt{P(n)-P(n+1)}
\le\frac{\sqrt{P(2)-P(3)}}{1-2^{-1/2}}<\infty.}
\]
No determinant assumption or RH is used.

The earlier divergent *column* sum \(\sum_p\|R_p^{(2)}\|=\sum_p1/p\) is correct, but divergence of one chosen nuclear expansion does not prove that an operator is not nuclear. The row expansion proves the opposite here.

For \(k=1\), even boundedness on \(\ell^2\) fails: its first row has squared norm \(\sum_p(p^{-1}-p^{-2})=\infty\). By duality no bounded operator can have that row. Thus “not Hilbert-Schmidt” understated this particular failure.

## 3. The sharp domain threshold

For \(k\ge1\) and \(1<q\le\infty\), let \(q'=q/(q-1)\), with \(q'=1\) when \(q=\infty\). Then
\[
\boxed{V_k:\ell^q(\mathcal P)\longrightarrow\mathcal K
\text{ is bounded iff } kq'/2>1.}
\]
**Necessity.** The first nonzero row must define a bounded functional on \(\ell^q\). Its coefficients are comparable to \(p^{-k/2}\), so they must belong to \(\ell^{q'}\). At the endpoint \(\sum_p1/p\) diverges.

**Sufficiency.** Once the first row belongs to \(\ell^{q'}\),
\[
\|a_n\|_{q'}\le 2^{-(n-k)/2}\|a_k\|_{q'},\quad n\ge k.
\]
Summing the row norms gives a bounded map into \(\mathcal K\). For \(q=\infty\), define the extension by these absolutely convergent row sums; it agrees with synthesis on finite supports. For \(q=1\), all the maps are bounded directly from the uniform column bound. QED.

Consequently:

| Map or evaluation | First tail that works |
|---|---|
| Common-module synthesis from \(\ell^2(\mathcal P)\) | \(k=2\), already trace class |
| Synthesis on bounded coefficient sequences, including \(c_p=1\) | \(k=3\) |
| Absolute summation of the column vectors | \(k=3\) |

Thus the second arithmetic channel is a **singular boundary-evaluation obstruction**, not a failure of trace class for \(V_2\).

In particular, trace class does not license applying \(V_2\) to the all-ones sequence: that sequence is not in \(\ell^2\), and the \(e_2\) coordinate of the cutoff result diverges as \(\sum_p\sqrt{1-1/p}/p\).

## 4. Why the local unitary transform is not yet an adelic isometry

The recovered Jacobi transform \(U\) is unitary on one common \(\mathcal K\). It sends each coherent vector to its explicit hyperbolic-secant exponential tilt. It does not by itself identify the independent-prime direct sum \(\bigoplus_p\mathcal K_p\) with the shared coherent family while preserving orthogonality of the prime labels.

After two jets are removed the shared synthesis is compact, even nuclear. It therefore has no bounded left inverse on an infinite-dimensional prime coefficient space. Before those removals the common synthesis has the divergences above.

Two low occupation labels do not mean two global scalar degrees of freedom: their coefficients still carry all prime labels and modular phases. Any claimed finite-rank global sewing must prove that reduction, not infer it from the local occupation truncation.

## 5. Reproducibility

The companion script sieves all primes through \(10^6\), uses occupation rows \(2,\ldots,42\), and evaluates row bounds and column boundary growth. Through \(10^4\), a direct SVD gives nuclear sum approximately \(0.816112\), while the 41-row nuclear upper bound is \(1.490995\). At \(10^6\) the row bound is approximately \(1.491004\), whereas the first-row \(\ell^1\) sum has grown to \(2.632403\).

These are finite controls only. The analytic geometric bound proves nuclearity, and the harmonic-prime divergence proves failure on the all-ones boundary vector.
