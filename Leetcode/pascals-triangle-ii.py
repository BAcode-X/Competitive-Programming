class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        
        for i in range(2, rowIndex + 1):
            prev = 1
            for j in range(1, i):
                temp = row[j]
                row[j] = prev + row[j]
                prev = temp
        
        return row
