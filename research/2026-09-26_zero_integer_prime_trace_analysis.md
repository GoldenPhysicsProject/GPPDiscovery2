# Zero/integer ratio and prime reconstruction from the zero spectrum

Date: 2026-09-26  
Status: mathematical/data audit using the project datasets \`zeros-2000k.txt\` (2,001,052 ordinates) and \`zeros-100k-hd.txt\` (100,000 high-precision indexed ordinates). No external literature search was used for this derivation.

## 1. The raw ratio of zero count to integers is not constant

For zero ordinates \(0<\gamma\le T\), the smooth Riemann--von Mangoldt count is

\[
\bar N(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}
+\frac78.
\]

Therefore

\[
\frac{N(T)}{T}
\sim
\frac1{2\pi}
\left(\log\frac{T}{2\pi}-1\right),
\]

whereas the number of positive integers up to \(T\) is \(T\). The ratio thus grows logarithmically.

The project data give:

\[
\begin{array}{c|c|c}
T & N(T) & N(T)/T\\ \hline
100 & 29 & 0.29\\
1000 & 649 & 0.649\\
10000 & 10142 & 1.0142\\
100000 & 138069 & 1.38069\\
10^6 & 1747146 & 1.747146
\end{array}
\]

The first observed crossing \(N(T)>T\) occurs at zero number \(9137\):
\[
\gamma_{9137}=9136.679196436\ldots .
\]

The leading asymptotic predicts the crossing near
\[
2\pi e^{2\pi+1}=9145.91\ldots .
\]

At the top of the 2M data,
\[
T=1132490.658714411,\qquad N=2001052,
\]
so
\[
N/T=1.7669479078\ldots .
\]

## 2. The natural comparison with integers is after Archimedean unfolding

Define the smooth spectral coordinate
\[
u(T)=
\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}
+\frac78.
\]

At a zero, use the half-counted staircase. Across all 2,001,052 zeros the quantity
\[
\delta_n=(n-\tfrac12)-u(\gamma_n)
\]
has

\[
\text{mean}=8.1\times10^{-8},
\qquad
\text{std}=0.33216,
\]
with observed range approximately
\[
-1.3325\le\delta_n\le1.2994.
\]

Thus the zeros become a nearly unit-density sequence under the Archimedean unfolding:
\[
\boxed{u(\gamma_n)\approx n-\tfrac12.}
\]

The average unfolded nearest-neighbor spacing is
\[
0.99999996.
\]

This is the precise sense in which there is approximately one zero per integer spectral cell: **not in raw \(T\), but after the Gamma/Archimedean Weyl normalization.**

Ignoring the fluctuation gives the explicit Lambert-\(W\) approximation
\[
\boxed{
\gamma_n^{(0)}
=
2\pi\,
\frac{n-\frac{11}{8}}
{W\!\left((n-\frac{11}{8})/e\right)}.
}
\]

Across the 2M sample its median absolute error is about \(0.130\) in raw height, or \(0.230\) local mean spacings.

## 3. Why \(2\pi\) appears in the zero density

Write the Riemann--Siegel Archimedean phase as
\[
\theta(T)
=
\operatorname{Im}\log\Gamma\!\left(\frac14+\frac{iT}{2}\right)
-\frac{T}{2}\log\pi .
\]

The zero count decomposes schematically as
\[
N(T)=1+\frac{\theta(T)}{\pi}+S(T),
\]
where \(S(T)\) contains the finite-prime fluctuation.

Stirling gives
\[
\theta(T)
=
\frac{T}{2}\log\frac{T}{2\pi}
-\frac{T}{2}
-\frac{\pi}{8}
+O(T^{-1}),
\]
hence
\[
\bar d(T)=\bar N'(T)
=
\boxed{
\frac1{2\pi}\log\frac{T}{2\pi}
}
+O(T^{-2}).
\]

Thus the smooth density of zeros is controlled by the **Archimedean completed-zeta factor**. This is the same \(2\pi\) normalization already appearing in the real-place Fourier/modular/horizon analysis.

At \(T=10^6\), the project dataset contains \(1,747,146\) zeros, while the smooth formula gives
\[
1,747,145.5086\ldots .
\]

## 4. Integers in the prime Fock space are not zero eigenvalues

The arithmetic bosonic Hamiltonian is
\[
H_{\rm arith}
=
\sum_p(\log p)N_p.
\]

A Fock state
\[
n=\prod_p p^{N_p}
\]
has energy
\[
E_n=\log n.
\]

Hence the number of raw Fock states below energy \(E\) is
\[
\#\{n:\log n\le E\}
=
\lfloor e^E\rfloor.
\]

This exponential density is completely different from
\[
N_{\rm zeros}(T)\sim\frac{T\log T}{2\pi}.
\]

Therefore
\[
\boxed{
\gamma_n\neq\log n
}
\]
and the Riemann zeros cannot be the raw eigenvalues of the free prime-number Hamiltonian.

The correct relation is trace-formula/Fourier duality.

## 5. Prime powers are the Fourier lengths conjugate to zero ordinates

On the critical half-density line,
\[
n^{-1/2-iT}
=
n^{-1/2}e^{-iT\log n}.
\]

Thus \(T\) is Fourier-conjugate to the logarithmic multiplicative coordinate
\[
y=\log n.
\]

Formally/smoothed, the oscillating part of the zero density is

\[
\boxed{
d_{\rm osc}(T)
=
-\frac1\pi
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\cos(T\log n).
}
\]

Since \(\Lambda(n)\) vanishes except at prime powers, the Fourier spectrum of the zero-density fluctuation must live at
\[
\boxed{y=\log p^m.}
\]

This gives the exact local/global dictionary:

\[
\boxed{
\text{prime powers }p^m
\leftrightarrow
\text{logarithmic orbit lengths }m\log p,
}
\]

\[
\boxed{
\text{zeta zeros}
\leftrightarrow
\text{global spectral frequencies }T.
}
\]

## 6. Direct reconstruction of the primes from the 2M zero file

We histogrammed the 2,001,052 zero ordinates, subtracted the smooth Archimedean density, applied a Hann window, and Fourier transformed the residual **without supplying the prime positions**.

The strongest Fourier maxima occur at

\[
\begin{array}{c|c}
u_{\rm peak} & e^{u_{\rm peak}}\\ \hline
1.945911605 & 7.000010\\
2.397894118 & 10.999987\\
2.564947779 & 12.999979\\
2.944438657 & 18.999994\\
3.135493451 & 22.999982\\
1.609435241 & 4.999987\\
2.833215651 & 17.000039\\
3.433987439 & 31.000007\\
3.610916739 & 36.999957\\
3.367293581 & 28.999935\\
1.098614997 & 3.000008\\
0.693147857 & 2.000001
\end{array}
\]

i.e. the logarithms of
\[
7,11,13,19,23,5,17,31,37,29,3,2,\ldots .
\]

The next strong repetition peaks include
\[
e^{2.197224446}=8.999999\approx3^2,
\qquad
e^{1.386295714}=4.000005\approx2^2.
\]

Among the 100 strongest local maxima between \(u=0.65\) and \(u=8\), all 100 land within \(0.6\) Fourier bins of a prime power; 97 are primitive primes and 3 are prime squares.

So the stored zero spectrum numerically reconstructs the prime spectrum under logarithmic Fourier transform.

## 7. The amplitudes reconstruct the von Mangoldt half-density current

The frequency locations are only half the result. The predicted trace weight is
\[
\boxed{
J(n)=\frac{\Lambda(n)}{\sqrt n}.
}
\]

Using the high-precision 100k zero file, a Hann-windowed direct transform at the exact frequencies \(u=\log n\) gives the expected finite-window amplitude

\[
A_n^{\rm pred}
=
\frac{T_{\max}}{4\pi}
\frac{\Lambda(n)}{\sqrt n}.
\]

Examples:

\[
\begin{array}{c|c|c|c}
n & A_{\rm observed} & A_{\rm pred} & A_{\rm obs}/A_{\rm pred}\\ \hline
2 & 2923.83 & 2922.15 & 1.00057\\
3 & 3765.63 & 3781.61 & 0.99578\\
4 & 2074.77 & 2066.28 & 1.00411\\
5 & 4253.84 & 4291.23 & 0.99129\\
7 & 4356.40 & 4384.97 & 0.99349\\
8 & 1454.63 & 1461.08 & 0.99559\\
9 & 2191.97 & 2183.31 & 1.00397\\
25 & 1919.40 & 1919.10 & 1.00016
\end{array}
\]

The transform phase is approximately \(\pi\), agreeing with the negative sign in the oscillatory trace contribution.

This is a direct numerical audit, from the project's own zero data, of the same weight
\[
\boxed{\Lambda(n)n^{-1/2}}
\]
that already appears in the AFT causal boundary anomaly and in the von-Mangoldt halo calculation.

## 8. One master arithmetic current

Define a positive half-density current on logarithmic scale,

\[
\boxed{
d\mu_{\rm arith}(y)
=
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\delta(y-\log n)\,dy.
}
\]

Then three previously separate project constructions are transforms of the same object.

### Zero-spectrum trace transform
\[
d_{\rm osc}(T)
=
-\frac1\pi
\int\cos(Ty)\,d\mu_{\rm arith}(y).
\]

### AFT causal heat transform
\[
\mathcal A(\tau)
=
\frac1{\sqrt{4\pi\tau}}
\int e^{-y^2/(4\tau)}\,d\mu_{\rm arith}(y).
\]

### Static halo transform
Since \(n=e^y\),
\[
\mathcal D(x)
=
\int
F(2xe^{-y/2})\,d\mu_{\rm arith}(y),
\qquad
F(z)=1-(1+z)e^{-z}.
\]

The already-derived PNT asymptotic
\[
\mathcal D(x)\sim4x
\]
therefore belongs to the **same arithmetic current** whose Fourier trace reconstructs the Riemann zeros.

This is the strongest mathematical unification found in this audit.

## 9. The current is an energy-weighted critical TFD amplitude

For \(n=p^m\),
\[
\frac{\Lambda(n)}{\sqrt n}
=
(\log p)p^{-m/2}.
\]

With prime modular energy
\[
E_p=\log p,
\]
this is
\[
\boxed{
J_{p,m}
=
E_p e^{-mE_p/2}.
}
\]

But the critical Haar probability is
\[
P_p(m)=(1-e^{-E_p})e^{-mE_p},
\]
whose TFD/half-density amplitude is proportional to
\[
e^{-mE_p/2}.
\]

Hence the von-Mangoldt half-density current is exactly
\[
\boxed{
\text{modular energy}\times\text{critical TFD amplitude}.
}
\]

Moreover
\[
p^{-m(1/2+iT)}
=
e^{-mE_p/2}
e^{-iTmE_p}.
\]

Thus
\[
\boxed{
s=\frac12+iT
}
\]
is precisely the critical Haar **square-root Gibbs amplitude** plus real modular evolution.

This supplies a direct physical/mathematical meaning for the half-density line without claiming that it alone proves RH.

## 10. Level repulsion: zeros behave as a collective unitary spectrum

Using the smooth local density to unfold the 2M zeros gives mean nearest-neighbor spacing \(1\).

For small spacing \(s\), a fit of the empirical CDF gives
\[
P(S\le s)\propto s^{2.936},
\]
so the corresponding density behaves approximately as
\[
p(s)\propto s^{1.936},
\]
very close to quadratic repulsion.

A simple GUE Wigner-surmise comparison gives a Kolmogorov distance about
\[
D_{\rm GUE}\approx0.0125,
\]
whereas an exponential/Poisson spacing law gives
\[
D_{\rm Poisson}\approx0.292.
\]

For example,
\[
P(S<0.2)_{\rm data}=0.00715,
\]
versus
\[
0.00839
\]
for the GUE surmise and
\[
0.18127
\]
for independent Poisson levels.

This strongly supports the interpretation of the zeros as a correlated collective spectrum rather than independent prime modes.

## 11. Consequence for the GPP operator program

The data and exact transforms force the following separation:

\[
\boxed{
\text{primes}=\text{local/primitive arithmetic channels},
}
\]

\[
\boxed{
\text{integers}=\text{occupation configurations of those channels},
}
\]

\[
\boxed{
\text{prime powers}=\text{repetitions/logarithmic trace lengths},
}
\]

\[
\boxed{
\text{Riemann zeros}=\text{global spectral/resonant data after Archimedean sewing}.
}
\]

The raw free Hamiltonian \(H_{\rm arith}|n\rangle=(\log n)|n\rangle\) is therefore not the Hilbert--Pólya operator. The desired global operator must be a nontrivial scattering/transfer/OS reconstruction whose trace formula has the prime-power current on one side and the zero spectrum on the other.

The immediate theorem target is to derive both
\[
d\mu_{\rm arith}(y)
\]
and the Archimedean phase \(\theta(T)\) from a single adelic modular standard form, then prove that the completed no-ghost quotient makes all global resonances real.
