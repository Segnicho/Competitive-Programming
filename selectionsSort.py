
class Solution: 
    def select(self, arr, i):
        # code here 
        mn = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[mn]:
                mn = j
        return mn
    def selectionSort(self, arr,n):
        for i in range(n):
            minInd = self.select(arr, i)
            arr[i], arr[minInd] = arr[minInd], arr[i]
        
            
          
