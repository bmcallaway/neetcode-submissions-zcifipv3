class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque()

        time = 0
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))
        
        while q:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1

        return time - 1 if time > 0 else 0