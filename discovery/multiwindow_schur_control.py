"""Exact multi-window counterexample and sufficient aggregate bounds.

Purpose: falsify the assertion that uniform pairwise Cauchy-Schwarz bounds
with some epsilon>0 guarantee positivity of an arbitrary sum of windows.

For n windows let Q_r have diagonal 1 and all off-diagonals -r:
    Q_r(x) = (1+r)*sum(x_i^2) - r*(sum(x_i))^2.
Every two-window restriction is positive for 0<=r<=1, with pairwise
|Q_ij|^2 = r^2 Q_ii Q_jj. Yet the all-ones vector gives
    Q_r(1,...,1) = n*(1-r*(n-1)),
which is negative once n>1+1/r. Full PSD requires r<=1/(n-1).

A whole-matrix row-sum bound is sufficient, unlike pairwise control.
This is a model falsifier, not a calculation of the actual Weil form.
"""

from fractions import Fraction as F


def form(r, x):
    return (1+r)*sum(t*t for t in x) - r*(sum(x))**2


def check():
    for r in (F(3,5), F(1,10), F(1,100)):
        assert F(0) < r < F(1)
        epsilon = 1-r*r
        assert F(0) < epsilon < 1
        assert r*r == (1-epsilon)
        # Exact PSD of every 2x2 principal restriction via square-completion:
        # a^2+b^2-2rab=(a-rb)^2+(1-r^2)b^2 >= 0.
        for a in range(-4,5):
            for b in range(-4,5):
                assert form(r, (F(a),F(b))) == (F(a)-r*F(b))**2+(1-r*r)*F(b*b)
                assert form(r, (F(a),F(b))) >= 0
        threshold_n = int(1/r)+2
        x = [F(1)]*threshold_n
        assert form(r, x) == threshold_n*(1-r*(threshold_n-1))
        assert form(r, x) < 0

    # The smallest three-window counterexample at r=3/5.
    r=F(3,5)
    assert form(r, (F(1),F(1),F(1))) == F(-3,5)
    assert form(r, (F(1),F(0),F(0))) == 1
    assert form(r, (F(1),F(1),F(0))) == F(4,5)
    # Exact all-window criterion for equicoupled form: eigenspaces have
    # eigenvalues 1+r (sum-zero), and 1-r*(n-1) (all-ones).
    for n in range(2,9):
        for r in (F(1,10), F(1,n-1), F(2,n-1)):
            if r>1:
                continue
            expected_psd = 1-r*(n-1)>=0
            if expected_psd:
                # decomposition: x=m*1+z with sum(z)=0
                for seed in range(-4,5):
                    x=[F((i*seed+i*i)%7-3) for i in range(n)]
                    mean=sum(x)/n
                    z=[xi-mean for xi in x]
                    assert sum(z)==0
                    decomposition=(1+r)*sum(zi*zi for zi in z)+n*(1-r*(n-1))*mean*mean
                    assert form(r,x)==decomposition
                    assert decomposition>=0
            else:
                assert form(r, [F(1)]*n)<0

    print("PASS: all two-window restrictions PSD with strict pairwise epsilon")
    print("PASS: three windows can be indefinite: r=3/5, Q(1,1,1)=-3/5")
    print("PASS: arbitrary small pairwise coupling fails at sufficiently many windows")
    print("PASS: aggregate condition r*(n-1)<=1 is sharp for this model")


if __name__ == "__main__":
    check()
