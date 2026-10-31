# The genuine completed first-prime Weil form is strictly positive on the ENTIRE mirror-odd Hilbert subspace at L=7/10

**2026-10-31, Codex / GPPDiscovery2; new all-function, true-prime, first activation result.** This supersedes the earlier locally endpoint-even restricted-subspace result. It is a rigorous analytic infinite-dimensional positivity theorem for **all globally reflection-odd complex functions** on a single fixed logarithmic support L=0.7, including the actual p=2 atom and all corrected pole/Archimedean terms. It does NOT prove positivity in the globally mirror-even sector, other support lengths, or RH.

## Theorem

Let \(L=7/10\), \(a=\log 2<L<\log3\), \(\varepsilon=L-a>0\), and let the true corrected completed v34 Weil quadratic form \(Q_L\) act on the completed logarithmic kinetic form domain of \(L^2(0,L;\mathbb C)\). Let \(\Theta f(x)=f(L-x)\). Then

\[
\boxed{
\text{For every }f\in\mathrm{Dom}(Q_L)\text{ with }\Theta f=-f,\qquad
Q_L[f]\ge\frac1{100}\|f\|_2^2.
}
\]

**No restrictions whatsoever on the local symmetry or endpoint traces of f**, unlike the previous compatibility theorem. The class is infinite-dimensional and includes endpoint-supported functions in both signs of the first-prime source. This is positivity of the **actual completed prime-inclusive form** at L=0.7, **not** merely E−S positivity or an extrapolated finite Fourier test.

## Proof 1: exact completed source including the real first-prime edge

Define \(H(z)=\log\coth(z/2)\),
\[
V_L(x)=\tfrac12[H(x)+H(L-x)],\quad
r(y)=\frac{e^{y/2}-1}{2\sinh y},\quad
\Gamma_L(x)=\int_0^x r(y)dy+\int_0^{L-x}r(y)dy,
\]
and \(c_\infty=\log(4\pi)+\gamma_E\). The exact completed positive gamma interior jump is
\[
J_\gamma[f]=\int_0^L\frac{e^{y/2}}{2\sinh y}
 \int_0^{L-y}|f(x+y)-f(x)|^2 dx\,dy.
\]
Let \(C_f=\int_0^L f(x)\cosh((x-L/2)/2)dx\),
\(T_f=\int_0^L f(x)\sinh((x-L/2)/2)dx\).
At this L only the prime power n=2 is active, with \(w=a/\sqrt2\). Define end strips \(A=[0,\varepsilon]\), \(B=[a,L]\), and
\(D[f]=\int_0^\varepsilon|f(x)-f(x+a)|^2 dx\).

The EXACT full form identity (see discovery/first_prime_exact_completed_resource_ledger.md) is
\[
\boxed{Q_L[f]=\int_0^L
(V_L-\Gamma_L-c_\infty-w1_{A\cup B})|f|^2 dx
+J_\gamma[f]+wD[f]+2|C_f|^2-2|T_f|^2.}
\]
This includes the full gamma tail, correct negative odd pole and the actual signed arithmetic prime; the identity does not presume RH or any fitted contact.

## Proof 2: PAY THE ENTIRE prime boundary mass using ONLY the unused Hardy TAYLOR REMAINDER

Let \(t=(x-L/2)/L\). For \(x\in(0,L)\), the symmetric Hardy potential has the convergent **positive even-power series**
\[
V_L(x)=H(L/2)+\sum_{r=1}^\infty K_{2r}t^{2r},\quad
K_{2r}=\frac{L^{2r}}{(2r)!}H^{(2r)}(L/2)>0.
\]
It follows directly from \(H(z)=2\sum_{j\ge0}e^{-(2j+1)z}/(2j+1)\) and the cosh expansion. For R=6 define
\[
P_6(t)=H(L/2)+\sum_{r=1}^{6}K_{2r}t^{2r},\qquad
R_6(t)=V_L(x)-P_6(t)=\sum_{r\ge7}K_{2r}t^{2r}\ge0.
\]
Because EVERY K is strictly positive, \(R_6(t)\) is increasing as \(|t|\) increases from 0 to 1/2. The two endpoint strips satisfy \(|t|\ge(\tfrac12-\varepsilon/L)\). Therefore the **minimum** of the true unused remainder on their union is exactly at x=ε or x=a:
\[
\inf_{x\in A\cup B} R_6(t(x))
=\tfrac12\bigl[H(\varepsilon)+H(a)\bigr]
-H(L/2)-\sum_{r=1}^6 K_{2r}
\bigl(\tfrac{\varepsilon-L/2}{L}\bigr)^{2r}.
\]
Here **H(log2)=log3** exactly. A 256-bit outward FLINT/Arb calculation using exact rational L=7/10, exact a=log2, exact recurrence for the 12th Hardy derivative and exact Arb transcendentals certifies
\[
\boxed{
\inf_{x\in A\cup B}R_6(t(x))
=0.51086057394217007168\ldots
> w=\frac{\log2}{\sqrt2}
=0.49012907173427359585\ldots
}
\]
with a rigorous **strict surplus >0.02073**, not a grid sample. Since the remainder is nonnegative everywhere,
\[
\boxed{V_L(x)-w\,1_{A\cup B}(x)\ge P_6(t(x))
\quad\text{for a.e. }x\in(0,L).}
\]
This is the central new mechanism: **the same positive Hardy singularity near the endpoints pays the ENTIRE negative p=2 boundary tax, pointwise, while leaving all six finite positive Hardy curvature modes and the actual positive prime-edge gradient wD untouched.** No portion of V is double spent.

