class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # get neighbour of a specific node
        def getNeigh(node):
            res = []                
            for i, num in enumerate(node):
                num = int(num)
                left = ""
                right = ""
                if num == 0:
                    left = node[:i] + "1" + node[i+1:]
                    right = node[:i] + "9" + node[i+1:]
                elif num == 9:
                    left = node[:i] + "8" + node[i+1:]
                    right = node[:i] + "0" + node[i+1:]
                else:
                    left = node[:i] +  str(num-1) + node[i+1:]
                    right = node[:i] + str(num+1) + node[i+1:]
                res.append(left)
                res.append(right)
            return res
        q = deque()
        if "0000" in set(deadends):
            return -1
        if target == "0000":
            return 0
        node = "0000"
        q.append((node, 0))
        visited = set()
        while q:
            node, dis = q.popleft()
            neighbours  = getNeigh(node)
            for neigh in  neighbours:
                if neigh not in visited and neigh not in set(deadends):
                    q.append((neigh, dis + 1))
                    visited.add(neigh)
                if neigh == target:
                    return dis +1 
        return -1
        
        