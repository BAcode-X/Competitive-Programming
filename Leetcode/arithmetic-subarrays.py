from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        ans = []
        for i in range(m):
            flag = True
            arr = nums[l[i]:r[i]+1]
            arr.sort()
            prev = None
            for j in range(1, len(arr)):
                if prev is None:
                    prev = abs(arr[j-1] - arr[j])
                else:
                    if prev != abs(arr[j-1] - arr[j]):
                        flag = False
                        break
            if flag:
                ans.append(True)
            else:
                ans.append(False)
        return ans
