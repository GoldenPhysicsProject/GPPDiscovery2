(* Golden Physics Project 2026-10-17
   Exact ALL-order arithmetic Ward-cumulant split for completed xi.
   Mathematica exact tests m=2..7; no sign claim about their sum,
   no identification with physical celestial W-current OPE. *)
ClearAll[s,m,xi,check];
check[tag_,bool_]:=If[TrueQ[bool],Print["PASS: ",tag],
 Print["FAIL: ",tag];Abort[]];
xi[z_]:=z(z-1)Pi^(-z/2)Gamma[z/2]Zeta[z]/2;
Do[
 Module[{lhs,rhs},
  lhs=(-1)^m D[Log[xi[s]],{s,m}];
  rhs=(-1)^m D[Log[Zeta[s]],{s,m}]+
    (m-1)!/2^m HurwitzZeta[m,1+s/2]-(m-1)!/(s-1)^m;
  check["complete prime+gamma-pole identity derivative m="<>ToString[m],
      FullSimplify[lhs==rhs,Assumptions->s>1]];
 ],{m,2,7}];
check["nonnegative exact infinite gamma ladder m=2",
 FullSimplify[PolyGamma[1,s/2]/4-1/s^2==
  HurwitzZeta[2,1+s/2]/4,Assumptions->s>1]];
check["completed functional equation reflection numeric control",
 Abs[N[xi[13/10]-xi[-3/10],40]]<10^-30];
Print["Analytical all-m infinite derivation for Re s>1:"];
Print["(-∂s)^m log(zeta(s))=sum_p sum_(k>=1) k^(m-1)log(p)^m p^(-ks)"];
Print["(-∂s)^m log(xi(s)) = prime_m + (m-1)!sum_(ell>=1)(s+2ell)^(-m)"];
Print["                             - (m-1)! (s-1)^(-m), m>=2."];
Print["No assumption of positivity of the total, nor c=0, nor RH/GRH."];
