class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rLen, cLen = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        q = deque()

        for row in range(rLen):
            for col in range(cLen):
                if grid[row][col] == 0:
                    q.append((row, col))
        dist = 0
        while q:
            qLen = len(q)
            for _ in range(qLen):
                r, c = q.popleft()
                if grid[r][c] == 2147483647 or dist == 0:
                    grid[r][c] = dist
                    for dr, dc in directions:
                        row = r + dr
                        col = c + dc
                        if 0 <= row < rLen and 0 <= col < cLen:
                            q.append((row, col))
            dist += 1

        