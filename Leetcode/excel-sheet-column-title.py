class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        
        while columnNumber > 0:
            columnNumber -= 1
            q = columnNumber // 26
            r = columnNumber % 26
            ans.append(chr(65 + r))
            columnNumber = q
        return ''.join(ans[::-1])
