(* GPP Oct17 — OPE / W_{1+infinity} / central charge and mirror sewing.
   Kac–Radul differential-operator central extension, explicit Virasoro
   subalgebra and wedge test, plus cL-cR anomaly on opposite orientation.
   Tree wedge cannot determine quantum c; no RH inference. *)
ClearAll[n,m,x,j,cL,cR,poly,calc,expected,central,check];
check[lab_,truth_]:=Print[If[TrueQ[truth],"PASS: ","FAIL: "],lab];

poly[a_,d_]:=d+(a+1)/2;
calc=Expand[poly[n,x+m]poly[m,x]-poly[m,x+n]poly[n,x]];
check["exact spin-2 Witt differential commutator",
  FullSimplify[calc==(m-n)poly[n+m,x]]];
(* For n>0 and m=-n, the Kac-Radul cocycle is
   Sum_{j=1}^n f_n(-j)f_{-n}(n-j), both factors equal
   (n+1)/2-j. *)
expected=FullSimplify[Sum[((n+1)/2-j)^2,{j,1,n}],
  Assumptions->Element[n,Integers]&&n>=1];
check["exact Kac-Radul n(n²-1)/12 coefficient",
  FullSimplify[expected==n(n^2-1)/12,
    Assumptions->Element[n,Integers]&&n>=1]];
central[cc_,nn_]:=cc(nn^3-nn)/12;
check["orientation reflected -n reverses Virasoro cocycle",
  FullSimplify[central[cL,n]+central[cR,-n]==central[cL-cR,n]]];
check["same positive central charge cancels glued anomaly",
  FullSimplify[central[cL,n]+central[cL,-n]==0]];
check["global conformal wedge (-1,0,1) blind to c",
  FullSimplify[And@@Table[central[cL,z]==0,{z,{-1,0,1}}]]];
check["first nontrivial mode 2 detects c/2",
  FullSimplify[central[cL,2]==cL/2]];
Print[{"KacRadul_spin2_cocycle",expected,
 "chiral_positive_norm_Lminus2",cL/2,
 "glued_mode2_central",central[cL-cR,2]}];
Print["Note: this does not determine actual celestial cL, cR or W1infty C."];
Print["A centerless wedge algebra is compatible with NONZERO quantum c."];
Print["The physical RH-strength arithmetic sewing identity remains OPEN."];