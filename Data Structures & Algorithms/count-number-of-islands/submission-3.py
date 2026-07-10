class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return #return and not break because it is a function, if it was a loop then break or continue

            grid[r][c] = "0"

            for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                dfs(r+dr,c+dc)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands

        