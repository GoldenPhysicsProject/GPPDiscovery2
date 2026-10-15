#!/usr/bin/env python3
"""Uniform primitive Dirichlet small-window Weil gap, explicit gamma parity.

At h<=1/25 the support prohibits EVERY prime-power translation. Compute
the certified analytic lower-bound formulas (floating diagnostics only).
The strict positive gap is established by elementary inequalities in
GPP-bridge 2026-10-15_uniform_small_window_all_dirichlet_weil_gap.md.

Golden Physics Project / Daniel Toupin; Codex 2026-10-15.
"""
import mpmath as mp
mp.mp.dps=70

def lower_bound(h, conductor, parity, trivial=False):
    r=mp.exp(-h)
    c0=mp.log(8*mp.pi)+mp.euler+mp.pi/2
    c1=c0-mp.pi
    t0=2*(mp.atanh(r)+mp.atan(r))
    t1=2*(mp.atanh(r)-mp.atan(r))
    if trivial:
        assert conductor==1 and parity==0
        return t0-c0-2*(mp.sinh(h)-h)
    return (t0-c0 if parity==0 else t1-c1)+mp.log(conductor)

def main():
    for hh in (mp.mpf(1)/32,mp.mpf(1)/25):
        print("h =", mp.nstr(hh,25))
        for cond,eps in [(1,0),(3,1),(4,1),(5,0),(7,1)]:
            value=lower_bound(hh,cond,eps,cond==1)
            print("  conductor",cond, "odd parity",eps,
                  "complete Q lower bound",mp.nstr(value,30))
            assert value>mp.mpf(".01")
        r=mp.exp(-hh)
        lhs=2*(mp.atanh(r)-mp.atan(r))-(mp.log(8*mp.pi)+mp.euler-mp.pi/2)
        rhs=2*(mp.atanh(r)+mp.atan(r))-(mp.log(8*mp.pi)+mp.euler+mp.pi/2)
        assert abs(lhs-rhs-(mp.pi-4*mp.atan(r)))<mp.mpf("1e-60")
    print("PASS: exact odd-even tail relation and numerical strict positivity; RH/GRH OPEN.")

if __name__=="__main__":
    main()
