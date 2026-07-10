class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #every queen has to be in a different row, and different column
        #the diagonals are the tricky part
        #backtracking
        #negative diagonals pattern is R - C
        #positive diagonals pattern is R + C
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                #if column position in any of the 3 sets, skip it
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r + 1)

                #backtrack and clean up 
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res



        