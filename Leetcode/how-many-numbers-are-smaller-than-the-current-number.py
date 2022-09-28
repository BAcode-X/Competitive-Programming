from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = nums[:]
        a.sort()
        return [a.index(i) for i in nums]
