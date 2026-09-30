# An explicit zero-retaining Poisson Hilbert quotient and its exact scale growth

Date: 2026-09-30 UTC / 2026-09-29 America/Toronto.

Status: an explicit Hilbert construction retaining every nontrivial zero; proofs of its exact functional norms, reflection, and scale covariance; an exact obstruction to using its inherited or any equivalent norm for the required subexponential dynamics. A second, inequivalent time-averaged metric is constructed on finite spans of critical zero values, but its extension to all zero values is not proved. This is NOT an RH proof. No Lean certification or novelty claim is made.

Daniel asked for completion, not an audit. The work below actually constructs the proposed completion and calculates its dynamics. Failure of this completion's dynamical estimate says nothing against RH or principal-series membership. It identifies a topology that cannot establish that membership.

## 1. Starting state and inputs

The starting Discovery2 workbench head was `6590967a1e1cde10d416c1fc7d8c1246273b35cd`, specifically `research/2026-09-29_completed_global_projective_poisson_complex.md`. Its final target had three conditions: all zero functionals survive continuously; one dilation is contractive; Poisson reflection and the elementary channels are respected. The current construction establishes the first and third conditions, then computes why the second fails for this norm.

The supplied global-representation paper was read directly: Barrero, Barthel, Pol, Strickland, Williamson, *Global representation theory: Homological foundations*, arXiv:2505.21449v2, especially Definition 3.10, Proposition 3.13, the proof of Proposition 3.21, Theorem 7.7 and Lemma 7.10. The finite-abelian category used in the current note is a multiplicative global family. Its cyclic evaluation is divisor incidence. As the existing construction already explicitly records, the density lines L_s are all algebraically isomorphic to the unit. Their metric information must therefore be supplied by an analytic construction.

Read the current bridge bootstrap, research tail, heuristics, and latest Supabase Codex records. The visible GPPVerify PR #216 head was `e3e57f073d422d8fd05848f1296399bb9c651375`; this session did not change GPPVerify or establish a new CI result.

After deriving the weighted construction, the operator-domain precedent was checked against Ralf Meyer, *A spectral interpretation for the zeros of the Riemann zeta function*, arXiv:math/0412277v3, Theorems 3.3 and 4.1 and Corollary 4.2. Meyer already constructs zero spectral data on a nuclear Frechet quotient. No claim is made that zero cohomology itself is a new discovery. Our explicit weighted Hilbert norm and its failure analysis are the calculation needed here.

## 2. A fully specified Poisson domain

Use the Fourier convention

    fhat(y) = integral_R f(x) exp(-2 pi i x y) dx.

Let

    S_0 = {f in S(R): f even, f(0)=0, fhat(0)=0}.

Both Fourier transformation and normalized dilation preserve this space. For u>0 put

    (E f)(u) = sqrt(u) sum_{n>=1} f(nu),
    k_f(x) = (E f)(exp x).

For every u>0 the sum converges absolutely. Poisson summation, evenness, and the two vanishing conditions give exactly

    sum_{n>=1} f(nu) = u^(-1) sum_{n>=1} fhat(n/u),
    E f(u) = E fhat(1/u),
    k_f(x) = k_fhat(-x).

For any A>0, Schwartz decay bounds the first sum by O(u^(-A)) as u tends to infinity, after adjusting A for the half-density. Applying the same bound to fhat in the Poisson identity gives O(u^A) as u tends to zero. Thus k_f decays faster than every exponential at both ends. The same is true after differentiating in x.

This proves the actual target-domain statement; it does not merely formally continue a divergent Euler sum.

For Re(s)>1, absolute convergence and v=nu give

    integral_R k_f(x) exp((s-1/2)x) dx
      = zeta(s) M f(s),
    M f(s) = integral_0^infinity f(u) u^(s-1) du.

