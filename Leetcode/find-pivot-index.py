from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        left = 0
        for i in range(len(nums)):
            val = nums[i]
            if left == tot - val:
                return i
            left += val
            tot -= val
        return -1
