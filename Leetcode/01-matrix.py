class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat

        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = []

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')
        while queue:
            row, col = queue.pop(0)
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] > mat[row][col] + 1:
                    mat[nr][nc] = mat[row][col] + 1
                    queue.append((nr, nc))
        return mat
