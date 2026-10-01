class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        max_area = 0

        def bfs(row, col):
            queue = [(row, col)]
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            curr_area = 1
            seen.add((row, col))
            while queue:
                curr = queue.pop(0)
                for direction in directions:
                    nx, ny = curr[0] + direction[0], curr[1] + direction[1]
                    if (0 <= nx < rows) and (0 <= ny < cols) and grid[nx][ny] == 1 and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        curr_area += 1
                        queue.append((nx, ny))
                
            return curr_area

        
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in seen and grid[i][j] == 1:
                    max_area = max(bfs(i, j), max_area)


        return max_area