class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def dp(i, arr):
            if i == len(arr) - 1:
                return arr
            else:
                next_arr = [1]
                for j in range(1, len(arr)):
                    next_arr.append(arr[j]+arr[j-1])       
                next_arr.append(1)
                return dp(i, next_arr)
            
        if rowIndex == 0:
            return [1]
        return dp(rowIndex, [1])
        