# bfs solution
# go through the entire array and find the rotting fruit
# run the rotting fruit bfs
# for each direction, if new x and new y is a 1 and within bounds, and add it to the queue. rot the current one.
# we need to get the length of the additions so that we can count by the "minute"

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        minutes = 0
        fresh = 0
        queue = []
        savedX, savedY = 0, 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
                    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# [(1,3), (1, 1)]
# minutes: 1
        while fresh > 0 and queue:
            length = len(queue)
            for i in range(length):
                tx, ty = queue.pop(0)
            
                for dx, dy in directions:
                    nx, ny = dx + tx, dy + ty
                    if (0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1):
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh -= 1
            
            minutes += 1


        return minutes if fresh == 0 else -1