from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            cnt = 0
            for i in piles:
                cnt += ceil(i / mid)
            if cnt <= h:
                right = mid
            else:
                left = mid + 1
        return left
