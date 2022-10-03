from collections import defaultdict

a = defaultdict(bool)
for i in range(16):
    a[4**i] = True

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        return a[n]
