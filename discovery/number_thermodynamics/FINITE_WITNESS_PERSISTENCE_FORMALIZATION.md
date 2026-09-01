# Finite three-point Fisher witness: persistence result

Codex/GPT track.

The finite Fisher/Vandermonde layer in `GPPVerify2` has now been strengthened from nonnegativity to strict positivity from a single three-point witness.

For finite support weights `p_i >= 0` and observables `x_i`, define the ordered energy

\[
E(p,x)=\sum_{i,j,k}p_i p_j p_k\big[(x_i-x_j)(x_i-x_k)(x_j-x_k)\big]^2.
\]

If there exist `i,j,k` with

\[
p_i,p_j,p_k>0,
\qquad
x_i\ne x_j,\quad x_i\ne x_k,\quad x_j\ne x_k,
\]

then one summand is strictly positive and every summand is nonnegative, hence

\[
\boxed{E(p,x)>0}.
\]

The exact finite moment identity already present in Verify2 is

\[
E(p,x)=D(m_0,m_1,m_2,m_3,m_4),
\]

where `D` is the cubic moment discriminant, together with

\[
6\,N_F=m_0D,
\]

where `N_F` is the mass-aware Fisher covariance numerator. Because the same witness gives `m_0>0`, the strengthened finite theorem yields

\[
\boxed{N_F>0}.
\]

This is the precise finite-prefix persistence mechanism needed for the two-parameter number-Gibbs model. Once a finite prefix contains three positive weights at three distinct log-support values, every larger prefix retains a strictly positive Fisher numerator.

For

\[
w_n(\beta,\eta)=n^{-\beta}e^{-\eta(\log n)^2},
\qquad x_n=\log n,
\]

all weights are strictly positive for finite real `beta,eta`, and `x_1=0`, `x_2=\log2`, `x_3=\log3` are pairwise distinct. Therefore every prefix containing states `1,2,3` has strict finite Fisher positivity.

What remains for strict *countable* positivity is not another finite Vandermonde argument. The remaining analytic step is to preserve a positive lower witness through the countable moment limit. Mere convergence of positive finite numerators to a limit only gives nonnegativity; strictness requires either:

1. a uniform lower bound by the fixed `(1,2,3)` Vandermonde contribution, or
2. a countable Cauchy-Binet/Vandermonde expansion whose positive `(1,2,3)` term survives explicitly.

The second route aligns directly with the first-correction asymptotics already derived for the two-parameter number-Gibbs determinant.

## Verify2 commits

- `049f61b26993d43707d7e6dfee4a3ef243d0189d`: strict ordered Vandermonde energy from one witness.
- `b1dcd0ec8c374eae1278c62800bf487ff2f69be2`: strict mass-aware finite Fisher numerator from one witness.

No RH/Weil claim follows from this result; it is a finite/countable thermodynamic Fisher-geometry ingredient only.
