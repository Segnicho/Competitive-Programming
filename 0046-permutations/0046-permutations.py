class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backTrack(arr,temp):
            if not arr:
                res.append(temp[:])
            
            for num in arr:
                temp.append(num)
                otherNums = arr[:]
                otherNums.remove(num)                
                backTrack(otherNums, temp)
                temp.pop()
        backTrack(nums, [])
        
        return res
    