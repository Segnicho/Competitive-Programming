class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(x):
            start = 0
            while start < x:
                arr[start] , arr[x] = arr[x],arr[start]
                start+=1
                x-=1
        res = []
        for i in range(len(arr)-1,-1,-1):
            maxI = i
            for j in range(i,-1,-1):
                if arr[j] > arr[maxI]:
                    maxI = j
            if maxI != i:
                flip(maxI)
                flip(i)
                res.append(maxI+1)
                res.append(i+1)
        return res
