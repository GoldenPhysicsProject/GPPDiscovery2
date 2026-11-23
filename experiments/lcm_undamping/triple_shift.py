"""Three-magnitude cube certificate (python-flint 0.9.0)."""
from flint import arb, acb, arb_mat, acb_mat, ctx
from null_interference import values

ctx.prec = 392
pi = arb.pi()
sizes = (64, 65, 66)
mesh, cutoff = 8, 265


def grid(n):
    angles = [pi*(2*j+1)/(2*n) for j in range(n)]
    return [(1+a.cos())/32 for a in angles], arb_mat([
        [arb(1)/n if k == 0 else 2*(k*a).cos()/n for a in angles]
        for k in range(n)])


def xi(s):
    return s*(s-1)/2 * (-s*pi.log()/2).exp() * (s/2).gamma() * s.zeta()


def raw_grams(nodes):
    roots = [u.sqrt() for u in nodes]
    count = len(nodes)
    totals = [acb_mat(count,count) for _ in range(2)]
    for first in range(0,mesh*cutoff+1,32):
        rows = [[],[]]
        weighted = [[],[]]
        for k in range(first,min(first+32,mesh*cutoff+1)):
            s = acb(10,arb(k)/mesh)
            h,m = values(s)
            factor = (1 if k==0 else 2)*m
            odd,even = [],[]
            for u,r in zip(nodes,roots):
                a,d = xi(s+r),xi(s-r)
                odd.append((a-d)/(2*r))
                even.append(((a+d)/2-h)/u)
            for j,(row,weight) in enumerate(((odd,-factor),(even,factor))):
                rows[j].append(row)
                weighted[j].append([weight*x for x in row])
        for j in range(2):
            totals[j] += acb_mat(rows[j]).transpose()*acb_mat(weighted[j])
    rate = arb(7)/5
    tail = 10**37*(1+cutoff)**5*(-rate*cutoff).exp()/(rate-arb(5)/(1+cutoff))
    alias = 2*arb(10)**41/((14*pi*mesh).exp()-1)
    err = arb(0,(tail+alias).upper())
    errors = arb_mat([[err]*count for _ in nodes])
    return [g.real/(pi*mesh)+errors for g in totals]


def cube(g, grids):
    (us,dx),(vs,dy),(ws,dz) = grids
    n,m,p = sizes
    planes = []
    for k,w in enumerate(ws,n+m):
        plane = arb_mat(n,m)
        for i,u in enumerate(us):
            a,c = g[i,i],g[i,k]
            for j,v in enumerate(vs,n):
                b,d,e,f = g[i,j],g[j,j],g[j,k],g[k,k]
                det = a*(d*f-e*e)-b*(b*f-c*e)+c*(b*e-c*d)
                plane[i,j-n] = det/((u-v)*(u-w)*(v-w))**2
        planes.append(dx*plane*dy.transpose())
    # Contract the last Chebyshev axis, then sum the nonconstant coefficients.
    coeff = dz*arb_mat([[plane[i,j] for i in range(n) for j in range(m)]
                         for plane in planes])
    variation = sum(abs(coeff[k,j]) for k in range(p) for j in range(n*m) if k or j)
    rem = 3*arb(10)**60*(1/arb(62)**n+2*n/arb(62)**m+4*n*m/arb(62)**p)
    return coeff[0,0]+arb(0,(variation+rem).upper())


if __name__ == '__main__':
    grids = [grid(n) for n in sizes]
    grams = raw_grams([u for nodes,_ in grids for u in nodes])
    for label,g in zip(('odd','even'),grams):
        enclosure = cube(g,grids)
        print(label,enclosure.lower(),enclosure.upper(),flush=True)
        assert enclosure > 0
