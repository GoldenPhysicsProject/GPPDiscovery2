# The BPY vacuum graph: exact Schur defect and a quantified failure of uniform completion

Date: 2026-09-29, America/Toronto.
Status: exact operator derivation using the existing connected BPY estimates. No arithmetic no-escape bound, no RH proof, no Lean certification.

This is the arithmetic-specific continuation of the preceding scale-growth attempt. It computes a genuine positive Schur complement and identifies what it measures. It is NOT identified with the RH Stieltjes function m_*.

## 1. Established inputs and conventions

From research/2026-09-27_bohr_bpy_connected_intertwiner.md and discovery/rh/RH_BPY_CONNECTED_MOBIUS_STATE_2026-09-25.md, let H_ar=ell2(N), H_B=L2(P), and let e=1 be the unit vacuum vector. The bounded connected synthesis is

    C_s c = sum_n c_n [U_n Omega_s - a(s)e],
    Omega_s=Q^(s/2),
    a(s)=E[Q^(s/2)]=2 xi(s).

Its range lies in e-perp. It is locally bounded for Re s>0. In particular, the workbench proves a covariance majorant by a bounded GCD kernel. At s=1/2 it is even bounded below by a first-chaos estimate. The lower bound is not needed below; the existing upper bound suffices.

For Re s>1/2 the Mobius coefficient vector

    c_s=(mu(n)n^(-s))_n

belongs to ell2 and depends holomorphically on s. Its connected image is bounded on compact parameter sets. The completed vector is

    Psi_s=A(s)e+C_s c_s,
    A(s)=s(s-1) pi^(-s/2) Gamma(s/2).

It agrees with ordinary Mobius-decimated BPY synthesis in Re s>1. This is the established connected continuation. It does not assert convergence of the raw vacuum sum in Re s>1/2.

We use the product Hilbert norm on H_ar direct-sum H_B.

## 2. Exact closure of the raw synthesis graph

On finite coefficient vectors define

    E(c)=sum_n c_n,
    T_s c=C_s c+a(s)E(c)e.

If a(s) is nonzero, this operator is not closable. For example,

    h_N=(1/N)sum_(n=1)^N e_n

has ||h_N||=N^(-1/2), E(h_N)=1 and C_s h_N ->0, while T_s h_N ->a(s)e.

More precisely,

    closure graph(T_s)
      = {(c,C_s c+beta e): c in ell2, beta in C},       if a(s)!=0;

    closure graph(T_s)
      = {(c,C_s c): c in ell2},                         if a(s)=0.

Proof: the orthogonal projection onto e-perp of every graph vector is C_s c; this relation survives closure. Conversely approximate any c by finite vectors c_j. Correct the scalar sum of each c_j with a sufficiently long, sufficiently small constant block supported on unused indices. The correction has any prescribed sum and arbitrarily small ell2 norm. Boundedness of C_s makes its connected correction tend to zero. This realizes every beta when a(s)!=0. When a(s)=0, ordinary bounded-operator graph closure gives the second formula. QED.

Thus at a zero of xi the vertical vacuum line DISAPPEARS from the closed linear relation. The boundedness of the connected map does not prevent that change.

This result concerns this specific raw synthesis and product topology. It is not a statement that every possible arithmetic domain must be nonclosable, or that the co-Poisson construction is the same operator.

## 3. The completed vector's exact graph defect

Define

    d(s)=dist((c_s,Psi_s), closure graph(T_s)).

The preceding theorem gives the exact formula

    d(s)=0,             if a(s)!=0;
    d(s)=|A(s)|,        if a(s)=0.

At a zero, (0,A(s)e) is perpendicular to graph(C_s), so the distance is exactly its norm, not merely bounded below by it.

At every nontrivial zero in Re s>1/2, A(s)!=0: Gamma has no zeros or poles there, s is nonzero, and s=1 is not a zero of xi. Consequently a hypothetical right-half-plane zero is precisely a nonzero vacuum graph defect of the analytically continued vector.

This makes the limit-order issue concrete. At a zero rho,

    T_rho c = C_rho c

has zero vacuum mean for every finite c and for its bounded extension. Yet

    <e,Psi_rho>=A(rho)!=0.

Continuing the completed vector in s and closing the raw synthesis at s=rho do not give the same result. Assuming that they commute would insert exactly the missing theorem.

## 4. A regulated graph and its exact positive Schur complement

Let u_N=sum_(n<=N)e_n and E_N(c)=sum_(n<=N)c_n. Regulate only the singular vacuum channel:

    T_(s,N)c=C_s c+a(s)E_N(c)e.

This is a bounded operator on the full arithmetic Hilbert space. N is a vacuum cutoff, not a claim that C_s itself has been replaced by a finite-rank approximation.

Set

    G_s=I+C_s^* C_s,
    q_N(s)=<u_N,G_s^(-1)u_N>,
    b_N(s)=A(s)-a(s)E_N(c_s).

Because I<=G_s<=(1+||C_s||^2)I,

    N/(1+||C_s||^2) <= q_N(s) <= N.

Then the distance to the regulated graph is exactly

    d_N(s)^2
       := dist((c_s,Psi_s),graph(T_(s,N)))^2
        = |b_N(s)|^2 / [1+|a(s)|^2 q_N(s)].

Proof: write a candidate graph input as c_s+h. Orthogonality of e and Ran(C_s) makes the squared distance

    <h,G_s h> + |a(s)E_N(h)-b_N(s)|^2.

