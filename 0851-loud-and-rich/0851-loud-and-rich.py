class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        res = [0] * n
        graph = defaultdict(list)
        for rich, poor in richer:
            graph[poor].append(rich)
        
        def dfs(i):
            if res[i]:
                return res[i]
            res[i] = i 
            for nei in graph[i]:
                to = dfs(nei)
                if quiet[res[to]] < quiet[res[i]]:
                    res[i] = res[nei]
            return res[i]
        for i in range(n):
            dfs(i)
        return res
