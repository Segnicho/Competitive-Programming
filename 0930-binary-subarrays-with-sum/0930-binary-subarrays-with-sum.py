class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefSum = Counter({0:1})
        currSum = 0
        res = 0
        
        for num in nums:
            currSum += num
            res += prefSum[currSum-goal]
            prefSum[currSum] += 1
        return res