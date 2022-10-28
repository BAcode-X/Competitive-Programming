fibo = [1, 1]

for i in range(2, 33):
    fibo.append(fibo[i-1] + fibo[i-2])

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return fibo[n-1]
