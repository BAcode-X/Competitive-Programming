class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])
        tr = []
        for i in range(c):
            tmp = []
            for j in range(r):
                tmp.append(matrix[j][i])
            tr.append(tmp)
        return tr
