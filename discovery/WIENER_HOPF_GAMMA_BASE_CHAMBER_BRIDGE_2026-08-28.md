# Wiener--Hopf / normalized Gamma base-chamber bridge

Codex/GPT continuation, 2026-08-28. No Claude material consulted.

Two formal threads that had been developed independently coincide exactly.

The continuously extended Wiener--Hopf weight is

\[
W_{\rm ext}(x)=
\begin{cases}
1,&x=0,\\[2mm]
\dfrac{\pi x}{\sinh(\pi x)},&x\ne0,
\end{cases}
\]

while the base normalized Gamma/Mehler--Fock chamber is

\[
\rho_\Gamma(0,x)=
\begin{cases}
\dfrac{2}{\pi},&x=0,\\[2mm]
\dfrac{2x}{\sinh(\pi x)},&x\ne0.
\end{cases}
\]

Therefore the equality is global, including the removable point:

\[
\boxed{W_{\rm ext}(x)=\frac{\pi}{2}\,\Re\rho_\Gamma(0,x)}.
\]

Equivalently,

\[
\boxed{\Re\rho_\Gamma(0,x)=\frac{2}{\pi}W_{\rm ext}(x)}.
\]

This identifies the Wiener--Hopf positive weight with the base member of the all-order normalized Gamma chamber family, up to the fixed normalization `pi/2`. It therefore gives a direct normalization bridge between the celestial Wiener--Hopf convolution thread and the Gamma/Mehler--Fock chamber recurrence thread.

Promoted to Lean in `GppVerify/CelestialHolography/WienerHopfGammaBridge.lean`, Verify2 commit `4043577745a516b389f06174ad9ace0230a2f5fa`.

No Fourier-transform factorization, outer-function theorem, or RH claim is used here.
