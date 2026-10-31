# Completed Weil all-test positivity through L = 29/100 (2026-10-31)

Codex / GPPDiscovery2. New **unconditional local theorem for the corrected v34 completed semilocal Weil form**: every complex finite-energy f supported on an interval of length 0<L<=29/100 satisfies

Q[f] >= (1/100) ||f||_2^2.

This is **not RH** and no prime atoms occur (29/100<log2). It extends the earlier prime-free completed Q all-function endpoint L<=5/32 by a factor 1.856. It is logically distinct from the separate E−S four-prime bound at L<=83/50.

## Source formula and exact decomposition

For zero-extended f on [0,L], q_f(y)=2Re integral conj(f(x))f(x+y)dx, c_inf=log(4pi)+EulerGamma, E=integral (q(0)-q(y))/(2sinh y) dy, A=integral_0^L (exp(y/2)-1)q(y)/(2sinh y)dy, and P=integral_0^L q(y)(exp(y/2)+exp(-y/2))dy. Since L<log2, Q=E+P-c_inf||f||²-A.

Let H(z)=log coth(z/2), V_L(x)=[H(x)+H(L-x)]/2, r(y)=(exp(y/2)-1)/(2sinh y), Gamma_L(x)=integral_0^x r+integral_0^(L-x)r, w(y)=exp(y/2)/(2sinh y). The previous corrected exact identity is

Q[f]= integral_0^L(V_L-Gamma_L-c_inf)|f|²dx
+ integral_0^L w(y) integral_0^(L-y)|f(x+y)-f(x)|² dx dy
+2|C_f|²-2|S_f|²,

where C_f=integral f(x)cosh((x-L/2)/2)dx and S_f=integral f(x)sinh((x-L/2)/2)dx. The infinite gamma tail y>L is included in V.

## Step 1: exact local potential bound

H is convex, so V_L>=H(L/2)=-log tanh(L/4). AM-GM gives r(y)<=exp(y/4)/4. Consequently

Gamma_L(x) <= exp(x/4)+exp((L-x)/4)-2 <= exp(L/4)-1,

the second inequality by convexity and endpoint maximum. Therefore V-Gamma-c_inf >= beta(L), where beta(L)=H(L/2)-(exp(L/4)-1)-c_inf. At L=29/100 beta is negative, approximately -0.557514063, so DO NOT drop the positive jump or pole terms.

## Step 2: mean and variance

Write f=a+g on [0,L], a=(1/L)integral f, integral g=0. Then ||f||²=L|a|²+||g||². The weight w is strictly decreasing. The *exact* variance identity is

integral_0^L dy integral_0^(L-y)|f(x+y)-f(x)|²dx = L||g||².

Hence J_jump >= L w(L) ||g||². This uses no Fourier truncation or assumed spectral gap.

## Step 3: positive cosh pole vs negative sinh pole

Define c(x)=cosh((x-L/2)/2), s(x)=sinh((x-L/2)/2),
C0=integral c=4sinh(L/4),
delta_c²=||c-C0/L||²=L/2+sinh(L/2)-C0²/L,
s_norm²=||s||²=sinh(L/2)-L/2.

Then C_f=a C0+integral g(c-C0/L) and S_f=integral g s. For 0<eta<1, the elementary complex Young inequality |u+v|² >= (1-eta)|u|²-(eta^(-1)-1)|v|², followed by Cauchy-Schwarz, yields

P>=2(1-eta)C0²|a|² - [2(eta^(-1)-1)delta_c²+2s_norm²]||g||².

## Step 4: explicit one-sided two-channel bound

The exact form therefore obeys Q[f]>=B_mean(L,eta)*L|a|² + B_fluct(L,eta)*||g||², with

B_mean=beta + 2(1-eta)C0²/L,
B_fluct=beta + L w(L) - 2(eta^(-1)-1)delta_c² - 2s_norm².

Set L0=29/100 and eta=1/100. FLINT Arb at 256-bit outward precision certifies:

B_mean(L0,eta) = 0.017692688392961281110777... > 1/100,
B_fluct(L0,eta) = 0.011430048456797679627264... > 1/100.

So Q[f]>=1/100||f||² for EVERY admissible f supported in [0,L0]. The same inequality holds for EVERY shorter support by zero extension to [0,L0] and translation invariance of the completed form; no unproved monotonicity is used.

**CI SUCCESS:** https://github.com/GoldenPhysicsProject/GPPDiscovery2/actions/runs/41212896127 . Exact head d3380c606ceb209ad0cc556f76f66661437d2e47. Certificate source: discovery/short_support_mean_variance_weil_arb.py. No floating value decides the sign. The source file's analytic derivation above is a mathematical proof; the scalar endpoint was certified using Arb, not formalized in Lean.

## Limits and Lean handoff

This result is completely prime-free. Full completed Q positivity for arbitrary L and RH remain open. For larger support the prime edge SOS and gamma jump must be combined with this moment–variance method, with actual signed prime controls.

Verify has already merged PathSOS and PoleCoshSinh. Next new finite/analytic formalization targets: (1) variance double-integral identity, (2) two-channel moment inequality, (3) scalar criterion reducing Q positivity to B_mean>=0 and B_fluct>=0. The uniform interval extension still needs analytic domain and Archimedean tail verification inside Lean. Do not label finite pole algebra as a complete Weil positivity theorem.
