class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #track each pos visited, if visited i can skip because i know this island has been counted

        print(repr(grid[0][0])) 
        used = [[0] * len(grid[0]) for _ in range(len(grid))]
        count = 0
        def dfs(row, col):
            if row < 0 or row >= len(grid):
                return
            elif col < 0 or col >= len(grid[0]):
                return
            elif grid[row][col] == '0' or used[row][col] == 1:
                return
            used[row][col] = 1
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if used[row][col] == 1 or grid[row][col] == '0':
                    continue
                count += 1
                dfs(row, col)
        return count
                

        