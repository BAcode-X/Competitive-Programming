class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = []
        cnt = 0
        n = len(nums)
        i = 0
        while i < n-1:
            if nums[i] == 0:
                cnt += 1
            elif nums[i] == nums[i+1]:
                ans.append(nums[i]*2)
                cnt += 1
                i += 1
            else:
                ans.append(nums[i])
            i += 1
        if i < n:
            ans.append(nums[-1])
        ans = ans + [0]*cnt
        return ans
