class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        uf  = UnionFind(n)
        for city1, city2, dis in roads:
            uf.union(city1-1, city2-1)
            
        mn = float("inf")
        for city1, city2, dis in roads:
            if  uf.find(city1-1) == uf.find(0):
                mn = min(mn, dis)
        return mn

        
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    

    def union(self, x, y):
        
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1