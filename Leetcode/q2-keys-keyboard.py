class Solution:
    def minSteps(self, n: int) -> int:
        copy = 0
        cnt = 0
        i = 1
        while i < n:
            if n % i == 0:
                copy = i
                cnt += 1
            i += copy
            cnt += 1
        return cnt
