class Solution:
    def get_max(self, grid, x, y):
        m = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                try:
                    m = max(grid[x+i][y+j], m)
                except:
                    pass
        return m

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        ans = []
        for i in range(1, r - 1):
            tmp = []
            for j in range(1, c - 1):
                tmp.append(self.get_max(grid, i, j))
            ans.append(tmp)
        return ans
