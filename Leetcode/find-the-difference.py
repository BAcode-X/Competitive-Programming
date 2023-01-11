from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        for i in range(len(s)):
            if t[i] != s[i]:
                return t[i]
        return t[-1]
