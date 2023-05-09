class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
     
        nums = set()
        for i, j in prerequisites:
            nums.add(i)
            nums.add(j)
            
        res =[]
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        indegree = Counter()
        
        q = deque()
        seen = set()
        for ky, val in graph.items():
            ky not in seen and q.append(ky) 
            for num in val:
                seen.add(num)
                indegree[num] += 1
                if num in q:
                    q.remove(num)
        for i in range(numCourses):
            if i not in nums:
                q.append(i)
        while q:
            curr = q.popleft()
            res.append(curr)
            for num in graph[curr]:
                if indegree[num] == 1:
                    q.append(num)
                indegree[num] -= 1
        for ky, val in indegree.items():
            if val > 0:
                return False
        return True