## Proof 3: an entire infinite-dimensional odd-sector Schur argument

In the exact completed Q, use the pointwise bound just proved and drop ONLY the positive \(wD\). For global mirror-odd f, the pole cosh moment vanishes \(C_f=0\), while the actual negative odd sinh pole obeys
\(-2|T_f|^2\ge-2(\sinh(L/2)-L/2)\|f\|^2\). The regular gamma tilt satisfies \(\Gamma_L\le e^{L/4}-1\). The rigorously established gamma jump surplus on \(0<y\le7/10\) yields
\[
J_\gamma[f]\ge \sum_{n\ge1}(H_n+11L/50)|f_n|^2
\]
in normalized shifted-Legendre coordinates, where \(H_n\) are harmonic numbers and \(f_n=\langle e_n,f\rangle\). For global odd f only odd Legendre n appear. Hence
\[
Q_L[f]\ge
\Bigl[-\log\tanh(L/4)-(e^{L/4}-1)-c_\infty\Bigr]\|f\|^2
+\sum_{n\text{ odd}}(H_n+11L/50)|f_n|^2
+\sum_{r=1}^6 K_{2r}\|t^r f\|^2
-2(\sinh(L/2)-L/2)\|f\|^2.
\]
All terms are genuine **lower bounds** on the actual completed prime-inclusive form.

The exact Legendre Jacobi recurrence gives multiplication by \(t^{2r}\) bandwidth \(2r\); with R=6, split the odd basis into finite low \(e_1,e_3,\ldots,e_{11}\) (six coefficients) and **every** odd high \(e_{13},e_{15},\ldots\). The only cross coupling is via the first six high odd indices \(13,15,\ldots,23\), computed by exact products of the Jacobi matrix. The high–high Hardy curvature is **positive** and may be dropped only as a LOWER bound; harmonic-number plus gamma surplus supplies the explicit scalar high floor
\[
h_o=\beta+H_{13}+11L/50-2(\sinh(L/2)-L/2),
\quad\beta=-\log\tanh(L/4)-(e^{L/4}-1)-c_\infty.
\]
For κ=1/100, the exact low 6×6 Schur matrix
\(M_o-\kappa I-C_o C_o^\mathsf{T}/(h_o-\kappa)\) is **strictly positive by outward 256-bit Arb LDL**, with all SIX pivots positive; its smallest printed pivot ≈0.07583694909, and the high floor satisfies \(h_o>\kappa\). Completing the square against the **entire infinite high Hilbert subspace**, not a Galerkin extrapolation, proves the theorem.

**Reproducible certificate:** discovery/arb_true_p2_odd_hardy_remainder_7_10.py; GitHub Actions **41232717596 SUCCESS**, exact workflow head 5792ce996f11ad31f51e330bf6216cd43fb018bd. The successful output prints the strictly enclosed endpoint remainder, w, all six positive Hardy coefficients and six positive odd LDL pivots. The earlier prime-omitted odd background check 41232465138 is no longer needed for this stronger result; the preceding restricted local-parity theorem is superseded.

## Significance and limits

1. We have **strict positivity for the ACTUAL completed, first-prime-inclusive Weil form** at a support length *past log2*, on the **entire infinite-dimensional mirror-odd test sector**. Both locally stabilizing and locally destabilizing p2 configurations are covered. This is stronger than the locally endpoint-even conditional result and stronger than merely absorbing E−S.
2. The proof is not based on a globally positive p2-omitted Q0. In fact at L=3/4 a certified odd Legendre witness gives Q0<0 and the true p2 source repairs it. The decisive new resource is the **positive Hardy Taylor remainder localized precisely where the arithmetic prime tax lives**.
3. It still does NOT prove positivity for the mirror-EVEN sector at L=0.7, does not control all support lengths or all primes, does not rule out shifted false-zeta Fθ, and hence does not prove RH. A numerical near-null mirror-even mode at much larger support remains the primary global obstruction.
4. Next natural attempt: use a shorter Hardy tower whose unused endpoint remainder still pays w, while retaining enough curvature/J_gamma/pole structure to prove a mirror-EVEN one-sided Schur bound, or a more faithful non-polynomial localized Hardy remainder split. Do not use the prime-free Q0 gap at all L; that hypothesis is independently falsified by L=3/4.
