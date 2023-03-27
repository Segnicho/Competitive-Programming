class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [nums1[i] - nums2[i] for i in range(len(nums1))]
        self.res = 0
        def merge(leftArr, rightArr):
            i = j = 0
            while i < len(leftArr) and j < len(rightArr):
                if leftArr[i] <= (rightArr[j] + diff):
                    self.res += (len(rightArr) - j )                    
                    i += 1
                else:
                    j += 1
                    
            i = j = 0
            res = []
            
            while i < len(leftArr) and j < len(rightArr):
                if leftArr[i] < rightArr[j]:
                    res.append(leftArr[i])
                    i+=1
                else:
                    res.append(rightArr[j])
                    j+=1
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
    