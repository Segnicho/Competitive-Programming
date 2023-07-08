class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 2
        n = len(nums)
        for j in range(2,n):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        return i