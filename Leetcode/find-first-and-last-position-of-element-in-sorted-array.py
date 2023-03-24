class Solution:

    def search(self, nums, target, mode):
        l, r = 0, len(nums) - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                ans = mid
                if mode == 'first':
                    r = mid - 1
                else:
                    l = mid + 1
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.search(nums, target, 'first')
        last = self.search(nums, target, 'last')
        return [first, last]
