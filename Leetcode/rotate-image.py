class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(i, c):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i] = reversed(matrix[i])
