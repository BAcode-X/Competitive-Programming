class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            grid[i] = sorted(grid[i])
        ans = 0
        for i in range(m):
            m = 0
            for j in range(n):
                m = max(m, grid[j].pop())
            ans += m
        return ans
