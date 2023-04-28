from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        stack = []
        for i in nums2:
            while stack and stack[-1] < i:
                ans[stack.pop()] = i
            stack.append(i)
        return [ans.get(i, -1) for i in nums1]
