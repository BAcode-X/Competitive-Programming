from collections import Counter

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        set_list = [set(i) for i in words]
        str_list = [''.join(sorted(i)) for i in set_list]
        rep = Counter(str_list)
        vals = rep.values()
        ans = 0
        for i in vals:
            ans += (i*(i-1))//2
        return ans
