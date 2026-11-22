/*
Which prime echoes can be removed from the sparse energy criterion?

On [0,L], L=log X, put U(u)=sum_{n<=exp(u)} mu(n)/sqrt(n).
U_y keeps n=1 and only n whose smallest prime factor exceeds y. Fix y
for the ENTIRE horizon. Use uncentered signals. The R33 centered signal
differs from U by c, of L2 norm |c|sqrt(L), harmless for a subpower test.
Let S_h f(u)=f(u-h) with f zero before time 0. Delays are contractions.

 U = D_y U_y,   U_y = D_y^{-1} U,
 D_y=product_{p<=y}(I-p^(-1/2) S_log(p)).
The first identity is unique squarefree factorization; the inverse
expands as sum over y-smooth n<=X of n^(-1/2) S_log(n), including 1.
Longer delays vanish. Both norms are at most
 V(X,y)=sum_{n<=X, n y-smooth} n^(-1/2),
by triangle inequality (the signed forward expansion uses only
squarefree smooth indices). For y=(log X)^A with fixed A>0,
   log ||D_y^{-1}|| / log X -> max(0,1/2-1/A).
Here the norm is the unrestricted operator norm on L2[0,L].

For a real quadratic character, Lee Crossley uses the factors I-chi(p)p^(-1/2) S_log(p) to remove primes up to (log d)^2 from a Gaussian sum, where d is the field discriminant. See equation (3b) in https://doi.org/10.5281/zenodo.24418495.

Upper proof: for s>max(0,1/2-1/A), V <= X^s product_{p<=y}
(1-p^(-1/2-s))^(-1). The log product is O_s(1+sum_{n=2}^y
n^(-1/2-s))=o(log X), by elementary integral comparison (taking the
logarithmic case separately). Let s decrease to the threshold.
Lower proof for A>2: apply the inverse to the constant unit-amplitude
signal. On the last log-time unit its output is at least V(X/e,y).
Take products of k=floor(log(X/e)/log y) distinct primes <=y. The
products are distinct and each weighs at least X^(-1/2).
With P=pi(y), binomial(P,k)>=(P/k)^k, and PNT gives
k log(P/k)=(1-1/A+o(1))log X. Dividing the output norm by sqrt(L)
does not change the exponent. For A<=2 a norm lower bound of 1 follows
from the nonnegative coefficients and the identity term on the
constant input. No lower bound on the true Mobius signal is inferred
from the operator norm.

Consequently for any sequence X_j->infinity and fixed A<=2, full
centered energy is X_j^o(1) in the upper-bound sense iff uncentered
rough energy ||U_y||^2 is at most X_j^o(1), along the SAME sequence.
The two triangle bounds prove both directions after adding/subtracting
the fixed centering. This statement concerns the accumulated prefix
energy behind the window criterion; it does not assert equality of
truncated sliding-window energies. A>2 has a genuine power cost for
arbitrary-input reconstruction of the rough signal from the full one.
This does not preclude a better estimate on Mobius data.

The code reverses each Euler factor on integer coefficients by an
ascending sweep (geometric series); descending sweeps restore all
original coefficients. The weights n^(-1/2) are applied at the
energy evaluation; multiplicativity gives the stated delay weights.
*/
// Run with node. Check the coefficient identities exactly before computing energies.
function check(N) {
  const L=Math.log(N), Y=Math.floor(L*L);
  const mu=new Int8Array(N+1).fill(1), least=new Int32Array(N+1), primes=[];
  for(let p=2;p<=N;p++) if(!least[p]) {
    primes.push(p);
    for(let n=p;n<=N;n+=p){mu[n]=-mu[n]; if(!least[n]) least[n]=p;}
    for(let n=p*p;n<=N;n+=p*p) mu[n]=0;
  }
  const restored=Int32Array.from(mu);
  for(const p of primes) {
    if(p>Y) break;
    for(let n=p;n<=N;n+=p) restored[n]+=restored[n/p];
  }
  let full=0,rough=0,fullEnergy=0,roughEnergy=0;
  for(let n=1;n<=N;n++){
    const wanted=n===1 || least[n]>Y ? mu[n] : 0;
    if(restored[n]!==wanted) throw Error('inverse mismatch at '+n);
    full+=mu[n]/Math.sqrt(n); rough+=restored[n]/Math.sqrt(n);
    const width=n<N?Math.log1p(1/n):0;
    fullEnergy+=width*full*full;
    roughEnergy+=width*rough*rough;
  }
  for(const p of primes) {
    if(p>Y) break;
    for(let n=N-N%p;n>=p;n-=p) restored[n]-=restored[n/p];
  }
  for(let n=1;n<=N;n++) if(restored[n]!==mu[n])throw Error('forward mismatch');
  return {N,Y,uncenteredFull:fullEnergy,uncenteredRough:roughEnergy};
}
for(const N of [10000,100000,1000000]) console.log(JSON.stringify(check(N)));
