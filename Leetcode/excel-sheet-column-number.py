class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        ans = 0
        for i in range(n):
            ans += (26**i) * (ord(columnTitle[n-1-i]) - 64)
        return ans
