class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        res = [0]*n
        graph = defaultdict(list)
        labelsCounter = defaultdict(int)
        visited = set()
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        def dfs(start):
            visited.add(start)
            res[start] -= labelsCounter[labels[start]]
            labelsCounter[labels[start]] += 1
            
            for neigh in graph[start]:
                if not neigh in visited:
                    dfs(neigh)
            
            resU = res[start]
            res[start] += labelsCounter[labels[start]]
            if resU >= 0:
                labelsCounter[labels[start]] -= 1
        
        dfs(0)
        return res