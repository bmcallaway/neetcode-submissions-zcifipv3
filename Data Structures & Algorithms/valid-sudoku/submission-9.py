class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for rows in board:
            for col in rows:
                if col == ".":
                    continue
                if col in seen or int(col)>9 or int(col)<0:
                    return False
                seen.add(col)
            seen.clear()

        for c in range(len(board[0])):
            for r in range(len(board)):
                entry = board[r][c]
                if entry == ".":
                    continue
                if entry in seen or int(entry)>9 or int(entry)<0:
                    return False
                seen.add(entry)
            seen.clear()

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for row in board[i:i+3]:
                    for col in row[j:j+3]:
                        if col == ".":
                            continue
                        if col in seen or int(col)>9 or int(col)<0:
                            print(col)
                            return False
                        seen.add(col)
                seen.clear()

        return True
