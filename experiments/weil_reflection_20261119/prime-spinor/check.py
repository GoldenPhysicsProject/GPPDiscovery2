"""Compare the equal-weight beat with the completed Weil form without zero data."""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'positivity'))
from translates import gram_column, models
from translated_bounds import enclose

L=3
j=20
d=np.log(7)
def overlap(t):
    x=np.abs(t)
    k=j*np.pi/L
    return np.where(x<L,(1-x/L)*np.cos(k*x)+np.sin(k*x)/(k*L),0.)

# f=(g+T_d g)/sqrt(2), preserving the sector amplitudes without
# renormalizing the coherently combined scalar test function.
def corr(t):
    return overlap(t)+(overlap(t+d)+overlap(t-d))/2

for name,model in [('zeta',models.zeta()),('FTH',models.fth(.2))]:
    w=sum(gram_column(model,L,np.array([j]),v,32)[0] for v in (0.,d))
    bound=enclose(name,j,7,1,unit_shift=True)/2
    print(name,'W',w,'interval',bound)
    for cutoff in (141,1000,5000):
        use=model['n']<=cutoff
        n=model['n'][use]
        weights=model['c'][use]/np.sqrt(n)
        cross=-2*np.dot(weights,corr(np.log(n)))
        diagonal=2*corr(0)*weights.sum()
        beat=2*np.dot(weights,corr(0)-corr(np.log(n)))
        assert np.isclose(beat-diagonal,cross)
        print(cutoff, 'beat, diagonal, prime cross term',beat,diagonal,cross)
    assert (bound.a>0 if name=='zeta' else bound.b<0)

# The finite residue test at (2,1), coefficients from the exact kernel.
terms=[(1,1,1),(-2,2,1),(1,2,2),(-2,2,4),(-1,1,1),
       (1,4,1),(2,4,2),(-2,8,1),(-1,8,2),(2,4,1)]
a=sum(c*f*g**5 for c,f,g in terms)%5
b=(a-4)%5
assert (a,b)==(0,1)
omega=np.exp(2j*np.pi/5)
for v in (a,b):
    print('residue, antisymmetric probability',v,abs((omega**v-omega**(-v))/2)**2)
