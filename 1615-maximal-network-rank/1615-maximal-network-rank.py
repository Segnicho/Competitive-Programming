class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        
        for start, end in roads:
            graph[start].add(end)
            graph[end].add(start)
        
        ans = 0
        for node1 in graph:
            for node2 in graph:
                if node1 != node2:
                    rank = len(graph[node1]) + len(graph[node2])
                    if node1 in graph[node2]:
                        rank -= 1
                    ans = max(ans, rank)
        return ans
        