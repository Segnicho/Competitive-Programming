class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])            
        q = [[-1, start_node]]
        res = math.inf
        visited = set()
        while q:
            prob,  node = heappop(q)
            prob *= -1
            if node in visited:
                continue
            if node == end_node:
                return prob
            visited.add(node)
            for neigh, weigh in graph[node]:
                    heappush(q, [prob*weigh*-1, neigh])
        return 0