class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)            
        
        mx = 0
        res = 0
        for node in graph:
            if len(graph[node]) > mx:
                mx = len(graph[node])
                res = node
        return res