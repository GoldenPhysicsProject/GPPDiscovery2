/*
Least-prime recursion and a fixed-depth obstruction for the rough prefix.

For fixed horizon X let y=floor((log X)^2) and U_b(x) be the uncentered
sum of mu(n)/sqrt(n) over n<=x with all prime factors >b, including 1
for x>=1. For x>=1,
  U_y(x)=1-sum_{y<p<=x} U_p(x/p)/sqrt(p).
This counts each squarefree n>1 once by its smallest factor p and
retains the requirement that all factors of the cofactor exceed p.

Write F_p for each signed group prefix and F_1=1. In this program the
diagonal is integral sum_g F_g^2 du and the cross term is the signed
integral over ordered DISTINCT group pairs, including the group {1}.
When group p gets a kick a at n, its increment to the integrated
diagonal is log(X/n)(2 a F_p(old)+a^2). The increment to the cross
term is 2 log(X/n) a (U(old)-F_p(old)). We validate their sum against
separate direct integration over the log intervals, and compare each
kick from the cofactor recursion against mu from an independent sieve
rule. For each horizon the twist rotates primes in (X/2,3X/4]; within
the cutoff no composite changes. These primes are singleton groups
so their flips preserve the group diagonal. All energies are uncentered.

Paper lemma (fixed k>=1): truncate U_y to n with at most k prime factors,
giving U_{y,<=k}. Then integral_0^{log X}|U_{y,<=k}(exp u)|^2 du =
X^{1+o(1)}. Thus no fixed truncation can yield a fixed power saving for
this unsigned-in-time energy, even with the genuine Mobius signs.

Proof: uniformly for X/2<=x<=X, select k-1 distinct primes from
(y,x^{1/(4k)}], write d for their product, and take a last prime q in
(x/(2d), x/d]. This q is larger than every selected factor for large X.
PNT on dyadic intervals gives at least a constant times x/(d log X)
choices, uniformly since x/d>=x^{3/4}. The weighted contribution from
these k-factor terms is therefore at least
  c_k sqrt(X)(log log X)^{k-1}/log X.
Indeed Mertens' reciprocal-prime estimate on the selected range gives
sum 1/p asymptotic to log log X: the lower cutoff costs only
O(log log log X). Repeated coordinates in the fixed ordered tuple
are negligible by sum 1/p^2=O(1); divide by (k-1)! to forget order.
For k=1 the empty tuple gives the same bound directly.
All other k-factor terms have the same sign. The classical fixed-j
Landau almost-prime upper bound, followed by partial summation against
1/sqrt(n), bounds each j<k positive-depth layer by
  O_j(sqrt(X)(log log X)^{j-1}/log X)
even before excluding small primes. The constant term is 1. Thus the
top layer dominates pointwise throughout [X/2,X], yielding a lower
energy of order at least X(log log X)^{2k-2}/log^2 X. The absolute
prefix is <=2 sqrt(x), so the full integral is <=4X. This proves the
exponent for each fixed k. All implied constants may depend on k;
the argument does not cover growing k or the full sum.

Tests at 10^6, 10^7, 10^8 are finite numerical observations. At 10^8
the group diagonal was 1271.67792, the cross term +563117.20642, and
the total 564388.88434. The sparse twist lowered the total to
436863.06647. The 7327 three-prime terms were the deepest occupied
layer. No estimate for growing-depth cancellation, quasi-RH or RH
follows from these runs. Memory at the largest cutoff is about 300 MB.
*/
// Compile: c++ -O3 -std=c++17 least_prime.cpp -o least_prime && ./least_prime
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <vector>

struct Work {
    std::vector<double> prefix;
    double total=1, energy=0, diagonal=0, cross=0;
    explicit Work(int root):prefix(root+1,0){}
    void add(int p, double a, double remaining) {
        // Large least primes occur only at their own singleton n=p.
        double old = p < int(prefix.size()) ? prefix[p] : 0;
        if(p < int(prefix.size())) prefix[p]+=a;
        diagonal+=remaining*a*(2*old+a);
        cross+=2*remaining*a*(total-old);
        total+=a;
    }
};

void run(int N) {
    int root=std::sqrt(N), y=std::log(N)*std::log(N);
    std::vector<uint16_t> least(N+1,0);
    std::vector<int8_t> mu(N+1,1);
    for(int p=2;p<=N;++p) if(!least[p]) {
        for(int n=p;n<=N;n+=p) mu[n]=-mu[n];
        for(long long n=1LL*p*p;n<=N;n+=1LL*p*p) mu[n]=0;
        if(p<=root) for(int n=p*p;n<=N;n+=p)
            if(!least[n]) least[n]=p;
    }
    Work real(root),twist(root);
    double direct=1, directTwist=1;
    double L=std::log(N);
    real.diagonal=twist.diagonal=L; // class {1}
    std::vector<int> counts(10);
    for(int n=1;n<=N;++n) {
        int p=least[n]?least[n]:n;
        if(n>1 && p>y) {
            int m=n/p;
            int kick=(m%p==0)?0:-mu[m];
            if(kick!=mu[n])throw std::runtime_error("factor recursion mismatch");
            if(kick) {
                int j=1,rest=m;
                while(rest>1){rest/=least[rest]?least[rest]:rest;++j;}
                ++counts.at(j);
                double a=kick/std::sqrt(n), remaining=std::log(double(N)/n);
                bool flip=(p==n && n>N/2 && n<=3*N/4);
                real.add(p,a,remaining);
                twist.add(p,flip?-a:a,remaining);
                direct+=mu[n]/std::sqrt(n);
                directTwist+=(flip?-mu[n]:mu[n])/std::sqrt(n);
            }
        }
        double width=n==N?0:std::log1p(1.0/n);
        real.energy+=width*direct*direct;
        twist.energy+=width*directTwist*directTwist;
    }
    for(const Work* w : {&real,&twist}) {
        double error=w->energy-(w->diagonal+w->cross);
        if(std::abs(error)>1e-7*(1+w->energy))throw std::runtime_error("energy mismatch");
        std::cout<<N<<" "<<y<<" "<<(w==&real?"ordinary":"twist")
                 <<" "<<w->energy<<" "<<w->diagonal<<" "<<w->cross
                 <<" "<<error<<" counts";
        for(auto v:counts) if(v)std::cout<<" "<<v;
        std::cout<<"\n";
    }
}
int main(){std::cout<<std::setprecision(12);for(int n:{1000000,10000000,100000000})run(n);}
