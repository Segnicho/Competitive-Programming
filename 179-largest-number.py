class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range (len(nums)):
            nums[i] = str(nums[i])
        def compr(num1,num2):
            if num1 + num2 > num2 + num1:
                return -1
            if num1 + num2 < num2 + num1:
                return 1
            else: 
                return 0
        nums = sorted(nums, key = cmp_to_key(compr))
        return str(int("".join(nums)))
