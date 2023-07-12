class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)
        def getHD(arr):
            s1 =Counter(source[i] for i in arr)
            s2 =Counter(target[i] for i in arr)
            return sum(val for val in (s1-s2).values())
        for i, j in allowedSwaps:
            uf.union(i, j)
        group = defaultdict(list)
        for i in range(n):
            group[uf.find(i)].append(i)
        return sum(getHD(v) for v in group.values())
            
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
    def find(self, u):
        if self.root[u] == u:
            return u
        self.root[u] = self.find(self.root[u])
        return self.root[u]
    
    def union(self, u, v):
        rootu = self.find(u)
        rootv = self.find(v)
        if rootu == rootv:
            self.ans = [u+1, v+1]
        if rootu != rootv:
            if self.rank[rootu] > self.rank[rootv]:
                self.root[rootv] = rootu
            elif self.rank[rootv] > self.rank[rootu]:
                self.root[rootu] = rootv
            else:
                self.root[rootu] = rootv
                self.rank[rootv] += 1
        