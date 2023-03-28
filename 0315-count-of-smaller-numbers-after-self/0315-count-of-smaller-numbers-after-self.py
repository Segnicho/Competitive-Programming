class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        arr = [(num, idx) for idx, num in  enumerate(nums)]
        
        self.res = [0]*len(nums)
        
        def merge(leftArr, rightArr):
            i =len(leftArr) - 1
            j = len(rightArr) - 1
            while i >= 0 and j >= 0:
                if leftArr[i][0] > (rightArr[j][0]):
                    self.res[leftArr[i][1]]  += ( j+1 )
                    i -= 1
                else:
                    j -= 1
                    
            i = j = 0
            res = []
            
            while i < len(leftArr) and j < len(rightArr):
                if leftArr[i][0] < rightArr[j][0]:
                    res.append(leftArr[i])
                    i+=1
                else:
                    res.append(rightArr[j])
                    j += 1
                    
            res.extend(leftArr[i:])
            res.extend(rightArr[j:])
            return res

        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
            return merge(left_half, right_half)
        mergeSort(0, len(arr)-1, arr)
        
        return self.res