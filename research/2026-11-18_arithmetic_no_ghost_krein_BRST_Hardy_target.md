# 2026-11-18 — Arithmetic no-ghost theorem: a strict Krein/BRST obstruction and the global Hardy target

**Source-based investigation.** Read ONON-5-2-1-3.tex §No-Ghost Theorem, arithmetic_principal_series_RH_program-34.tex §§completed Krein square / exact arithmetic no-ghost theorem, and the verified modules `FiniteNoGhost.lean`, `ArithmeticNoGhostInertia.lean`, `ArrowWeilHodgeClosure.lean`. Discovery5 Round14B already examines the same goal and labels No-Ghosts ⇔ RH as Weil's classical positivity criterion. This note supplies an exact elementary BRST commutation obstruction and an explicit spectral witness. No RH claim.

## The isolated off-critical spectral block

Suppose a zero exists at rho=1/2+δ+iγ with δγ≠0. Its reflected partner at the same ordinate is rho#=1/2−δ+iγ. As a **proposed**, not constructed, boundary energy define E(s)=−i(s−1/2), giving the conjugate nonreal energies γ−iδ and γ+iδ. On V=C² put

```
H=diag(γ−iδ,γ+iδ), J=[[0,1],[1,0]], [v,w]=v†Jw.
```

**Exact Lemma A.** H†J=JH. The form [v,v]=2Re(conj(v1)v2) has inertia (1,1); (1,±1)/√2 have norm ±1. H is Krein-self-adjoint but not self-adjoint in any positive metric because its eigenvalues are nonreal. Propagation exp(−itH) has factors exp(±δt); ghost and exponential instability are two aspects of the same nonreal pair.

**Exact Lemma B (simple-pair BRST obstruction).** If Q:V→V is complex-linear, Q²=0, and [Q,H]=0, then Q=0. Proof: since δ≠0, distinct eigenvalues force Q to be diagonal; a nilpotent diagonal matrix vanishes. Therefore H(Q)=V and its negative direction survives. This applies only to the isolated two simple modes with no auxiliary degeneracy; enlarging to an independently constructed cochain complex could evade it. A putative 'no ghost' proof may not simply postulate that all off-line zero modes are BRST exact while also claiming all zeros occur as physical eigenstates.

## Explicit two-time negative Hankel minor

Set z=rho−1/2=δ+iγ, α=−z²=A+iB, with A=γ²−δ², B=−2δγ. The pair contributes K(t_i,t_j)=2exp(−A(t_i+t_j))cos(B(t_i+t_j)). Factor K=2(uuᵀ−vvᵀ), u_i=e^(−At_i)cos(Bt_i), v_i=e^(−At_i)sin(Bt_i). Then

```
det K_{t1,t2}=−4 exp(−2A(t1+t2)) sin²(B(t2−t1)).
```

This is negative for suitable positive t1,t2 whenever δγ≠0. It is an exact ghost witness *for the isolated pair*. To make it a witness for the actual completed zeta heat kernel, one must isolate its contribution from infinitely many other zeros without assuming RH; zero-dependent spectral test polynomials prove necessity, not an arithmetic positive construction.

## Quantitative global Nyman–Burnol obstruction

On the disk coordinate w=(s−1)/s, a zero rho=σ+iγ with σ>1/2 maps to |w(rho)|<1. Let B be the Blaschke factor over right-half-plane zeros and K_B=H²(D)⊖B H²(D) the model-space obstruction to Nyman–Burnol completeness. Projection of the disk Hardy constant 1 satisfies

```
||P_K_B 1||²=1−|B(0)|².
```

The presence of any rho forces |B(0)|≤|w(rho)|, so

```
||P_K_B 1||²≥1−|w(rho)|²=(2σ−1)/(σ²+γ²)>0.
```

Thus off-line zeros force quantitatively positive *odd-cohomology leakage*. This is a positive-norm obstruction and should NOT be confused with the negative-norm Krein ghost; the missing arithmetic intertwiner must connect the two.

## Where the true no-ghost theorem must be proved

Find a **zero-independent** all-prime/Tate–Poisson/Gamma/pole boundary Hilbert or Krein complex with (i) actual completed signed Weil pairing, not an independently postulated Gram square; (ii) a closed global boundary differential, compatible with real structure and time evolution; (iii) faithful spectral completeness for *every* completed zeta zero, with multiplicity; (iv) proof that physical cohomology is positive (e.g., uniform odd coercivity or zero boundary leakage). The global no-ghost theorem would imply every E(ρ) is real, hence Re ρ=1/2. Every clause is necessary; (iv) or the faithful arithmetic intertwiner remains RH-strength and OPEN.

The `FiniteNoGhost` theorem assumes a positive-type kernel and only covers truncated charts. `ArrowWeilHodgeClosure` assumes exact block conditions at a width. ONON's K=T†T proof presently needs the missing equality K=actual signed completed Weil operator; Gram square positivity by itself cannot supply that equality. Its 'Δ=1+ix' parametrization also cannot be used to exclude off-line Δ without an independent spectral completeness argument.

The prime-local Koszul contracting homotopy is a bad route: a local inverse makes the cohomology trivial if it preserves the boundary domain, and the paper already proves it does not preserve the correct global Tate boundary. So the next target is the **global causal Archimedean/prime gluing energy identity** or Hardy model-space leakage estimate, not local ghost deletion.

**Control**: The shifted completed product Fθ(s)=ξ(s−θ)ξ(s+θ) has both involutions and nonreal proposed E-values. A successful arithmetic mechanism must fail a specific nontrivial global hypothesis for this control.

Symbolic proof of Lemma A, Lemma B and determinant and Cayley bound verified with SymPy in local companion `verify_no_ghost_krein_2026_11_18.py`. Independent Lean formalization of the commuting-nilpotent two-mode obstruction is a small self-contained next step; Lean toolchain unavailable in this session, so no compilation claim.
