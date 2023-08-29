class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(list)
        indegree = [0]*n
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            indegree[i] += 1
            indegree[j] += 1
        level = []
        visited = set()
        for num in range(n):
            if indegree[num] == 1:
                level.append(num)
                visited.add(num)
        res = level[:]
        while level:
            newLevel = []
            for i in range(len(level)):
                node = level.pop()
                visited.add(node)
                for neigh in graph[node]:
                    if neigh not in visited:
                        indegree[neigh] -= 1
                        if indegree[neigh] == 1:
                            newLevel.append(neigh)
            if len(newLevel) > 0:
                res = newLevel[:]
            level = newLevel            
        return res