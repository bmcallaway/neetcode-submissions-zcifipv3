class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in board:
            for i in row:
                if(i.isdecimal() and i in seen):
                    print("1")
                    return False
                elif(i.isdecimal()):
                    seen.add(i)
            seen = set()
        seen = set()
        for c in range(len(board)):
            for r in range(len(board[0])):
                if(board[r][c].isdecimal() and board[r][c] in seen):
                    print("2")
                    return False
                elif(board[r][c].isdecimal()):
                    seen.add(board[r][c])
            seen = set()
        seen = set()
        #[0,0]   [0,3] [0,6]
        #[3,0].  [3,3] [3,6]
        coff = 0
        for i in range(3):
            for r in range(3):
                print("coff:",coff)
                for c in range(coff, coff+3):
                    print("board[r][coff] or board[",r,"][",c,"]: ",board[r][c])
                    if(board[r][c].isdecimal() and board[r][c] in seen):
                        return False
                    elif board[r][c].isdecimal():
                        seen.add(board[r][c])
            coff += 3
            seen = set()

        coff = 0
        for i in range(3):
            for r in range(3, 6):
                print("coff:",coff)
                for c in range(coff, coff+3):
                    print("board[r][coff] or board[",r,"][",c,"]: ",board[r][c])
                    if(board[r][c].isdecimal() and board[r][c] in seen):
                        return False
                    elif board[r][c].isdecimal():
                        seen.add(board[r][c])
            coff += 3
            seen = set()

        coff = 0
        for i in range(3):
            for r in range(6,9):
                print("coff:",coff)
                for c in range(coff, coff+3):
                    print("board[r][coff] or board[",r,"][",c,"]: ",board[r][c])
                    if(board[r][c].isdecimal() and board[r][c] in seen):
                        return False
                    elif board[r][c].isdecimal():
                        seen.add(board[r][c])
            coff += 3
            seen = set()
        return True
        