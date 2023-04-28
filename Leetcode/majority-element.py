class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        prev = [nums[0], 1]
        prev_num = nums[0]
        cnt = 1
        for ind in range(1, n):
            if nums[ind] == prev_num:
                cnt += 1
            else:
                if cnt > prev[1]:
                    prev = [prev_num, cnt]
                prev_num = nums[ind]
                if ind != n-1:
                    cnt = 1
        if cnt > prev[1]:
            prev = [nums[ind-1], cnt]
        return prev[0]
