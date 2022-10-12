from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        d = Counter(arr)
        f = list(d.items())
        f.sort(key=lambda x:x[1], reverse=True)
        cnt = 1
        s = f[0][1]
        for i in range(1, n):
            if s >= n / 2:
                break
            s += f[i][1]
            cnt += 1
        return cnt
