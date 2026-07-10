class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs
        #iterate through rows and cols, see if there is a 1
        #then go through using dfs changing any touching tiles that are 1 also to 0
        #count that as 1 island
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            #base case
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == "0"):
                return

            grid[r][c] = "0" #turn visited tile to 0

            for dr, dc in directions:
                dfs(r + dr, c + dc)

            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # print("island found")
                    dfs(r,c)
                    islands+=1

        return islands