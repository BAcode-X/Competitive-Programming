class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        if n < 3:
            return n
        prev1 = 1
        prev2 = 2
        for i in range(2, n):
            ans = prev1 + prev2
            prev1 = prev2
            prev2 = ans
        return ans
