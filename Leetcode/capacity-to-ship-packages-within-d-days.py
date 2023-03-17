class Solution:
    def check(self, weights, val) -> int:
        days = 1
        cap = val
        for i in weights:
            if i <= cap:
                cap -= i
            else:
                cap = val - i
                days += 1
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), (sum(weights))
        ans = float('inf')
        while left <= right:
            mid = (left + right) // 2
            if self.check(weights, mid) <= days:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans
