from collections import deque

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums = deque(nums)
        tmp = []
        n = len(nums)
        i = 0
        while i < n:
            if i % 2 == 0:
                tmp.append(nums.pop())
            else:
                tmp.append(nums.popleft())
            i += 1
        return tmp
