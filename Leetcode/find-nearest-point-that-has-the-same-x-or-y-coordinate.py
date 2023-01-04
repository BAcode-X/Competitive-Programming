class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valids = [i for i in points if i[0] == x or i[1] == y]
        min_d = float('inf')
        ind = -1
        for i in valids:
            if min_d > (abs(x - i[0]) + abs(y- i[1])):
                min_d = (abs(x - i[0]) + abs(y - i[1]))
                ind = points.index(i)
        return ind
