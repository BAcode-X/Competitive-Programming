from collections import defaultdict

class Solution:
    def isHappy(self, n: int) -> bool:
        d = defaultdict(int)
        n = str(n)
        while True:
            b = sum(map(lambda x:int(x)**2, list(n)))
            if b == 1 or d[b]:
                break
            d[b] = 1
            n = str(b)
        return True if b == 1 else False
