class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        used = [[False] * len(board[0]) for _ in range(len(board))]
        print(used)
        def dfs(i, j, pos):
            if pos == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
                print("1")

                return False

            if used[i][j]:
                print("2")

                return False
            if board[i][j] != word[pos]:
                print("3")
                return False
            used[i][j] = True
            val = dfs(i+1,j,pos+1) or dfs(i-1,j,pos+1) or dfs(i,j+1,pos+1) or dfs(i,j-1,pos+1)
            used[i][j] = False
            return val
        
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if dfs(i, j, 0):
                    return True
        
        return False