class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        r, c = len(matrix), len(matrix[0])
        ans = []
        while i < r and j < c:
            for row in range(j, c):
                ans.append(matrix[i][row])
            i += 1
            for col in range(i, r):
                ans.append(matrix[col][c-1])
            c -= 1
            if i < r:
                for col in range(c-1, j-1, -1):
                    ans.append(matrix[r-1][col])
                r -= 1
            if j < c:
                for row in range(r-1, i-1, -1):
                    ans.append(matrix[row][j])
                j += 1
        return ans
