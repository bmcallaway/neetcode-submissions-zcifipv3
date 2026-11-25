class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        

        count = 0

        def dfs(pos):
            r, c = pos
            if grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                    dfs((row, col))
            

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1   
                    dfs((row, col))

        return count