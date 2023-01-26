from itertools import chain

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat_mat = list(chain.from_iterable(mat))
        n = len(flat_mat)
        if r * c != n:
            return mat
        return [flat_mat[i*c: i*c+c] for i in range(r)]
