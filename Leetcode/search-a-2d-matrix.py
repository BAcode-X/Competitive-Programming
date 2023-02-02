class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        flag = False
        for i in range(r):
            if matrix[i][0] <= target and target <= matrix[i][-1]:
                for num in matrix[i]:
                    if num == target:
                        flag = True
                        break
                break
            
        return flag
