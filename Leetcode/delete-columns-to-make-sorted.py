class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        r = len(strs)
        c = len(strs[0])
        for i in range(c):
            for j in range(r-1):
                if strs[j][i] > strs[j+1][i]:
                    cnt += 1
                    break
        return cnt
