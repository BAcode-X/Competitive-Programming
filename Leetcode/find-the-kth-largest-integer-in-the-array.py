from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums1 = [int(i) for i in nums]
        nums1.sort(reverse=True)
        return str(nums1[k-1])
