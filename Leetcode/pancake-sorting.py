from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        end = len(arr)
        tmp = arr[:]
        tmp.sort()
        ans = []
        while tmp != arr:
            m = max(arr[:end])
            i = arr.index(m)
            ans.append(i+1)
            arr = arr[:i+1][::-1] + arr[i+1:]
            ans.append(end)
            arr = arr[:end][::-1] + arr[end:]
            end -= 1
        return ans
