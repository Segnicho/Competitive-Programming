class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        uf = UnionFind(n)
        
        for i in range(n):
            c1 = ord(s1[i]) - ord("a")
            c2 = ord(s2[i]) - ord("a")
            uf.union(c1, c2)
        
        parent = (uf.parent)
        res = ""
        for c in baseStr:
            root = uf.find(ord(c)-ord("a"))
            for i in range(26):
                connected = uf.find(i)
                if connected == root:
                    res += chr(ord("a")+i)
                    break
        return res
        
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(26)]
        self.rank  = [1 for i in range(26)]
    
    def find(self, u):
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return self.parent[u]
    
    def union(self, u, v):
        parentu = self.find(u)
        parentv = self.find(v)
        
        if self.rank[parentu] < self.rank[parentv]:
            self.parent[parentu] = parentv
            self.rank[parentu] += self.rank[parentv]
        else:
            self.parent[parentu] = parentv
            self.rank[parentu] += self.rank[parentv]
            