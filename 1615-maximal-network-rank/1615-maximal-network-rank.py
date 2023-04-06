class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        
        for start, end in roads:
            graph[start].add(end)
            graph[end].add(start)
        
        ans = 0
        
        for i in range(n):
            for j in range(i+1, n):
                    rank = len(graph[i]) + len(graph[j])
                    if j in graph[i]:
                        rank -= 1
                    ans = max(ans, rank)
        return ans
        