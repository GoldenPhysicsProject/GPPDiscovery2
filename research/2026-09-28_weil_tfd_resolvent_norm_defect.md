# Direct OS attack: the Weil prime and real-place terms are exact TFD/resolvent norm defects

Date: 2026-09-28
Status: exact zero-independent operator identities on the additive log line. This is a direct attack on the missing reflection-positive realization, not a proof of RH.

Let H=L2(R,dx), and let (U_a f)(x)=f(x+a) be the unitary translation group. For f in a compactly supported smooth core, write h_f(a)=<f,U_a f>.

## 1. One prime: the whole prime-power tower is one TFD norm defect

Fix a prime p, put L_p=log p, r_p=p^(-1/2), U_p=U_{L_p}, and define

  D_p = sqrt(1-r_p^2) (I-r_p U_p)^(-1).

Because U_p is unitary,

  D_p^* D_p = I + sum_{k>=1} r_p^k (U_p^k + U_p^(-k)).

Hence

  ||D_p f||^2-||f||^2 = 2 sum_{k>=1} p^(-k/2) Re h_f(k log p),

and therefore

  (log p)(||D_p f||^2-||f||^2)
    = 2 sum_{k>=1} Lambda(p^k)/sqrt(p^k) Re h_f(log p^k).

Thus the entire p-power tower in Weil's explicit formula is exactly one norm defect. This is the operator form of the previously derived equality between the TFD boundary intensity, Blaschke defect intensity, and Poisson/group-delay kernel.

## 2. Prime contribution to the Weil form

For compact support, h_f(a)=0 for all sufficiently large |a|, so only finitely many prime powers contribute. Thus

  2 sum_{n>=2} Lambda(n)/sqrt(n) Re h_f(log n)
    = sum_p (log p)(||D_p f||^2-||f||^2).

## 3. The real place is a discrete tower of ordinary resolvent norms

Let A=-i d/dx be the self-adjoint translation generator. For alpha>0 define

  R_alpha = sqrt(2 alpha) (alpha+i A)^(-1).

By Plancherel,

  ||R_alpha f||^2 = 2 int_0^infinity exp(-alpha y) Re h_f(y) dy.

Use

  e^(y/2)/(e^y-e^(-y)) = sum_{m>=0} exp(-(2m+1/2)y),
  1/(e^y-e^(-y))       = sum_{m>=0} exp(-(2m+1)y).

For the standard real-place distribution

  W_R(h)=(log(4 pi)+gamma)h(0)
         + int_0^infinity [2e^(y/2)h(y)-2h(0)]/(e^y-e^(-y)) dy,

we get the paired renormalized resolvent expansion

  W_R(h_f)=(log(4 pi)+gamma)||f||^2
           + sum_{m>=0}[ ||R_{2m+1/2}f||^2 - 2/(2m+1)||f||^2 ].

The two pieces in each summand must remain paired.

## 4. Direct operator form of the Weil quadratic form

With the current normalization

  Q_W(f)=2 a_+(f)a_-(f)-W_R(h_f)
         -2 sum_{n>=2} Lambda(n)/sqrt(n) Re h_f(log n),

where a_+(f)=int f(x)e^(x/2)dx and a_-(f)=int f(x)e^(-x/2)dx, the preceding identities give

  Q_W(f)=2a_+a_- -(log(4 pi)+gamma)||f||^2
         -sum_{m>=0}[||R_{2m+1/2}f||^2-2/(2m+1)||f||^2]
         -sum_p(log p)[||D_p f||^2-||f||^2].

This is a zero-independent Hilbert-space realization of every local term of the Weil form. What is not yet proved is positivity of the renormalized combination.

## 5. Why this is stronger than relabelling Weil positivity

The finite-place operators D_p are the exact local TFD/Blaschke transfers with parameter p^(-1/2). The real-place R_alpha are ordinary resolvents of the self-adjoint translation generator, with the same half-integer Archimedean ladder already derived from the SU(1,1) K0 module.

So the missing RH theorem is now an explicit passivity statement for one multichannel system: prime TFD channels + real-place resolvent channels + the rational/pole endpoint channel.

## 6. Exact local no-go: each prime channel is not contractive by itself

On a translation eigenphase U_p -> e^(i theta),

  |D_p(theta)|^2=(1-r_p^2)/(1-2r_p cos theta+r_p^2)=P_{r_p}(theta).

At theta=0 this equals (1+r_p)/(1-r_p)>1. Hence prime-by-prime OS positivity is impossible; the completion must be global.

## 7. The prime defect is a cross-sheet object before resummation

For each prime power define a doubled feature

  A_{p,k}(f)=sqrt((log p)p^(-k/2)) (f,U_{kL_p}f) in H+H,

and let S swap the two sheets. Then

  <A_{p,k}(f), S A_{p,k}(f)>
    =2(log p)p^(-k/2) Re h_f(kL_p).

So the finite-place contribution is literally a TFD cross-sheet reflected pairing before it is resummed into the Poisson norm defect.

## 8. Closure target

The local OS representation is now explicit. The remaining theorem is that after adjoining the pole channel, the renormalized combined observation map is contractive. Equivalently: construct the single completed Julia/Schur colligation whose input defect is exactly Q_W.

## 9. Counterexample filter

The local factorization alone would survive arbitrary Beurling-like replacement of the prime lengths/weights. Therefore it is not yet arithmetic enough. The closing contraction must use the global real-place/pole sewing fixed by Poisson/self-dual lattice structure. The next calculation must be on the combined colligation, never on a local D_p in isolation.