# Direct OS factorization: Weil prime terms are critical-KMS half-shift cross-sheet pairings

Date: 2026-09-28
Status: exact zero-independent finite-place identity; explicit real-place companion; no RH claim.

Let f be a compactly supported logarithmic-line test function and let F be its unitary Fourier transform. Then

  h_f(y)=<f,T_y f>=int_R |F(t)|^2 e^(i t y) dt.

For y real define the half-shift multiplication operators on the spectral line

  M_y^+ F(t)=e^(+i t y/2)F(t),
  M_y^- F(t)=e^(-i t y/2)F(t).

Then exactly

  <M_y^- F, M_y^+ F> = h_f(y).

Thus every reflected translation correlation is a cross-sheet overlap of two opposite half-shifts.

## 1. Insert the critical Bost-Connes KMS channel

At beta=1 the Bost-Connes midpoint Hilbert form satisfies

  <mu_m,mu_n>_mid = delta_mn n^(-1/2).

For a finite prime-power cutoff A define

  V_A(f)
   = sum_{n in A} sqrt(Lambda(n)) mu_n tensor
       ( M_{log n}^- F  direct_sum  M_{log n}^+ F ).

Let S swap the two spectral sheets. Orthogonality of the multiplicative KMS channels gives

  <V_A(f),(I tensor S)V_A(f)>
   = 2 sum_{n in A} Lambda(n)/sqrt(n) Re h_f(log n).

Hence the finite-place term in Weil's form is EXACTLY the negative of one critical-KMS/TFD sheet-exchange pairing.

This couples in one formula:
- the Bost-Connes critical midpoint n^(-1/2);
- the von Mangoldt channel energy Lambda(n);
- the additive logarithmic translation log n;
- the two-sheet reflection.

No zeta zeros or analytic continuation enter.

## 2. The Archimedean cross term has the identical half-shift architecture

Write

  w_inf(y)=e^(y/2)/(e^y-e^(-y)), y>0.

The non-diagonal part of the standard real-place term is

  2 int_0^infinity w_inf(y) Re h_f(y) dy.

Define the continuum feature

  V_inf(f;y)=sqrt(w_inf(y))
    (M_y^-F direct_sum M_y^+F).

Then

  int <V_inf(f;y),S V_inf(f;y)> dy
   =2 int_0^infinity w_inf(y) Re h_f(y)dy.

So finite and infinite places have the SAME reflected half-shift channel geometry: the finite places sample a discrete arithmetic set y=log p^k with KMS weights, while the real place integrates the same sheet-exchange overlap against a continuous thermal weight.

## 3. Renormalized diagonal of the real place

Since

  ||M_y^+F-M_y^-F||^2 = 2(h_f(0)-Re h_f(y)),

the full real-place functional

  W_R(h)=(log(4pi)+gamma)h(0)
   + int_0^infinity [2e^(y/2)h(y)-2h(0)]/(e^y-e^(-y)) dy

can be rewritten without a singular separated cross term as

  W_R(h_f)
   = C_inf ||f||^2
     - int_0^infinity w_inf(y)||M_y^+F-M_y^-F||^2 dy,

where the finite constant is

  C_inf = log(4pi)+gamma + pi/2 + log 2
        = log(8pi)+gamma+pi/2.

The identity

  2 int_0^infinity (e^(y/2)-1)/(e^y-e^(-y)) dy
   = pi/2+log 2

was independently checked symbolically/numerically.

Thus the Archimedean term is a positive continuous half-shift Dirichlet energy subtracted from one explicit diagonal contact.

## 4. What is now explicit

Claude's requested OS feature map no longer needs to be guessed at the local level. Both finite and infinite places are built from the same two-sheet half-shift representation. The only nonlocal pieces left are:

1. the renormalized diagonal/contact channel;
2. the pole pair 2 a_+(f)a_-(f);
3. the global restriction/quotient selecting the physical positive subspace.

The finite-place feature is genuinely arithmetic because the channel labels and midpoint norms come from the Bost-Connes multiplicative system. The real-place feature is the SU(1,1)/thermal continuum channel.

## 5. Why this is still RH-bearing

The sheet-swap S is not positive on the full doubled Hilbert space. Reflection positivity means positivity only after restricting to the correct arithmetic/Hardy physical subspace. Showing that the completed image of all admissible f lies in an S-positive graph is exactly the remaining theorem.

However, this representation has reduced the problem from 'construct an OS form' to:

  identify the ONE completed graph/Schur relation between the two half-shift sheets that absorbs the contact and pole channels.

That graph relation is the object to compare directly with the existing BPY closed graph C_omega and its contractivity criterion.