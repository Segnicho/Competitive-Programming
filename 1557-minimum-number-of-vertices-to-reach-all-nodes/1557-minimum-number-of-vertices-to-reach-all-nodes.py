class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        indegree = [0]*n
        for start, end in edges:
            indegree[end] += 1
        for node in range(n):
            if indegree[node] ==0 :
                res.append(node)
        return res