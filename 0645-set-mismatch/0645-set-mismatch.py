class Solution:
    def findErrorNums(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)):
            while arr[i] != arr[arr[i]-1] and arr[i] != i+1:
                temp = arr[i]
                arr[i] = arr[temp - 1]
                arr[temp-1] = temp

        for i in range(len(arr)):
            if i + 1 != arr[i]:
                res.append(arr[i])
                res.append(i+1)
        return res
    