class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        mem = [[0 for _ in range(cols)] for _ in range(rows)]
        res = 0
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def dfs(i, j):
            if mem[i][j] != 0:
                return mem[i][j]
            
            for m in range(4):
                x, y = i + dx[m], j + dy[m]
                if 0 <= x < rows and 0 <= y < cols and matrix[x][y] > matrix[i][j]:
                    mem[i][j] = max(mem[i][j], dfs(x, y))
            
            mem[i][j] += 1
            return mem[i][j]
        
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j))
        
        return res