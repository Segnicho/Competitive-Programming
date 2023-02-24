class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefx = postfx =  1
        n = len(nums)
        res = [1]*n
        for i in range(n):
            res[i] = prefx
            prefx *= nums[i]

        for i in range(n-1, -1, -1):
            res[i] *= postfx
            postfx *= nums[i]
        return res