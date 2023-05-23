class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        m = len(source)
        uf = UnionFind(m)
        
        for i, j in allowedSwaps:
            uf.union(i,j)
        
        hm = defaultdict(list)
        
        for i in range(m):
            hm[uf.find(i)].append(i)
        
        total = 0
        
        for x in hm.values():
            s = Counter()
            t = Counter()
            
            for i in x:
                s[source[i]] += 1
                t[target[i]] += 1
        
            final = s & t
            total += sum(final.values())
        return m - total
        
#         parent = defaultdict(int)
#         children = defaultdict(set)
        
#         for i in range(m):
#             root = uf.find(i)
#             children[root].add(source[i])
#             parent[i] = root
#         count = Counter(source)
#         cnt = 0
#         for i in range(m):            
#             if (target[i] != source[i] and target[i] not in children[parent[i]]) or ((target[i] ==source[i] or target[i] in children[parent[i]]) and count[target[i]] <= 0) :
#                 cnt += 1
#             if target[i] ==source[i] or target[i] in children[parent[i]]:
#                 count[target[i]] -= 1
#         return cnt
        
        
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
