# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        pick = self.bs(0, n-1, mountain_arr)
        res = self.bsleft(0, pick, mountain_arr, target)
        if res != -1:
            return res
        rightres = self.bsright(pick, n-1, mountain_arr, target)
        return rightres
    
    def bs(self, left, right, mountain_arr):
        pick = -1
        while left < right:
            middle = (left + right) // 2
            md = mountain_arr.get(middle)            
            if md > mountain_arr.get(middle-1) and md > mountain_arr.get(middle+1):
                return middle
            elif mountain_arr.get(middle-1) < md <  mountain_arr.get(middle+1):
                left = middle + 1
            else:
                right = middle 
        return pick 
    
        
    def bsleft(self, left, right, mountain_arr, target):
        while left <= right:
            middle = (left + right) //2
            md = mountain_arr.get(middle)
            if md  == target:
                return middle
                break
            elif  md < target:
                left = middle + 1
            else:
                right = middle -1
        return -1 
    def bsright(self, left, right, mountain_arr, target):
        while left <= right:
            middle = (left + right) //2
            md = mountain_arr.get(middle)
            if md  == target:
                return middle
                break
            elif  md < target:
                right = middle -1
            else:
                left = middle + 1
        return -1 
                
        