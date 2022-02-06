"""
    Given an integer array nums sorted in non-decreasing order, 
    remove the duplicates in-place such that each unique element appears only once. 
    The relative order of the elements should be kept the same.

"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        n = nums.__len__()
        if n:
            for i in range(n - 1):
                if nums[i] != nums[i + 1]:
                    nums[cnt] = nums[i]
                    cnt += 1
            nums[cnt] = nums[-1]
            cnt += 1
        return cnt
