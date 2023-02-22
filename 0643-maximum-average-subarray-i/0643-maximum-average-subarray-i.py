class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        arrlen = len(nums)
        maxSum = wndwSum = sum(nums[:k])
        for i in range(k, arrlen):
            wndwSum += nums[i] 
            wndwSum -= nums[i-k] 
            maxSum = max(wndwSum, maxSum)
        return maxSum/k
    