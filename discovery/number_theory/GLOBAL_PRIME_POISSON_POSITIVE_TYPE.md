# Global prime-Poisson response is positive type on a>1

Codex/GPT discovery track, 2026-08-25.

For a>1 define the absolutely convergent global prime response

G_a(t)=sum_p W_{p,a}(t).

The verified local theorem gives, for every prime p,

W_{p,a} is positive type,

because it is log(p)>=0 times a rescaled vacuum-subtracted Poisson kernel K_r-1 with r=p^{-a} in (0,1).

The verified global prime-power/Fubini theorem gives absolute convergence of

sum_p W_{p,a}(t)

for every real t, and the exact identity

G_a(t)=2 Re[-zeta'/zeta(a+it)].

Now fix finitely many x_i in R and c_i in C. The Gram form is

Q_a = Re sum_{i,j} conjugate(c_i)c_j G_a(x_i-x_j).

Because the i,j sums are finite and every prime series at the finitely many differences x_i-x_j is absolutely convergent, interchange is legitimate:

Q_a
 = sum_p Re sum_{i,j} conjugate(c_i)c_j W_{p,a}(x_i-x_j).

Every summand on the right is >=0 by local positive type. Hence

boxed:

G_a is positive type for every a>1.

Using the global logarithmic-derivative identity,

boxed:

t -> 2 Re[-zeta'/zeta(a+it)]

is therefore a positive-type function on R for every a>1.

This is a genuine infinite-prime positivity theorem in the half-plane of absolute convergence. It is stronger than the earlier finite-prime statement, but it does NOT extend positivity into the critical strip. Any such continuation would require additional analytic input and is not inferred here.

This result is the clean arithmetic-side positive-type object to compose with convolution-square/Weil test kernels before investigating a controlled boundary limit a->1+.
