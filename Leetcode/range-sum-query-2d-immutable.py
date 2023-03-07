class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r, c = len(matrix), len(matrix[0])
        self.prefix = [[0]*(c+1) for i in range(r+1)]
        for i in range(1, r+1):
            for j in range(1, c+1):
                prev_col = self.prefix[i][j-1]
                prev_row = self.prefix[i-1][j]
                prev_diag = self.prefix[i-1][j-1]
                self.prefix[i][j] = prev_row + prev_col + matrix[i-1][j-1] - prev_diag

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        right_top = self.prefix[row1][col2+1]
        left_bottom = self.prefix[row2+1][col1]
        prev_diag = self.prefix[row1][col1]
        return self.prefix[row2+1][col2+1] - right_top - left_bottom + prev_diag
