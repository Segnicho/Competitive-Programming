class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        
        for i, j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
            
        q = deque()
        for num in range(numCourses):
            if indegree[num] == 0:
                q.append(num)
                
        while q:
            node = q.popleft()
            numCourses -= 1
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return numCourses == 0
    