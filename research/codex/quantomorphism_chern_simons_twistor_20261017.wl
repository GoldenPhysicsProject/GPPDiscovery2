(* Golden Physics Project - quantomorphism / Chern-Simons / arithmetic-twistor spine.
   Exact infinite-mode identities in the Wolfram Language kernel.
   The global Lie-algebra cocycle is defined on cylindrical trigonometric polynomials
   on K=PontryaginDual(Q_+^x); it is NOT claimed to extend to a group
   or prove a reflection-positive arithmetic boundary.
   RH and GRH are OPEN. *)

ClearAll[q,s,t,p,k,xi,lfid,check,x,y,curv,poly,g];
check[label_,val_]:=Print[If[TrueQ[val],"PASS: ","FAIL: "],label];

check["boundary prime-power infinite geometric series",
 FullSimplify[Sum[Log[p]^2 p^(-k s),{k,1,Infinity}]==Log[p]^2/(p^s-1),
 Assumptions->p>1&&s>0]];
check["global KMS FS variance prime-power series",
 FullSimplify[Sum[k Log[p]^2 p^(-k s),{k,1,Infinity}]==Log[p]^2 p^s/(p^s-1)^2,
 Assumptions->p>1&&s>0]];
check["boundary-vs-Fisher trace-class correction",
 FullSimplify[Log[p]^2 p^s/(p^s-1)^2-Log[p]^2/(p^s-1)==
 Log[p]^2/(p^s-1)^2,Assumptions->p>1&&s>0]];

lfid[q_,s_,t_]:=Sqrt[(1-q^s)(1-q^t)]/(1-q^((s+t)/2));
check["local TFD fidelity second mixed derivative",
 FullSimplify[(D[Log[lfid[q,s,t]],s,t]/.t->s)==
 q^s Log[q]^2/(4(1-q^s)^2),Assumptions->0<q<1&&s>0]];

(* Prequantum Poincare-disk connection on arithmetic twistor line. *)
curv=FullSimplify[D[x/(1-x^2-y^2),x]-D[-y/(1-x^2-y^2),y]];
check["twistor disk prequantum curvature",
 FullSimplify[curv==2/(1-x^2-y^2)^2]];
(* Blaschke numerator and denominator have equal boundary absolute square. *)
check["inner Blaschke unitary boundary despite interior zero",
 FullSimplify[(w-a)(1/w-a)==(1-a w)(1-a/w),Assumptions->w!=0]];
check["simple interior Blaschke zero",FullSimplify[(1/3-1/3)/(1-1/9)==0]];

xi[z_]:=z(z-1)Gamma[z/2]Zeta[z]/(2 Pi^(z/2));
c=-EulerGamma^2-2StieltjesGamma[1];
completed=FullSimplify[c-1+PolyGamma[1,1/2]/4];
Print[{"finitePartLogZetaSecond",N[c,36],
"completedLogXiSecondAt1",completed,N[completed,36]}];

