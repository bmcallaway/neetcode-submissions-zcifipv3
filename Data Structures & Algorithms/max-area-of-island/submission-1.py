class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        used = [[0] * len(grid[0]) for _ in range(len(grid))]
        maxArea = 0
        currMax = 0

        def dfs(row, col):
            nonlocal currMax
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            if used[row][col] == 1 or grid[row][col] == 0:
                return
            used[row][col] = 1
            currMax += 1
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                currMax = 0
                dfs(row, col)
                maxArea = max(maxArea, currMax)
                #currMax = 0

        return maxArea