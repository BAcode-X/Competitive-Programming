class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        d = {intervals[i][0]: i for i in range(n)}
        starts = sorted(intervals, key=lambda x: x[0])
        ans = []
        for interval in intervals:
            end_time = interval[1]
            i, j = 0, n - 1
            min_start, min_start_index = float('inf'), -1
            
            while i <= j:
                mid = i + (j - i) // 2
                if starts[mid][0] >= end_time:
                    if starts[mid][0] < min_start:
                        min_start = starts[mid][0]
                        min_start_index = d[min_start]
                    j = mid - 1
                else:
                    i = mid + 1
            
            ans.append(min_start_index if min_start_index != -1 else -1)
        
        return ans
