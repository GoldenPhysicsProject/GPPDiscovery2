# Number entropy, the canonical Nyman transfer, and the bad-zero entropy

Date: 2026-09-17
Status: exact identities plus literature-identified BSY criterion. No RH claim.

## 1. Arithmetic prime-gas thermodynamics

For real beta > 1, use positive integers n as microstates with arithmetic energy E_n = log n and

P_beta(n) = n^{-beta}/zeta(beta).

Then

Z(beta)=zeta(beta),
U(beta)=-zeta'(beta)/zeta(beta)=sum_{n>=2} Lambda(n)n^{-beta},
S_N(beta)=log zeta(beta)+beta U(beta).

Hence

S_N'(beta)=beta U'(beta)
          =-beta sum_{n>=2} Lambda(n) log(n)n^{-beta}.

Thus the Nyman/Ramanujan target coefficients Lambda(n) and the prime-gas Fisher/heat-capacity density Lambda(n) log(n)n^{-beta} are the same arithmetic vector before and after scale differentiation plus Gibbs weighting.

## 2. The canonical Nyman transfer is a normalized partition function

For 0<lambda<1 the Nyman generator has Mellin transform

rhohat_lambda(s)=((lambda-lambda^s)/s) zeta(s).

Factor

rhohat_lambda(s)=Z_N(s) ((lambda-lambda^s)/(s-1)),

where

Z_N(s)=((s-1)/s) zeta(s).

This Z_N is the common causal transfer function of the Nyman family. It is also a canonical pole-subtracted arithmetic partition function:

Z_N(1)=1,
Z_N(s)->1 as real s->+infinity,
|Z_N(1/2+it)|=|zeta(1/2+it)|

because |(s-1)/s|=1 on Re(s)=1/2.

Its logarithmic energy response is

U_N(s)=-d/ds log Z_N(s)
      =-zeta'(s)/zeta(s)-1/(s-1)+1/s
      =U(s)-1/(s-1)+1/s.

Using zeta(1+epsilon)=epsilon^{-1}+gamma+O(epsilon),

Z_N(1+epsilon)=1+(gamma-1)epsilon+O(epsilon^2),

so

U_N(1)=1-gamma.

If one formally keeps the canonical entropy expression

S_N^ren(s)=log Z_N(s)+s U_N(s),

then

S_N^ren(1)=1-gamma.

This is a genuine dimensionless Cayley-renormalized Hagedorn response constant. It should NOT be confused with a Boltzmann constant: a Boltzmann constant is a unit-conversion factor, whereas 1-gamma is a derived finite response value.

## 3. No independent arithmetic Boltzmann constant in the prime gas alone

Restore an arithmetic energy unit epsilon_* and an entropy/temperature conversion k_N:

E_n=epsilon_* log n,
P(n) proportional to exp[-E_n/(k_N T_N)].

Then

P(n) proportional to n^{-beta},
beta=epsilon_*/(k_N T_N).

Only epsilon_*/(k_N T_N) is observable in the pure prime gas. The simultaneous rescaling

epsilon_* -> c epsilon_*,
k_N -> c k_N

leaves the distribution and all dimensionless thermodynamics unchanged. Therefore the prime gas by itself cannot determine a nontrivial independent k_N. In canonical arithmetic units one sets k_N=1 and entropy is measured in nats. A dimensionful nontrivial k_N can acquire meaning only after another sector independently fixes both an arithmetic energy scale and a physical temperature scale.

## 4. Nyman target equals the internal-energy coefficient vector

In the Casimir/Ramanujan exact-conductor basis R_m, the target coupling derived previously is

<delta_0,R_m>_{-1,C}=-Lambda(m).

But Lambda(m) is exactly the Dirichlet coefficient of the arithmetic internal energy U(s). Thus the Nyman target is the negative internal-energy coefficient vector in exact-conductor coordinates.

Differentiating in beta promotes Lambda(m) to Lambda(m) log(m)m^{-beta}, exactly the positive Fisher/heat-capacity measure already used in arithmetic field theory.

## 5. Bad-zero model space and a canonical ghost entropy

Let B be the Blaschke product of the zeros rho of zeta with Re(rho)>1/2, in the disk Cayley coordinate

beta_C=(s-1)/s.

The zero rho maps to

a_rho=(rho-1)/rho,

which lies in the disk precisely when Re(rho)>1/2.

The Nyman-Burnol ghost is

