from itertools import accumulate

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        prefLR = [0]+list(accumulate(nums))[:-1]
        prefRL = [0]+list(accumulate(nums[::-1]))[:-1]
        prefRL = prefRL[::-1]
        ans = []
        for i in range(len(nums)):
            ans.append(abs(prefRL[i]-prefLR[i]))
        return ans
