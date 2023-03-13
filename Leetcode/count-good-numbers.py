class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = n // 2
        odd = n - even
        mod = 10**9 + 7
        return (pow(4, even, mod) * pow(5, odd, mod)) % mod
