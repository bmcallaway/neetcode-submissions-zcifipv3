class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        maxArea = 0
        currMax = 0
        def dfs(pos):
            nonlocal currMax
            r, c = pos
            if grid[r][c] == 0:
                return
            grid[r][c] = 0
            currMax += 1
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                    dfs((row, col))
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    currMax = 0
                    dfs((row, col))
                    maxArea = max(maxArea, currMax)

        return maxArea