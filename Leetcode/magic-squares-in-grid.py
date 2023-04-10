class Solution:
    def checkSubGrid(self, grid, x, y):
        a = []
        for i in range(-1, 2):
            a += grid[x+i][y-1:y+2]
        a.sort()
        if a != list(range(1, 10)):
            return False
        s = sum(grid[x][y-1:y+2])
        if sum(grid[x-1][y-1:y+2]) != s:
            return False
        if sum(grid[x+1][y-1:y+2]) != s:
            return False
        for i in range(-1, 2):
            t = 0
            for j in range(-1, 2):
                t += grid[x+j][y+i]
            if t != s:
                return False
        if (grid[x-1][y-1] + grid[x][y] + grid[x+1][y+1]) != s:
            return False
        if (grid[x-1][y+1] + grid[x][y] + grid[x+1][y-1]) != s:
            return False
        return True
        
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        cnt = 0
        for i in range(1, r-1):
            for j in range(1, c-1):
                if self.checkSubGrid(grid, i, j):
                    cnt += 1
        return cnt
