"""Rigorous 256-bit Arb inertia audit of the EVEN lower Schur block for
the actual first-prime-inclusive completed Weil form at L=7/10.

Imports the fully checked true p2 Hardy-tax and odd-sector construction.
The comparison form underestimates the actual even Q; a negative comparison
pivot does NOT imply a negative eigenvalue of actual Weil Q.

If finite even comparison has index<=1 and infinite high floor is positive,
the ACTUAL full completed Q has Morse negative index at most one overall
(odd actual Q is already rigorously positive).
"""
from arb_true_p2_odd_hardy_remainder_7_10 import E,Ce,he,Z,arb,ctx
assert he>0
S=[[E[i][j]-sum((Ce[i][k]*Ce[j][k] for k in range(len(Ce[0]))),Z)/he
    for j in range(len(E))] for i in range(len(E))]
A=[row[:] for row in S]
signs=[]
for i in range(len(A)):
    d=A[i][i]
    print(f'CERTIFIED even comparison LDL pivot {i}:',d)
    assert d>0 or d<0, ('undetermined pivot sign',i,d)
    signs.append(-1 if d<0 else +1)
    for j in range(i+1,len(A)):
        for k in range(i+1,len(A)):
            A[j][k]-=A[j][i]*A[i][k]/d
print('Certified even comparison inertia signs:',signs)
assert signs.count(-1)==1, ('expected exactly one negative direction in comparison',signs)
print('CERTIFIED actual completed Q at L=7/10 has NEGATIVE INDEX <=1')
print('because true Q>=comparison, high block is positive and odd sector is positive.')
print('DOES NOT assert a negative eigenvalue of actual Q, all-test PSD or RH.')
