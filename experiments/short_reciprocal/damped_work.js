/*
Damped Mobius work on a finite log-time interval

Fix X>=3, L=log X, c=1/zeta(1/2), a_n=mu(n)/sqrt(n)-c[n=1].
Set B(u)=sum_{n<=exp u} a_n and Q=int_0^L B^2. Within EACH run fix a
rate r>0. Start y(0-)=0. Let y'=-r y between kicks and add a_n at
u=log n, counting the endpoint kick in y(L). Then exactly

 y(L)^2 + 2r int_0^L y^2 = W,
 W = sum_n a_n^2 + 2 sum_{m<n<=X} a_m a_n (m/n)^r.

Proof: the square falls at rate 2r y^2 between kicks, and its jump
is a_n^2+2 a_n y(log n-). The pre-kick value is the sum of earlier
kicks attenuated by (m/n)^r. This storage, work and dissipated energy
are explicit; the dissipated signal is y, whereas Heart observes B.
Integrating the differential equation gives B(u)=y(u)+r int_0^u y.
Triangle inequality and the L^2 convolution bound for 1_[0,L] yield

 Q <= (1+rL)^2 int_0^L y^2 <= (1+rL)^2 W/(2r).

Localization: take any K>=1 with log K=o(L), r=L K. On pairs with
log(n/m)>1/K the absolute kernel weight is <=1/X. Their total absolute
contribution to W is <=(sum |a_n|)^2/X <=(2 sqrt X+|c|)^2/X = O(1).
The diagonal is O(1+L). Thus a ONE-SIDED subpower upper bound for the
signed sum on 0<log(n/m)<=1/K, even on one sequence X_j->infinity,
suffices for Q(log X_j)<=X_j^o(1): the recovery multiplier is subpower.
By the sparse-energy criterion that implies RH. K=L (r=L^2) is used
in the program. No absolute-value bound on each shift is required.

The remaining arithmetic estimate is open. Trivial absolute bounds on
the near pairs do not give subpower growth. Applying a lossless echo
or postulating nonpositive interference is not an argument: the code
already finds positive cross work for genuine mu. This is a finite-horizon
damped filter with horizon-dependent rate; no single time-invariant
filter for all horizons is assumed. In the sparse sign-flip control
only primes X/2<p<=3X/4 are rotated and centering is held fixed.
The earlier rigorous Q >> X/log^2 X for that control and the recovery
bound force W >> X/log^7 X for r=L^2 (and thus force the near-pair
work to exceed subpower). These asymptotic claims for the control
are distinct from the small-cutoff numerical checks below.
*/
// Run with node. All energies use log time and a fixed damping rate per run.
function run(X) {
  const mu = new Int8Array(X+1).fill(1), composite = new Uint8Array(X+1);
  for(let p=2;p<=X;p++) if(!composite[p]) {
    for(let n=p;n<=X;n+=p){mu[n]=-mu[n];if(n>p)composite[n]=1;}
    for(let n=p*p;n<=X;n+=p*p)mu[n]=0;
  }
  const L=Math.log(X), rate=L*L, c=1/-1.4603545088095868;
  for(const twist of [false,true]) {
    let y=0, diag=0, cross=0, dissipated=0, prefix=0, Q=0;
    for(let n=1;n<=X;n++) {
      const gap=n===1?0:Math.log1p(1/(n-1));
      const attenuation=Math.exp(-rate*gap);
      dissipated+=y*y*(-Math.expm1(-2*rate*gap));
      Q+=prefix*prefix*gap;
      y*=attenuation;
      const flip=twist && n>X/2 && n<=3*X/4 && !composite[n];
      const a=mu[n]*(flip?-1:1)/Math.sqrt(n)-(n===1?c:0);
      cross+=2*y*a; diag+=a*a; y+=a; prefix+=a;
    }
    const residual=Math.abs(y*y+dissipated-diag-cross);
    if(residual>1e-8*Math.max(1,diag+cross))throw Error('energy mismatch');
    console.log(JSON.stringify({X,twist,rate,diag,cross,work:diag+cross,Q,residual}));
  }
}
for(const X of [10000,100000,1000000])run(X);
