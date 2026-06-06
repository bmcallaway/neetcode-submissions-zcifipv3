class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        used = []
        for _ in range(row):
            used.append([False] * col)

        def dfs(i, j, pos):
            if pos >= len(word):
                return True
            if i < 0 or i >= row or j < 0 or j >= col:
                return False
            if used[i][j]:
                return False
            if board[i][j] == word[pos]:
                used[i][j] = True
                valid = dfs(i + 1, j, pos + 1) or dfs(i - 1, j, pos + 1) or dfs(i, j+1, pos+1) or dfs(i, j-1, pos+1)
                used[i][j] = False

                return valid
            else:
                return False

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
                
        return False