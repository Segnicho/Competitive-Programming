class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        
        adjList = defaultdict(set)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row != col and grid[row][col] == 1:
                    adjList[row].add(col)
                    adjList[col].add(row)
                elif row == col:
                    adjList[row].add(col)        
        visited = set()
        res = 0
        def dfs(i):
            if i  in visited:
                return
            visited.add(i)
            for number in adjList[i]:
                dfs(number)
        
        for num in adjList:
            if num not in visited:
                dfs(num)
                res += 1
        return res