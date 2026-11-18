# 2026-11-18 — Arithmetic scale circles: logarithmic spectral density and an exact two-face no-ghost criterion

**Checked sources:** Connes–Consani, *Spectral triples and ζ-cycles*, Enseign. Math. 69 (2023), 93–148, Theorem 1.1 / 6.4 (https://ems.press/content/serial-article-files/44477); GPPDiscovery5 Round14D commit 7e89769; GPPVerify FiniteNoGhost and ArithmeticNoGhostInertia; earlier WWIF/Hopf D2 notes. RH remains OPEN. This is an exact carrier/obstruction, not a spectral identification of ξ.

## 1. Connes's literal circles and a correction to Round14D commentary

With u=log x let C_L=R/LZ, L=log μ. In L²(C_L), the rotation eigenfrequencies of D_L=−i∂_u are 2πk/L. Connes–Consani (2023) prove that the orthogonal complement of the periodized arithmetic map Σ_μ E(S_0^ev) contains frequencies corresponding precisely to **critical** ζ-zero ordinates, at circle lengths γL∈2πZ. This does **not** exclude other, off-line zeros.

CORRECTION to our earlier D2 Connes topology warning: the elementary multiplication-operator M_F on unweighted Fourier L²(R) has dense range when F≠0 almost everywhere; but the periodized constrained map on L²(C_L) is a different operator with a nontrivial orthogonal complement. In 2023 Connes–Consani explicitly replace the older Sobolev construction by the canonical L²(C_L). We must NOT claim every nontrivial Connes quotient requires weighted Sobolev topology. Only a *naked global multiplication quotient* is trivial in unweighted L².

## 2. Global fixed-circle counting no-go

For any standard first-order smooth elliptic Dirac-type operator on a fixed compact circle with a fixed finite-rank internal orientation bundle, the positive-eigenvalue count grows O(T) (for r copies of −i∂_u, r LT/(2π)+O(r)). But the number of nontrivial ζ zeros in the upper half-plane, with multiplicity, obeys the unconditional Riemann–von Mangoldt asymptotic

N_ζ(T)=T/(2π)(log(T/(2π))−1)+O(log T).

Hence a single fixed, ordinary local first-order Dirac circle with two/four orientation faces cannot have ALL zeta ordinates as its positive eigenvalues, even if RH holds. This does not constrain nonlocal/log-order operators, singular/running geometry, or the Connes–Consani family of circles.

The local effective circumference for counting is L_loc(T)~log(T/(2π)). The average inferred circumference is L_avg(T)=2πN_ζ(T)/T=log(T/(2π))−1+O(log T/T). A Haar logarithmic scale is therefore a natural required extension, not a finished construction.

## 3. Exact ultraviolet heat-trace fingerprint

Let K_ζ(τ)=Σ_{γ>0}m_γ exp(−τγ), counting *ordinates of every zero*, irrespective of horizontal location. Integration by parts gives K=τ∫exp(−τT)N_ζ(T)dT. Plugging RvM, using ∫xe^{−x}dx=1 and ∫xe^{−x}log x dx=1−γ_E, yields

K_ζ(τ)= [log(1/(2πτ))−γ_E]/(2πτ)+O(log(1/τ)), τ→0+.

This is **unconditional as a counting statistic**. It becomes a Hilbert heat trace of physical zeta modes only IF full spectral realization and RH have independently been established. By contrast an ordinary positive-frequency circle has K_C(τ)=1/(exp(2πτ/L)−1)=L/(2πτ)−1/2+O(τ). A faithful single-boundary generator needs the logarithmic enhancement.

## 4. Explicit selfadjoint, nonlocal UV carrier constructed without zeros

Let A(T)=T/(2π)(log(T/(2π))−1), increasing on T>2πe. For n≥1 define
lambda_n=A^{-1}(n)=2πn/W(n/e), with W Lambert's principal W function.
On L²(S¹), Fourier basis e_k, define D_log e_0=0 and D_log e_{±n}=±lambda_n e_{±n}, with domain Σ lambda_|k|² |c_k|²<∞. This is selfadjoint with compact resolvent, with EXACT positive count floor(A(T)) for T≥lambda_1. It reproduces the smooth RvM two-term count, lambda_n~2πn/log n, and the logarithmic heat-trace leading term. No zeta zeros are inputs. It is not the ζ spectrum: lambda_1≈22.5636817 versus ζ's first ordinate≈14.134725. This is a credible *nonlocal logarithmic kinematic carrier* but not RH, nor a conformally invariant local Dirac operator.

The more accurate arithmetic decomposition is N_ζ(T)=theta(T)/π+1+S(T), with Riemann–Siegel theta from Gamma and S(T)=arg ζ(1/2+iT)/π (standard branch/conventions, away from zeros). One can invert the increasing high-energy Gamma phase to define a background generator; the signed prime contribution must realize S(T) as a globally controlled relative spectral shift, not merely a positive ||ζ g||² norm. This is a research target, not established.

## 5. Exact two-face holonomy criterion

Hypothetical reflected zero pair at the same ordinate:
rho_+=1/2+δ+iγ and rho_-=1/2−δ+iγ, real δ≠0.
The log-scale characters e^{(±δ+iγ)u} acquire after one circle a monodromy
M=e^{iγL} diag(e^{δL},e^{−δL}).
For the indefinite J=[[0,1],[1,0]], M†JM=J EXACTLY for every δ,γ,L. This expresses conservation of the mixed, signed two-face pairing and shows why mirror-self-duality by itself tolerates ghosts. However M†M=diag(e^{2δL},e^{−2δL}) is not identity when δL≠0.

**No-ghost monodromy lemma (exact):** If there exists ANY positive definite Hermitian P with M†PM=P and L>0, then δ=0. Proof: M has eigenvector with eigenvalue λ=e^{δL+iγL}, and 0<v†Pv=v†M†PMv=|λ|²v†Pv forces |λ|=1, hence δ=0. Conversely δ=0 gives unitary phase M=e^{iγL}I. For a literally periodic section also γL∈2πZ.

This generalizes the earlier isolated Krein block into **circle holonomy**: opposite exponential growths can preserve a Krein form but cannot preserve a positive Hilbert norm. It is NOT an RH proof, because a zero-independent arithmetic construction carrying EVERY ξ-zero faithfully into positive-unitary monodromy is still missing. Declaring the off-line resonances absent from the positive Hilbert space would be circular.

## 6. Specific next step

Find from Tate/Poisson, the genuine prime Euler log derivative and the completed real/pole terms a global arithmetic connection or relative trace whose monodromy realizes every ξ-zero, including hypothetical off-line pairs, and prove a conserved positive metric from independently constructed boundary correlations. The shifted complete F_theta must violate the arithmetic hypothesis at a pinpointed step. Only then does the no-ghost monodromy lemma force δ=0 and RH.

JS independent numerical inversion of A: n=1, λ=22.563681698501348 (residual 4e−16); n=10 λ=54.312014448351945; n=100 λ=238.36665536251616; n=1000 λ=1421.1115236089381; n=100000 λ=74921.81145539443 (residual 1e−11). All other identities are exact algebra/calculus.


## 7. Further exact theorem: every zero ordinate lies within O(1) of the constructed log-Dirac carrier

Order all positive ordinates of nontrivial ξ-zeros, including multiplicity, as γ_1≤γ_2≤…, irrespective of whether RH holds. From RvM, N_ζ(T)=A(T)+O(log(T+2)); at an ordinate the multiplicity of its jump is O(log(T+2)), since N(T+1)−N(T−1)=O(log T). Therefore A(γ_n)=n+O(log γ_n). Meanwhile A(lambda_n)=n, with A'(T)=log(T/(2π))/(2π). Both γ_n and lambda_n are asymptotic to 2πn/log n; the mean-value theorem then gives

    γ_n−lambda_n = O(1) as n→∞ (UNCONDITIONAL).

This is a quantitative new-to-this-project kinematic observation, derivable from classical Riemann–von Mangoldt and not independent evidence for RH. The difference is not known to converge to zero and we do not claim it does. It says the entire **ordinate multiset** is a bounded spectral displacement of the zero-independent log-Dirac carrier.

A sharp falsifier to an inadequate Hilbert–Pólya claim follows: if one *inserts the actual ordinates as input*, the diagonal operator D_γ e_{±n}=±γ_n e_{±n} is selfadjoint and differs from D_log by a bounded diagonal operator, regardless of whether any zero is off the critical line. Its selfadjointness alone thus proves no RH! The genuinely missing claim is an independently defined arithmetic characteristic determinant/Weil trace whose FULL COMPLEX zeros equal {1/2+i eigenvalues}, and which forbids additional off-line resonances. Merely matching ordinates or the T log T counting law is insufficient.