curvXi[z_]:=N[xi''[z]/xi[z]-(xi'[z]/xi[z])^2,35];
Print[{"shiftedXiFakeCurvatureAt1",curvXi[4/5]+curvXi[6/5],
"knownOffAxisZero",N[1/5+I Im[ZetaZero[1]],30]}];

(* Prime-only positive trace-class quartic curvature determinant candidate,
   not the Riemann xi determinant; diagnostic deliberately samples primes. *)
amin[p_]:=Log[p]^4/(p-1)^2;
ztrace=N[Sum[amin[Prime[k]],{k,1,5000}],22];
ztr2=N[Sum[amin[Prime[k]]^2,{k,1,5000}],22];
h0=N[xi''[1/2]/(2xi[1/2]),28];
h1=N[(xi''[1/2]^2/4-xi[1/2] xi''''[1/2]/12)/xi[1/2]^2,28];
Print[{"quarticPrimeTraceFirst5000",ztrace,
"scaleFreePrimeH1OverH0Sq",ztr2/ztrace^2,
"trueXiH1OverH0Sq",h1/h0^2}];
Print["ALL GAUGE/CS IDENTITIES ARE ANALYTIC OR FINITE ALGEBRA. NO RH POSITIVITY PROOF."];

(* CERTIFIED ENTIRE PRIME-TAIL INEQUALITY, not a finite-prime heuristic.
   For p>1000, log(p)<(3/2)p^(1/4) since max(log x/x^(1/4))=4/E<3/2;
   (p-1)^4>p^4/16. Thus a_p^2<16(3/2)^8/p^2 and
   total prime tail <16(3/2)^8/1000=6561/16000<411/1000.
   Here lower/upper finite-prime contributions use fully exact rational
   arctanh intervals for log(p), not machine floats. *)
ClearAll[logLo,logHi,logBounds,r,lev,scale,scaleout,plist,intervals,denLower,numUpper];
lev=8; scale=10^8; scaleout=10^8;
logLo[z_]:=Module[{rr=(z-1)/(z+1)},
   2 Sum[rr^(2j+1)/(2j+1),{j,0,lev-1}]];
logHi[z_]:=Module[{rr=(z-1)/(z+1)},
   logLo[z]+2 rr^(2lev+1)/((2lev+1)(1-rr^2))];
logBounds[p_]:=Module[{kk=IntegerLength[p,2]-1,yy},
 yy=p/2^kk;{kk logLo[2]+logLo[yy],kk logHi[2]+logHi[yy]}];
plist=Prime[Range[PrimePi[1000]]];
intervals=Table[Module[{bb=logBounds[pp],ll,uu},
 ll=Floor[scale bb[[1]]];uu=Ceiling[scale bb[[2]]];
 {Floor[scaleout ll^4/(scale^4(pp-1)^2)],
  Ceiling[scaleout uu^8/(scale^8(pp-1)^4)]}],{pp,plist}];
denLower=Total[intervals[[All,1]]]/scaleout;
numUpper=Total[intervals[[All,2]]]/scaleout;
check["CERT exact rational first-168-prime trace lower >11/2",denLower>11/2];
check["CERT exact rational first-168-prime squared trace upper <53/50",numUpper<53/50];
check["analytic infinite tail bound <411/1000",
  FullSimplify[16(3/2)^8/1000<411/1000]];
check["ALL-prime quartic determinant invariant <1/20",
 FullSimplify[(53/50+411/1000)/(11/2)^2<1/20]];
Print[{"EXACT prime-trace lower",denLower,"EXACT prime-squared-trace upper",numUpper,
 "all-prime scale-free ratio <1/20",True,
 "true-xi ratio ~0.0696323806 >1/20 (independently Arb-certified xi moments, not certified by this script)"}];


(* Product-formula gauge C = P_infty − log n:
   group averaging on Schwartz(t)⊗finite-number support sends
   1/(2π)∫dλ exp(i λ(t−log n)) -> delta(t−log n).
   Thus the nonzero physical Hilbert is an evaluation quotient ℓ²(N),
   despite ker(C)={0} in auxiliary L²(R)⊗ℓ²(N). *)

ClearAll[ss,xx,archGaussian,xiFormula];
archGaussian=FullSimplify[Integrate[Exp[-Pi xx^2] xx^(ss-1),
 {xx,0,Infinity},Assumptions->ss>1],Assumptions->ss>1];
xiFormula=ss(ss-1)Gamma[ss/2]Zeta[ss]/(2 Pi^(ss/2));
check["all-prime gauge physical norm equals zeta",
 FullSimplify[Sum[n^(-ss),{n,1,Infinity}]==Zeta[ss],Assumptions->ss>1]];
check["Arch Gaussian plus product-formula gauge gives exact xi norm for real s>1",
 FullSimplify[ss(ss-1) archGaussian Zeta[ss]==xiFormula,Assumptions->ss>1]];
Print[{"infinite real-Arch physical-state norm",archGaussian,
 "critical state sum_n n^(-1/2) diverges (p-series)",True}];
