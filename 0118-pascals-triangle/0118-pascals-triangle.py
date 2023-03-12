class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        def dp(i, arr):
            res.append(arr[:])
            if i == len(arr):
                return    
            next_arr = [1]
            for j in range(1, len(arr)):
                next_arr.append(arr[j]+arr[j-1])       
            next_arr.append(1)
            return dp(i, next_arr)
        dp(numRows, [1])
        
        return res
    