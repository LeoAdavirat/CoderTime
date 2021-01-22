import re
def isPrime(n):
	return re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None
def Primes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return list([i for i in range(len(prime)) if prime[i] == True])