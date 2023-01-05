class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        mi, mx = points[0][0], points[0][1]
        arrows = 1
        for point in points:
            if point[0] >= mi and point[0] <= mx:
                mi = max(point[0], mi)
                mx = min(point[1], mx)
            else:
                arrows += 1
                mi, mx = point[0], point[1]
        return arrows
