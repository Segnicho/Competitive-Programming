class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        path = set()
        def outOfBound(i, j):
            return i < 0 or i >= m or j < 0 or j >= n
        def dfs(r, c, i):
            if i == len(word):
                return True
            if outOfBound(r, c) or word[i] != board[r][c] or (r, c) in path:
                return False
            path.add((r, c))
            res = dfs(r+1, c, i + 1) or \
                dfs(r-1, c, i + 1) or \
                dfs(r, c+1, i + 1) or \
                dfs(r, c-1, i + 1)
                
            path.remove((r,c))
            return res
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                        return True
        return False