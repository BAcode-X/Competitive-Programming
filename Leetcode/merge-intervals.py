from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        mi, ma = intervals[0]
        ans = []
        for i in intervals:
            if ma >= i[0]:
                ma = max(i[1], ma)
            else:
                ans.append([mi, ma])
                mi, ma = i[0], max(i[1], ma)
        ans.append([mi, ma])
        return ans
