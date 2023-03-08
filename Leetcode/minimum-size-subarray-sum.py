from itertools import accumulate

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] + list(accumulate(nums))
        min_ = float('inf')
        left = 0
        right = 1
        while right <= n:
            s = pref[right] - pref[left]
            if s >= target:
                min_ = min(min_, right - left)
                left += 1
            else:
                right += 1
        if min_ != float('inf'):
            return min_
        return 0
