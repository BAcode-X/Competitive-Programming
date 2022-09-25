"""
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.
"""
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(list)
        for i, j in enumerate(nums):
            dic[j].append(i)
        for i in dic:
            x = target - i
            if x == i and len(dic[i]) > 1:
                return [dic[i][0], dic[i][1]]
            elif x != i and x in dic:
                return [dic[i][0], dic[x][0]]
