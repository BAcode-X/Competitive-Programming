from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = 0, 0
        while i < n and j < n:
            if nums[i] == 0:
                if nums[j] == 0:
                    j += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                j += 1
