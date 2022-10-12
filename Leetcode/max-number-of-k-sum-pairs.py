from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        cnt = 0
        while i < j:
            val = nums[i] + nums[j]
            if val == k:
                cnt += 1
                i += 1
                j -= 1
            elif val < k:
                i += 1
            else:
                j -= 1
        return cnt
