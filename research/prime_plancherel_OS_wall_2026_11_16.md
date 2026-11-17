# Prime Plancherel / OS wall at critical half-density (2026-11-16)

**Research status:** unconditional Euler-product and completed-functional-equation identities; high-precision numerical audit; **not** a proof of RH, ARP, OB-6 or a positive celestial arithmetic model. The underlying identities are classical; the new usefulness is identifying exactly where a naive Mellin/Haar transfer fails in our project.

## 1. An actual, unconditionally positive prime Hilbert kernel

For real sigma > 1, define the feature map J_sigma(t) indexed by n>=2:

    J_sigma(t)[n] = sqrt(Lambda(n)) * n^(-sigma/2-t),    t>=0.

It is in ell2 by absolute Euler-product convergence. With h(s):=-zeta'(s)/zeta(s), the *Hankel/reflection* kernel is

    K_sigma(t,u)=<J_sigma(t),J_sigma(u)>
                =sum_{n>=2}Lambda(n)*n^(-sigma-t-u)
                =h(sigma+t+u),       sigma>1, t,u>=0.

For any finite set c_j and t_j>=0,

    sum_i,j conj(c_i)c_j K_sigma(t_i,t_j)
      = sum_n Lambda(n)n^(-sigma) |sum_j c_j n^(-t_j)|^2 >= 0.

This is a real arithmetic reflection-positive semigroup kernel **without any zero input**. It is NOT the completed Weil form and its positivity is NOT RH.

## 2. The exact normalizability threshold for this feature map

At critical half-density sigma=1/2,

    ||J_(1/2)(t)||^2 = sum_n Lambda(n)n^(-1/2-2t).

It converges **if and only if t>1/4**. For exponents >1 use the absolutely convergent Euler product. The boundary series at exponent 1 diverges because h(s) has a simple positive pole as s->1+, and every smaller exponent has larger nonnegative terms. This proves the iff without PNT/RH. The critical-half-density feature vectors are well-defined and positive for t,u>1/4 but the boundary vector at t=0 does NOT exist in this Hilbert space.

The one-quarter threshold is a precise fact about this specific prime Laplace feature map, not a universal physical boundary or a theorem about celestial zero states.

## 3. Exact functional-equation value of the continued prime kernel

From xi(s) = (s(s-1)/2)*pi^(-s/2)*Gamma(s/2)*zeta(s) and xi(s)=xi(1-s), with xi(1/2)!=0, obtain xi'(1/2)=0. Logarithmic differentiation at 1/2 (where 1/s+1/(s-1)=0) gives

    h(1/2) = 1/2*(psi(1/4)-log(pi))
           = 1/2*(-gamma-log(pi)-pi/2-3log(2))
           = C_infty/2
           = -2.6860917096128327911164787487... < 0.

**C_infty** is exactly the negative real-place constant in GPPVerify:
GppVerify/RiemannHypothesis/ArchimedeanFloor.lean.

### Three precise NO-GO results, all unconditional

(A) The naive analytic continuation K_ac(t,u)=h(1/2+t+u) is **not** reflection positive, already because K_ac(0,0)<0. It also has a pole along t+u=1/2 inside the positive quadrant (the pole of zeta at s=1).

(B) Every finite prime cutoff K_N(t,u)=sum_{2<=n<=N}Lambda(n)n^(-1/2-t-u) is PSD, and any pointwise finite-kernel limit of PSD Gram forms remains PSD. Thus no positivity-preserving pointwise limit of these kernels on a domain containing (0,0) equals the negative analytic continuation. **Analytic continuation does not commute with positivity-preserving limit.**

(C) The unique constant counterterm c=-h(1/2) which makes the continued diagonal at (0,0) exactly 0 still fails PSD: a PSD matrix with K(0,0)=0 must have K(0,t)=0 for every t; h(1/2+t)-h(1/2) is nonzero at arbitrarily small positive t because h is nonconstant analytic near 1/2 (in particular its pole at 1 proves nonconstancy). Hence a neutral constant rank-one counterterm cannot rescue the reflected kernel. Removing only the scalar pole h(s)-1/(s-1) leaves critical diagonal C_infty/2+2=-0.6860917096... <0.

