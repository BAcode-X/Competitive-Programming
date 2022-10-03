from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        ans = ''
        for i in range(n):
            m = nums[0]
            for j in nums:
                if int(str(j) + str(m)) > int(str(m) + str(j)):
                    m = j
            ans += str(m)
            nums.remove(m)
        return str(int(ans))
