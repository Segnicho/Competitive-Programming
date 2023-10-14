class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjList = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]:
                    adjList[i].append(j)
                    adjList[j].append(i)  
        
        visited = [0]*(n)     
        components = 0
        for node in range(n):
            if not visited[node]:
                components += 1
                self.dfs(node, -1, visited, adjList)
            
        return components     
    
    def dfs(self,node, parent, visited, adjList):
        visited[node] += 1
        for neigh in adjList[node]:
            if not visited[neigh] and neigh != parent:
                self.dfs(neigh,node, visited, adjList)
