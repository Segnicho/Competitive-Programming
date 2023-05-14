class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        arr = []
        for u, v in adjacentPairs:
            arr.append(u)
            arr.append(v)
            graph[u].append(v)
            graph[v].append(u)          
        count = Counter(arr)
        root = adjacentPairs
        for num in count:
            if count[num] == 1:
                root = num
                break
        
        res = []
        visited = set()
        def dfs(i):
            visited.add(i)
            res.append(i)
            for num in graph[i]:
                if num not in  visited:
                    dfs(num)
        dfs(root)
        return res