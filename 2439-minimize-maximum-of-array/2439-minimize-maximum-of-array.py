class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        res = 0 
        prefSum = 0
        for  i, num in enumerate(nums):
            prefSum += num
            res = max(res, math.ceil(prefSum/(i+1)))
        return res