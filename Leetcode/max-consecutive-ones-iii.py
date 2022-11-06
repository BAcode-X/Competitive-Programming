from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        a = 0
        cnt = 0
        for i in range(n):
            k -= 1 - nums[i]
            if k < 0:
                k += 1 - nums[a]
                a += 1
            cnt = max(cnt, i-a+1)
        return cnt