# Golden finite-place point as the self-dual Casimir fold

Date: 2026-09-18

Let the RH Cayley coordinate be beta(s)=(s-1)/s. For q>1 the finite-place/Casimir impedance contraction is

r_q=(sqrt(q)-1)/(sqrt(q)+1).

Equating r_q=beta(s) gives the unique real s>1

s_q=(sqrt(q)+1)/2.

Then

u_q:=s_q(s_q-1)=(q-1)/4,

while the discrete Casimir transfer mass derived earlier is

mu_q^2=4/(q-1)=1/u_q.

Thus the finite-place parameter q simultaneously determines a folded Casimir coordinate u and its reciprocal transfer mass.

The self-dual point u=mu^2 occurs iff u=1, hence iff q=5. At q=5,

s_5=phi,
1-s_5=-phi^{-1},
u_5=1,
mu_5^2=1,
r_5=beta(phi)=phi^{-2},
lambda_5=r_5^{-1}=phi^2.

The equation u=1 is

s(s-1)=1,

whose two roots are phi and -phi^{-1}. These are exactly the two real Möbius fixed points of the minimal trace-three matrix A=[[2,1],[1,1]] already formalized in GoldenRatioHyperbolicSector.lean. The functional-equation shadow s->1-s exchanges these two fixed points because 1-phi=-phi^{-1}.

Therefore the following structures meet at one exact self-dual point:
- discriminant q=5;
- the minimal hyperbolic SL2(Z) fixed-point pair;
- folded Casimir u=1;
- inverse Casimir transfer mass mu^2=1;
- Cayley contraction phi^-2;
- finite-place center / unstable eigenvalue phi^2;
- rapidity kappa=log phi.

No RH implication is claimed from this identity alone. Its significance is that the golden point is the fixed point of the reciprocal map u<->1/u relating the RH Casimir fold to the discrete transfer mass, rather than an independently inserted normalization.