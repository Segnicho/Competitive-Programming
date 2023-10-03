class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        q = [[0, (0, 0)]]
        directions = [(1, 0), (0, 1),(0, -1), (-1, 0)]
        visited = set()
        
        def inbound(x, y):
            return 0<=x<m and 0<=y<n
        
        while q:
            dist, cell = heappop(q)
            if cell in visited:
                continue
            visited.add(cell)
            if cell == (m-1, n-1):
                return dist
            for i, j in directions:
                x, y = cell[0]+i, cell[1]+j
                if inbound(x, y):
                    diff = abs(heights[x][y] -heights[cell[0]][cell[1]])
                    heappush(q, [max(dist, diff), (x, y)])