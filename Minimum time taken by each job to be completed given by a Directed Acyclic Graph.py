from typing import List


from typing import List
from collections import defaultdict

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        graph = defaultdict(list)
		visited = set()
		indegree  = defaultdict(int)
		for start, end in edges:
		    graph[start].append(end)
		    indegree[end] += 1
        
        level = []
        for i in range(1, n+1):
            if not indegree[i]:
                level.append(i)
        res = [0]*n
        i = 0
        while level:
            nxt = []
            i += 1
            for num in level:
                visited.add(num)
                res[num-1] = i
                for neigh in graph[num]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0 and neigh not in visited:
                        nxt.append(neigh)
            level = nxt
      
        return " ".join(str(r) for r in res)
#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends
