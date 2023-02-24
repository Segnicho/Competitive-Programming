class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        currSum = 0
        res = float("inf")
        for right in range(n):
            currSum+=nums[right]
            while currSum >= target:
                res = min(res, right-left+1)
                currSum-=nums[left]
                left+=1
        return res if res != float(inf) else 0