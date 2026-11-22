# A causal route to the generic inequality in Verify #660

Let c be real, M(u)=sum_{n<=exp u} mu(n)/sqrt(n), B=M-c on u>=0, zero extended to u<0. Q(L)=integral_0^L |B|². For any zero zeta(1/2+r)=0 with d=Re r>0 and every L>=0 this derivation gives

    sqrt(2d) |r-1/2| exp(dL) / |1+r|^4 <= 5/2 + 9|c| + 18 sqrt(Q(L)).

This is the generic EnergyZeroInequality with alternative constants. It is a paper derivation for audit, independent of an unconditional arithmetic upper bound. It does not deliver the earlier sharper constants.

## 1. A causal tail estimate

Suppose k is a causal L1 kernel, h a causal L2 kernel, B locally L2, h=k*B on [0,infinity), and the Laplace transform of k vanishes at r. Write hats for Laplace transforms. Then

    sqrt(2d) exp(dL) |hat h(r)| <= ||h||2 + ||k||1 ||B||_{L2(0,L)}.

Indeed split hat h(r) at L. The portion beyond L, multiplied in modulus by exp(dL), is bounded by ||h||2/sqrt(2d) by Cauchy-Schwarz. On [0,L], substitute the convolution and integrate first over B(u). The inner integral is integral_0^{L-u} exp(-rv)k(v)dv. Since hat k(r)=0, replace this by the negative integral from L-u to infinity. After multiplication by exp(dL), the absolute value of the whole piece is bounded by integral_0^L |B(u)| D(L-u)du, with D(w)=integral_w^infty |k(v)| exp(-d(v-w))dv. By weighted Cauchy-Schwarz, D(w)^2 <= ||k||1 integral_w^infty |k(v)|exp(-2d(v-w))dv. Tonelli and integration over w>=0 give ||D||2² <= ||k||1²/(2d). Apply Cauchy-Schwarz once more. All swaps on the finite triangle are absolutely convergent. No Hardy or Fourier isometry is used.

## 2. Make the kernels and prove the causal identity

On t>=0 put g_j(t)=exp(-t)t^(j-1)/(j-1)! for j=1,...,4, zero elsewhere. Set w=g_3-(3/2)g_4 and nu=sum n^(-1/2) delta_{log n}; use locally finite translates Z=nu*w, k=nu*w', h=w-cZ. Since w(0)=0, Z'=k and the causal integral of k is Z. The exact identity h=k*B follows from finite divisor sums on each finite horizon: k*M is the sum over m,n of mu(m)/sqrt(mn) w(t-log(mn)); grouping mn gives w(t). Removing c from M subtracts cZ. No Laplace uniqueness theorem is needed for this step.

For Re s>1/2 the transforms are
    hat w=(s-1/2)/(1+s)^4,  hat Z=zeta(1/2+s) hat w,  hat k=s hat Z.
The factor s-1/2 removes zeta's pole. The bounds below give holomorphic transforms for Re s>0, so the identities extend there by analytic continuation (or directly use the Euler fractional-part formula). At r, hat k(r)=hat Z(r)=0, and hat h(r)=(r-1/2)/(1+r)^4.

## 3. Size bounds without boundary Fourier estimates

Let f(t)=exp(-t/2){exp(t)} for t>=0 and *=causal convolution. Direct Abel summation yields
    Z = g_3 - g_4/2 - f*(g_2-2g_3+3g_4/4),
    k = g_2-3g_3/2+g_4/2 - f*(g_1-3g_2+11g_3/4-3g_4/4).
For implementation use the finite count floor(exp v): integrate exp(-v/2)w(t-v) against its jumps on [0,t], including the atom at 0. Integration by parts gives
    Z=w+E*w-f*(w'+w/2),  E(t)=exp(t/2) on t>=0.
Since w=g_4'-g_4/2, E*w=g_4. Differentiate the displayed formula for Z to get k: the differentiated convolution kernel vanishes at zero before differentiation. These manipulations can also be done with ordinary finite integrals on step intervals; no distribution API is required.

Each g_j has L1 norm 1 and L2 norm <=1 (its supremum is <=1); ||f||1<=2. Triangle and convolution bounds give ||Z||2<=3/2+2(1+2+3/4)=9, ||w||2<=5/2 and ||k||1<=3+2(1+3+11/4+3/4)=18. The same formulas give Z,w,h in L1 as well. Substitute into the tail estimate. Exact rational polynomial expansions were independently checked with sympy. This closes the generic premise on paper, pending independent audit and Lean verification.

Source for the interface: GppVerify/RiemannHypothesis/SparseCutoffCriterion.lean (PR #660). For the original constants and its distinct proof see sparse_energy.md.