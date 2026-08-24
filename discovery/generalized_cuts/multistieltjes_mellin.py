"""Universal Mellin kernel for an L-fold Stieltjes dispersion representation.

If
  F(S_1,...,S_L)=int_{R_+^L} rho(x) prod_j (x_j+S_j)^(-1) d^Lx,
then, whenever Tonelli/Fubini and Mellin convergence hold and 0<Re sigma_j<1,

  M[F](sigma) = pi^L prod_j csc(pi sigma_j) M[rho](sigma).

This is the iterated identity int_0^inf S^(sigma-1)/(x+S)dS
= pi x^(sigma-1)/sin(pi sigma). It is a mathematical dispersion theorem;
it does NOT assert that an arbitrary multiloop amplitude has such an unsubtracted
multi-Stieltjes representation.

The numerical check below uses L=2 and rho(x,y)=exp(-x-y), for which both sides
factorize but are integrated independently.
"""
import mpmath as mp
mp.mp.dps=40


def stieltjes1(S):
    return mp.quad(lambda x: mp.e**(-x)/(x+S), [0,1,5,mp.inf])


def lhs(sig1,sig2):
    # For the factorized test density, F(S,T)=f(S)f(T). Compute each Mellin
    # transform by quadrature independently; their product is the full L=2 lhs.
    def one(sig):
        return mp.quad(lambda u: mp.e**(sig*u)*stieltjes1(mp.e**u),
                       [-mp.inf,-5,0,5,mp.inf])
    return one(sig1)*one(sig2)


def rhs(sig1,sig2):
    # Mellin rho = Gamma(sig1) Gamma(sig2).
    return ((mp.pi/mp.sin(mp.pi*sig1))*mp.gamma(sig1))* \
           ((mp.pi/mp.sin(mp.pi*sig2))*mp.gamma(sig2))


if __name__=='__main__':
    for a,b in [(mp.mpf('.3'),mp.mpf('.7')),(mp.mpf('.45'),mp.mpf('.62'))]:
        L=lhs(a,b); R=rhs(a,b)
        err=abs(L-R)/max(1,abs(R))
        assert err < mp.mpf('1e-25')
        print(a,b,'relative error',mp.nstr(err,6))
    print('PASS: L=2 Mellin transform multiplies the two Stieltjes kernels by pi*csc(pi*sigma) each')
