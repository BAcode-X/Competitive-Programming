from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        mon_stack = []

        for i in range(n):
            while mon_stack and temperatures[i] > temperatures[mon_stack[-1]]:
                j = mon_stack.pop()
                ans[j] = i - j
            mon_stack.append(i)
        
        return ans
        