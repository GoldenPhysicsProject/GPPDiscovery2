# Exact one-ghost reduction of the completed logarithmic derivative

Date: 2026-09-27
Status: exact algebraic/operator reduction of the current Krein decomposition. No RH proof. No external literature search used.

## 1. Start from the exact four-channel Krein square

For \(q>1\), the current RH manuscript gives
\[
B(q)=\frac{\xi'}{\xi}(q)
=
g_\infty(q)+\frac1q+\frac1{q-1}+\frac{\zeta'}{\zeta}(q)
\]
and
\[
\Delta_qh(a,b)=h(q+a)+h(q+b)-h(q)-h(q+a+b).
\]

The exact feature decomposition is
\[
\Delta_qB(a,b)
=
\langle\Phi_q^\Gamma(a),\Phi_q^\Gamma(b)\rangle
+
\langle\Phi_q^{\rm p}(a),\Phi_q^{\rm p}(b)\rangle
-
\langle\Phi_q^0(a),\Phi_q^0(b)\rangle
-
\langle\Phi_q^1(a),\Phi_q^1(b)\rangle,
\]
where
\[
\Phi_q^\Gamma(a;x)
=
\frac{e^{-qx/2}}{\sqrt{1-e^{-2x}}}(1-e^{-ax}),
\]
\[
\Phi_q^0(a;x)
=
e^{-qx/2}(1-e^{-ax}),
\]
\[
\Phi_q^1(a;x)
=
e^{-(q-1)x/2}(1-e^{-ax}),
\]
and
\[
\Phi_q^{\rm p}(a;p,m)
=
(\log p)^{1/2}p^{-mq/2}(1-p^{-ma}).
\]

## 2. The \(s=0\) pole cancels the Gamma ground mode exactly

The Gamma square has density
\[
\frac{e^{-qx}}{1-e^{-2x}}
=
e^{-qx}+e^{-(q+2)x}+e^{-(q+4)x}+\cdots.
\]

The negative \(0\)-pole square is exactly the first term
\[
e^{-qx}.
\]

Therefore
\[
\boxed{
\langle\Phi_q^\Gamma(a),\Phi_q^\Gamma(b)\rangle
-
\langle\Phi_q^0(a),\Phi_q^0(b)\rangle
=
\mathfrak D_{q+2}(a,b),
}
\]
where
\[
\mathfrak D_{q+2}(a,b)
=
\int_0^\infty
\frac{e^{-(q+2)x}}{1-e^{-2x}}
(1-e^{-ax})(1-e^{-bx})\,dx.
\]

Thus the four-channel Krein decomposition collapses exactly to

\[
\boxed{
\Delta_qB(a,b)
=
\mathfrak D_{q+2}(a,b)
+
\langle\Phi_q^{\rm p}(a),\Phi_q^{\rm p}(b)\rangle
-
\langle\Phi_q^1(a),\Phi_q^1(b)\rangle.
}
\]

The completed logarithmic derivative has only one surviving negative boundary channel after the Gamma ground mode and the \(s=0\) pole are paired.

## 3. SU(1,1) meaning of the positive Gamma remainder

Let \(K_0\) be the compact generator in the universal paired \(k=1/2\) module,
\[
K_0e_n=\left(n+\frac12\right)e_n.
\]

Its heat character is
\[
\chi_{1/2}(x)
=
\operatorname{Tr}e^{-2xK_0}
=
\frac1{2\sinh x}.
\]

Since
\[
\frac{e^{-(q+2)x}}{1-e^{-2x}}
=
e^{-(q+1)x}\chi_{1/2}(x),
\]
we obtain
\[
\boxed{
\mathfrak D_{q+2}(a,b)
=
\int_0^\infty
e^{-(q+1)x}
\operatorname{Tr}(e^{-2xK_0})
(1-e^{-ax})(1-e^{-bx})\,dx.
}
\]

Equivalently, if
\[
R_c=(2K_0+c-1)^{-1},
\]
then the four-term combination is trace class and
\[
\boxed{
\mathfrak D_{q+2}(a,b)
=
\operatorname{Tr}
\left[
R_{q+2}
-R_{q+a+2}
-R_{q+b+2}
+R_{q+a+b+2}
\right].
}
\]

Thus the entire surviving Gamma correction is a positive finite-difference resolvent trace of the same \(K_0\) that generates the prime TFD heat character.

## 4. The only negative channel is the PNT continuum baseline

The remaining negative kernel is
\[
\langle\Phi_q^1(a),\Phi_q^1(b)\rangle
=
\int_0^\infty
e^{-(q-1)x}
(1-e^{-ax})(1-e^{-bx})\,dx.
\]

Set \(y=e^x\). Since \(dx=dy/y\),
\[
e^{-(q-1)x}\,dx
=
y^{-q}\,dy.
\]

Therefore
\[
\boxed{
\langle\Phi_q^1(a),\Phi_q^1(b)\rangle
=
\int_1^\infty
y^{-q}
(1-y^{-a})(1-y^{-b})\,dy.
}
\]

The positive prime square is
\[
\boxed{
\langle\Phi_q^{\rm p}(a),\Phi_q^{\rm p}(b)\rangle
=
\sum_{n\ge2}
\Lambda(n)n^{-q}
(1-n^{-a})(1-n^{-b}).
}
\]

Writing the Chebyshev measure
\[
d\psi(y)=\sum_{n\ge2}\Lambda(n)\,\delta_n(dy),
\]
the signed arithmetic remainder is exactly

\[
\boxed{
\int_1^\infty
y^{-q}(1-y^{-a})(1-y^{-b})
\,d(\psi(y)-y).
}
\]

Hence the completed kernel admits the reduced exact form

\[
\boxed{
\Delta_qB(a,b)
=
\mathfrak D_{q+2}(a,b)
+
\int_1^\infty
y^{-q}(1-y^{-a})(1-y^{-b})
\,d(\psi(y)-y).
}
\]

## 5. Interpretation

This is a sharper separation than the original four-field Krein square.

The real-place completion splits into:

1. a manifestly positive excited Gamma/SU(1,1) tower
   \[
   \mathfrak D_{q+2}\succeq0;
   \]

2. a single signed prime-versus-continuum discrepancy
   \[
   d\psi(y)-dy.
   \]

The \(dy\) term is exactly the continuum density associated with the zeta pole at \(s=1\). The prime measure has the same leading density by the prime number theorem.

Thus the sole surviving ghost is not an arbitrary negative sector. It is precisely the smooth continuum baseline that the discrete von-Mangoldt measure must be compared against.

## 6. Why fixed-q positivity still fails

This simplification does not evade the ultraviolet/support obstruction already proved in the RH manuscript. At a fixed \(q\), the discrepancy measure
\[
d\psi-dy
\]
is signed, and the positive Gamma remainder does not dominate it on every finite feature combination.

The gain is conceptual and constructive: there is now only one genuinely unresolved signed channel.

## 7. New global target

The RH problem can be sharpened to:

Construct the global Archimedean/rational sewing for the single discrepancy
\[
d\psi-dy
\]
inside the positive \(k=1/2\) SU(1,1) Gamma resolvent background.

Equivalently, seek the positive parent operator whose conditional/Schur complement produces
\[
\mathfrak D_{q+2}
+
\int y^{-q}(1-y^{-a})(1-y^{-b})\,d(\psi-y)
\]
after the nonlocal \(q\)-integration / Stieltjes completion already known to be equivalent to RH.

This is a one-ghost completion problem, not a two-independent-ghost problem.
