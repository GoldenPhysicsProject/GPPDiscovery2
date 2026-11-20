(* GPP Oct17: user insight "the negatives are positives pointing the other way".
   Positive Haar/FS measure versus signed oriented FS 2-form, corrected
   Jacobian, parity/Krein decomposition of actual Weil polar contribution.
   No assertion that sign bookkeeping proves RH. *)

ClearAll[x,y,r,X,Y,jac,fs,J,two,check,ar,ai,br,bi,aa,bb];
check[tag_,bool_]:=Print[If[TrueQ[bool],"PASS: ","FAIL: "],tag];
r=x^2+y^2;X=-x/r;Y=-y/r;
jac=D[{X,Y},{{x,y}}];
J={{0,-1},{1,0}};
rho[t_]:=1/(1+t)^2;
check["antipodal real Jacobian is negative inverse radius fourth",
 FullSimplify[Det[jac]==-1/r^2,Assumptions->r>0]];
check["antipodal is anti-holomorphic (J anti-commutes)",
 FullSimplify[jac.J+J.jac==ConstantArray[0,{2,2}],Assumptions->r>0]];
check["FS positive Haar/area density invariance using ABS jacobian",
 FullSimplify[rho[X^2+Y^2](-Det[jac])==rho[r],Assumptions->r>0]];
check["FS signed oriented TWO-FORM changes sign",
 FullSimplify[rho[X^2+Y^2]Det[jac]==-rho[r],Assumptions->r>0]];
check["FS positive metric pullback unchanged",
 FullSimplify[Transpose[jac].jac rho[X^2+Y^2]==IdentityMatrix[2]rho[r],
 Assumptions->r>0]];
aa=ar+I ai;bb=br+I bi;
pole=ComplexExpand[2Re[aa Conjugate[bb]]];
orient=ComplexExpand[Abs[(aa+bb)/Sqrt[2]]^2-Abs[(aa-bb)/Sqrt[2]]^2];
check["Weil pole EXACT even-forward-square MINUS odd-reverse-square",
 FullSimplify[pole==orient]];
check["odd reflected polar is negative, not ordinary PSD",
 FullSimplify[(pole/.{br->-ar,bi->-ai})==-2(ar^2+ai^2)]];
check["even reflected polar positive",
 FullSimplify[(pole/.{br->ar,bi->ai})==2(ar^2+ai^2)]];
Print["The actual signed Weil form equals positive arch/prime jump energies"];
Print["plus this positive-even-minus-positive-odd polar pair, minus mass"];
Print["(2 S_L-omega0)||f||². It is NOT proved nonnegative for all f."];
Print["Loop/Cut integrand positivity does not imply signed Weil positivity"];
Print["without exact arithmetic sewing equality and causal prescriptions."];
Print["RH/GRH OPEN."];