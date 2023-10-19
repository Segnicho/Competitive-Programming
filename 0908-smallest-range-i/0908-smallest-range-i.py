class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0] - (2*k)
        
        return 0 if res < 1 else res
        