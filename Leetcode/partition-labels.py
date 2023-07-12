class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        occ = {}
        for i in range(n):
            occ[s[i]] = i
        
        ans = []
        cur = 0
        ind = 0
        for i in range(n):
            ind = max(ind, occ[s[i]])
            if i == ind:
                ans.append(i - cur + 1)
                cur = i + 1
        return ans
