// For fixed support, R=2(log(X) sum_{m<n} a_m a_n - sum_{m<n} a_m a_n log(n/m)).
 // It is affine in log(X) between integers. Check both sides of jumps;
 // this is floating-point evidence, without an interval error bound.
// node scan_comparison.js [N]; check both limits at every cutoff.
const N=Number(process.argv[2] || 10000000);
const mu=new Int8Array(N+1).fill(1), composite=new Uint8Array(N+1);
for(let p=2;p<=N;p++) if(!composite[p]){
  for(let n=p;n<=N;n+=p){composite[n]=1;mu[n]=-mu[n];}
  for(let n=p*p;n<=N;n+=p*p) mu[n]=0;
}
let sum=0,moment=0,pairs=0,distance=0,norm=0;
let max=-Infinity, where, violations=0;
function inspect(n,side,L){
  const R=2*(L*pairs-distance), ratio=R/(L*norm);
  if(ratio>max){max=ratio;where=[n,side,R];}
  if(R>0) violations++;
}
for(let n=1;n<=N;n++){
  const L=Math.log(n), a=mu[n]/Math.sqrt(n)-(n===1?1/-1.4603545088095868:0);
  if(n>3) inspect(n,'left',L);
  pairs+=a*sum;
  distance+=a*(L*sum-moment);
  sum+=a; moment+=a*L; norm+=a*a;
  if(n>=3) inspect(n,'right',L);
}
console.log(JSON.stringify({N,max,where,violations}));
