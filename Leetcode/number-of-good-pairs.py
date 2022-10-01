from typing import List
from math import factorial
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for val in cnt.values():
            if val > 1:
                ans += int(factorial(val) / (2*factorial(val-2)))
        return ans
