class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        mn = nums[0]
        res = 0
        for i in range(n):
            if nums[i] -mn > k:
                res += 1
                mn = nums[i]
        return res + 1