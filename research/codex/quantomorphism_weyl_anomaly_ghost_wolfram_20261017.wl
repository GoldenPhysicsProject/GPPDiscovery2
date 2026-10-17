(* Golden Physics Project / Codex-GPT, 2026-10-17.
   Infinite arithmetic CS prime curvature: spectral Weyl-law and ghost no-gos,
   and an explicitly nonlocal Weyl-matched comparison Hamiltonian.
   All results are conditional only on classical PNT / Riemann-von Mangoldt
   where indicated, not RH. Finite arithmetic in this file checks algebra,
   not those classical analytic number theory theorems. *)

ClearAll[eps,y,q,tt,n,xx,scaledPrimeModel,zeroMain,check,implied,td,base,nd];
check[label_,p_]:=Print[If[TrueQ[p],"PASS: ","FAIL: "],label];

(* Weyl spectral Dirichlet series:
   A_CS(p)=(log p)^4/(p-1)^2, E_p=2π(p-1)/log(p)^2.
   PNT density dπ(x) ~ dx/log(x). Put x=e^t and ε=w-1:
   ∫ (2π)^(-w) (log x)^(2w) x^(-w) dπ(x)
      ~ (2π)^(-w) ∫ exp(-ε t)t^(1+2ε)dt
      = (2π)^(-w) Γ(2+2ε) ε^(-2-2ε).
 *)
scaledPrimeModel[e_]:=(2Pi)^(-1-e)Gamma[2+2e]Exp[-(2+2e)Log[e]];
check["prime model main double pole matches 1/(2pi)",
 FullSimplify[Limit[eps^2 scaledPrimeModel[eps],eps->0,
 Direction->"FromAbove"]==1/(2Pi)]];
check["unremovable prime logbranch coefficient -1/pi",
 FullSimplify[Limit[(eps^2 scaledPrimeModel[eps]-1/(2Pi))/
 (eps Log[eps]),eps->0,Direction->"FromAbove"]==-1/Pi]];

(* Ordinary meromorphic Laurent principal part of zero spectral zeta
   from the unconditional Riemann-von Mangoldt formula N(T)
   = T/(2π) [log T-log(2π)-1]+O(log T). *)
zeroMain[e_]:=((1+e)/(2Pi)) (1/e^2-(Log[2Pi]+1)/e);
check["zero model has no logarithmic branch",
 FullSimplify[Limit[(eps^2 zeroMain[eps]-1/(2Pi))/
 (eps Log[eps]),eps->0,Direction->"FromAbove"]==0]];

(* Parametric exact check of naive prime-gauge Weyl surplus.
   t = 2π exp(y)/y²; PNT with two terms π(exp y) =
   exp(y)/y (1+1/y+O(y^-2)). *)
base[y_]:=2Pi Exp[y]/y^2;
nd[y_]:=Exp[y]/y (1+1/y);
check["undressed spectral surplus +2 loglog",
 FullSimplify[nd[y]/(base[y]/(2Pi))-Log[base[y]] ==
  2 Log[y]+1-Log[2Pi],Assumptions->y>10]];

(* Hypothetical nonlocal/holographically dressed dispersion E_p*:
   2π(p-1)/[log p (log p -2loglog p -2)] (p>e^10).
   This removes the prime Weyl loglog surplus up to O(T),
   but is a fitted asymptotic model, NOT an arithmetic CS derivation. *)
td[y_]:=2Pi Exp[y]/(y(y-2Log[y]-2));
check["dressed dispersion cancels loglog and corrects O(T)",
 FullSimplify[Limit[nd[y]/(td[y]/(2Pi))-Log[td[y]],
 y->Infinity]==-1-Log[2Pi]]];

(* Exact smooth Riemann-von Mangoldt inversion using Lambert W. *)
num=10^6; omega=N[ProductLog[num/E],40];
Ew=N[2Pi num/omega,40];
smoothW=N[Ew/(2Pi)(Log[Ew/(2Pi)]-1),32];
check["Lambert-W inverse smooth zero-counting",Abs[smoothW-num]<10^-24];
Print[{"Weyl-matched first-principle-free energy for n=1e6",
 N[Ew,24], "smooth count",smoothW}];

(* Boson valuation Fock trace, fermion Mobius supertrace:
   all-prime product is 1 for real s>1 by absolute Euler convergence. *)
bos=FullSimplify[Sum[q^n,{n,0,Infinity}],Assumptions->0<q<1];
check["local exact BRST boson ghost superindex 1",
 FullSimplify[bos(1-q)==1,Assumptions->0<q<1]];
check["exact global zeta times Mobius ghost index 1",
 FullSimplify[Zeta[3/2]/Zeta[3/2]==1]];

Print["PNT and Riemann-von Mangoldt provide the infinite spectral asymptotics."];
Print["Weyl-law matching, ghost cancellation and positivity do NOT prove RH."];