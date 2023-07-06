class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = []
        for i in range(0, n, 2):
            arr += [nums[i+1]]*nums[i]
        return arr
