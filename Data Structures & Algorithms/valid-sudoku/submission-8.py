class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for row in board:
            seen.clear()
            for entry in row:
                if entry.isnumeric():
                    if int(entry) < 1 or int(entry) > 9 or entry in seen:
                        return False
                    seen.add(entry)
        for c in range(len(board)):
            seen.clear()
            for r in range(len(board)):
                if board[r][c].isnumeric():
                    if int(board[r][c]) < 1 or int(board[r][c]) > 9 or board[r][c] in seen:
                        return False
                    seen.add(board[r][c])

        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                seen.clear()
                for row in board[i:i+3]:
                    for val in row[j:j+3]:
                        if val in seen:
                            return False
                        if val.isnumeric():
                            seen.add(val)

        return True