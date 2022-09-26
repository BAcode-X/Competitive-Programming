class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        n = len(s)
        ans = ['' for i in range(n)]
        for i in range(n):
            ans[int(s[i][-1])-1] = s[i][:-1]
        return ' '.join(ans)