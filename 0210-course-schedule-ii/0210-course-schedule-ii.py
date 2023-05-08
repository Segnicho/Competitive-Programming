class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        black = set()
        gray = set()
        stack = []
        cycle =False
        def dfs(node):
            nonlocal cycle
            if node in black:
                return
            if node in gray:
                cycle = True
                return
            gray.add(node)
            if node not in graph:
                stack.append(node)
                black.add(node)
                return
            for neigh in graph[node]:
                dfs(neigh)
            stack.append(node)            
            black.add(node)
        for i in range(numCourses):
            dfs(i)

        if cycle or len(stack) < numCourses:
            return []
        stack.reverse()
        return stack
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        # print(graph, q)
        while q:
            curr = q.popleft()
            res.append(curr)
            for num in graph[curr]:
                if indegree[num] == 1:
                    q.append(num)
                indegree[num] -= 1
        for ky, val in indegree.items():
            if val > 0:
                return []
        return res