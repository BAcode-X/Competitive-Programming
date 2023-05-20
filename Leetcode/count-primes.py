from bisect import bisect_left


max_n = (5* 10**6) + 1
is_prime = [True for _ in range(max_n)]
is_prime[0] = is_prime[1] = False

i = 2

while i*i <= max_n:
    if is_prime[i]:
        for j in range(i*i, max_n, i):
            is_prime[j] = False
    i += 1
primes = [i for i in range(max_n) if is_prime[i]]


class Solution:
    def countPrimes(self, n: int) -> int:
        return bisect_left(primes, n)
