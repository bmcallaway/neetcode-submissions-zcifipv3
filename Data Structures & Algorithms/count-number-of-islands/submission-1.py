class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        seen = [[0] * len(grid[0]) for _ in range(len(grid))]

        count = 0

        def dfs(pos):
            r, c = pos
            if grid[r][c] == '0' or seen[r][c] == 1:
                return
            seen[r][c] = 1    
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                    dfs((row, col))
            

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and seen[row][col] == 0:
                    count += 1   
                    dfs((row, col))

        return count