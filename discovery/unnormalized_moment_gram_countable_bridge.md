# Unnormalized moment-Gram route to the countable two-parameter Fisher witness

## Result

For a positive discrete measure with weights `w_n` and support values `x_n`, define moments

`m_k = sum_n w_n x_n^k`, `k = 0,...,4`,

and the 3x3 moment Gram determinant

`D = m0 (m2 m4 - m3^2) - m1 (m1 m4 - m2 m3) + m2 (m1 m3 - m2^2)`.

For finite support, Cauchy--Binet gives exactly

`D = sum_{i<j<k} w_i w_j w_k (x_i-x_j)^2 (x_i-x_k)^2 (x_j-x_k)^2`.

The key point for the countable Gibbs problem is that finite prefixes do **not** need to be renormalized. If the weighted moments through order four converge absolutely, then the finite-prefix moments `m_k^(N)` converge to `m_k`; hence the determinant, being a polynomial in those five moments, converges to `D`. The finite Cauchy--Binet sums are monotone because every term is nonnegative, so their limit is the countable triple sum. Therefore

`D = sum_{i<j<k} w_i w_j w_k Vandermonde(x_i,x_j,x_k)^2`.

For normalized weights (`m0=1`) this Gram determinant is exactly the covariance determinant of `(X,X^2)`. Thus any fixed positive triple is a quantitative lower witness for the infinite Fisher determinant.

For the two-parameter number Gibbs family

`w_n = exp(-beta log n - eta (log n)^2) / Z(beta,eta)`, `eta > 0`,

choose `n=1,2,3`, so `x=(0,log 2,log 3)`. Then

`det g >= w_1 w_2 w_3 [log 2 log 3 log(3/2)]^2 > 0`,

or equivalently

`det g >= exp(-beta log 6 - eta[(log 2)^2+(log 3)^2]) / Z(beta,eta)^3 * [log 2 log 3 log(3/2)]^2 > 0`.

## Formalization consequence

The previous normalization/truncation obstacle can be removed. The finite unnormalized three- and four-state identities are now formalized in `GPPVerify2/GppVerify/RiemannHypothesis/UnnormalizedMomentGramVandermonde.lean`. The remaining Lean work is:

1. general finite Cauchy--Binet for an arbitrary finite prefix, or an equivalent finite-set induction;
2. convergence of the five two-parameter Gibbs moments for `eta > 0`;
3. continuity of the determinant polynomial under those moment limits;
4. monotone convergence of the nonnegative triple-minor partial sums.

This route yields the infinite determinant identity itself, not merely qualitative positive-definiteness.

## Boundaries

This is a thermodynamic/Fisher result. It does not imply Weil positivity or RH. It also does not alter the scalar-box DCT, Yang--Mills sewing, or spectral chamber-convolution boundaries.
