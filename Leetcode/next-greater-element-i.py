from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = {i: -1 for i in nums2}
        n = len(nums2)
        for i in range(n):
            for j in range(i + 1, n):
                if nums2[j] > nums2[i]:
                    a[nums2[i]] = nums2[j]
                    break
        return [a[i] for i in nums1]