The left side is entire. Since f is even and f(0)=0, f(u)=O(u^2) near zero, so M f is holomorphic for Re(s)>-2. Also M f(1)=0 because fhat(0)=2 integral_0^infinity f=0. The zeta pole at s=1 is therefore cancelled. Analytic continuation proves the displayed identity throughout the critical strip. In particular every nontrivial zero rho annihilates every k_f, without a convergence assumption at rho.

The conditions f(0)=fhat(0)=0 remove the two elementary Poisson channels before completion. This is a precise choice of domain, not a proof that every unrestricted-domain mapping cone is equivalent to it.

## 3. The Hilbert quotient and all-zero retention

For a>0 define

    H_a = L2(R, exp(2a|x|) dx),
    R_a = closure_{H_a}{k_f: f in S_0},
    Q_a = H_a / R_a.

These objects use the integer lattice, Fourier transformation, and a specified norm. They do not use a zero list or impose any zero location.

For |Re(z)|<a define the complex-linear functional

    ell_z(h) = integral_R h(x) exp(zx) dx.

Cauchy--Schwarz gives its exact ambient norm:

    ||ell_z||^2 = integral_R exp(2 Re(z)x-2a|x|) dx
                 = a/(a^2-Re(z)^2).

With inner product <h,g>=integral conjugate(h) g exp(2a|x|) dx, its Riesz vector is

    h_z(x) = exp(conjugate(z)x-2a|x|).

If z=rho-1/2 for a nontrivial zero rho in this strip, Section 2 shows that ell_z annihilates R_a. Consequently h_z belongs to R_a-perp, and ell_z descends to Q_a with EXACTLY the same norm. It is nonzero because h_z is a nonzero vector in that perpendicular space. Equivalently ell_z(h_z)=||h_z||^2>0.

Taking a=1/2 includes EVERY nontrivial zero, since 0<Re(rho)<1. If beta=Re(rho),

    boxed: ||ell_{rho-1/2}||_{Q_(1/2)^*}^2 = 1/[2 beta(1-beta)].

This completes bounded, nonzero retention of every zero in this explicit Hilbert space. It includes a hypothetical off-line zero. It does not silently complete such a zero away.

It also specifies what is NOT proved: no claim that every element of the dual is a convergent sum of these zero functionals, or that this quotient is faithfully equivalent to the entire nuclear mapping cone. Retention of every zero functional is enough for the proposed RH implication, and is the statement established here.

## 4. A single arithmetic Gaussian seed detects exactly the desired parameters

The following seed is already consistent with the project's Riemann-seed construction:

    phi(u) = (4 pi^2 u^4 - 6 pi u^2) exp(-pi u^2).

Let D=u d/du and g(u)=exp(-pi u^2). Then phi=D(D+1)g. Fourier transformation sends D to -(D+1), while g is self-dual. Hence phi is self-dual. Also phi(0)=0 and integral_R phi=0, so phi belongs to S_0.

Integration by parts gives

    M phi(s) = [s(s-1)/2] pi^(-s/2) Gamma(s/2).

Therefore

    integral_R k_phi(x) exp((s-1/2)x) dx = xi(s).

This derives the completed function from a fixed arithmetic Gaussian seed. It does not insert xi as a differential by definition. The kernel k_phi is even by Poisson and strictly positive: for x>=0 each summand has nu>=1 and 4 pi^2(nu)^4-6 pi(nu)^2>0; reflection handles x<0.

Consequently, for a=1/2 and |Re(z)|<1/2,

    ell_z annihilates R_a  iff  xi(1/2+z)=0.

The reverse direction follows from Section 2; the forward direction follows by testing just k_phi. Thus among these centered Mellin evaluation functionals, the annihilator selects precisely the nontrivial zero parameters. No spurious point-evaluation spectrum is being substituted.

Positivity and evenness of k_phi alone do not locate its complex Laplace zeros. The earlier survival-amplitude counterexamples remain relevant.

## 5. Exact covariance, reflection, and the ambient bound

Let (T_t h)(x)=h(x+t). A change of variables gives

    ||T_t||_{H_a}=exp(a|t|).

