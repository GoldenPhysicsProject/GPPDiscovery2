#!/usr/bin/env python3
"""Check the completed Suzuki conditional mean normalization.

Not a test of RH. The critical-line zeros below form a finite illustrative
partial sum, and do not certify the absence of off-line zeros.
"""
from __future__ import annotations
import mpmath as mp

def run(zeros: int = 20) -> None:
    mp.mp.dps = 65
    s = mp.mpf("0.5")
    z = mp.zeta(s)
    zp = mp.diff(mp.zeta, s)
    zpp = mp.diff(mp.zeta, s, 2)
    c_gamma = -8 + mp.polygamma(1, mp.mpf("0.25")) / 4 + zpp / z - (zp / z)**2
    xi = lambda x: mp.mpf("0.5")*x*(x-1)*mp.power(mp.pi, -x/2)*mp.gamma(x/2)*mp.zeta(x)
    c_xi = mp.diff(xi, s, 2) / xi(s)
    assert abs(c_xi - c_gamma) < mp.mpf("1e-54")
    print("xi''/xi(1/2) =", mp.nstr(c_xi, 55))
    print("gamma/zeta decomposition =", mp.nstr(c_gamma, 55))
    partial = sum((2 / mp.im(mp.zetazero(k))**2 for k in range(1,zeros+1)), mp.mpf(0))
    print(f"First {zeros} critical-line zero-pair partial sum =",mp.nstr(partial,40))
    print("Remaining difference (not a zero-free error certificate) =",mp.nstr(c_xi-partial,40))
    print("PASS: two independent normalization formulas agree")

if __name__ == "__main__":
    import sys
    run(int(sys.argv[1]) if len(sys.argv)>1 else 20)
