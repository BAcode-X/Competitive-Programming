from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        rep = Counter(tasks)
        rep_val = list(rep.values())
        chk = all([i > 1 for i in rep_val])
        if not chk:
            return -1
        ans = 0
        for i in rep_val:
            ans += i // 3
            if i % 3 != 0:
                ans += 1
        return ans
