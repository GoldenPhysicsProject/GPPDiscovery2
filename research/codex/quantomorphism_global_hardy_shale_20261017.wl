(* GPP Oct17: global arithmetic Hardy polarization / Shale-Stinespring failure.
   One-prime rank-one boundary commutators do NOT globalize as
   Hilbert-Schmidt operators in the rational-Fourier Hardy space.
   Full mathematical argument in the private bridge research note.
   RH / GRH OPEN. *)

ClearAll[p,m,n,q,check];
check[tag_,v_]:=Print[If[TrueQ[v],"PASS: ","FAIL: "],tag];
q[m_,p_]:=(m+1)/(m+p);

check["explicit rational family in the Hardy crossing interval",
 FullSimplify[1/p<=q[m,p]&&q[m,p]<1,
 Assumptions->p>=2&&m>=0&&Element[{p,m},Integers]]];
check["prime multiplication crosses each family mode above frequency 1",
 FullSimplify[p q[m,p]>=1,
 Assumptions->p>=2&&m>=0&&Element[{p,m},Integers]]];
check["rational family pairwise distinct",
 FullSimplify[q[m,p]-q[n,p]==
 (p-1)(m-n)/((m+p)(n+p)),
 Assumptions->p>=2&&Element[{p,m,n},Integers]&&m>=0&&n>=0]];
check["infinite crossing occurs also for the prime 2",
 FullSimplify[q[m,2]==(m+1)/(m+2),Assumptions->m>=0]];

Print["Let e_q denote orthonormal rational Fourier characters on K_phase."];
Print["For each p>1, [P_plus,U_p]e_q=e_(pq) iff 1/p<=q<1, else 0."];
Print["The q_m family gives infinitely many orthonormal inputs and outputs."];
Print["Hence [P_plus,U_p] is not compact, not Hilbert-Schmidt, and"];
Print["U_p is not in the restricted unitary group of this polarization."];
Print["On the one-prime integer lattice q=p^k, only k=-1 crosses."];
Print["Tensoring rank-one local defects by identity on infinitely many other"];
Print["prime states produces infinite rank, not Hilbert-Schmidt."];
Print["Diagonal positive weights making ALL prime translations unitary"];
Print["must be constant: w(pq)=w(q), primes generate Q_positive."];
Print["This says nothing by itself about the existence of a different"];
Print["modular/idele-class/relative polarization (GNS, semifinite modules)."];
Print["RH/GRH OPEN."];