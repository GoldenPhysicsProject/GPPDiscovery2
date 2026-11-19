"""Exact arithmetic on y²=x³+x+1 over F5, then over F25=F5[u]/(u²-2)."""
from itertools import product
from sympy import Poly, symbols, Matrix
from sympy.polys.matrices import DomainMatrix
from sympy import GF

x,y=symbols("x y")
def reduce_curve(expr):
    out=0
    for (a,b),c in Poly(expr,x,y,modulus=5).terms():
        out+=c*x**a*y**(b%2)*(x**3+x+1)**(b//2)
    return Poly(out,x,y,modulus=5)
def basis(n):
    return [x**(i//2) if i%2==0 else x**((i-3)//2)*y
            for i in range(n+1) if i!=1]
def order(poly):
    return max(2*a+3*b for (a,b),c in poly.terms() if c)
def mul(z,w):
    a,b=z
    c,d=w
    return ((a*c+2*b*d)%5,(a*d+b*c)%5)
def add(z,w):
    return tuple((a+b)%5 for a,b in zip(z,w))
def eval_poly(poly,z,w):
    total=(0,0)
    for (i,j),c in poly.terms():
        term=(int(c)%5,0)
        for _ in range(i): term=mul(term,z)
        for _ in range(j): term=mul(term,w)
        total=add(total,term)
    return total
pairs=list(product(basis(7),basis(4)))
columns=[reduce_curve(f*g**5) for f,g in pairs]
rows=sorted(set().union(*(pol.monoms() for pol in columns)))
mat=Matrix([[col.coeff_monomial(m) for col in columns] for m in rows])
D=DomainMatrix.from_Matrix(mat).convert_to(GF(5))
ker=D.nullspace().to_Matrix()
c=list(ker.row(0))
assert reduce_curve(sum(a*f*g**5 for a,(f,g) in zip(c,pairs))).is_zero
aux=reduce_curve(sum(a*f**5*g for a,(f,g) in zip(c,pairs)))
field=list(product(range(5),repeat=2))
affine=[(z,w) for z,w in product(field,repeat=2)
        if mul(w,w)==add(add(mul(mul(z,z),z),z),(1,0))]
assert all(eval_poly(aux,z,w)==(0,0) for z,w in affine)
assert order(aux)>0 and len(affine)<=order(aux)
print("columns, rank, kernel dimension:",len(pairs),D.rank(),ker.rows)
print("nonzero terms (coefficient,f,g):",[(int(a),f,g) for a,(f,g) in zip(c,pairs) if a])
print("auxiliary polynomial:",aux.as_expr())
print("pole order, affine count, projective count:",order(aux),len(affine),len(affine)+1)
idx=pairs.index((x**2*y,y))
changed=c.copy()
assert changed[idx]==2
changed[idx]=1
bad=reduce_curve(sum(a*f*g**5 for a,(f,g) in zip(changed,pairs)))
assert order(bad)==22
print("changed relation at (2,1):",eval_poly(bad,(2,0),(1,0)))
assert eval_poly(bad,(2,0),(1,0))==(1,0)
