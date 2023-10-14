class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        n = len(isConnected)
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    uf.union(i, j)
                    
        return uf.components
    
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1]* size
        self.components = size
    
    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return self.parent[node]
    def union(self, u, v):
        parentu = self.find(u)
        parentv = self.find(v) 
        if parentu == parentv: 
            return 0
        
        if self.rank[parentu] < self.rank[parentv]:
            self.parent[parentv] = parentu
            self.rank[parentu] += self.rank[parentv]
        else:
            self.parent[parentu] = parentv
            self.rank[parentv] += self.rank[parentu]
        self.components -= 1
        return 1