class Solution:
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        adjList = defaultdict(list)
        
        for i in range(len(graph)):
            adjList[i] = graph[i] 
        res = []
        
        def dfs(i, arr):
            arr.append(i)
            if i+1 == len(graph):
                res.append(arr[:])
                return
            for number in adjList[i]:
                dfs(number, arr)
                arr.pop()
        for number in adjList[0]:
            arr = [0]
            dfs(number, arr)
        return res
    
    
    
    