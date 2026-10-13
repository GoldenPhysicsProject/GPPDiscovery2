import mpmath as mp, json
from pathlib import Path
HERE=Path(__file__).resolve().parent

def logxi(s):
    return 1/s+1/(s-1)-mp.log(mp.pi)/2+mp.digamma(s/2)/2+mp.zeta(s,derivative=1)/mp.zeta(s)

def m(u,theta=None):
    r=mp.sqrt(1+u); s=mp.mpf('.5')+r
    return logxi(s)/(2*r) if theta is None else (logxi(s-theta)+logxi(s+theta))/(2*r)

def run(dps,N):
    mp.mp.dps=dps; u0=mp.mpf(1); radius=mp.mpf(16)
    points=[mp.exp(2j*mp.pi*k/N) for k in range(N)]
    output={'dps':dps,'samples':N,'center':str(u0),'radius':str(radius),'controls':[]}
    for label,theta in [('zeta',None),('theta_1_4',mp.mpf(1)/4),('theta_1_10',mp.mpf(1)/10)]:
        vals=[m(u0+radius*z,theta) for z in points]
        # b_j = radius**j * Taylor coefficient; no factorial derivatives needed.
        b=[mp.re(sum(v/z**j for v,z in zip(vals,points))/N) for j in range(12)]
        for n in (3,4,5,6):
            C=mp.matrix(n)
            for i in range(n):
                for j in range(n): C[i,j]=(-1)**(i+j+1)*b[i+j+1]/radius
            ev=mp.eigsy(C,eigvals_only=True)
            row={'control':label,'n':n,'min':mp.nstr(ev[0],35),'relative_min':mp.nstr(ev[0]/ev[n-1],35)}
            output['controls'].append(row); print(json.dumps(row),flush=True)
    return output
if __name__=='__main__':
    results=[run(90,128),run(140,192)]
    with open(HERE/'confluent_results.json','w') as f:json.dump(results,f,indent=2)
