class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(arr, left, right):
            l = left -1
            pivot = arr[right]
            for i in range(left, right):
                if arr[i] <= pivot:
                    l += 1
                    arr[l] , arr[i] = arr[i], arr[l]
            arr[l + 1], arr[right] = arr[right] , arr[l + 1]
            return l + 1        
        def quickSort(arr, left, right):
            if left <= right:
                ptr = partition(arr, left, right)
                if ptr == len(arr) - k:
                    return arr[ptr]
                elif ptr < len(arr) - k:
                    return quickSort(arr, ptr + 1, right)    
                elif ptr > len(arr) - k:
                    return quickSort(arr, left, ptr - 1)
        return quickSort(nums,0, len(nums) -1)