K_B=H^2 \ominus B H^2.

For the Hardy vacuum 1,

||P_{K_B}1||^2=1-|B(0)|^2.

Define

S_ghost=-log |B(0)|^2 >= 0.

Then

||P_{K_B}1||^2=1-exp(-S_ghost).

Since |a_rho|=|rho-1|/|rho|,

S_ghost=sum_{Re(rho)>1/2} m_rho log(|rho|^2/|rho-1|^2),

with the usual Blaschke interpretation if the sum is infinite. Every term is nonnegative because

|rho|^2-|rho-1|^2=2 Re(rho)-1>0.

RH is equivalent to S_ghost=0.

## 6. BSY equals the Casimir ghost entropy

The Balazard-Saias-Yor formula gives

integral_{-infinity}^{infinity} log|zeta(1/2+it)|/(t^2+1/4) dt
 = 2 pi sum_{Re(rho)>1/2} m_rho log|rho/(1-rho)|.

Therefore

S_ghost
 = (1/pi) integral_R log|zeta(1/2+it)|/(t^2+1/4) dt.

Equivalently, with the normalized Cauchy/harmonic measure

dmu_C(t)=dt/[2 pi (t^2+1/4)],

-log|B(0)| = E_{mu_C}[log|zeta(1/2+iT)|],
S_ghost = 2 E_{mu_C}[log|zeta(1/2+iT)|].

The weight 1/(t^2+1/4) is exactly the spectral multiplier of the Casimir Green operator

H_C^{-1}=(-D^2+1/4)^{-1}.

Thus the same Casimir metric that makes the logarithmic Nyman map an exact negative-graph isometry also measures the Jensen/BSY entropy of the bad-zero sector.

This gives the exact framework identity

Nyman ghost <-> K_B <-> Casimir H_C^{-1} <-> critical-line log-partition ghost entropy.

The BSY criterion itself is classical; the point here is its exact identification with the Casimir graph and arithmetic thermodynamic structures already present in GPP.

## 7. Inner-outer thermodynamic split

The normalized transfer satisfies

Z_N(1)=1.

If its canonical factorization is

Z_N = B O

in the Nyman Hardy half-plane, then at the Cayley origin

0=log|Z_N(1)|=log|B(0)|+log|O(0)|,

so

-log|B(0)|=log|O(0)|.

The bad-zero Jensen entropy is therefore exactly the outer gain needed to compensate the inner attenuation at the thermodynamic/Hagedorn base point.

The logarithmic derivative also splits:

U_N = -B'/B - O'/O

(with derivatives taken in a common coordinate). At the base point the total is the finite constant 1-gamma. This gives a precise future target: determine whether the inner contribution can be bounded or eliminated using the zero-independent arithmetic/Fisher data of the outer channel. No such bound is proved here.

## 8. Operator range statement

The exact-conductor arithmetic inputs are triangularly complete in the orthonormal logarithmic cell space found previously. Their outputs under the common transfer Z_N have the same closed span as the reciprocal Nyman generators. By the Nyman-Burnol theorem and the Baez-Duarte reciprocal reduction,

closure Ran(T_{Z_N}) = B H^2.

Therefore

P_range = M_B M_B^*,
P_ghost = I-M_B M_B^*.

Equivalently, after Z_N=B O,

the outer factor O is cyclic on the arithmetic cell input subspace, and the entire obstruction is the inner factor B.

This is the correct operator endpoint. Another boundary quadratic-form argument can see |O| but is blind to B. Closure requires an interior/causal theorem that forces B to be constant.

## 9. Next targets

1. Formalize the algebraic identity U_N(s)=U(s)-1/(s-1)+1/s and the Nyman factorization through Z_N.
2. If Mathlib has the needed Laurent expansion infrastructure, formalize U_N(1)=1-gamma; otherwise keep this as an analytic discovery theorem pending infrastructure.
3. Express the prime-gas Fisher hierarchy as the scale derivative of the Lambda target vector in the exact-conductor/Casimir basis.
4. Study the inner/outer derivative split at the Cayley origin and compare the inner Green/Jensen energy with the BPY/Hardy anticausal leakage operator.
5. Search for a zero-independent entropy-production or passivity inequality strong enough to give an upper bound S_ghost<=0. Since BSY gives S_ghost>=0, such an upper bound would force S_ghost=0 and RH. No such inequality is presently known or claimed.
