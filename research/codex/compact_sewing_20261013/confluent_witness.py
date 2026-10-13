import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
from confluent_control import mp,m
mp.mp.dps=100
rows=[]
for theta,n in [(mp.mpf(1)/4,4),(mp.mpf(1)/10,5)]:
    # Independent real-axis numerical differentiation (no contour sampling).
    a=mp.taylor(lambda x:m(x,theta),mp.mpf(1),2*n-1)
    astar=mp.taylor(lambda x:m(x),mp.mpf(1),2*n-1)
    C=mp.matrix(n); Cs=mp.matrix(n)
    for i in range(n):
        for j in range(n):
            C[i,j]=(-1)**(i+j+1)*a[i+j+1]*16**(i+j)
            Cs[i,j]=(-1)**(i+j+1)*astar[i+j+1]*16**(i+j)
    ev,vec=mp.eigsy(C)
    v=vec[:,0]; v/=max(abs(x) for x in v)
    nums=[int(mp.nint(x*10**12)) for x in v]; q=mp.matrix([mp.mpf(x)/10**12 for x in nums])
    row={'theta':str(theta),'dimension':n,'scaled_matrix_min_eigenvalue':mp.nstr(ev[0],50),'witness_numerators':nums,'denominator':10**12,'theta_form':mp.nstr((q.T*C*q)[0],50),'zeta_form':mp.nstr((q.T*Cs*q)[0],50),'taylor_coefficients':[mp.nstr(x,65) for x in a]}
    rows.append(row); print(json.dumps(row),flush=True)
with open(HERE/'confluent_witness.json','w') as f:json.dump(rows,f,indent=2)
