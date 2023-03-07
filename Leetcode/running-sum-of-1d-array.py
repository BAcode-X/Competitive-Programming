class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        prev = nums[0]
        for i in nums[1:]:
            prev += i
            ans.append(prev)
        return ans
