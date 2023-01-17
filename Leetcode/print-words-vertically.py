class Solution:
    def printVertically(self, s: str) -> List[str]:
        ss = s.split()
        mx = 0
        for i in ss:
            mx = max(mx, len(i))
        ans = []
        for i in range(mx):
            row = ''
            for j in ss:
                try:
                    row += j[i]
                except:
                    row += ' '
            ans.append(row.rstrip())
        return ans
