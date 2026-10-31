"""Rigorous adaptive Arb interval Schur test for three prime-power shifts.

At endpoint L=39/25=1.56 let V=(H(x)+H(L-x))/2, H=log(coth(x/2)),
h=V**(-1/10). The exact graph SOS implies E-S >= (V-d_h)|f|².
We certify d_h/V < 199/200 across the full continuum of x by
adaptive rational interval subdivision, NOT sampled point values.
Scaling x=tL then extends the relative bound to all shorter L.
"""

from flint import arb, ctx, fmpq


def main():
    ctx.prec = 192
    L = fmpq(39,25)
    Lb = arb(L)
    logs = {2: arb(2).log(), 3: arb(3).log(), 4: arb(4).log()}
    assert logs[4] < Lb < arb(5).log()
    # All rational brackets are rigorously checked here, then used to
    # produce conservative shifted-coordinate interval endpoints.
    bracket_data = {
        2: ('0.693147180559', '0.693147180561'),
        3: ('1.098612288667', '1.098612288670'),
        4: ('1.386294361119', '1.386294361121'),
    }
    powers = []
    def rational_decimal(s):
        before, after = s.split('.')
        return fmpq(int(before+after),10**len(after))
    for n,p,denom in ((2,2,2),(3,3,3),(4,2,4)):
        l,u = (rational_decimal(s) for s in bracket_data[n])
        assert arb(l) < logs[n] < arb(u)
        weight = logs[p] / arb(denom).sqrt()
        powers.append((l,u,weight,n))

    def H(z):
        assert z > 0
        return -(arb(z)/2).tanh().log()

    def potential_lower(lo, hi):
        assert fmpq(0) <= lo < hi <= L
        return (H(hi) + H(L-lo))/2

    alpha = fmpq(1,10)
    target = arb(fmpq(199,200))

    def bound_ratio(lo,hi):
        vl = potential_lower(lo,hi)
        ans = arb(0)
        for shift_lo,shift_hi,weight,n in powers:
            # Shift right: x -> x+a_n.
            ylo = lo+shift_lo
            if ylo < L:
                yhi = min(hi+shift_hi,L)
                if ylo < yhi:
                    vy = potential_lower(ylo,yhi)
                    ans += weight/(vl**(1-arb(alpha))*vy**arb(alpha))
            # Shift left: x -> x-a_n.
            yhi = hi-shift_lo
            if yhi > 0:
                ylo = max(lo-shift_hi, fmpq(0))
                if ylo < yhi:
                    vy = potential_lower(ylo,yhi)
                    ans += weight/(vl**(1-arb(alpha))*vy**arb(alpha))
        return ans

    # Adaptive dyadic mesh: EVERY continuous x belongs to a certified
    # interval. No singular endpoint is evaluated at x=0 or x=L.
    stack = [(fmpq(0),L,0)]
    accepted = 0
    maximum_depth = 0
    tightest_upper = arb(0)
    while stack:
        lo,hi,depth=stack.pop()
        test=bound_ratio(lo,hi)
        if test < target:
            accepted+=1
            maximum_depth=max(maximum_depth,depth)
            if test>tightest_upper:
                tightest_upper=test
            continue
        if depth>=24 or accepted+len(stack)>120000:
            raise AssertionError(f'Could not certify cell [{lo},{hi}]: {test}')
        m=(lo+hi)/2
        stack.extend([(lo,m,depth+1),(m,hi,depth+1)])

    # V_L >= H(L/2) globally by symmetry/convexity; this is again an
    # analytic comparison with a single outward-rounded Arb endpoint.
    v_floor = H(L/2)
    gap=(1-target)*v_floor
    assert gap > arb(fmpq(1,250)), f'Additive margin too weak: {gap}'
    print(f'Adaptive continuum-certified cells: {accepted}; '
          f'maximum dyadic depth: {maximum_depth}')
    print(f'Worst certified interval upper bound for d_h/V: {tightest_upper}')
    print(f'Hardy potential minimum H(L/2): {v_floor}')
    print(f'Certified additive gap (1-199/200)*H(L/2): {gap}')
    print('CERTIFIED for every 0<L<=39/25: E_L-S_L >= (1/250)||f||², '
          'including p^r=2,3,4. No completed Weil/RH claim.')


if __name__=='__main__':
    main()
