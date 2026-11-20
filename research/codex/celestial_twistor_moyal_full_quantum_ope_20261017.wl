(* GPP 2026-10-17: Quantization of the ACTUAL twistor Poisson bracket
   behind tree-level celestial w_(1+infinity) gravity currents.
   Exact polynomial Moyal star product, not a physical measured
   one-loop graviton OPE. Connected to full Kac–Radul Schwinger cocycle
   as separate quantum loop/central extension. RH/GRH OPEN. *)
ClearAll[x,y,h,k,j,star,br,pb,ref,assert,a,b,c,d];
star[f_,g_,order_:9]:=Expand[Sum[(h/2)^k/k!*Sum[
 (-1)^j Binomial[k,j]*D[f,{x,k-j},{y,j}]*D[g,{x,j},{y,k-j}],
 {j,0,k}],{k,0,order}]];
br[f_,g_]:=FullSimplify[(star[f,g]-star[g,f])/h];
pb[f_,g_]:=D[f,x]D[g,y]-D[f,y]D[g,x];
ref[f_]:=f/.y->-y;
assert[label_,truth_]:=If[TrueQ[truth],Print["PASS: ",label],
 Print["FAIL: ",label];Abort[]];

assert["TREE celestial twistor Poisson monomial OPE",
 FullSimplify[pb[x^a y^b,x^c y^d] ==
 (a d-b c)x^(a+c-1)y^(b+d-1),
 Assumptions->a>=1&&b>=1&&c>=1&&d>=1]];
assert["QUANTUM Moyal cubic pair includes nonzero order h² scalar",
 FullSimplify[br[x^3,y^3]==9x^2y^2+3h^2/2]];
pairs={{x^3,y^3},{x^4,y^3},{x^4 y,x^2 y^3},
 {x^3 y^2,x y^4},{x^5+y^2,x^3+y^5}};
assert["quantum classical limit over full tested polynomial collection",
 And@@Table[FullSimplify[Limit[br[p[[1]],p[[2]]],h->0]==
 pb[p[[1]],p[[2]]]],{p,pairs}]];
assert["HALF-ORIENTATION reflection exchanges +h and -h star products",
 And@@Table[
  TrueQ[FullSimplify[star[ref[p[[1]]],ref[p[[2]]]]==
   ref[star[p[[1]],p[[2]]]/.h->-h]]],
  {p,pairs}]];
assert["full quantum Moyal bracket anti-oriented",
 And@@Table[TrueQ[FullSimplify[
 br[ref[p[[1]]],ref[p[[2]]]]==-ref[br[p[[1]],p[[2]]]]]],
 {p,pairs}]];
Print["Classical Poisson is the actual known celestial w-infinity OPE pole."];
Print["Moyal h² correction is algebraic quantum deformation; it is NOT"];
Print["by itself the Kac-Radul quantum loop central cocycle."];
Print["For a quantum celestial model, combine star-Poisson OPE, loop"];
Print["Kac-Radul Schwinger cocycle, FS orientation and Haar trace."];
Print["No physical gravity OPE coefficient or RH theorem is proved."];
