from itertools import chain

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            c = [board[j][i] for j in range(9) if board[j][i] != '.']
            if len(set(c)) != len(c):
                return False
            r = [board[i][j] for j in range(9) if board[i][j] != '.']
            if len(set(r)) != len(r):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                tmp = []
                for k in range(i, i+3):
                    for kk in range(j, j+3):
                        if board[k][kk] != '.':
                            tmp.append(board[k][kk])
                if len(set(tmp)) != len(tmp):
                    return False
        return True
