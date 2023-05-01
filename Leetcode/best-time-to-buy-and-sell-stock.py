class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        ans = 0
        for i in prices:
            if i > mi:
                ans = max(ans, i - mi)
            else:
                mi = i
        return ans
