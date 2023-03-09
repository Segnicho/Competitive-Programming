class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        def recur(start, temp):
            if len(temp) == k:
                res.append(temp.copy())
                return 
            for i in range(start, n + 1):
                temp.append(i)
                recur(i+1, temp)
                temp.pop()
        recur(1, [])
        return res