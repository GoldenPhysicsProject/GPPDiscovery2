# Number entropy, the canonical Nyman transfer, and the bad-zero entropy

Date: 2026-09-17
Status: exact identities plus literature-identified BSY criterion. No RH claim.

## 1. Arithmetic prime-gas thermodynamics

For real beta > 1, positive integers are microstates with arithmetic energy E_n = log n and

P_beta(n) = n^{-beta}/zeta(beta).

Then

Z(beta)=zeta(beta),
U(beta)=-zeta'(beta)/zeta(beta)=sum_{n>=2} Lambda(n)n^{-beta},
S_N(beta)=log zeta(beta)+beta U(beta),

and

S_N'(beta)=-beta sum_{n>=2} Lambda(n) log(n)n^{-beta}.

Thus the Nyman/Ramanujan target coefficients Lambda(n) and the prime-gas Fisher/heat-capacity density Lambda(n) log(n)n^{-beta} are the same arithmetic vector before and after scale differentiation and Gibbs weighting.

## 2. Canonical normalized Nyman transfer

For 0<lambda<1,

rhohat_lambda(s)=((lambda-lambda^s)/s) zeta(s)
                =Z_N(s) ((lambda-lambda^s)/(s-1)),

where

Z_N(s)=((s-1)/s) zeta(s).

This is the common causal transfer of the continuum Nyman family and a canonical pole-subtracted arithmetic partition function:

Z_N(1)=1,
Z_N(s)->1 as real s->+infinity,
|Z_N(1/2+it)|=|zeta(1/2+it)|.

Its logarithmic response is

U_N(s)=-d/ds log Z_N(s)
      =-zeta'(s)/zeta(s)-1/(s-1)+1/s.

From zeta(1+epsilon)=epsilon^{-1}+gamma+O(epsilon),

Z_N(1+epsilon)=1+(gamma-1)epsilon+O(epsilon^2),
U_N(1)=1-gamma.

If one keeps the canonical entropy expression S_N^ren=log Z_N+s U_N, then

S_N^ren(1)=1-gamma.

This is a dimensionless finite Hagedorn response value, not a Boltzmann conversion constant.

## 3. No independent arithmetic Boltzmann constant from the prime gas alone

If

E_n=epsilon_* log n,
P(n) proportional to exp[-E_n/(k_N T_N)],

then beta=epsilon_*/(k_N T_N). Only this ratio is observable in the pure arithmetic ensemble. Simultaneously rescaling epsilon_* and k_N leaves the theory unchanged. Hence the prime gas alone does not determine a nontrivial dimensionful k_N. In canonical arithmetic units k_N=1 and entropy is measured in nats.

## 4. Nyman target equals the internal-energy coefficient vector

In the Casimir/Ramanujan exact-conductor basis R_m,

<delta_0,R_m>_{-1,C}=-Lambda(m).

But Lambda(m) is exactly the Dirichlet coefficient of U(s). Thus the Nyman target is the negative arithmetic internal-energy coefficient vector in exact-conductor coordinates.

## 5. Continuum bad-zero model space and ghost entropy

For the full continuum Nyman space, let B be the Blaschke product of zeros rho with Re(rho)>1/2 in the Cayley coordinate beta_C=(s-1)/s. Then

K_B=H^2 \ominus B H^2.

For the Hardy vacuum,

||P_{K_B}1||^2=1-|B(0)|^2.

Define

S_ghost=-log|B(0)|^2 >= 0.

Then

||P_{K_B}1||^2=1-exp(-S_ghost),

and

S_ghost=sum_{Re(rho)>1/2} m_rho log(|rho|^2/|rho-1|^2)

with the usual Blaschke interpretation. RH is equivalent to S_ghost=0.

## 6. BSY equals the Casimir ghost entropy

Balazard-Saias-Yor gives

integral_R log|zeta(1/2+it)|/(t^2+1/4) dt
 =2 pi sum_{Re(rho)>1/2} m_rho log|rho/(1-rho)|.

Therefore

S_ghost=(1/pi) integral_R log|zeta(1/2+it)|/(t^2+1/4) dt.

The weight 1/(t^2+1/4) is exactly the spectral multiplier of

H_C^{-1}=(-D^2+1/4)^{-1}.

Thus the continuum Nyman bad-zero defect is measured by the same Casimir Green weight used by the logarithmic Nyman graph.

## 7. Inner-outer thermodynamic split

For a canonical factorization Z_N=B O in the continuum Nyman Hardy half-plane,

0=log|Z_N(1)|=log|B(0)|+log|O(0)|,

hence

-log|B(0)|=log|O(0)|.

The bad-zero Jensen entropy is exactly the outer gain compensating inner attenuation at the base point. This is an identity, not a proof that B is constant.

## 8. Correction: the reciprocal/cell range is not known to equal B H^2 off RH

The exact-conductor arithmetic inputs are triangularly complete in the orthonormal logarithmic cell space, and their outputs have the same closed span as the reciprocal Baez-Duarte family.

However, Baez-Duarte's strong criterion proves that RH is equivalent to the target lying in the reciprocal closure. Bagchi/Noor strengthen this to: RH iff the corresponding discrete Hardy span is dense in H^2. These results do NOT identify the reciprocal closed span with the continuum Nyman space B H^2 when RH fails.

Therefore the earlier statement

closure Ran(T_{Z_N}|cell) = B H^2

was unjustified and is retracted.

The correct hierarchy is:

N_discrete subset N_continuum,
closure(N_continuum)=B H^2,
RH iff closure(N_discrete)=H^2.

Thus, off RH, the discrete orthogonal defect may contain the continuum bad-zero defect plus an additional sampling/completeness defect. One must not identify the two without a theorem.

This correction makes the discrete boundary-regularity theory of Bagchi/Noor directly relevant: it can constrain the extra sampling defect instead of silently assuming it absent.

## 9. Exact Euler boundary split

For the contraction C=M_sqrt(1-{e^t}) and v_1(t)=e^{-t/2}, ||v_1||=1,

||C v_1||^2=gamma,
||(I-C^2)^(1/2) v_1||^2=1-gamma.

Equivalently,

1-gamma=int_1^infinity {x}/x^2 dx.

Thus the same finite Hagedorn response 1-gamma is the exact fractional-part defect weight of the Euler/Nyman contraction at the boundary state.

## 10. Next targets

1. Use the exact Casimir-to-weighted-Bergman identification to compare directly with Noor's unitary Hardy model of the reciprocal criterion.
2. Keep the continuum K_B defect and the discrete reciprocal defect distinct.
3. Translate Noor's local-Dirichlet no-ghost theorem into the Casimir tail variables.
4. Determine whether the Casimir/shadow structure supplies the extra boundary regularity that would force the discrete ghost into the local Dirichlet domain.
5. Formalize the elementary algebraic identities above where Mathlib infrastructure suffices.
