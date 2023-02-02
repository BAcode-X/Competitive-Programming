from collections import defaultdict

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        r, c = len(matrix), len(matrix[0])
        flag = True
        d = defaultdict(bool)
        for i in range(r):
            if not flag:
                break
            for j in range(c):
                if d[j-i] is False:
                    d[j-i] = matrix[i][j]
                else:
                    if matrix[i][j] != d[j-i]:
                        flag = False
                        break
        return flag