The upper bound follows from |x-t|-|x|<=|t|; equality follows from functions supported sufficiently far on the appropriate half-line.

Writing f_t(u)=exp(t/2)f(exp(t)u) gives

    k_{f_t}(x)=k_f(x+t).

Hence R_a is invariant under T_t for both signs of t. There is a strongly continuous quotient group V_t on Q_a, satisfying initially

    ||V_t||<=exp(a|t|),
    ell_z(V_t q)=exp(-zt)ell_z(q).

Reflection J h(x)=h(-x) is isometric on H_a. Since J k_f=k_fhat, it preserves R_a, descends to Q_a, and satisfies J V_t J=V_(-t). Complex conjugation also descends. They implement the usual zero symmetries on the retained functionals.

Thus the required scale character and Poisson symmetry genuinely survive Hilbert completion. The remaining issue is the size of V_t.

## 6. Exact two-mode obstruction to contractivity

For two retained zero parameters z,w, the Riesz Gram matrix is

    <h_z,h_w> = K_a(z,w)
               = 4a/[4a^2-(z+conjugate(w))^2].

For critical zeros z=i gamma and w=i eta the normalized overlap is

    r = 4a^2/[4a^2+(gamma-eta)^2] > 0.

Their dual eigenvalues under V_t^* are exp(i gamma t) and exp(i eta t). A contraction cannot have two distinct eigenvalues on the unit circle with nonorthogonal eigenvectors: in their normalized basis, positivity of G-A^* G A would require a positive matrix with zero diagonal but nonzero off-diagonal entry. Such a matrix has one negative eigenvalue.

More quantitatively, on this two-dimensional invariant dual space the exact operator norm is

    sqrt(1+q^2)+q,
    q = r |sin((gamma-eta)t/2)|/sqrt(1-r^2).

For a=1/2, t=log 2, and the first two familiar approximate ordinates, this is 1.0142461176278486. An independent generalized-eigenvalue computation agrees to floating-point precision. The numbers are illustrative, not a new certification of zero ordinates.

This failure is caused by overlap between critical characters, not by a discovered off-critical zero. It therefore cannot be read as evidence against RH.

## 7. Stronger result: the inherited quotient norm has the full exponential growth

In fact the upper bound in Section 5 is exact:

    boxed: ||V_t||_{Q_a} = exp(a|t|) for every a>0 and real t.

The lower bound uses only zeros already known unconditionally to lie on the critical line. It does not assume RH, hypothetical off-line zeros, or multiple zeros.

### 7.1 External input, stated narrowly

Bui--Conrey--Young, arXiv:1002.4127v2, Theorem 1.1, proves a positive proportion of simple critical zeros. Combined with the classical zero-counting asymptotic, this gives a set Gamma of DISTINCT critical ordinates whose count in [0,T] is at least c T log T for large T, with some c>0. The exact proportion is immaterial here.

It follows by partitioning [0,T] into intervals of length epsilon that, for every integer n and every epsilon>0, some interval of that length contains n+1 distinct elements of Gamma. Taking epsilon to zero produces arbitrarily tight finite clusters of any prescribed size. A fixed bounded interval cannot contain infinitely many such zeros, so the cluster centers escape to large height.

### 7.2 Remove the harmless common frequency

Identify a Riesz vector h with F=exp(2a|x|)h. Its norm is

    ||h||_{H_a}^2 = integral_R |F(x)|^2 exp(-2a|x|) dx.

The dual action becomes F(x) -> F(x-t). Critical Riesz vectors correspond to exp(-i gamma x). Multiplication by a common phase exp(i gamma_0 x) is isometric in this weighted space, and changes the translated function only by a scalar phase of modulus one. It therefore does not affect any norm ratio.

### 7.3 A cluster approximates every polynomial of fixed degree

Choose n+1 critical ordinates gamma_0,...,gamma_n in an interval of length epsilon. Their exponential functions are in the invariant dual space. For each j<=n take the divided difference of gamma -> exp(-i gamma x) at the first j+1 nodes and multiply it by j!/(-i)^j and by exp(i gamma_0 x).

