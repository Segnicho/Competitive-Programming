class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(len(nums))
        nums = list(set(nums))
        idx = {}

        for i, num in enumerate(nums):
            idx[num] = i
        st = set()
        for i, num in enumerate(nums):
            if num - 1 in st:
                uf.union(i, idx[num-1])
            if num + 1 in st:
                uf.union(i, idx[num+1])
            st.add(num)
        res = defaultdict(int)
        for i, num in enumerate(nums):
            root = uf.find(i)
            res[root] += 1
        return max(res.values()) if res else 0
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
    