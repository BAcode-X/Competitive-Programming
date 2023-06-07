class Solution:
    def countDigits(self, num: int) -> int:
        s = str(num)
        cnt = 0
        for val in s:
            if num % int(val) == 0:
                cnt += 1
        return cnt 
