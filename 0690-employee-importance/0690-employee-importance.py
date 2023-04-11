"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        adjList = defaultdict(list)
        
        importance = defaultdict()
        for employee in employees:
            # for iid, imp, arr in employee:
            importance[employee.id] = employee.importance
            
            adjList[employee.id] = employee.subordinates
        self.res = 0
        visited = set()
        def dfs(i):
            if i  in visited:
                return
            visited.add(i)
            self.res += importance[i]
            for number in adjList[i]:
                dfs(number)
        for num in adjList:
            if num == id and num not in visited:
                dfs(num)
                break
        return self.res
        