As epsilon tends to zero, this tends to x^j. The integral formula for divided differences bounds its absolute value by |x|^j. The same bound with |x-t| holds after translation. Dominated convergence against exp(-2a|x|) therefore proves convergence in both the original and translated weighted norms.

Linear combinations show that, for every polynomial p,

    ||V_t|| >= ||p(.-t)||_{L2(exp(-2a|x|)dx)}
                / ||p||_{L2(exp(-2a|x|)dx)}.

Although the common-frequency modulation need not preserve the arithmetic dual space, every vector BEFORE modulation is a linear combination of actual zero Riesz vectors. Modulation is used only to compare equal norm ratios. This distinction is essential.

### 7.4 Polynomials recover the full translation norm

Polynomials are dense in L2(R,exp(-2a|x|)dx). One direct proof: if F is orthogonal to every polynomial, then

    H(z)=integral_R F(x) exp(-2a|x|) exp(zx) dx

is holomorphic for |Re(z)|<a by Cauchy--Schwarz. All derivatives at zero vanish, so H vanishes in the strip. Fourier uniqueness implies F=0.

Translation is bounded with exact norm exp(a|t|) on this weighted L2 space. By density its norm is the supremum of the displayed polynomial ratios. Thus ||V_t||>=exp(a|t|), and the earlier upper bound proves equality. QED.

The finite controls approximate this limit for a=1/2 and t=log 2. Degree 1 gives 1.2746550499744564; degree 4 gives 1.4136577128125007; degree 12 gives 1.4142135623455763, compared with sqrt(2)=1.414213562373095. The proof is the cluster-and-density argument, not the numerical table.

### 7.5 Consequence for metric repair

An equivalent Hilbert norm changes operator norms by fixed multiplicative constants. It cannot change the exponential growth rate a to zero. Therefore neither a bounded positive invertible change of metric nor an equivalent quotient norm can make this Q_a dynamics subexponential or contractive.

This is stronger than finding an inconvenient two-mode overlap. The exponentially weighted completion is useful for retention and exact kernels, but is unsuitable as the final physical norm even if RH is true. A successful norm must be genuinely inequivalent to this one. The obstruction already uses simple critical zero values, so removing only multiple-zero jets does not fix it.

## 8. A concrete inequivalent metric attempt: time averaging

On a finite span of distinct retained value vectors, define

    B_T(v,w) = (1/(2T)) integral_{-T}^T <V_t^* v,V_t^* w> dt.

Its exact matrix is

    B_T(h_z,h_w)
      = K_a(z,w) sinh((z+conjugate(w))T)/[(z+conjugate(w))T],

with the continuous value 1 for the ratio at zero. Each finite B_T is positive.

If all parameters in the chosen finite span are critical and distinct, the diagonal remains 1/a and every off-diagonal term tends to zero. This constructs an invariant positive inner product on that algebraic span, with distinct frequencies orthogonal. Its completion over critical value vectors is unitary and need not retain derivative jets. Thus it does not assert that zeta zeros are simple.

For a retained parameter z with delta=Re(z)!=0, however,

    B_T(h_z,h_z)
      = ||h_z||^2 sinh(2 delta T)/(2 delta T)
      ~ ||h_z||^2 exp(2|delta|T)/(4|delta|T).

The metric diverges in that direction. Restricting to finite-mean vectors would erase a hypothetical off-line zero; claiming that all zero vectors have finite mean would assume exactly the missing location statement.

Therefore this attempt solves orthogonality on the critical value sector but does NOT solve all-zero retention for the averaged metric. Passing T to infinity cannot be justified by the finite-T positivity.

## 9. What the global-projective splitting can and cannot currently supply

The paper's Lemma 7.10 gives, from a torsion-free x in X(G), the algebraic split injection

    i_T([alpha]) = [alpha] tensor alpha^*(x).

