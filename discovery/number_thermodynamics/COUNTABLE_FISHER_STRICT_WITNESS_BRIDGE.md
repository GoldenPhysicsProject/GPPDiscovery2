# Countable Fisher strict-witness bridge

## Result

Let

\[
m_r^{(N)}=\sum_{n<N} w_n x_n^r,\qquad
m_r=\sum_{n\ge 0} w_n x_n^r,
\]

and let the division-free Fisher numerator be

\[
D(m_0,\ldots,m_4)
=(m_0m_2-m_1^2)(m_0m_4-m_2^2)
-(m_0m_3-m_1m_2)^2.
\]

If the weighted moments through order four are summable, then the existing
`CountableFisherMomentLimit` theorem gives

\[
D(m_0^{(N)},\ldots,m_4^{(N)})\to D(m_0,\ldots,m_4).
\]

Therefore a full countable Cauchy--Binet identity is *not required* merely to
prove strict positivity.  It is enough to produce one constant `c>0` such that

\[
D(m_0^{(N)},\ldots,m_4^{(N)})\ge c
\]

for every sufficiently large prefix.  Closedness of `[c,\infty)` under limits
then yields

\[
D(m_0,\ldots,m_4)\ge c>0.
\]

At unit total mass this is exactly strict positivity of the two-parameter
Fisher covariance determinant.

## Application target: zeta-Gibbs family

For

\[
w_n(\beta,\eta)=Z(\beta,\eta)^{-1}
\exp[-\beta\log n-\eta(\log n)^2],\qquad \eta>0,
\]

all weights are strictly positive.  The fixed states `n=1,2,3` have
Vandermonde witness

\[
c_{123}
=w_1w_2w_3
[\log 2\,\log 3\,\log(3/2)]^2>0.
\]

The remaining finite theorem should therefore be phrased as persistence of a
selected positive Vandermonde minor under addition of further nonnegative
states.  Once that is formalized, the new countable strict-witness bridge
passes `c_{123}` to the infinite determinant directly.

This route is strictly weaker than proving the full countable Cauchy--Binet
series identity, but it is sufficient for nondegeneracy of the Fisher metric.
The full identity remains mathematically valuable as a later strengthening.

## Formal status

`GPPVerify2` now contains the generic limit-transfer interface in
`CountableFisherStrictWitness.lean`.  The next missing theorem is the arbitrary
finite-prefix persistence/lower-bound lemma; no new limit argument is needed.
