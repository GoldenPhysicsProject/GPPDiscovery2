/*
From pair phases to block energy. Set u_n=log n, a_n as in damped_work.js
(or any real finite weights), and r>0. On a common celestial equator the
oriented pair phases z_ij=conj(e_i)e_j satisfy z_ij z_jk=z_ik. A change
of signs e_i -> s_i e_i preserves every such closure identity. After
Cauchy frequency averaging, the unsigned pair kernel is K_ij=exp(-r|u_i-u_j|).
For ordered triples it still factors: K_ij K_jk=K_ik. The signed version
factors as well since the middle sign squares to one.

Place rate-r Poisson cuts on the log axis. Two points share a cell iff
no cut lies between them, with probability K_ij. Expanding cell squares
gives the exact identity W=sum_ij a_i a_j K_ij =
E[sum over cells C of (sum_{u_i in C} a_i)^2]. This does not assume primes
are random. Only the measuring windows are randomized. Below all possible
cut patterns in the gaps are enumerated, with their exact Bernoulli
probabilities evaluated in floating point, for a small finite example.

There is also a fixed-range deterministic comparison. For a length h put
D(h)=integral over ALL real v of |sum_{v<u_i<=v+h} a_i|^2 dv.
Keep edge windows with v<0 and windows extending beyond the last index.
Pair overlap gives D(h)=sum_ij a_i a_j (h-|u_i-u_j|)_+. Thus exactly
 W = r^2 integral_0^infinity exp(-rh) D(h) dh .
Moreover W is comparable, by absolute positive constants, to
 J = r^2 integral_{1/r}^{2/r} D(h) dh.
Proof: by Plancherel the spectral multiplier of W is 2r/(r^2+t^2)
with dt/(2pi), multiplying |sum a_n exp(-it u_n)|^2. For J the multiplier
is (2/r) integral_1^2 (1-cos(y s))/y^2 ds, y=t/r. Their ratio is
(1+y^2) integral_1^2 (1-cos(y s)) ds / y^2. It has positive limit 7/6
at zero, stays strictly positive at every nonzero finite y, and tends
to 1 at infinity since the cosine integral is O(1/|y|). Continuity gives
both universal comparison constants. Averaging lengths prevents the
Fourier zeros of a single fixed interval from invalidating this argument.

For r=(log X)^2, these lengths are between 1/log^2 X and 2/log^2 X.
Their multiplicative widths near n are of order n/log^2 X.
A subpower bound for J on unbounded cutoffs would bound the genuine
damped work and hence Q by the preceding recovery and sparse-energy
lemmas. Proving this arithmetic estimate remains open. The phase-flip
control satisfies phase closure and the identical block identities,
but changes the signed mass inside each window. No gravitational field
or additional celestial dimension is used by the comparison.
*/
// Exhaustive independent cut-pattern check of the logarithmic block identity.
function check(indices, weights, rate) {
  const times = indices.map(Math.log);
  const keep = times.slice(1).map((t,i)=>Math.exp(-rate*(t-times[i])));
  let pairs=0, blocks=0, mass=0;
  for(let i=0;i<times.length;i++) for(let j=0;j<times.length;j++)
    pairs += weights[i]*weights[j]*Math.exp(-rate*Math.abs(times[i]-times[j]));
  for(let mask=0;mask<2**keep.length;mask++) {
    let probability=1, sum=weights[0], energy=0;
    for(let j=0;j<keep.length;j++) {
      if(mask & (1<<j)) {probability*=1-keep[j];energy+=sum*sum;sum=0;}
      else probability*=keep[j];
      sum+=weights[j+1];
    }
    blocks += probability*(energy+sum*sum);
    mass += probability;
  }
  if(Math.abs(mass-1)>1e-12 || Math.abs(blocks-pairs)>1e-12)throw Error('mismatch');
  return {pairs,blocks};
}
const indices=[1,2,3,5,6,7,10,11,13,14,15];
const signs=[1,-1,-1,-1,1,-1,1,-1,-1,1,1];
const weights=indices.map((n,i)=>signs[i]/Math.sqrt(n)-(i===0?1/-1.4603545088095868:0));
for(const rate of [.5,3,8]) {
  const control=weights.map((a,i)=>indices[i]===11?-a:a);
  console.log(JSON.stringify({rate,ordinary:check(indices,weights,rate),control:check(indices,control,rate)}));
}
