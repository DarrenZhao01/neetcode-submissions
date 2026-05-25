class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        num_rows = len(grid)
        num_cols = len(grid[0])

        seen = set()

        islands = 0

        def bfs(r, c):
            queue = deque()
            seen.add((r, c))
            queue.append((r, c))

            while queue:
                row, col = queue.pop()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                
                for dr, dc in directions:
                    if ((row + dr) in range(num_rows) and (col + dc) in range(num_cols) and grid[row + dr][col + dc] == "1" and 
                        (row + dr, col + dc) not in seen):
                        queue.append((row + dr, col + dc))

                        seen.add((row + dr, col + dc))

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    islands += 1
        
        return islands