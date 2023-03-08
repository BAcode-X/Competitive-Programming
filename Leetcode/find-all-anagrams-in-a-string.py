from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        result = []
        target_counts = Counter(p)
        window_counts = Counter(s[:n-1])
        for i in range(n - 1, len(s)):
            window_counts[s[i]] += 1
            if window_counts == target_counts:
                result.append(i - n + 1)
            window_counts[s[i - n + 1]] -= 1
            if window_counts[s[i - n + 1]] == 0:
                del window_counts[s[i - n + 1]]

        return result
