class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        tot = 0
        n = len(costs)
        a = [[ac-bc, idx] for idx, [ac, bc] in enumerate(costs)]
        a.sort()
        l = 0
        for l in range(n//2):
            tot += costs[a[l][1]][0]
        l+=1
        for i in range(l, n):
            tot += costs[a[i][1]][1]
        return tot