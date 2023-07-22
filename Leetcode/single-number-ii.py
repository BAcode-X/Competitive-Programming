class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = 0
        twice = 0
        for i in nums:
            once = (once ^ i) & ~twice
            twice = (twice ^ i) & ~once
        return once
