class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        freshFruit = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    freshFruit += 1
        print("fresh: ", freshFruit)
        time = 0
        while q:
            length = len(q)
            time += 1
            for _ in range(length):
                fruit = q.popleft()
                row = fruit[0]
                col = fruit[1]
                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    grid[row - 1][col] = 2
                    q.append((row - 1, col))
                    freshFruit -= 1
                if row + 1 < len(grid) and grid[row + 1][col] == 1:
                    grid[row + 1][col] = 2
                    q.append((row + 1, col))
                    freshFruit -= 1
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    grid[row][col - 1] = 2
                    q.append((row, col - 1))
                    freshFruit -= 1
                if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
                    grid[row][col + 1] = 2
                    q.append((row, col + 1))
                    freshFruit -= 1

        print(freshFruit)
        if freshFruit > 0:
            return -1
        return time - 1 if time > 0 else 0
                
        
                