class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        d = {}
        max_ = 0
        i = 0
        for j in range(n):
            if s[j] in d and d[s[j]] >= i:
                i = d[s[j]] + 1
            d[s[j]] = j
            max_ = max(max_, j - i + 1)
        return max_
