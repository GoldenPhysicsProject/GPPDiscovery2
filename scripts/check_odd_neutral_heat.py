"""Odd pole-neutral heat test, with an explicitly artificial off-axis quartet.

No actual zeta zeros are used. This tests the witness construction, not RH.
"""
import json
import mpmath as mp

mp.mp.dps = 80
quarter = mp.mpf(1)/4
z = mp.mpc('0.2', '2')
alpha = -z*z
w = lambda a: a*(a+quarter)**2
# Deflate the synthetic on-axis zero pair at +/-i, which precedes the quartet.
q = lambda a: 1-a
C = w(alpha)*q(alpha)**2
# exp(-alpha*t) has phase +0.8*t. Make C exp(-alpha*t) negative real.
t = (mp.pi-mp.arg(C)+2*mp.pi)/(-mp.im(alpha))
F = lambda zz: zz*(zz*zz-quarter)*q(-zz*zz)*mp.exp(t*zz*zz/2)
quartet = [z, -z, mp.conj(z), -mp.conj(z)]
direct = sum(F(zz)*F(-zz) for zz in quartet)
predicted = 4*mp.re(C*mp.exp(-alpha*t))
tail = 2*mp.fsum(w(mp.mpf(k*k))*q(mp.mpf(k*k))**2*mp.exp(-k*k*t)
                  for k in range(1,101))
K = lambda tt: 4*mp.re(mp.exp(-alpha*tt)) + 2*mp.fsum(mp.exp(-k*k*tt) for k in range(1,101))
tt = mp.mpf('0.7')
H_derivative = -mp.diff(K,tt,3)+mp.diff(K,tt,2)/2-mp.diff(K,tt)/16
H_sum = 4*mp.re(w(alpha)*mp.exp(-alpha*tt))+2*mp.fsum(w(mp.mpf(k*k))*mp.exp(-k*k*tt) for k in range(1,101))
out = {
 'status':'synthetic falsifier; not arithmetic positivity or RH verification',
 'dps':mp.mp.dps, 'artificial_centered_zero':str(z), 'time':mp.nstr(t,30),
 'pole_values':[str(F(quarter**mp.mpf('.5'))),str(F(-quarter**mp.mpf('.5')))],
 'deflated_line_value':str(F(mp.j)),
 'quartet_energy':mp.nstr(direct,30), 'positive_online_tail':mp.nstr(tail,30),
 'total_energy':mp.nstr(mp.re(direct)+tail,30),
 'quartet_identity_error':mp.nstr(abs(direct-predicted),8),
 'heat_derivative_identity_error':mp.nstr(abs(H_derivative-H_sum),8)
}
assert abs(direct-predicted)<mp.mpf('1e-70')
assert abs(H_derivative-H_sum)<mp.mpf('1e-70')
assert mp.re(direct)+tail<0
print(json.dumps(out,indent=2))
