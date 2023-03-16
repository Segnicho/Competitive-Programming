class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []
        def backTracking(i = 1, temp= []):
            if sum(temp) == n and len(temp) == k:
                res.append(temp[:])    
                return
            for index in range(i, n):    
                if sum(temp) + index > n or index > 9:
                    break
                temp.append(index)
                backTracking(index+1, temp)
                temp.pop()
        backTracking()
        return res