No-go C rejects only that natural constant subtraction; it does not rule out a carefully constructed completed gamma+pole reflection kernel.

## 4. A specific source-paper audit

The uploaded source 'haar_positivity_weil_wightman.tex' (title *Haar Positivity: From Weil to Wightman*) correctly distinguishes the positive-type **test** Omega^vee * Omega from positivity of the Weil **distribution** tested on it (its Weil-positive tests definition). This distinction is indispensable.

The paper's subsequent forward/converse proof sketch needs correction. It describes the Weil value as 'sum_rho |M Omega(rho)|^2 + (local terms, always >=0)' and then treats modulus-squared off-line contributions as capable of becoming negative. Those statements cannot simultaneously be correct: modulus squares are never negative; the **geometric** prime/gamma/pole and **spectral** zero sums are two expressions related by the explicit formula, not generically additive nonnegative terms.

In the usual critically normalized involution the individual spectral factor is instead the mixed pairing

    M Omega(rho) * conj(M Omega(1-conj(rho))),

which reduces to a modulus square only if Re(rho)=1/2 and is indefinite for off-line mirror pairs. Convergence/test conventions still have to be checked. This is an audit note, NOT an edit to Daniel's paper.

## 5. Celestial relevance and precise next construction

Kulp–Pasterski, *Multiparticle States for the Flat Hologram*, JHEP 08 (2025) 091, Section 3.3.1, https://arxiv.org/html/2501.00462, explicitly distinguish Poincare-quantized positive Hilbert norm and unitary Lorentz principal series from ordinary Euclidean OS reflection positivity. Therefore basic Mellin Plancherel or the label s=Delta cannot certify a particular reflected arithmetic Weil form.

Required next mathematical object: a test-space map J, a reflection Theta and a **completed** arithmetic quadratic form (prime + archimedean + pole) such that

    W_zeta(f,g)=<Jf, Theta Jg>

holds for actual source data, with positivity proved from independent arithmetic/physical input rather than from zeros, and a failure against the shifted F_theta control.

Important: The simple prime Hankel kernel constructed above is not this missing object. The no-go pinpoints where gamma/pole completion and nontrivial arithmetic correlations are essential.

## 6. Verification and Lean targets

Numerical audit script 'experiments/abel_prime_common_map/verify_prime_os_critical_obstruction.py': finite Gram=sum-of-squares checks; 65-digit agreement h(1/2)=C_infty/2; negative continued 2x2 diagonal; negative neutral-constant 2x2 determinant; negative pole-only-subtracted diagonal.

Lean targets: generic nonnegative weighted Gram PSD; generic pointwise PSD closure; zero-diagonal PSD row lemma; convergence/critical-wall lemma; completed-zeta log-derivative relation. The source's ArchimedeanFloor constant is already formalized, but **this bridge identity is not claimed Lean-proved**.

Do not promote any of this to ARP/RH. This is a precisely identified, unconditional obstruction to a tempting shortcut.


## 3b. Stronger no-go: completing the logarithmic derivative alone still fails

A tempting repair is to replace the bare prime h(s)=-zeta'/zeta(s) with the COMPLETED log derivative h_xi(s)=-xi'(s)/xi(s), so that the gamma and pole pieces enter. Define K_xi(t,u)=h_xi(1/2+t+u).

By xi(s)=xi(1-s), K_xi(0,0)=0 exactly. Since xi is nonconstant, h_xi is not identically zero in any neighborhood of 1/2; therefore K_xi(0,t)!=0 for arbitrarily small t>0. But ANY PSD kernel with K(0,0)=0 must have K(0,t)=0 for every t (2x2 determinant / Cauchy-Schwarz). Consequently **K_xi is not reflection positive**. Direct evaluation at t=.01 gives K_xi(0,.01)=-0.000462099787963... and the associated 2x2 determinant is approximately -2.1353621403564e-7.

This is a precise obstruction to the **naive completed logarithmic-derivative Hankel kernel**, not the true Weil quadratic form. Replacing zeta by xi under a logarithmic derivative is still not a way to construct the required completed arithmetic OS/GNS space. The actual Weil form tests convolution squares of the explicit-formula distribution, not the sum-of-positive-times logarithmic derivative.
