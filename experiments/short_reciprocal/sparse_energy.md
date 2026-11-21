# A sparse-cutoff criterion for Heart's Möbius energy

Let X=exp L >=1, c=1/zeta(1/2), B(u)=sum_{n<=exp u} mu(n)/sqrt(n)-c and Q(L)=integral_0^L |B(u)|^2 du. Suppose zeta(1/2+r)=0 with d=Re(r)>0. Then for EVERY L>=0,

    sqrt(2d) |r-1/2| exp(d L) / |1+r|^4
        <= (3|c|+1)/2 + (3/2) sqrt(Q(L)).                      (1)

Hence Q(log X) >= C_r X^(2d) for all sufficiently large X, with C_r>0. Multiplicities, ordinate spacing, and signs of residues do not enter. No off-line zero is being assumed in the criterion below; the inequality is the consequence if one exists.

## Proof

Use the finite Laplace transform P_L(s)=c+s integral_0^L B(u) exp(-su) du, an entire function. In Re s>1/2, absolute convergence and summing the step functions give c+s integral_0^infty B exp(-su) du = 1/zeta(1/2+s). Consequently
P_L(s)-1/zeta(1/2+s) = -s integral_L^infty B(u)exp(-su)du there.

Set w=s+1/2 and
    T_L(s) = exp(sL) (s-1/2) [zeta(w) P_L(s)-1] / (1+s)^4 .
It is analytic on the closed right half-plane (meaning locally across its boundary); the factor s-1/2 removes the pole at w=1. At s=r its absolute value is |r-1/2|exp(dL)/|1+r|^4.

Here are bounds justifying the use of the boundary integral. For Re s>=1, the tail identity and |B(u)|<=2 exp(u/2)+|c| give exp(Re(s)L)|P_L-1/zeta(w)| <= C_L |s|/(Re(s)-1/2); zeta(w) is bounded in this region. For 0<=Re s<=1, P_L=O_L(1+|s|). Euler summation gives zeta(w)=w/(w-1)-w integral_1^infty {x} x^(-w-1) dx for Re w>0, whence (w-1)zeta(w)=O((1+|s|)^2) uniformly there. Thus T_L is O_L((1+|s|)^(-1)) on the right semicircles. The constants here may depend on L because only removal of the large contour uses them.

On the imaginary axis there is a sharper estimate independent of L. With s=it set U=|1+s|=sqrt(1+t^2). Euler summation yields |(s-1/2)zeta(w)| <= |w|(1+2|w-1|) <= 3 U^2. Write b_L(t)=integral_0^L B(u)exp(-itu)du. Then
    |T_L(it)| <= (3|c|+1)/U^2 + 3 |t| |b_L(t)|/U^2.
Take the norm in L^2(dt/(2 pi)). The norm of 1/(1+t^2) is 1/2, sup |t|/(1+t^2)=1/2, and by Plancherel the norm of b_L is sqrt(Q(L)). The resulting bound is the right hand side of (1).

Cauchy's formula on right semicircles followed by Cauchy-Schwarz gives |T_L(r)| <= ||T_L(it)||_2 / sqrt(2d), because the squared boundary norm of 1/(it-r) is 1/(2d). This proves (1).

## Consequence and outstanding arithmetic

RH is equivalent to liminf_{L->infty} log(1+Q(L))/L=0. The forward direction uses the classical conditional estimate M(x)=O_eta(x^(1/2+eta)) for every eta>0 and partial summation. The reverse follows from (1) and reflection. The cutoffs witnessing the liminf can be arbitrarily far apart. More generally the liminf is >= 2d for each off-line zero. This is a localized version of a standard analytic mollifier argument; no claim of historical novelty.

In particular a sequence with G(log X)<=H(log X) suffices, since Q<=G and H=O((1+log X)^2). Even that comparison is stronger than necessary: Q(log X_j)<=X_j^o(1) alone suffices. To use this for RH one must construct unbounded X_j and bound the accumulated energy up to X_j using arithmetic. A small instantaneous prefix B(log X_j) does not do this. The proof supplies a necessary lower bound if a zero exists; it supplies no unconditional subpower upper bound.

## Check on a model with a known displaced zero

In the shifted variable take F(s)=1-2^(d-s), 0<d<1/2. Its inverse series has positive coefficients 2^(kd) at log positions k log 2. Center by c_F=1/F(0)=1/(1-2^d). On j log 2 <= u < (j+1)log 2 its centered prefix is exactly 2^((j+1)d)/(2^d-1). Hence at L=J log 2 its energy is
    (log 2) 2^(2d) (2^(2dJ)-1) / ((2^d-1)^2 (2^(2d)-1)).
It has exact exponential rate 2d; bracketing adjacent powers gives that rate for all cutoffs. This checks the predicted exponent in a separately soluble model. Inequality (1)'s explicit constants were derived for zeta.
