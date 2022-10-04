from collections import Counter
from typing import List

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []
        changed.sort()
        a = Counter(changed)
        cnt = 0
        val = []
        for i in changed:
            if cnt >= (n//2):
                break
            if a.get(i, 0):
                a[i] -= 1
                if a.get(i*2, 0):
                    a[i*2] -= 1
                    cnt += 1
                    val.append(i)
                else:
                    return []
        return val