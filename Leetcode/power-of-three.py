from collections import defaultdict

a = defaultdict(bool)
for i in range(21):
    a[3**i] = True

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        return a[n]