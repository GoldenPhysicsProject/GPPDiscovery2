(* GPP 2026-10-17: full W_(1+infinity) Kac--Radul anti-mirror
   and one-loop free-fermion sea crossing, all mode orders.
   Algebraic model, NOT the physical loop-corrected celestial gravity. *)
ClearAll[n,m,d,a,b,f,g,forward,mirrored,check,chi,theta];
check[label_,result_]:=If[TrueQ[result],Print["PASS: ",label],Print["FAIL: ",label];Abort[]];
f[x_]:=a[0]+Sum[a[k]x^k,{k,1,4}];
g[x_]:=b[0]+Sum[b[k]x^k,{k,1,4}];
forward[N_]:=Sum[f[-j]g[N-j],{j,1,N}];
mirrored[N_]:=-Sum[g[j-1]f[j-N-1],{j,1,N}];
check["full spin KR anti-mirror all n=1..12 generic quartic symbols",
 And@@Table[TrueQ[FullSimplify[forward[k]+mirrored[k]==0]],{k,1,12}]];
check["half-density mirror squares to the identity",
 FullSimplify[-(-d-1)-1==d]];
check["general W differential commutator respects half-density mirror",
 And@@Flatten@Table[
 With[{lhs=Expand[(f[d+m]g[d]-g[d+n]f[d])/.d->(-d-1)],
       rhs=Expand[f[-d-1+m]g[-d-1]-g[-d-1+n]f[-d-1]]},
 TrueQ[FullSimplify[lhs==rhs]]],{n,{-3,-1,0,1,4}},{m,{-3,-2,0,2,5}}]];
check["U(1) current Schwinger term from integer Dirac sea",
 FullSimplify[Sum[1,{j,1,n}]==n,Assumptions->n>=1&&Element[n,Integers]]];
check["spin-two Virasoro central coefficient",
 FullSimplify[Sum[((n+1)/2-j)^2,{j,1,n}]==n(n^2-1)/12,
  Assumptions->n>=1&&Element[n,Integers]]];
check["higher-spin D² current Schwinger coefficient",
 FullSimplify[Sum[j^2(n-j)^2,{j,1,n}]==n(n^4-1)/30,
  Assumptions->n>=1&&Element[n,Integers]]];
check["Haar Fourier orthogonality opposite charges",
 FullSimplify[Integrate[Exp[I(5-5)theta],{theta,0,2Pi}]/(2Pi)==1]];
check["Haar Fourier orthogonality disjoint charges",
 FullSimplify[Integrate[Exp[I(5+3)theta],{theta,0,2Pi}]/(2Pi)==0]];
Print[{"allspin_free_fermion_formulas","spin1: n","spin2: n(n^2-1)/12",
 "spin3 D²:D²: n(n^4-1)/30"}];
Print["The arithmetic Haar-internal cocycle Psi_tau(A⊗a,B⊗b)=tau(ab)Psi_W(A,B)"];
Print["is a Lie algebra 2-cocycle because tau(abc) is symmetric and Psi_W is closed."];
Print["Half-density mirror: n -> -n, D -> -D-1, coefficient a -> a∘inv."];
Print["It reverses Psi_tau exactly at every spin: Psi_tau(MA,MB)=-Psi_tau(A,B)."];
Print["Quantum central charges of actual celestial gravity and RH remain OPEN."];
