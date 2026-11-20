(* GPP / Daniel Toupin — full infinite signed prime-Archimedean heat formula.
   Wolfram symbolic inverse Laplace checks and high-precision NUMERICAL diagnostic.
   RH and complete monotonicity NOT assumed or proved. *)
ClearAll[u,t,a,b,tau,al,k,j,jMax,omega,archPartial,tail,primeTerm,heat,zeros];
assert[label_,cond_]:=If[TrueQ[cond],Print["PASS: ",label],Print["FAIL: ",label];Abort[]];
assert["prime Gaussian subordination",
 FullSimplify[InverseLaplaceTransform[Exp[-b Sqrt[u]]/(2 Sqrt[u]),u,t,
 Assumptions->b>0&&t>0]-Exp[-b^2/(4t)]/(2 Sqrt[Pi t]),
 Assumptions->b>0&&t>0]==0];
assert["gamma erfc inverse Laplace",
 FullSimplify[InverseLaplaceTransform[1/(Sqrt[u]+a),u,t,
 Assumptions->a>0&&t>0]-(1/Sqrt[Pi t]-a Exp[a^2 t] Erfc[a Sqrt[t]]),
 Assumptions->a>0&&t>0]==0];
assert["pole heat inverse Laplace",
 FullSimplify[InverseLaplaceTransform[1/(u-1/4),u,t]==Exp[t/4],Assumptions->t>0]];
assert["Suzuki scalar Gaussian kernel inverse transform",
 FullSimplify[InverseLaplaceTransform[Sqrt[u] Exp[-b Sqrt[u]],u,t,
 Assumptions->b>0&&t>0]-
 ((b^2/(2t)-1)Exp[-b^2/(4t)])/(2 Sqrt[Pi] t^(3/2)),
 Assumptions->b>0&&t>0]==0];
Print["Analytic full arithmetic heat trace for t>0:"];
Print["K(t)=exp(t/4)+omega0/(4sqrt(pi t))+"];
Print["sum_j[1/(2alpha_j sqrt(pi t))-exp(alpha_j^2 t)erfc(alpha_j sqrt(t))/2]"];
Print["-sum_(n>=2) MangoldtLambda[n] exp(-(log n)^2/(4t))/(2 sqrt(pi t n))"];
Print["alpha_j=2j+1/2; omega0=PolyGamma[0,1/4]-log(pi)."];
Print["The full heat function is expected to be completely monotone iff RH; that remains OPEN."];
(* Numeric check only. Accelerate the convergent gamma tail via 6 asymptotic terms;
   note: asymptotics here are NOT outward-rounded interval certificates. *)
tau=SetPrecision[1/20,60]; jMax=150; al[j_]:=2j+1/2;
omega=N[PolyGamma[0,1/4]-Log[Pi],60];
archPartial=Sum[N[1/(2 al[j] Sqrt[Pi tau])-
 Exp[al[j]^2 tau]Erfc[al[j]Sqrt[tau]]/2,55],{j,0,jMax}];
tail=Sum[(-1)^(k+1)(2k-1)!! HurwitzZeta[2k+1,jMax+5/4]/
 (2^(3k+2) Sqrt[Pi] tau^(k+1/2)),{k,1,6}];
primeTerm=Sum[N[MangoldtLambda[n] Exp[-Log[n]^2/(4 tau)]/Sqrt[n],55],
 {n,2,350}]/(2 Sqrt[Pi tau]);
heat=N[Exp[tau/4]+omega/(4 Sqrt[Pi tau])+archPartial+tail-primeTerm,35];
zeros=N[Sum[Exp[-(Im[N[ZetaZero[j],55]])^2 tau],{j,1,8}],35];
Print[{"K(.05) from arithmetic",heat,"first eight verified critical zeros",zeros,
 "difference numeric",N[heat-zeros,25]}];
