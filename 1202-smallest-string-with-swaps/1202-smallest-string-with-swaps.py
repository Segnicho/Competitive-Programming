class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        res = []
        for i, j in pairs:
            uf.union(i, j)
        
        group = defaultdict(list)
        for i, c in enumerate(s):
            lead = uf.find(i)
            group[lead].append(c)
        for ky, val in group.items():
            val.sort(reverse=True)
        for i, c in enumerate(s):
            lead = uf.find(i)
            letter = group[lead].pop()
            res.append(letter)
        return "".join(res)
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
        