(* 2026-10-20, Golden Physics Project / Codex-GPT.
   Astra/Turbo prime-only Cesaro signal + multiplicity-sensitive BOHR energy.
   Strict claims:
   1. IF RH: the centered/transient-subtracted J has an absolutely
      convergent almost-periodic Fourier series, and mean-square exists.
   2. The mean-square weights multiplicity^2, while xi logarithmic
      derivative trace weights multiplicity linearly.
   3. Therefore under RH the mean-square >= exactly computable xi
      local moment; equality iff ALL nontrivial zeros simple.
   4. Finite mean-square unconditionally would imply RH by Astra's
      prime-only Laplace continuation theorem. The needed upper bound
      on the prime signal is NOT proved here.
   The symbolic comparison is independent of the first 200 zeros. *)

ClearAll[xi,ss,traceMoment0,traceMomentQ,traceConst,mul,gg,bohrTerm,
         detTerm,check,gammaList,partial];
xi[z_] := z(z-1) Pi^(-z/2) Gamma[z/2] Zeta[z]/2;
check[tag_,yes_] := If[TrueQ[yes],Print["PASS: ",tag],
    Print["FAIL: ",tag];Abort[]];

(* m(0)=xi''(1/2)/(2xi(1/2)).
   m(1/4)=xi'(1)/xi(1) where the value at s=1 is a removable limit.
   DO NOT directly substitute the unsimplified zeta pole into xi'(1). *)
traceMoment0 = N[(Derivative[2][xi][1/2])/(2 xi[1/2]),55];
traceMomentQ = N[1+EulerGamma/2-Log[2]-Log[Pi]/2,55];
traceConst=8(traceMoment0-traceMomentQ);
Print[{"conditional_simplicity_threshold",N[traceConst,47],
   "m0",traceMoment0,"mQuarter",traceMomentQ}];

bohrTerm[mul_,gg_] := 2 mul^2/(gg^2(gg^2+1/4));
detTerm[mul_,gg_] := 2 mul/(gg^2(gg^2+1/4));
check["multiplicity gap =2m(m-1)/[gamma²(gamma²+1/4)]",
 FullSimplify[bohrTerm[mul,gg]-detTerm[mul,gg] ==
   2 mul(mul-1)/(gg^2(gg^2+1/4)),
   Assumptions->mul>=1&&gg>0]];
check["gap nonnegative for integer multiplicity",
 FullSimplify[bohrTerm[mul,gg]>=detTerm[mul,gg],
   Assumptions->Element[mul,Integers]&&mul>=1&&gg>0]];
check["gap strictly positive at multiplicity 2",
 FullSimplify[bohrTerm[2,gg]>detTerm[2,gg],Assumptions->gg>0]];

(* The first 200 known ordinates are a NUMERICAL cross-check ONLY;
   they are not the whole unknown zero set and do not prove RH. *)
gammaList = Table[Im[N[ZetaZero[j],40]],{j,1,200}];
partial=N[Total[bohrTerm[1,#]&/@gammaList],40];
Print[{"first200_zero_partial",partial,
 "difference_from_xi_threshold",N[traceConst-partial,32]}];

Print["PROOF under RH: for centered B(t)=J(t)-kappa-R(t),"];
Print["B(t)=-sum_{gamma!=0}m_gamma exp(i gamma t)/(rho(rho-1/2))."];
Print["Sum |coeff|<infinity from RvM, so Bohr Parseval applies."];
Print["M_B=2 sum_gamma>0 m_gamma²/[gamma²(gamma²+1/4)]."];
Print["Xi Hadamard gives C_xi=2 sum_gamma>0 m_gamma/[gamma²(gamma²+1/4)]."];
Print["M_B>=C_xi, with equality iff all zeros simple."];
Print["A finite Cesaro limsup implies RH by the INDEPENDENT"];
Print["prime-side Laplace criterion, NOT by this Wolfram test."];
Print["Thus limsup mean-square(B)<=C_xi iff RH plus simple zeros."];
Print["RH, zero simplicity, full signed-prime energy bound NOT PROVED."];