class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sm = sum(nums[:k])
        max_av = sm / k
        i = 0
        while i + k < n:
            sm -= nums[i]
            sm += nums[i+k]
            max_av = max(max_av, sm / k)
            i += 1
        return max_av
