class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited = set()
        n =len(grid)
        q = deque()
        directions = [(-1, 0), (0,-1), (0, 1), (1, 0)]
        st = set()
        
        def inbound(i, j):
            return 0 <= i < n and 0 <= j < n
        def dfs(i, j):
            if (i, j) in visited:
                return
            visited.add((i, j))
            q.append((i, j, 0))
            for x, y in directions:
                rw, col = i + x, y + j
                if inbound(rw, col) and grid[rw][col]== 1:
                    dfs(rw, col)
        
        for i in range(n):
            flag = False
            for j in range(n):
                # visited = set()
                if grid[i][j] == 1:
                    flag = True
                    dfs(i, j)
                    break
            if flag:
                break
        while q:
            for _ in range(len(q)):
                i, j, dis = q.popleft()
                visited.add((i, j))   
                for x, y in directions:
                    r = i + x
                    c = j + y
                    if inbound(r, c)  and (r, c) not in visited:
                        if grid[r][c] == 1:
                            return dis
                        q.append([r, c, dis+1])
                        visited.add((r, c))   
                        
        # return res
                                
                                
                                    