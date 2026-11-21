/*
Endpoint test for Heart's Round 34. Use K(m,n)=log X-|log(n/m)| on m,n<=X,
a_n=mu(n)/sqrt(n)-c[n=1], c=1/zeta(1/2). Let E(z)=sum a_m a_n K(m,n)
z^k, where k counts primes dividing exactly one of the two squarefree
indices. The diagonal convention at n=m=1 includes the centering.

At X=3, E(z)=H-Az+Bz^2, A=sqrt(2)(1-c)log(3/2), B=2 log(2)/sqrt(6).
Only (1,2) and (2,3) contribute off the diagonal; (1,3) has zero weight.
A<2B: write eta=(1-sqrt(2))*zeta(1/2). The alternating sum for eta
exceeds 1/2, since 2 eta - 1 is the alternating series of first
differences n^(-1/2)-(n+1)^(-1/2), positive and decreasing. Thus
1-c < 1+2(sqrt(2)-1) < 1.83, giving A<1.06 whereas 2B>1.13.
The unique minimum is A/(2B)=0.85348924..., strictly inside the interval.
The universal endpoint minimum is therefore false. This does not change
the positivity identity or refute the weaker comparison E(1)<=H.

For any integer X, f_p denotes the subvector of f supported on multiples
of p. With the K bilinear form, E'(1)=2 sum_p <f_p, f-f_p>. Each ordered
pair has been counted once per differing prime. The program obtains
<f_p,f> from ordinary prefix sums and <f_p,f_p> from prefixes over
multiples of p. No layer coefficients, random sampling, or zeros enter.
Complexity O(X log log X) time and O(X) memory. At X=10^7 the long-double
result is +11.65679399 (numerical). Heart's published layers independently
give +11.65686288; at z=.9999 they give E(z)-E(1)=-.0008857880.
Her 81-point grid has final step .025. At the same X those layers give
E(.2)=62774.78 > (E(0)+E(.4))/2=33325.79, excluding global convexity
numerically. The X=3 analytic counterexample is independent of either
large-X computation. Whether the minimum fails at arbitrarily large X
is open in this analysis.
*/
// g++ -O3 -std=c++17 endpoint_derivative.cpp -o endpoint && ./endpoint 10000000
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    int N = argc > 1 ? std::atoi(argv[1]) : 3;
    if (N < 2 || N > 100000000) return 1;
    std::vector<int> primes;
    std::vector<bool> composite(N+1);
    std::vector<signed char> mu(N+1, 1);
    for (int p=2; p<=N; ++p) {
        if (composite[p]) continue;
        primes.push_back(p);
        for (int n=p; n<=N; n+=p) {
            composite[n]=true;
            mu[n]=-mu[n];
        }
        for (long long n=1LL*p*p; n<=N; n+=1LL*p*p) mu[n]=0;
    }

    using Real = long double;
    const Real L=std::log(Real(N)), c=1 / -1.460354508809586812889499152515298L;
    std::vector<Real> a(N+1), logn(N+1), prefix(N+1), moment(N+1);
    for (int n=1; n<=N; ++n) {
        a[n]=mu[n]/std::sqrt(Real(n))-(n==1 ? c : 0);
        logn[n]=std::log(Real(n));
        prefix[n]=prefix[n-1]+a[n];
        moment[n]=moment[n-1]+a[n]*logn[n];
    }
    Real derivative=0;
    for (int p : primes) {
        Real sum=0, weighted=0, inner=0, self=0;
        for (int n=p; n<=N; n+=p) {
            if (!mu[n]) continue;
            Real left=(L-logn[n])*prefix[n]+moment[n];
            Real right=(L+logn[n])*(prefix[N]-prefix[n])-(moment[N]-moment[n]);
            inner+=a[n]*(left+right);
            self+=2*a[n]*((L-logn[n])*sum+weighted)+L*a[n]*a[n];
            sum+=a[n];
            weighted+=a[n]*logn[n];
        }
        derivative+=2*(inner-self);
    }
    std::cout<<std::setprecision(15)<<N<<" "<<derivative<<"\n";
}
