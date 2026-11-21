/*
Two tests of the Fejer off-diagonal for the ordinary Mobius coefficients

Write L=log X, c=1/zeta(1/2)<0 and a_n=mu(n)/sqrt(n)-c[n=1]. R=2 sum_{m<n<=X} a_m a_n (L-log(n/m)). Set m=gu,n=gv with coprime u<v. Away from the centering correction, the contribution from an entire reduced ratio v/u equals
2 (L-log(v/u)) mu(u)mu(v)/sqrt(uv) times sum_{g<=X/v, gcd(g,uv)=1} mu(g)^2/g.
The correction on u=1 is -2c (L-log v)mu(v)/sqrt(v). This follows directly from unique factorization, including zeros when squares divide u or v. Reflection of the ratio exchanges the ordered pair and keeps its sign. Distinct reduced ratios must cancel for a small total.

For v/u=p prime the entire contribution is negative (zero at the outer endpoint p=X). It is -2(L-log p)/sqrt p times (sum_{g<=X/p,p does not divide g} mu(g)^2/g - c). Their sum is negative of magnitude at least a constant times sqrt(X)/log X for large X by primes between X/2 and 3X/4, keeping only g=1. This is larger than the O(log^2 X) scale permitted for a negative total R, since G=H+R>=0 and H=O(log^2 X). Hence compensating positive contributions from other ratios are mathematically necessary. A proof only counting these negative pairs misses cancellation of a larger order. The signs on individual additive shifts need not be estimated separately to establish an aggregate bound.

For an X-dependent control rotate only prime coordinates in (X/2,3X/4] by -1. At length X only these prime coefficients change, since their proper multiples exceed X. The divisor inverse identity survives at all n<=X except the rotated primes themselves. All centered Haar norms agree. On 3X/4<=y<=X the centered half-weighted prefix changes by the same 2 sum_{X/2<p<=3X/4} 1/sqrt(p), of order sqrt(X)/log X by PNT. The true centered prefix is o(sqrt(X)/log X) uniformly there, from the classical unconditional Mertens estimate M(y)=O_A(y/log^A y) and partial summation with A=2. Therefore the control's Q is bounded below by a positive constant times X/log^2 X on integrating over that fixed log-length. Since G>=Q and H=O(log^2 X), the twisted R is eventually positive. This is a finite-scale stress test, not an assertion about a fixed twisted L-function. It tests any proposed uniform argument using only a density-one set of inverse identities or all identities up to X/2, together with translation-invariant norms; fixing the exact ordinary-integer inverse at every prime is outside that scope.

Numerics use prefix integration between consecutive integers and the R33 identity for G. The prime-ratio subtotal is computed independently by its sign-definite formula. Exact formulas and asymptotic bounds above are separate from floating-point examples.
*/
// Run with node. The twist flips primes in (X/2, 3X/4].
function compare(X) {
  const mu = new Int8Array(X+1).fill(1);
  const composite = new Uint8Array(X+1), primes = [];
  for (let p=2;p<=X;p++) {
    if (composite[p]) continue;
    primes.push(p);
    for (let k=p;k<=X;k+=p) { mu[k]*=-1; if(k>p) composite[k]=1; }
    for (let k=p*p;k<=X;k+=p*p) mu[k]=0;
  }
  const L=Math.log(X), c=1 / -1.4603545088095868;
  const cells = [false,true].map(twist => {
    let prefix=0, Q=0, floor=0, diagonal=0;
    for (let n=1;n<=X;n++) {
      const flip=twist && n>X/2 && n<=3*X/4 && !composite[n];
      const a=mu[n]*(flip?-1:1)/Math.sqrt(n)-(n===1?c:0);
      prefix+=a;
      const width=n===X?0:Math.log1p(1/n);
      Q+=width*prefix*prefix;
      floor+=width*prefix;
      diagonal+=a*a;
    }
    const H=L*diagonal, G=2*Q+L*prefix*prefix-2*prefix*floor;
    return {Q,R:G-H,H};
  });
  let primeRatio=0;
  for (const p of primes) {
    let inner=0;
    for (let g=1;g*p<=X;g++) if(g%p!==0) inner+=mu[g]*mu[g]/g;
    primeRatio-=2*(L-Math.log(p))*(inner-c)/Math.sqrt(p);
  }
  return {X,cells,primeRatio};
}
for (const X of [10000,100000,1000000]) console.log(JSON.stringify(compare(X)));
