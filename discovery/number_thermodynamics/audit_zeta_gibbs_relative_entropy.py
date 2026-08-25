import mpmath as mp

mp.mp.dps = 70


def U(beta):
    return -mp.diff(mp.zeta, beta) / mp.zeta(beta)


def fisher(beta):
    z = mp.zeta(beta)
    z1 = mp.diff(mp.zeta, beta)
    z2 = mp.diff(mp.zeta, beta, 2)
    return z2/z - (z1/z)**2


def kl_closed(beta, gamma):
    return mp.log(mp.zeta(gamma)) - mp.log(mp.zeta(beta)) + (gamma-beta)*U(beta)


def kl_term(n, beta, gamma):
    pb = mp.power(n, -beta) / mp.zeta(beta)
    pg = mp.power(n, -gamma) / mp.zeta(gamma)
    return pb * mp.log(pb/pg)


def kl_sum(beta, gamma, N):
    return mp.fsum(kl_term(n, beta, gamma) for n in range(1, N+1))


def kl_nsum(beta, gamma):
    return mp.nsum(lambda n: kl_term(n, beta, gamma), [1, mp.inf])


def jeffreys_closed(beta, gamma):
    return (gamma-beta)*(U(beta)-U(gamma))


if __name__ == '__main__':
    for beta, gamma in [(2,3), (1.3,2.2), (4,4.5)]:
        print('beta,gamma =', beta, gamma)
        kc = kl_closed(beta,gamma)
        for N in [100,1000,10000]:
            ks = kl_sum(beta,gamma,N)
            print(' N',N,'raw cutoff error',mp.nstr(abs(ks-kc),12))
        kn = kl_nsum(beta,gamma)
        print(' nsum KL error =', mp.nstr(abs(kn-kc),12))
        J = kl_closed(beta,gamma)+kl_closed(gamma,beta)
        print(' Jeffreys identity error =', mp.nstr(abs(J-jeffreys_closed(beta,gamma)),12))
        gint = mp.quad(fisher,[beta,gamma])
        print(' integrated Fisher error =', mp.nstr(abs(J-(gamma-beta)*gint),12))
