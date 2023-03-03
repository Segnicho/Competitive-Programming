class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        stack = []
        for i in range (n*2):
            i = i%len(nums)
            while stack and nums[i] > stack[-1][0]:
                res[stack.pop()[-1]] = nums[i]
            stack.append((nums[i], i))
        return res