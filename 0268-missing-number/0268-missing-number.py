class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while  nums[i] < len(nums) and nums[i] != i:
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
    