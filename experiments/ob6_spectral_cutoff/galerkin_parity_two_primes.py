"""Source-only parity/Krein pilot at widths .72, 1.05, 1.15 with genuine prime powers.
FLOAT64 diagnostic, NOT a rigorous positivity certificate or RH proof.
"""
import math
import numpy as np
from scipy.linalg import eigh
import galerkin_two_pole_source as model

PRIMES_CUTOFF=[2,3,5,7,11]

def trial(L,M,drop_prime3=False):
    model.L=L
    model.U=math.exp(-L/2)
    model.ARCH_TAIL=2*(math.atanh(model.U)+math.atan(model.U))
    B,ignored,W0,E=model.build(M,True)
    cs=np.array([model.pole_moment(i+1,'c') for i in range(M)])
    ss=np.array([model.pole_moment(i+1,'s') for i in range(M)])
    events=[]
    for p in PRIMES_CUTOFF:
        if math.log(p)>=L:continue
        q=p
        while math.log(q)<L:
            events.append((q,math.log(p),math.log(q),math.log(p)/math.sqrt(q)))
            q*=p
    V=model.THETA*np.eye(M)
    for q,lp,lag,weight in events:
        if drop_prime3 and q==3:continue
        K=np.zeros((M,M))
        for i in range(M):
            for j in range(i,M):
                K[i,j]=K[j,i]=model.sym_shift(i+1,j+1,lag)
        V+=2*weight*K
    W=B-V
    H=W-2*np.outer(cs,cs)+2*np.outer(ss,ss)
    output={'L':L,'M':M,'events':[int(x[0]) for x in events if not(drop_prime3 and x[0]==3)],
            'drop_prime3':drop_prime3}
    for parity in [0,1]:
        idx=np.arange(parity,M,2)
        w=W[np.ix_(idx,idx)];h=H[np.ix_(idx,idx)]
        b=B[np.ix_(idx,idx)];v=V[np.ix_(idx,idx)]
        eigs=np.linalg.eigvalsh(h)
        label='even' if parity==0 else 'odd'
        data={'unhealed_eigs':eigs[:4].tolist(),'negative_index_in_truncation':int((eigs<0).sum()),
              'full_Weil_Ritz_bottom':float(np.linalg.eigvalsh(w)[0]),
              'normalized_prime_top':float(eigh(v,b,eigvals_only=True)[-1])}
        if parity==0:
            c=cs[idx]; y=np.linalg.solve(h,c)
            q=float(c@y);d=float(2*y@y)
            data.update(krein_q=q,krein_scalar_margin=float(-1-2*q),
                        secular_derivative_zero=d,
                        predicted_soft_eigenvalue=float(-(1+2*q)/d),
                        actual_soft_eigenvalue=float(np.linalg.eigvalsh(w)[0]))
        else:
            s=ss[idx]; data['odd_pole_loading']=float(2*s@np.linalg.solve(h,s))
        output[label]=data
    return output

if __name__=='__main__':
    for L in [.72,1.05,1.15]:
        for M in [24,48]:
            print(trial(L,M))
    print('PRIME-3-REMOVAL CONTROL',trial(1.15,48,True))
    print('Interpretation: L=.72 full positivity is ALREADY PROVED in Verify/WindowBL036.lean.')
    print('L=1.15 and all source scalar/index checks here are FLOATING diagnostics, not certified.')
