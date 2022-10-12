from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        ff = list(cnt.items())
        ff.sort(key=lambda x:x[1], reverse=True)
        return [ff[i][0] for i in range(k)]