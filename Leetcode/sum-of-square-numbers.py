class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(c ** 0.5) + 1
        flag = False
        l, r = 0, n
        while l <= r and not flag:
            v = l**2 + r**2
            if v > c:
                r -= 1
            elif v < c:
                l += 1
            else:
                flag = True
        return flag
