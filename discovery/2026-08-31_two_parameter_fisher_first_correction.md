# Codex/GPT continuation — two-parameter Fisher first correction

For the number-Gibbs family
\[
Z(\beta,\eta)=\sum_{n\ge1}e^{-\beta\log n-\eta(\log n)^2},\qquad \eta>0,
\]
let `L123` denote the normalized Vandermonde contribution of the triple `n=(1,2,3)` to the Fisher determinant of `(X,X^2)`, with `X=log n`.

The previous leading asymptotic was
\[
\det g/L_{123}\to1\qquad(\eta\to\infty).
\]
The finite Vandermonde ordering gives a sharper discovery. The leading quadratic cost is uniquely the triple `(1,2,3)`, with cost `(log 2)^2+(log 3)^2`. The unique next cost is `(1,2,4)`, with cost `(log 2)^2+(log 4)^2`. Hence, for fixed real `beta`, the candidate first correction is
\[
\frac{\det g}{L_{123}}
=1+C_\beta e^{-\eta\Delta}+o(e^{-\eta\Delta}),
\]
where
\[
\Delta=(\log4)^2-(\log3)^2
\]
and
\[
C_\beta=(4/3)^{-\beta}
\frac{4(\log2)^4}{(\log3)^2[\log(3/2)]^2}.
\]
The coefficient follows exactly from the ratio of the `(1,2,4)` and `(1,2,3)` Gibbs weights and squared Vandermonde factors. The normalization `Z^{-3}` cancels from the ratio.

For `beta=1`,
\[
\Delta\approx0.7148630948602235,\qquad
C_1\approx3.490014400919589.
\]
The executable probe `discovery/two_parameter_fisher_first_correction.py` gives:

- eta=10: exact `det g/L123 = 1.0027499746...`; first-correction prediction `1.0027429396...`.
- eta=15: exact `1.0000769041...`; prediction `1.0000768972...`.
- eta=20: exact `1.0000021558...`; prediction `1.0000021558...`.

Thus the first exponentially small correction explains essentially all of the previously observed deviation by eta=15–20.

Status: executable discovery, not yet a Lean theorem. A rigorous countable asymptotic requires (i) finite-prefix Vandermonde-minor persistence, (ii) proof that `(1,2,4)` is the unique second-cost triple, and (iii) a uniform tail estimate showing all remaining triples are `o(exp(-eta Delta))` relative to `L123` for fixed beta.

Cross-front boundaries are unchanged: scalar-box regulator removal still needs the concrete nested Integrable/AE/Tonelli/DCT assembly; YM/gravity still requires the honest fixed-loop-momentum nonzero-mu tree-sewing numerator after scalar closure; the principal-series/completed-zeta/Mehler-Fock/Wiener-Hopf structure still lacks the global prime-plus-Archimedean Weil-form identification and positivity theorem; higher Gamma chambers remain exact without a repeated-sech-convolution claim.

Claude material was not inspected or used.
