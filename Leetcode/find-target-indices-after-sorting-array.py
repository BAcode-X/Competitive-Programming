from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        v = 0
        while True:
            try:
                x = nums.index(target, v)
                ans.append(x)
                v = x + 1
            except:
                break
        return ans