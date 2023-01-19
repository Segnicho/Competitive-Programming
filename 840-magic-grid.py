class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        def checkMagic(board, i, j):
            arr = [board[i-1][j-1] , board[i-1][j],  board[i-1][j+1],
            board[i+1][j-1] , board[i+1][j] , board[i+1][j+1],
            board[i][j-1], board[i][j], board[i][j+1]
            ]
            for num in arr:
                if not 1<=num<=9:
                    return False
            if len(Counter(arr))< 9:
                return False
            rw1 = board[i-1][j-1] + board[i-1][j] + board[i-1][j+1] 
            rw3 = board[i+1][j-1] + board[i+1][j] + board[i+1][j+1] 

            col1 = board[i-1][j-1] + board[i][j-1] + board[i+1][j-1] 
            col3 = board[i-1][j+1] + board[i][j+1] + board[i+1][j+1] 

            up = board[i][j] + board[i][j-1] + board[i][j+1] 
            hor = board[i][j] + board[i-1][j] + board[i+1][j]
            dleft = board[i-1][j-1] + board[i][j] + board[i+1][j+1]
            dright = board[i-1][j+1] + board[i][j] + board[i+1][j-1]
            if rw1 == hor and rw1 == rw3  and col1 == up and col1 == col3 and rw1 == col1 and dleft == dright and rw1 == dleft:

            # if (up == hor) and (up == dleft) and (up == dright) and rw1 == rw3 and col1     ==  col3 and up == rw1 and up == col1 and rw1 == col1:
                return True
            return False
        for i in range(1, n-1):
            for j in range(1, m-1):
                if checkMagic(grid, i, j):
                    res+=1
        return res


        
