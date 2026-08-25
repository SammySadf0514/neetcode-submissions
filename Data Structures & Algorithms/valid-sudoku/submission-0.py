class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            hash = set()
            for i in range(9):
                if board[row][i] in hash:
                    return False
                if board[row][i] == ".":
                    continue
                hash.add(board[row][i])
        
        for column in range(9):
            hash = set()
            for i in range(9):
                if board[i][column] in hash:
                    return False
                if board[i][column] == ".":
                    continue
                hash.add(board[i][column])

        for R in range(0, 9, 3):
            for C in range(0, 9, 3):
                hash = set()
                for row in range(3):
                    for col in range(3):
                        r = row + R
                        c = col + C
                        if board[r][c] in hash:
                            return False
                        if board[r][c] == ".":
                            continue
                        hash.add(board[r][c])
        return True