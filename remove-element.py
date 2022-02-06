"""
    Given an integer array nums and an integer val, 
    remove all occurrences of val in nums in-place. 
    The relative order of the elements may be changed.
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        n = nums.__len__()
        if n:
            for i in range(n):
                if nums[i] != val:
                    nums[cnt] = nums[i]
                    cnt += 1
        return cnt
