class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        def moveZeroes(nums):
            lptr = 0 
            rptr = 1         
            while rptr < len(nums):
                if nums[lptr] != 0: 
                    lptr +=1
                    rptr +=1
                elif nums [rptr] == 0:
                    rptr+=1
                else:
                    nums[rptr],nums[lptr] = nums[lptr],nums[rptr]
        moveZeroes(nums)
        return nums
        
