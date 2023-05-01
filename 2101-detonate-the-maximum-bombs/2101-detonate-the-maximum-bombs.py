class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)
        calc_dis = lambda x, y: math.sqrt((x[0]-y[0]) ** 2 + (x[1]-y[1]) ** 2)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if bombs[i][2] >= calc_dis(bombs[i], bombs[j]):
                    graph[i].append(j)
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for el in graph[i]:
                dfs(el)
            return
        res = 1
        for i in range(len(bombs)):
            visited = set()
            dfs(i)
            res = max(res, len(visited))
        return res