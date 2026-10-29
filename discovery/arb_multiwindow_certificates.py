"""Arb/FLINT ball certificates for *finite* multiwindow quadratic forms.

Run with `python-flint` available, e.g. `PYTHONPATH=arb_vendor python3
discovery_research/arb_multiwindow_certificates.py`. Each inequality below
uses enclosures from FLINT Arb at 160-bit precision. No result here proves
continuum Weil positivity or identifies the true completed prime kernel.

The value of the test is distinguishing three properties:
  (a) all two-window principal blocks PSD;
  (b) full finite matrix PSD;
  (c) Gershgorin/||T||<=1 sufficient certificates.
These are distinct, even with exponential off-diagonal decay.
"""

from flint import arb, ctx, fmpq

ctx.prec = 160


def qrat(p, q=1):
    """An outward Arb enclosure of the exact rational p/q."""
    return arb(fmpq(p, q))


def quadratic(M, x):
    assert len(M) == len(x)
    return sum((x[i] * M[i][j] * x[j]
                for i in range(len(x)) for j in range(len(x))), arb(0))


def certify_positive_definite(M):
    """Arb LDL elimination with strictly positive lower pivot certificates.

    For symmetric real matrices, positive leading Schur pivots prove PD.
    If a pivot interval touches zero, the routine refuses to decide.
    """
    n = len(M)
    A = [[M[i][j] for j in range(n)] for i in range(n)]
    pivots = []
    for k in range(n):
        d = A[k][k]
        if not d > 0:
            raise AssertionError(f"pivot {k} not certified positive: {d}")
        pivots.append(str(d))
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i][j] -= A[i][k] * A[k][j] / d
    return pivots


def matrix_from_exponential_decay(n, alpha):
    q = (-alpha).exp()
    return [[q ** abs(i-j) for j in range(n)] for i in range(n)]


def main():
    # Original rigorous pairwise-vs-global counterexample.
    r = qrat(3,5)
    M = [[arb(1) if i == j else -r for j in range(3)] for i in range(3)]
    assert arb(1) - r*r > 0  # all principal 2x2 determinants positive
    witness = quadratic(M, [arb(1)]*3)
    assert witness < 0
    print("CERTIFIED negative 3-window all-ones direction:", witness)

    # NotebookLM's frustrated triangle, also strict pairwise PSD yet indefinite.
    r = qrat(7,10)
    M = [[arb(1), r, r], [r, arb(1), -r], [r, -r, arb(1)]]
    assert arb(1) - r*r > 0
    w = quadratic(M, [arb(1), arb(-1), arb(-1)])
    assert w < 0
    print("CERTIFIED negative frustrated-triangle direction:", w)

    # The 5-window exponential kernel is rigorously PD by positive LDL pivots.
    # Nevertheless the normalized T=M-I violates *both* strong sufficient
    # criteria. Here the constant vector Rayleigh bound certifies ||T||>1.
    E = matrix_from_exponential_decay(5, qrat(4,5))
    pivots = certify_positive_definite(E)
    T = [[E[i][j] if i != j else arb(0) for j in range(5)] for i in range(5)]
    row2 = sum((abs(z) for z in T[2]), arb(0))
    rayleigh = quadratic(T, [arb(1)]*5) / 5
    assert row2 > 1
    assert rayleigh > 1  # ||T|| >= this positive Rayleigh quotient
    print("CERTIFIED 5-window decay PD; LDL pivots:", pivots)
    print("CERTIFIED Gershgorin row sum >1:", row2)
    print("CERTIFIED ||T||>1 from Rayleigh quotient:", rayleigh)

    # A genuinely row-dominant 3-window matrix is certified PD.
    p = qrat(1,5)
    P = [[arb(1) if i == j else -p for j in range(3)] for i in range(3)]
    assert 2*p < 1
    print("CERTIFIED row-dominant 3-window PD; LDL pivots:",
          certify_positive_definite(P))

    # Sharp prime threshold blocks are semidefinite, with exact nulls.
    # An added arbitrary temporal cross contact breaks positivity even when
    # both local squares are zero. The constants here are toy coefficients.
    eps = qrat(1,100)
    prime_one = (arb(2) - 2)**2 / 4
    prime_two = qrat(2,9) * (arb(-3) - 3*arb(-1))**2
    cross = prime_one + prime_two + 2*eps*arb(1)*arb(-1)
    assert prime_one == 0 and prime_two == 0 and cross < 0
    print("CERTIFIED null-sector negative cross witness:", cross)
    print("Scope: finite Arb certificates only; global arithmetic positivity OPEN")


if __name__ == "__main__":
    main()
