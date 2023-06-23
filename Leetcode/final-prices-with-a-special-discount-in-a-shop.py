class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = []
        for i in range(n):
            for j in range(1, n):
                if j > i and prices[j] <= prices[i]:
                    ans.append(prices[i] - prices[j])
                    break
            else:
                ans.append(prices[i])
        return ans
