class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(board), len(board[0])
        def inbound(i, j):
            return 0 <= i < m and  0 <= j < n 
        visited = set()
        def dfs(i, j):
            if (i, j) in visited or board[i][j] == "X":
                    return
            visited.add((i, j))
            for x, y in directions:
                rw , col = i + x, y + j
                if inbound(rw, col): 
                    dfs(rw, col)
        
        for i in range(m):
            dfs(i,0)
            dfs(i, n-1)
        for i in range(n):
            dfs(0, i)
            dfs(m-1,i)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j]  = "X"
                if (i, j) in visited:
                    board[i][j] = "O"
                
                    