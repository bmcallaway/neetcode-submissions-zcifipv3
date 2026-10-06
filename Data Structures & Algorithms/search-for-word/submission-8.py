class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        height = len(board)
        width = len(board[0])

        used = []
        for _ in range(len(board)):
            used.append([False] * len(board[0]))
        
        def dfs(row, col, pos):
            nonlocal res
            if pos >= len(word):
                res = True
                return
            if row < 0 or row >= height or col < 0 or col >= width or board[row][col] != word[pos] or used[row][col] == True:
                return
            used[row][col] = True
            dfs(row - 1, col, pos + 1)
            dfs(row + 1, col, pos + 1)
            dfs(row, col - 1, pos + 1)
            dfs(row, col + 1, pos + 1)
            used[row][col] = False


        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, 0)
        
        return res