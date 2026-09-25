# Conservative prime colligation and the critical Schatten threshold

Date: 2026-09-25. Status: exact reduction, not RH.

For a>1/2 set r_p=p^{-a}, l_p=log p, q_p(z)=exp(i l_p z), and
b_p(z)=(q_p(z)-r_p)/(1-r_p q_p(z)).

The scalar disk map phi_r(q)=(q-r)/(1-r q) is the transfer function of the 2 by 2 unitary colligation
U_r=[[r,sqrt(1-r^2)],[sqrt(1-r^2),-r]].
Therefore b_p is a conservative delay-line transfer function and is inner in the upper half-plane.

For real k its phase derivative is
(1/i) b_p'(k)/b_p(k)
= l_p (1-r_p^2)/(1-2 r_p cos(k l_p)+r_p^2)
= l_p [1+2 sum_{m>=1} r_p^m cos(m k l_p)].

Hence the local prime-power current equals one half of the scattering phase derivative after subtracting the free delay l_p.

The global perturbation from the free direct-sum colligation is Hilbert-Schmidt for a>1/2 because its p-th block is O(r_p) and sum_p r_p^2=sum_p p^{-2a}<infinity. Thus the critical half-density line is exactly the boundary of the natural S2 class.

On prime state space define R_a=diag(p^{-a}) and Q_z=diag(exp(i z log p)). For a>1/2 the Carleman-Fredholm determinant exists and
-log det_2(I-R_a Q_z)
= sum_p sum_{m>=2} p^{-am} exp(i m z log p)/m.

Therefore every repeated prime orbit m>=2 is already contained in a canonical Hilbert-Schmidt determinant throughout a>1/2. The only Euler-log term excluded by det_2 is the primitive trace sum_p p^{-a} exp(i z log p).

This matches the independent Higgs derivative reduction: higher prime powers are controlled; the primitive-prime linear mode is the load-bearing trace anomaly.

New exact closure target: construct the co-Poisson/Archimedean completion as a zero-independent renormalized trace of the conservative S2 system. It must restore the primitive trace without importing analytic continuation of log zeta. If that renormalized trace is single-valued and compatible with the conservative dilation for every a>1/2, the resulting Hardy transfer is inner and RH follows.

Using zeta regularization for the primitive trace would be circular: its logarithmic singularities are exactly where zeta zeros enter.