If the quotient-map basis is orthonormal and X(T) has a Hilbert norm, then pointwise

    ||i_T v||^2 = sum_alpha |v_alpha|^2 ||alpha^*(x)||^2.

For every Hilbert left inverse r_T,

    ||r_T|| >= sup_alpha 1/||alpha^*(x)||.

The pointwise Moore--Penrose left inverse attains this lower bound, but need not be natural in T. The algebraic natural splitting in the paper supplies no uniform bound on these norms. Thus it cannot presently supply the domination needed to keep every zero finite in Section 8.

The current repo already records the underlying density-line obstruction: L_s is algebraically trivial for every s, while the counting-Haar norm of the quotient transport is k^(1/2-Re(s)). This session does not discard the categorical model; it makes explicit the quantitative estimate a categorical splitting would have to contribute.

## 10. Exact outcome and remaining work

Constructed and proved:

1. A specific Poisson test domain with justified Mellin continuation.
2. A zero-independent Hilbert quotient Q_(1/2) retaining EVERY nontrivial zero as a bounded nonzero functional.
3. Its exact functional norms, Gram kernel, scale characters, and Poisson reflection.
4. A fixed self-dual Gaussian derivative whose E-image has completed Mellin transform xi.
5. Exact exponential quotient-group growth, already forced by known simple critical zeros.
6. A positive invariant time-averaged metric on finite critical-value spans, with an exact divergence formula for hypothetical off-line directions.

Still unproved:

A single arithmetic norm, genuinely different from the weighted analytic norm above, that retains every zero value and has the requisite contractive or subexponential scale action. The time-average construction does not establish this. No inference from the true critical-line subset to all zeros is made.

Next constructive requirement: an arithmetic estimate for a selective value topology or a quantitatively controlled projective/Poisson realization. It must distinguish survival of zero values from uniform analytic control in neighborhoods of arbitrarily dense spectral clusters. Merely shrinking a fixed exponential weight, applying a bounded metric change, or invoking the algebraic splitting theorem will not provide that estimate.

Reproducible finite controls: `scripts/check_weighted_poisson_completion.py`; output `research/2026-09-30_weighted_poisson_controls.json`. The controls use numpy/scipy in float64 and verify normalizations, independent Gram calculations, and the polynomial norm limit. They are not infinite-dimensional proof checks.

## 11. Later clarification: one cyclic Gaussian orbit remains a viable target

The exact exponential operator norm above excludes a uniform subexponential operator bound in this topology. It does not exclude a subexponential bound for one fixed arithmetic state. The later note `research/2026-09-30_imaginary_axis_reconstruction_and_thermal_completion.md` constructs a zero-independent Gaussian q_tau whose evaluation is exp(tau z^2), nonzero at every possible zero, and proves that a subexponential bound on this single orbit already forces every zero onto the imaginary axis in the centered coordinate. Its translates are cyclic. Explicit Poisson trial functions give nearly constant residual norms over the tested times 0 through 20, without proving an all-time estimate. Thus a change of topology is necessary for the uniform-operator route described above, but is not shown necessary for this weaker sufficient route.

The controls referenced above were reconstructed after workspace replacement and are now actually saved in the repository. The regenerated values agree with the displayed finite norms; their numerical output records the reconstruction.

## References

- Supplied source: Barrero et al., *Global representation theory: Homological foundations*, arXiv:2505.21449v2, https://arxiv.org/abs/2505.21449 .
- Meyer, *A spectral interpretation for the zeros of the Riemann zeta function*, arXiv:math/0412277v3, https://arxiv.org/abs/math/0412277 . Used for the established operator-domain/spectral background, not as an RH theorem.
- Bui, Conrey, Young, *More than 41% of the zeros of the zeta function are on the critical line*, Theorem 1.1, https://arxiv.org/abs/1002.4127 . Used only for positive-density simple critical zeros.
- NIST DLMF Section 25.10, https://dlmf.nist.gov/25.10 . Background on the critical strip and zero symmetries.
