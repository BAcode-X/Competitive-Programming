from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        a = [((i[0]**2 + i[1]**2)**0.5, i) for i in points]
        a.sort(key=lambda x:x[0])
        return [a[i][1] for i in range(k)]
