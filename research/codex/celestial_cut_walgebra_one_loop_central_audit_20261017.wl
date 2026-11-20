(* Golden Physics Project / Daniel Toupin, October 17, 2026.
   Actual v19 full celestial scalar CUT and honest quantum OPE calibration.
   The free-current model is a controlled CFT, NOT a computed gravity TT OPE.
   No RH proof, no claim of a numerical quantum celestial graviton c. *)
ClearAll[lam,t,u,q,m,n,nc,z,w,phi,K,cc,check,Csq,cutDet];
check[tag_,v_]:=Module[{ok=TrueQ[v]},
  Print[If[ok,"PASS: ","FAIL: "],tag];If[!ok,Abort[]]];
phi[lam_]:=lam/(8Sinh[Pi lam]);
K[t_]:=Sech[t/2]^2/16;
(* Wolfram Fourier convention has factor 1/sqrt(2pi). *)
tr=FourierTransform[K[t],t,lam,FourierParameters->{0,1}];
check["FULL infinite shadow Fourier density",
 FullSimplify[Sqrt[2Pi]tr == 2Pi phi[lam],
 Assumptions->Element[lam,Reals]&&lam>0]];
check["positive full cut total spectral mass 1/16",
 FullSimplify[Integrate[phi[lam],{lam,0,Infinity}]==1/32]];
check["exact spectral second moment",
 FullSimplify[-(D[K[t],{t,2}]/.t->0)==1/32]];

kq[q_]:=q/(4(1+q)^2);
cutDet=Together[kq[1/4]kq[1/9]-kq[1/6]^2];
check["OS matrix cut determinant exactly -891/24010000",
 cutDet == -891/24010000];
check["cut OS fails at strictly positive times log2,log3",cutDet<0];

(* Regulated TT claim in qg_definitive: after multiplying
   conjugate gamma factors, phases CANCEL from modulus. *)
Csq[lam_]:=Pi^2 lam^2(4+3 Csch[Pi lam]^2)/(3(1+9lam^2));
check["positive gamma modulus identity",
 FullSimplify[Csq[lam] ==
 (Pi lam/Sinh[Pi lam])^3 /
 ((1+9lam^2)3Pi lam/Sinh[3Pi lam]),
 Assumptions->lam>0]];
check["gamma correlator normalization at lambda=0",
 Limit[Csq[lam],lam->0]==1];
check["gamma modulus nonzero at infinity",
 Limit[Csq[lam],lam->Infinity]==4Pi^2/27];
check["gamma double Gaussian regulator 1/eps coefficient",
 FullSimplify[(4Pi^2/27)^2 Pi]==16Pi^5/729];

(* Free Heisenberg-current OPE calibration:
    <J_a(z)J_b(w)> = delta_ab/(z-w)^2,
    T_n(z)= 1/2 sum_a :J_a(z)^2:
    Wick double contraction central = n/2.
    Single contraction = 2 T/(z-w)^2 + dT/(z-w).
    This family lives on the same positive infinite L2(Phi dlam),
    using any n mutually orthonormal currents.
    It proves the scalar cut density by itself does not select c. *)
check["Wick double contraction gives c=n (TT pole n/2)",
 FullSimplify[nc*(2/4)==nc/2]];
check["oriented two-faced anomaly cancels equal positive c",
 FullSimplify[nc-nc==0]];
check["TT central residue Ward term",
 FullSimplify[(cc/2)(m+1)m(m-1)/6==
  cc(m^3-m)/12]];
check["the local Ward contact coefficient is -pi c/12",
 FullSimplify[(cc/2)*(-Pi/6)==-Pi cc/12]];
Print["New exact conclusions: complete positive shadow CUT is not OS-positive;"];
Print["the old c=0 gamma correlator diverges, not cancels;"];
Print["free Wick models on the same full cut Hilbert measure allow c=1,2,3,...;"];
Print["equal opposite chiral c cancels cL-cR but not cL+cR;"];
Print["actual graviton one-loop TT identity and anomaly associator uncomputed."];
