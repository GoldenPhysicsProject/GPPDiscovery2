"""Uniform two-magnitude xi Gram certificate. Requires python-flint 0.9.0."""
from flint import arb, acb, arb_mat, acb_mat, ctx
from null_interference import values

ctx.prec = 192
N, M = 36, 37
T, mesh = 210, 12
pi = arb.pi()


def grid(n):
    angles = [pi*(2*j+1)/(2*n) for j in range(n)]
    return [(1+a.cos())/32 for a in angles], arb_mat([
        [arb(1)/n if k == 0 else 2*(k*a).cos()/n for a in angles]
        for k in range(n)])


def xi(s):
    return s*(s-1)/2 * (-s*pi.log()/2).exp() * (s/2).gamma() * s.zeta()


def arithmetic_grams(us):
    roots = [u.sqrt() for u in us]
    count = len(us)
    totals = [acb_mat(count,count) for _ in range(2)]
    for first in range(0,T*mesh+1,32):
        rows = [[], []]
        weighted = [[], []]
        for i in range(first,min(first+32,T*mesh+1)):
            s = acb(arb(9)/2,arb(i)/mesh)
            h,m = values(s)
            scale = (1 if i == 0 else 2)*m
            odd, even = [], []
            for u,r in zip(us,roots):
                a,d = xi(s+r),xi(s-r)
                odd.append((a-d)/(2*r))
                even.append(((a+d)/2-h)/u)
            for k,(row,weight) in enumerate(((odd,-scale),(even,scale))):
                rows[k].append(row)
                weighted[k].append([weight*x for x in row])
        for k in range(2):
            totals[k] += acb_mat(rows[k]).transpose()*acb_mat(weighted[k])
    alias = 2*arb(10)**19/((4*pi*mesh).exp()-1)
    tail = arb(10)**15*(1+T)**5*(-pi*T/4).exp()/(pi/4-arb(5)/(1+T))
    error = arb(0,(alias+tail).upper())
    return [g.real/(mesh*pi) + arb_mat([[error]*count for _ in us]) for g in totals]


def certify():
    us, dx = grid(N)
    vs, dy = grid(M)
    grams = arithmetic_grams(us+vs)
    for label,g in zip(('odd','even'),grams):
        det = arb_mat(N,M)
        for i,u in enumerate(us):
            for j,v in enumerate(vs):
                k = N+j
                det[i,j] = (g[i,i]*g[k,k]-g[i,k]**2)/(u-v)**2
        coef = dx*det*dy.transpose()
        variation = sum(abs(coef[i,j]) for i in range(N) for j in range(M) if i or j)
        # One-dimensional Cauchy error and the x-interpolation operator norm.
        rem = 3*arb(10)**40*(1/arb(62)**N + 2*N/arb(62)**M)
        enclosure = coef[0,0]+arb(0,(variation+rem).upper())
        print(label,'normalized determinant bounds:',enclosure.lower(),enclosure.upper(),flush=True)
        assert enclosure > 0


if __name__ == '__main__':
    certify()
