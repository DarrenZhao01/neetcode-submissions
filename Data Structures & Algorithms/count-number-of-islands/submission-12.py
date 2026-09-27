# when we hit a 1, we check if it is in a seen. if not, we can start BFS.
# during BFS, we need to check if the direction we go in is valid and if it is a one, and if it is, we add it to the queue
# after we return from the bfs, we can mark it as one island and then continue, checking if it is seen or a 1.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set() # coords
        n_rows = len(grid)
        n_cols = len(grid[0])

        res = 0

        def bfs(x_coord, y_coord):
            queue = [(x_coord, y_coord)]
            seen.add((x_coord, y_coord))
            
            while queue:
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                
                for x_move, y_move in directions:
                    nr = queue[0][0] + x_move
                    nc = queue[0][1] + y_move
                    if (0 <= nr < n_rows) and (0 <= nc < n_cols) and grid[nr][nc] == '1' and (nr, nc) not in seen:
                        queue.append((nr, nc))
                        seen.add((nr, nc))
                queue.pop(0)

        for row in range(n_rows):
            for col in range(n_cols):
                if (row, col) not in seen and grid[row][col] == '1':
                    bfs(row, col)
                    res += 1

        return res