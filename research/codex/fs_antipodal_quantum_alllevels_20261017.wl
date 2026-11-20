(* GPP October 17. ALL-LEVEL quantomorphism of CP1 Fubini-Study.
   Each level k>=0 has H0(CP1,O(k))=Sym^k(C²) dim k+1.
   The spinor antipode acts antiunitarily T_k on the SU2-invariant
   positive Hilbert form. The following basis identities prove
   T_k²=(-1)^k at EVERY level k, not a truncated RH criterion. *)
ClearAll[k,j,check,tSign];
check[label_,x_]:=If[TrueQ[x],Print["PASS: ",label],Print["FAIL: ",label];Abort[]];
tSign[k_,j_]:=(-1)^j (-1)^(k-j);
check["all checked levels (0..20) T² parity",
 And@@Flatten@Table[tSign[k,j]===(-1)^k,{k,0,20},{j,0,k}]];
check["all checked FS binomial weights mirror symmetric",
 And@@Flatten@Table[Binomial[k,j]==Binomial[k,k-j],{k,0,20},{j,0,k}]];
check["odd prequantum level has even complex dimension",
 And@@Table[EvenQ[k+1],{k,1,21,2}]];
Print["GENERAL PROOF FOR ALL k>=0, 0<=j<=k:"];
Print["T_k e_j = (-1)^j e_(k-j), with complex conjugation on coefficients."];
Print["T_k² e_j =(-1)^j(-1)^(k-j)e_j=(-1)^k e_j."];
Print["All SU2/FS orthonormal basis vectors preserve their norm under T_k."];
Print["Thus k odd: quaternionic/Kramers T²=-I; k even: real T²=+I."];
Print["At fixed k, dim H0(O(k))=k+1; FULL W-infinity needs an"];
Print["infinite-level or noncompact quantization (not finite k)."];
Print["Neither this structural fact nor central anomaly cancellation proves RH."];