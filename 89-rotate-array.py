class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        brk = (len(nums)-k )%len(nums)
        nums[:] = nums[brk:] + nums[:brk]

        
            
