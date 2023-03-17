from math import ceil

class Solution:
    def check(self, nums, val) -> int:
        return sum(map(lambda x: ceil(x/val), nums))

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right) // 2
            print(mid, self.check(nums, mid))
            if self.check(nums, mid) > threshold:
                left = mid + 1
            else:
                right = mid - 1
        return left
