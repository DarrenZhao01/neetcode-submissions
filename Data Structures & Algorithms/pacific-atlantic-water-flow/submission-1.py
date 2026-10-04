# instead of checking every cell and see if it touches the pacific ocean, we check the edges and see with dfs if it is higher (stream).


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])

        pacific = [[False] * col for _ in range(row)]
        atlantic = [[False] * col for _ in range(row)]

        def dfs(x, y, ocean, value):
            if not ((0 <= x < row) and (0 <= y < col)):
                return
            
            if ocean[x][y] or heights[x][y] < value:
                return

            if ocean == pacific:
                pacific[x][y] = True
            else:
                atlantic[x][y] = True
            
            dfs(x + 1, y, ocean, heights[x][y])
            dfs(x - 1, y, ocean, heights[x][y])
            dfs(x, y + 1, ocean, heights[x][y])
            dfs(x, y - 1, ocean, heights[x][y])
        
        # top and bottom of the squares
        for c in range(col):
            dfs(0, c, pacific, heights[0][c])
            dfs(row - 1, c, atlantic, heights[row - 1][c])
        
        for r in range(row):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, col - 1, atlantic, heights[r][col - 1])
        
        res = []

        for r in range(row):
            for c in range(col):
                if pacific[r][c] == True and atlantic[r][c] == True:
                    res.append([r, c])
        
        return res


        

        