The minimum of this strictly convex quadratic form is the displayed rank-one Schur complement. Equivalently apply the inverse formula for G_s plus the rank-one positive operator |a|^2 u_N u_N^*. QED.

This calculation uses positive Hilbert norms throughout. Therefore positivity of this Schur complement does not imply absence of the graph defect. The missing issue is its limit and arithmetic interpretation.

There is even an unconditional bound, uniform in the cutoff:

    d_N(s) <= |A(s)| + sqrt(||c_s||^2+||C_s c_s||^2).

Indeed, weighted Cauchy--Schwarz gives

    |E_N(c_s)| <= sqrt(q_N(s)) sqrt(<c_s,G_s c_s>),

and |a|sqrt(q_N)/sqrt(1+|a|^2 q_N)<=1. Thus the regulated distances are locally uniformly bounded on Re s>1/2 even if a hypothetical off-line zero exists. This is a particularly explicit reason not to replace holomorphy by positivity or local boundedness in the normal-family step.

## 5. Exact pointwise limit without RH

If a(s)=0, then d_N(s)=|A(s)| for every N.

If a(s)!=0, the Schur formula gives

    d_N(s) <= sqrt(1+||C_s||^2)
                [|A(s)/a(s)|/sqrt(N) + |E_N(c_s)|/sqrt(N)].

For every fixed c in ell2,

    E_N(c)/sqrt(N) ->0.

Proof: N^(-1/2)u_N converges weakly to zero. Alternatively split c into a fixed finite head and an ell2-small tail, and use Cauchy--Schwarz on the tail. This convergence is uniform over compact subsets of ell2.

It follows that

    d_N(s) -> d(s)

with d(s) exactly as in section 3. Convergence is locally uniform on compact subsets of Re s>1/2 that avoid the zeros of a(s), since c_s has compact image there and C_s is locally bounded.

For sigma_0 in (1/2,1) and a compact zero-free set with Re s>=sigma_0, the elementary bound

    |E_N(c_s)| <= sum_(n<=N)n^(-sigma_0)=O(N^(1-sigma_0))

even gives

    d_N(s)=O(N^(-1/2)+N^(1/2-sigma_0)).

No cancellation estimate for mu was used. This is graph-distance convergence, NOT convergence of the unregularized scalar Mobius series.

## 6. Quantified concentration at a hypothetical zero

Suppose rho is an interior zero of a(s), of multiplicity m>=1:

    a(s)=alpha(s-rho)^m+O((s-rho)^(m+1)), alpha!=0.

On a fixed compact neighborhood let ||C_s||<=M. At the parameter scale

    s_N=rho+h N^(-1/(2m)),

one has sqrt(N)a(s_N)->alpha h^m. Since c_s is a compact ell2-valued family,

    a(s_N)E_N(c_(s_N)) ->0,
    b_N(s_N) -> A(rho).

The Schur bounds therefore imply

    |A(rho)| / sqrt(1+|alpha h^m|^2)
       <= liminf d_N(s_N)
       <= limsup d_N(s_N)
       <= |A(rho)| / sqrt(1+|alpha h^m|^2/(1+M^2)).

So the nonzero defect can remain inside a parameter region shrinking like N^(-1/(2m)), while disappearing at every fixed neighboring point. Finite-cutoff positivity or pointwise convergence on a zero-free set cannot exclude this mechanism.

For the simple model C_s=cI, q_N=N/(1+|c|^2) exactly, and the scaled profile has a corresponding exact limit. Numerical controls below verify that algebra. They do not posit an actual off-critical zeta zero.

## 7. Meaning for the proposed proof

The attempted argument was: the connected BPY vector is holomorphic with controlled norm, its vacuum has explicit Archimedean completion, therefore the full arithmetic evolution should retain the zeros with controlled growth.

The calculation identifies the unresolved interchange exactly. The completed vacuum is independent of the connected norm. A nonzero vertical vacuum relation is available at every parameter with xi(s)!=0; at a zero it disappears. The analytic continuation of Psi_s does not automatically belong to the newly smaller graph there.

Proving local-uniform convergence d_N->0 throughout Re s>1/2 would exclude this defect and hence prove RH, by the usual functional-equation reflection. Conversely, under RH the compact zero-free convergence already proved gives that limit. This is an exact diagnosis, not a replacement proof or a claim that graph distance is the desired resolvent.

Moreover d_N^2 contains complex conjugates and adjoints. It is a real-valued positive diagnostic, not a holomorphic scalar family to which Vitali may be applied. A local bound for it is not the holomorphic bound needed by the other Codex's slit-resolvent programme.

The next genuinely new arithmetic input must control the completed vacuum's compatibility with the physical closed relation, or identify a different coupled boundary map that has the exact scalar response and avoids this discontinuous loss. Orthogonal connected-sector estimates alone do not supply it.

## 8. Reproducibility and limits

Run discovery/verify_scale_graph_completions.py. It checks the Schur minimum against independent complex least squares, tests the model concentration scale, checks the Sobolev/TFD trace precision and scale bound, and verifies the off-real evaluation growth formula. Inputs are explicit finite matrices and Gaussian functions. No zeta-zero data or numerical evidence for RH is used.

All proofs above are independent of those floating-point checks. The existing connected-synthesis and BPY Mellin identities are inputs from the cited workbench notes, not newly Lean-certified here. No GPPVerify file or other worker's Discovery2 branch is changed.
