from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        m = 0
        nums.sort()
        for i in range(n//2):
            m = max(m, nums[i] + nums[-(i+1)])
        return m
