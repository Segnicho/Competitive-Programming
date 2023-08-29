class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0]*numCourses
        graph = defaultdict(list)
        res = []
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        q = deque()
        for num in range(numCourses):
            if indegree[num] == 0:
                q.append(num)
                
        while q:
            node = q.popleft()
            res.append(node)
            numCourses -= 1
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return res if numCourses == 0 else []