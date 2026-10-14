#!/usr/bin/env python3
"""Unconditional short-window Weil positivity bound.

Analytic proof in bridge work/codex/2026-10-14_unconditional_small_mellin_window_weil_gap.md.
The decimal diagnostics here do NOT replace the inequalities in the proof.
Works for all real nonzero smooth compact supported g on [-h,h],
not just for the sharp test used by earlier scripts.
"""
import mpmath as mp
mp.mp.dps=70
Cstar=mp.log(8*mp.pi)+mp.euler+mp.pi/2

def tail(h):
    a=mp.exp(-h)
    return 2*(mp.atanh(a)+mp.atan(a))

def B(h):
    return tail(h)-Cstar-2*(mp.sinh(h)-h)

def elementary_lower(h):
    return mp.log((2-h)/(8*mp.pi*h))-mp.euler-mp.pi*h/2-2*(mp.sinh(h)-h)

for denom in [100,32,25]:
    h=mp.mpf(1)/denom
    print("h=1/%d; B(h)=%s; elementary lower=%s" %
          (denom,mp.nstr(B(h),30),mp.nstr(elementary_lower(h),30)))

assert B(mp.mpf(1)/32)>mp.mpf("0.3263")
assert B(mp.mpf(1)/25)>mp.mpf("0.0707")
assert elementary_lower(mp.mpf(1)/32)>mp.mpf("0.27")
assert elementary_lower(mp.mpf(1)/25)>mp.mpf("0.01")
# Rational-bounded numerical inequalities used for the paper proof:
assert mp.pi<mp.mpf(22)/7
assert mp.euler<mp.mpf("0.58")
assert mp.log(mp.mpf(5)/2)>mp.mpf("0.9")
assert mp.log(mp.mpf(343)/176)>mp.mpf("0.66")
assert 2*(mp.sinh(mp.mpf(1)/25)-mp.mpf(1)/25)<mp.mpf("0.00005")
print("All checks pass; the rigorous sign argument is the displayed analytic inequality chain.")
