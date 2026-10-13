"""Correctly completed adversarial analytic functions (no Euler cutoff)."""
import mpmath as m
m.mp.dps=50
alpha=(m.sqrt(10-2*m.sqrt(5))-2)/(m.sqrt(5)-1)
chi=[0,1,1j,-1j,-1]
def Lchi(s,conjugate=False):
 return 5**(-s)*sum((m.conj(chi[a]) if conjugate else chi[a])*m.zeta(s,m.mpf(a)/5) for a in range(1,5))
def D(s):
 return ((1-1j*alpha)*Lchi(s)+(1+1j*alpha)*Lchi(s,True))/2
def DH(s):
 return (5/m.pi)**(s/2)*m.gamma((s+1)/2)*D(s)
def xi(s):
 return s*(s-1)/2*m.pi**(-s/2)*m.gamma(s/2)*m.zeta(s)
def Ftheta(s,theta=m.mpf('.25')):
 return xi(s-theta)*xi(s+theta)
def Epstein_series(s):
 # Poisson-Chowla-Selberg exact rapidly convergent representation
 z=2*m.zeta(2*s)+2*m.sqrt(m.pi)*m.gamma(s-.5)/m.gamma(s)*5**(.5-s)*m.zeta(2*s-1)
 K=sum((m.mpf(k)/n)**(s-.5)*m.besselk(s-.5,2*m.pi*m.sqrt(5)*n*k) for n in range(1,6) for k in range(1,6))
 return z+8*m.pi**s/m.gamma(s)*5**(.25-s/2)*K
def Epstein(s):
 return s*(s-1)*(m.sqrt(5)/m.pi)**s*m.gamma(s)*Epstein_series(s)
def response(H,u):
 r=m.sqrt(1+u);s=m.mpf('.5')+r
 return m.diff(H,s)/(2*r*H(s))
if __name__=='__main__':
 for name,H in [('xi',xi),('shifted',Ftheta),('DH',DH),('Epstein',Epstein)]:
  s=m.mpc('.33','.52')
  print(name,'FE ratio',m.nstr(H(s)/H(1-s),20))
  print(name,'response u=1',m.nstr(response(H,m.mpf(1)),18))
