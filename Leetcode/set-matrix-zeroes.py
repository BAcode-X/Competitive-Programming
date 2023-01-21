from collections import defaultdict

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        rows = defaultdict(int)
        cols = defaultdict(int)
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1
        for i in range(row):
            for j in range(col):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
