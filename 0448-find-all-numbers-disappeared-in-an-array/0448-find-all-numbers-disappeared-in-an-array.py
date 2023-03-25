class Solution:
    def findDisappearedNumbers(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        
        for i in range(n):
            while arr[i] != arr[arr[i] -1] and arr[i] != i+1:
                temp = arr[i]
                arr[i] = arr[temp - 1]
                arr[temp-1] = temp
        
        for i in range(n):
            if i+1 != arr[i]:
                res.append(i+1)
        return res