from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort(reverse=True)
        cnt = 0
        for i in range(n//3):
            cnt += piles[(2*i) + 1]
        return cnt
