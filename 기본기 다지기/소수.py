m = int(input())
n = int(input())
primes = []

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for i in range(m, n+1):
    if isPrime(i):
        primes.append(i)

if len(primes):
    print(sum(primes))
    print(primes[0])
else:
    print(-1)