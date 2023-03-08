from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        result = []
        target_counts = Counter(s1)
        window_counts = Counter(s2[:n-1])
        for i in range(n - 1, len(s2)):
            window_counts[s2[i]] += 1
            if window_counts == target_counts:
                return True
            window_counts[s2[i - n + 1]] -= 1
            if window_counts[s2[i - n + 1]] == 0:
                del window_counts[s2[i - n + 1]]
        return False
