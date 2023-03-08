from itertools import accumulate

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]+list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]
