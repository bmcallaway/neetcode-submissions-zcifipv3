class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = set()
        for row in board:
            for entry in row:
                if entry.isnumeric():
                    if entry in rowSet:
                        return False
                    rowSet.add(entry)
            rowSet.clear()

        colSet = set()
        for col in range(len(board)):
            for row in range(len(board[0])):
                if board[row][col].isnumeric():
                    if board[row][col] in colSet:
                        return False
                    colSet.add(board[row][col])
            colSet.clear()

        groupSet = set()
        y = 0
        for i in range(3):
            x = 0
            for i in range(3):
                for row in board[y:y+3]:
                    for col in row[x:x+3]:
                        if(col.isnumeric()):
                            if col in groupSet:
                                return False
                            groupSet.add(col)
                groupSet.clear()
                x += 3   
            y += 3 

        return True

