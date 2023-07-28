class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return max(nums)

        max_money = [0] * (n)
        
        max_money[0] = nums[0]
        max_money[1] = nums[1]
        max_money[2] = max(nums[0] + nums[2], nums[1])

        for i in range(3, n):
            max_money[i] = max(max_money[i-2], max_money[i-3]) + nums[i]
        
        return max(max_money)
